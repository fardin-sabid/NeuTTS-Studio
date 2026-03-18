"""
NeuTTS Studio — Audio Utilities
Stitching, saving, and managing generated audio files.
"""

import numpy as np
from pathlib import Path
from datetime import datetime
from config import SAMPLE_RATE, CHUNK_SILENCE_MS, OUTPUTS


def silence_samples(ms: int = CHUNK_SILENCE_MS) -> np.ndarray:
    return np.zeros(int(SAMPLE_RATE * ms / 1000), dtype=np.float32)


def stitch(chunks: list[np.ndarray], gap_ms: int = CHUNK_SILENCE_MS) -> np.ndarray:
    """Merge audio chunks into one waveform with optional silence gaps."""
    if not chunks:
        return np.array([], dtype=np.float32)
    if len(chunks) == 1:
        return chunks[0].astype(np.float32)

    parts = []
    gap   = silence_samples(gap_ms) if gap_ms > 0 else None
    for i, chunk in enumerate(chunks):
        parts.append(chunk.astype(np.float32))
        if gap is not None and i < len(chunks) - 1:
            parts.append(gap)
    return np.concatenate(parts)


def save(audio: np.ndarray, category: str, name: str = None) -> Path:
    """
    Save a numpy audio array to the correct output subfolder.

    Args:
        audio:    Waveform (float32, 24kHz).
        category: One of 'tts', 'streaming', 'cloning'.
        name:     Optional filename (auto-timestamped if None).

    Returns:
        Path to saved .wav file.
    """
    import soundfile as sf

    out_dir = OUTPUTS.get(category, OUTPUTS["tts"])
    out_dir.mkdir(parents=True, exist_ok=True)

    if not name:
        ts   = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = f"{category}_{ts}"

    if not name.endswith(".wav"):
        name += ".wav"

    path = out_dir / name
    sf.write(str(path), audio, SAMPLE_RATE)
    return path


def save_chunks(
    chunks: list[np.ndarray],
    category: str,
    base_name: str = None,
) -> list[Path]:
    """Save each chunk as a separate .wav file."""
    import soundfile as sf

    out_dir = OUTPUTS.get(category, OUTPUTS["tts"])
    out_dir.mkdir(parents=True, exist_ok=True)

    if not base_name:
        base_name = datetime.now().strftime("%Y%m%d_%H%M%S")

    paths = []
    for i, chunk in enumerate(chunks, 1):
        name = f"{base_name}_chunk{i:03d}.wav"
        path = out_dir / name
        sf.write(str(path), chunk.astype(np.float32), SAMPLE_RATE)
        paths.append(path)
    return paths


def duration(audio: np.ndarray) -> float:
    """Audio duration in seconds."""
    return len(audio) / SAMPLE_RATE


def list_outputs(category: str) -> list[Path]:
    """List .wav files in an output folder, newest first."""
    folder = OUTPUTS.get(category, OUTPUTS["tts"])
    return sorted(folder.glob("*.wav"), key=lambda p: p.stat().st_mtime, reverse=True)


def all_outputs() -> dict[str, list[Path]]:
    """Return all output files grouped by category."""
    return {cat: list_outputs(cat) for cat in OUTPUTS}
