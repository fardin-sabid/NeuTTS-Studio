"""
NeuTTS Studio — Voice Selector
Shared interactive voice picker used across TTS, Streaming, and Cloning modules.
"""

import torch
from core.ui import menu, info, error, success, working, GY, CY, WH, GR, YL, MG, R, B
from core.engine import engine
from config import SAMPLE_VOICE_META, VOICES_DIR


def pick_voice() -> tuple[torch.Tensor, str, str] | None:
    """
    Show voice selection menu and return (ref_codes, ref_text, voice_name).
    Returns None if user cancels.
    """
    samples = engine.list_samples()
    customs = engine.list_voices()

    if not samples and not customs:
        error("No voices found. Add .wav files to data/samples/ or clone a voice first.")
        return None

    # Build menu options
    options = {}
    key_map = {}
    k = 1

    if samples:
        for name in samples:
            meta   = SAMPLE_VOICE_META.get(name, {})
            flag   = meta.get("flag", "🎙️")
            lang   = meta.get("lang", "Unknown")
            gender = meta.get("gender", "")
            options[str(k)] = {
                "label": f"{name.capitalize()}",
                "icon":  flag,
                "desc":  f"Sample voice · {lang}{' · ' + gender if gender else ''}",
                "badge": "SAMPLE",
            }
            key_map[str(k)] = ("sample", name)
            k += 1

    if customs:
        for name in customs:
            # Try to load metadata if exists
            flag = "👤"
            lang = "Unknown"
            gender = ""
            
            # Check for metadata file
            meta_path = VOICES_DIR / f"{name}.meta"
            if meta_path.exists():
                try:
                    for line in meta_path.read_text().splitlines():
                        if "=" in line:
                            key, val = line.split("=", 1)
                            if key == "flag":
                                flag = val
                            elif key == "lang":
                                lang = val
                            elif key == "gender":
                                gender = val
                except:
                    pass
            
            options[str(k)] = {
                "label": name,
                "icon":  flag,
                "desc":  f"Custom voice · {lang}{' · ' + gender if gender else ''}",
                "badge": "CUSTOM",
            }
            key_map[str(k)] = ("custom", name)
            k += 1

    choice = menu("Select Voice", options, back_label="← Cancel")
    if choice == "0":
        return None

    kind, name = key_map[choice]
    working(f"Loading voice: {name}...")

    try:
        if kind == "sample":
            ref_codes, ref_text = engine.load_sample(name)
        else:
            ref_codes, ref_text = engine.load_voice(name)

        success(f"Voice '{name}' loaded.")
        return ref_codes, ref_text, name

    except Exception as e:
        error(str(e))
        return None