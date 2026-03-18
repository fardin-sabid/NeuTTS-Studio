"""
NeuTTS Studio — Configuration
All constants, paths, model definitions, and app settings.
"""

import os
from pathlib import Path

# ─── Base Paths ───────────────────────────────────────────────────────────────
BASE_DIR    = Path(__file__).parent
DATA_DIR    = BASE_DIR / "data"
VOICES_DIR  = DATA_DIR / "voices"
SAMPLES_DIR = DATA_DIR / "samples"
MODELS_DIR  = DATA_DIR / "models"       # ← ALL downloaded models saved here

OUTPUTS = {
    "tts":       DATA_DIR / "outputs" / "tts",
    "streaming": DATA_DIR / "outputs" / "streaming",
    "cloning":   DATA_DIR / "outputs" / "cloning",
}

# Ensure all dirs exist at startup
for _p in [VOICES_DIR, SAMPLES_DIR, MODELS_DIR, *OUTPUTS.values()]:
    _p.mkdir(parents=True, exist_ok=True)

# ─── Timeout Settings ────────────────────────────────────────────────────────
HF_TIMEOUT = 60  # HuggingFace download timeout in seconds

# ─── Force HuggingFace to use local data/models/ ─────────────────────────────
# Prevents models from saving to hidden ~/.cache/huggingface/ folders.
# Everything stays inside the project — easy to find, backup, and delete.
os.environ["HF_HOME"]                        = str(MODELS_DIR)
os.environ["HUGGINGFACE_HUB_CACHE"]          = str(MODELS_DIR / "hub")
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"]= "1"   # Android fs has no symlink support — silence warning
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"]        = str(HF_TIMEOUT)  # Increase timeout
# Note: TRANSFORMERS_CACHE is deprecated in transformers v5 — use HF_HOME instead

# ─── Models (Nano Only) ───────────────────────────────────────────────────────
MODELS = {
    "1": {
        "name":      "NeuTTS-Nano  ·  SafeTensors",
        "short":     "Nano-ST",
        "repo":      "neuphonic/neutts-nano",
        "type":      "safetensors",
        "desc":      "Full precision · Multilingual · Finetuneable",
        "badge":     "FULL",
        "langs":     ["en-us", "es", "de", "fr-fr"],
        "streaming": False,
        "finetune":  True,
    },
    "2": {
        "name":      "NeuTTS-Nano  ·  GGUF Q8",
        "short":     "Nano-Q8",
        "repo":      "neuphonic/neutts-nano-q8-gguf",
        "type":      "gguf",
        "desc":      "8-bit quantized · Fast · Streaming ready",
        "badge":     "Q8",
        "langs":     ["en-us"],
        "streaming": True,
        "finetune":  False,
    },
    "3": {
        "name":      "NeuTTS-Nano  ·  GGUF Q4",
        "short":     "Nano-Q4",
        "repo":      "neuphonic/neutts-nano-q4-gguf",
        "type":      "gguf",
        "desc":      "4-bit quantized · Fastest · Lowest memory",
        "badge":     "Q4",
        "langs":     ["en-us"],
        "streaming": True,
        "finetune":  False,
    },
}

CODEC_REPO      = "neuphonic/neucodec"
CODEC_REPO_ONNX = "neuphonic/neucodec-onnx-decoder"

# ─── Audio ────────────────────────────────────────────────────────────────────
SAMPLE_RATE      = 24_000
REF_SAMPLE_RATE  = 16_000
CHUNK_SILENCE_MS = 200

# ─── Chunking ─────────────────────────────────────────────────────────────────
MAX_CHUNK_CHARS  = 250

# ─── Finetuning Defaults ──────────────────────────────────────────────────────
FINETUNE_DEFAULTS = {
    "lr":            0.00004,
    "max_steps":     10_000,
    "batch_size":    2,
    "warmup_ratio":  0.0,
    "lr_scheduler":  "cosine",
    "max_seq_len":   2048,
    "codebook_size": 65536,
    "logging_steps": 100,
    "save_steps":    20_000,
    "seed":          1337,
}

# ─── Sample Voice Metadata ────────────────────────────────────────────────────
SAMPLE_VOICE_META = {
    "dave":     {"lang": "English", "gender": "Male",   "flag": "🇬🇧"},
    "jo":       {"lang": "English", "gender": "Female", "flag": "🇬🇧"},
    "mateo":    {"lang": "Spanish", "gender": "Male",   "flag": "🇪🇸"},
    "greta":    {"lang": "German",  "gender": "Female", "flag": "🇩🇪"},
    "juliette": {"lang": "French",  "gender": "Female", "flag": "🇫🇷"},
}

# ─── App Info ─────────────────────────────────────────────────────────────────
APP_NAME    = "NeuTTS Studio"
APP_VERSION = "2.0.0"