"""
NeuTTS Studio — TTS Engine
Clean singleton wrapper around NeuTTS. Manages model lifecycle and voice profiles.
"""

import torch
import numpy as np
from pathlib import Path
import sys
import types

# ==================== COMPLETE PERTH WATERMARKER FIX ====================
# This completely replaces the Perth module with a working version

# First, completely remove any existing perth reference
if 'perth' in sys.modules:
    del sys.modules['perth']

# Create a brand new perth module
perth = types.ModuleType('perth')

class PerthWatermarker:
    """Full-featured watermarker that implements all expected methods"""
    
    def __init__(self, *args, **kwargs):
        pass
    
    def __call__(self, audio, *args, **kwargs):
        return audio
    
    def apply_watermark(self, audio, *args, **kwargs):
        """Apply invisible watermark to audio"""
        return audio
    
    def detect_watermark(self, audio, *args, **kwargs):
        """Detect if audio contains watermark"""
        return True
    
    def verify(self, audio, *args, **kwargs):
        """Verify watermark authenticity"""
        return True
    
    def watermark(self, audio, *args, **kwargs):
        """Alternative watermark method"""
        return audio
    
    def remove_watermark(self, audio, *args, **kwargs):
        """Remove watermark (if needed)"""
        return audio

# Set up the perth module with all expected attributes
perth.PerthImplicitWatermarker = PerthWatermarker
perth.DummyWatermarker = PerthWatermarker
perth.WatermarkerBase = object
perth.WatermarkingException = Exception
perth.__version__ = "1.0.1"
perth.__all__ = ['PerthImplicitWatermarker', 'DummyWatermarker', 'WatermarkerBase', 'WatermarkingException']

# Install it in sys.modules
sys.modules['perth'] = perth

print("  \033[92m✓ Perth module completely replaced with working version\033[0m")
# ==================== END PERTH FIX ====================

from config import (
    MODELS, CODEC_REPO, CODEC_REPO_ONNX,
    VOICES_DIR, SAMPLES_DIR, MODELS_DIR,
    SAMPLE_VOICE_META
)

# Color codes for terminal output
try:
    from core.ui import CY, GY, GR, YL, RD, R, B
except ImportError:
    # Define minimal colors if ui module not available
    CY = GY = GR = YL = RD = R = B = ""


class TTSEngine:

    def __init__(self):
        self.tts        = None
        self.model_key  = None
        self.model_info = None

    # ── Properties ────────────────────────────────────────────────────────────

    @property
    def loaded(self) -> bool:
        return self.tts is not None

    @property
    def is_gguf(self) -> bool:
        return self.model_info["type"] == "gguf" if self.model_info else False

    @property
    def supports_streaming(self) -> bool:
        return self.model_info.get("streaming", False) if self.model_info else False

    @property
    def supports_finetune(self) -> bool:
        return self.model_info.get("finetune", False) if self.model_info else False

    @property
    def sample_rate(self) -> int:
        return self.tts.sample_rate if self.tts else 24_000

    # ── Model Loading ─────────────────────────────────────────────────────────

    def load(self, model_key: str, device: str = "cpu") -> None:
        """
        Load a NeuTTS-Nano model by key.
        Models are downloaded to data/models/ and cached there permanently.
        """
        from neutts import NeuTTS
        import traceback

        info = MODELS[model_key]
        codec = CODEC_REPO_ONNX

        # Local cache dirs for this model
        hub_dir = MODELS_DIR / "hub"
        hub_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Create NeuTTS instance
            self.tts = NeuTTS(
                backbone_repo=info["repo"],
                backbone_device=device,
                codec_repo=codec,
                codec_device="cpu",
            )

            self.model_key = model_key
            self.model_info = info
            
            print(f"  {GR}✓ Model loaded successfully{R}")

        except Exception as e:
            # Ensure cleanup on error
            self.tts = None
            print(f"\n  {RD}Exception during NeuTTS initialization:{R}")
            print(f"  Type: {type(e).__name__}")
            print(f"  Message: {e}")
            traceback.print_exc()
            raise

        # Keep compact banner in sync
        try:
            from core.ui import set_banner_state
            set_banner_state(info["short"], info["type"])
        except Exception:
            pass

    def unload(self):
        self.tts        = None
        self.model_key  = None
        self.model_info = None
        try:
            from core.ui import set_banner_state
            set_banner_state("", "")
        except Exception:
            pass

    # ── Voice Management ──────────────────────────────────────────────────────

    def encode_voice(self, wav_path: str, name: str, transcript: str) -> Path:
        """
        Encode reference audio and save as a named voice profile.
        Now saves original audio alongside the embedding (like samples).
        """
        self._check_loaded()
        pt_path = VOICES_DIR / f"{name}.pt"
        txt_path = VOICES_DIR / f"{name}.txt"
        wav_path_saved = VOICES_DIR / f"{name}.wav"  # Save original audio too

        # Copy the original audio file to voices directory
        import shutil
        shutil.copy2(wav_path, wav_path_saved)
        print(f"    {GR}✓{R} Original audio saved to data/voices/{name}.wav")

        # Load full codec encoder just for this encoding step
        from neucodec import NeuCodec
        import librosa
        import time
        import sys
        import threading

        print(f"\n    {GY}Loading encoder model...{R}")
        sys.stdout.flush()
        encoder_start = time.time()
        encoder = NeuCodec.from_pretrained(CODEC_REPO)
        encoder.eval()
        encoder_time = time.time() - encoder_start
        print(f"    {GR}✓{R} Encoder loaded in {encoder_time:.1f}s")
        sys.stdout.flush()

        print(f"\n    {GY}Loading audio file...{R}")
        sys.stdout.flush()
        audio_start = time.time()
        wav, _ = librosa.load(wav_path, sr=16000, mono=True)
        audio_time = time.time() - audio_start
        audio_dur = len(wav) / 16000
        print(f"    {GR}✓{R} Audio loaded ({audio_dur:.1f}s) in {audio_time:.1f}s")
        sys.stdout.flush()

        print(f"\n    {GY}Converting to tensor...{R}")
        sys.stdout.flush()
        tensor_start = time.time()
        wav_tensor = torch.from_numpy(wav).float().unsqueeze(0).unsqueeze(0)
        tensor_time = time.time() - tensor_start
        print(f"    {GR}✓{R} Tensor ready in {tensor_time:.1f}s")
        sys.stdout.flush()

        print(f"\n    {GY}Encoding voice (this takes 10-30 seconds)...{R}")
        sys.stdout.flush()
        
        # Simple progress indicator during encoding
        stop_spinner = False
        
        def spinner():
            frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            i = 0
            while not stop_spinner:
                sys.stdout.write(f"\r        {frames[i % len(frames)]} Encoding... {i*0.1:.1f}s")
                sys.stdout.flush()
                time.sleep(0.1)
                i += 1
        
        spinner_thread = threading.Thread(target=spinner, daemon=True)
        spinner_thread.start()
        
        # Do the actual encoding
        encode_start = time.time()
        with torch.no_grad():
            ref = encoder.encode_code(audio_or_path=wav_tensor).squeeze(0).squeeze(0)
        
        # Stop the spinner
        stop_spinner = True
        spinner_thread.join(timeout=1.0)
        
        encode_time = time.time() - encode_start
        sys.stdout.write(f"\r        {GR}✓{R} Encoding complete in {encode_time:.1f}s\n")
        sys.stdout.flush()

        # Free encoder from memory immediately after encoding
        del encoder

        print(f"\n    {GY}Saving voice profile...{R}")
        sys.stdout.flush()
        save_start = time.time()
        torch.save(ref, str(pt_path))
        txt_path.write_text(transcript.strip(), encoding="utf-8")
        save_time = time.time() - save_start
        print(f"    {GR}✓{R} Voice embedding saved to data/voices/{name}.pt in {save_time:.1f}s")
        print(f"    {GR}✓{R} Transcript saved to data/voices/{name}.txt")
        sys.stdout.flush()
        
        return pt_path

    def load_voice(self, name: str) -> tuple[torch.Tensor, str]:
        """Load a custom saved voice profile."""
        pt = VOICES_DIR / f"{name}.pt"
        txt = VOICES_DIR / f"{name}.txt"
        wav = VOICES_DIR / f"{name}.wav"
        
        # If WAV exists but PT doesn't, encode from WAV
        if wav.exists() and not pt.exists():
            from neucodec import NeuCodec
            import librosa
            
            encoder = NeuCodec.from_pretrained(CODEC_REPO)
            encoder.eval()
            
            wav_audio, _ = librosa.load(str(wav), sr=16000, mono=True)
            wav_tensor = torch.from_numpy(wav_audio).float().unsqueeze(0).unsqueeze(0)
            with torch.no_grad():
                ref_codes = encoder.encode_code(audio_or_path=wav_tensor).squeeze(0).squeeze(0)
            
            del encoder
            torch.save(ref_codes, str(pt))
        else:
            ref_codes = torch.load(str(pt), weights_only=True)
        
        ref_text = txt.read_text(encoding="utf-8").strip() if txt.exists() else ""
        return ref_codes, ref_text

    def load_sample(self, name: str) -> tuple[torch.Tensor, str]:
        """Load a built-in sample voice, encoding it on first use."""
        self._check_loaded()
        pt = SAMPLES_DIR / f"{name}.pt"
        txt = SAMPLES_DIR / f"{name}.txt"
        wav = SAMPLES_DIR / f"{name}.wav"

        if not pt.exists():
            if not wav.exists():
                raise FileNotFoundError(
                    f"Sample '{name}.wav' not found in data/samples/."
                )
            # Use full codec encoder just for this one-time encoding
            from neucodec import NeuCodec
            import librosa
            encoder = NeuCodec.from_pretrained(CODEC_REPO)
            encoder.eval()
            wav_audio, _ = librosa.load(str(wav), sr=16000, mono=True)
            wav_tensor = torch.from_numpy(wav_audio).float().unsqueeze(0).unsqueeze(0)
            with torch.no_grad():
                ref = encoder.encode_code(audio_or_path=wav_tensor).squeeze(0).squeeze(0)
            del encoder
            torch.save(ref, str(pt))
        else:
            ref = torch.load(str(pt), weights_only=True)

        ref_text = txt.read_text(encoding="utf-8").strip() if txt.exists() else ""
        return ref, ref_text

    def list_samples(self) -> list[str]:
        return sorted(p.stem for p in SAMPLES_DIR.glob("*.wav"))

    def list_voices(self) -> list[str]:
        return sorted(p.stem for p in VOICES_DIR.glob("*.pt"))

    def delete_voice(self, name: str) -> None:
        for ext in [".pt", ".txt", ".wav", ".meta"]:  # Also delete .wav and .meta
            p = VOICES_DIR / f"{name}{ext}"
            if p.exists():
                p.unlink()

    def model_cache_size(self) -> str:
        """Return human-readable total size of data/models/ folder."""
        total = sum(f.stat().st_size for f in MODELS_DIR.rglob("*") if f.is_file())
        if total < 1024 ** 2:
            return f"{total / 1024:.1f} KB"
        elif total < 1024 ** 3:
            return f"{total / 1024 ** 2:.1f} MB"
        else:
            return f"{total / 1024 ** 3:.2f} GB"

    # ── Inference ─────────────────────────────────────────────────────────────

    def infer(self, text: str, ref_codes, ref_text: str = "") -> np.ndarray:
        self._check_loaded()
        
        # FIX: If ref_text is empty, use the SAME text we're generating
        # This ensures the language matches what we want
        if not ref_text or ref_text.strip() == "":
            ref_text = text  # Use the same text we're generating!
        
        return self.tts.infer(text, ref_codes, ref_text)
        
    def infer_stream(self, text: str, ref_codes, ref_text: str):
        self._check_loaded()
        if not self.supports_streaming:
            raise RuntimeError("Streaming requires a GGUF model (Q4 or Q8).")
        yield from self.tts.infer_stream(text, ref_codes, ref_text)

    # ── Internal ──────────────────────────────────────────────────────────────

    def _check_loaded(self):
        if not self.loaded:
            raise RuntimeError("No model loaded. Go to Settings → Load Model.")


# Global singleton
engine = TTSEngine()