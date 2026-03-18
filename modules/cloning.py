"""
NeuTTS Studio — Voice Cloning Module
Clone, manage, and test custom voice profiles.
"""

from pathlib import Path
from core.ui import (
    print_section, menu, ask, confirm,
    success, error, warning, info, working, pause, divider,
    CY, GY, WH, GR, YL, RD, B, R
)
from core.progress import DONE_MARK
from core.engine import engine
from core.audio import save, duration
from core.progress import StepTracker, Spinner
from config import VOICES_DIR, SAMPLES_DIR, SAMPLE_VOICE_META


def run():
    while True:
        print_section("Voice Cloning", subtitle="clone · manage · test")

        if not engine.loaded:
            error("No model loaded! Go to Settings → Load Model first.")
            pause()
            return

        choice = menu(
            "Voice Cloning",
            {
                "1": {"label": "Clone new voice",     "icon": "🎤", "desc": "Create a voice profile from a .wav file"},
                "2": {"label": "View all voices",     "icon": "📋", "desc": "Browse sample and custom voice profiles"},
                "3": {"label": "Test a voice",        "icon": "🔊", "desc": "Generate a test phrase with any voice"},
                "4": {"label": "Delete custom voice", "icon": "🗑️", "desc": "Remove a saved voice profile"},
                "5": {"label": "Migrate voice metadata", "icon": "🔄", "desc": "Add language/gender to existing voices"},
            }
        )
        if choice == "0":
            return
        elif choice == "1":
            _clone()
        elif choice == "2":
            _list_all()
        elif choice == "3":
            _test()
        elif choice == "4":
            _delete()
        elif choice == "5":
            migrate_voices_metadata()


def _clone():
    print_section("Clone New Voice")

    print(f"""  {GY}Reference audio guidelines:
  ─────────────────────────────────────────────────
  {GR}✓{GY}  3–15 seconds of clean speech
  {GR}✓{GY}  Mono channel · 16–44kHz · .wav format
  {GR}✓{GY}  Natural continuous speech (no long pauses)
  {RD}✗{GY}  No background noise, music, or multiple speakers{R}
""")

    wav = ask("Path to reference .wav file")
    if not wav:
        return
    wav = Path(wav)
    if not wav.exists():
        error(f"File not found: {wav}")
        return
    if wav.suffix.lower() != ".wav":
        error("Must be a .wav file.")
        return

    transcript = ask("Exact words spoken in the audio")
    if not transcript:
        error("Transcript is required.")
        return

    name = ask("Voice profile name (e.g. my_voice, alex)")
    if not name:
        return
    name = name.strip().lower().replace(" ", "_")

    # Simple language menu
    print("\n  Select language:")
    print("    [1] 🇬🇧 English")
    print("    [2] 🇺🇸 American")
    print("    [3] 🇪🇸 Spanish")
    print("    [4] 🇫🇷 French")
    print("    [5] 🇩🇪 German")
    print("    [6] 🇮🇹 Italian")
    print("    [7] 🇵🇹 Portuguese")
    print("    [8] 🇷🇺 Russian")
    print("    [9] 🇯🇵 Japanese")
    print("    [10] 🇰🇷 Korean")
    print("    [11] 🇨🇳 Chinese")
    print("    [12] 🇮🇳 Hindi")
    print("    [13] 🇧🇩 Bengali")
    print("    [14] 🇵🇰 Urdu")
    print("    [15] 🇸🇦 Arabic")
    print("    [16] Other")
    
    lang_choice = ask("Choice", default="13")
    
    lang_map = {
        "1": ("🇬🇧", "English"),
        "2": ("🇺🇸", "American"),
        "3": ("🇪🇸", "Spanish"),
        "4": ("🇫🇷", "French"),
        "5": ("🇩🇪", "German"),
        "6": ("🇮🇹", "Italian"),
        "7": ("🇵🇹", "Portuguese"),
        "8": ("🇷🇺", "Russian"),
        "9": ("🇯🇵", "Japanese"),
        "10": ("🇰🇷", "Korean"),
        "11": ("🇨🇳", "Chinese"),
        "12": ("🇮🇳", "Hindi"),
        "13": ("🇧🇩", "Bengali"),
        "14": ("🇵🇰", "Urdu"),
        "15": ("🇸🇦", "Arabic"),
    }
    
    if lang_choice in lang_map:
        flag, lang = lang_map[lang_choice]
    else:
        flag = "👤"
        lang = ask("Custom language", default="Unknown")
    
    # Simple gender menu
    print("\n  Select gender:")
    print("    [1] Male")
    print("    [2] Female")
    print("    [3] Other")
    
    gender_choice = ask("Choice", default="1")
    gender_map = {"1": "Male", "2": "Female", "3": "Other"}
    gender = gender_map.get(gender_choice, "Other")

    if name in engine.list_voices():
        if not confirm(f"Voice '{name}' already exists. Overwrite?", default=False):
            return

    tracker = StepTracker(["Encode audio", "Save profile"])
    try:
        with tracker.step("Encode audio"):
            pt = engine.encode_voice(str(wav), name, transcript)
        with tracker.step("Save profile"):
            # Save metadata alongside voice
            meta_path = VOICES_DIR / f"{name}.meta"
            meta_path.write_text(f"lang={lang}\ngender={gender}\nflag={flag}", encoding="utf-8")

        success(f"Voice '{name}' saved to data/voices/")
        info("Use this voice in TTS or Streaming mode.")
    except Exception as e:
        error(str(e))

    pause()


def _list_all():
    print_section("All Available Voices")

    samples = engine.list_samples()
    customs = engine.list_voices()

    if samples:
        print(f"  {CY}{B}Sample Voices{R}  {GY}(built-in){R}\n")
        for name in samples:
            meta = SAMPLE_VOICE_META.get(name, {})
            flag = meta.get("flag", "🎙️")
            lang = meta.get("lang", "?")
            gen  = meta.get("gender", "")
            print(f"  {flag}  {WH}{B}{name.capitalize()}{R}  {GY}{lang}{' · ' + gen if gen else ''}{R}")
            print()
    else:
        info("No sample voices found. Add .wav + .txt files to data/samples/")

    if customs:
        print(f"  {CY}{B}Custom Voices{R}  {GY}(your cloned voices){R}\n")
        for name in customs:
            # Load metadata
            flag = "👤"
            lang = "Unknown"
            gender = ""
            
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
            
            print(f"  {flag}  {WH}{B}{name}{R}  {GY}{lang}{' · ' + gender if gender else ''}{R}")
            print()
    else:
        print(f"  {GY}No custom voices yet. Use 'Clone new voice' to create one.{R}\n")

    pause()


def _test():
    print_section("Test a Voice")

    from modules.voice_selector import pick_voice
    import time

    voice = pick_voice()
    if not voice:
        return

    ref_codes, ref_text, voice_name = voice
    phrase = ask("Test phrase", default="Hello! This is a test of my cloned voice.")
    if not phrase:
        return

    with Spinner(f"Generating test audio for '{voice_name}'..."):
        t0    = time.time()
        audio = engine.infer(phrase, ref_codes, ref_text)
        elapsed = time.time() - t0

    dur  = duration(audio)
    path = save(audio, category="cloning", name=f"test_{voice_name}")

    success(f"Test audio saved → {CY}{path.name}{R}")
    print(f"  {GY}Duration: {dur:.2f}s  ·  Generated in {elapsed:.2f}s  ·  RTF {elapsed/dur:.2f}{R}\n")
    info(f"Location: data/outputs/cloning/")
    pause()


def _delete():
    print_section("Delete Custom Voice")

    customs = engine.list_voices()
    if not customs:
        info("No custom voices to delete.")
        pause()
        return

    opts = {str(i + 1): {"label": name, "icon": "👤", "desc": str(VOICES_DIR / f"{name}.pt")}
            for i, name in enumerate(customs)}
    choice = menu("Select Voice to Delete", opts)
    if choice == "0":
        return

    name = customs[int(choice) - 1]
    if not confirm(f"Delete '{name}'? This cannot be undone.", default=False):
        return

    with Spinner(f"Deleting '{name}'..."):
        engine.delete_voice(name)
        # Also delete metadata
        meta_path = VOICES_DIR / f"{name}.meta"
        if meta_path.exists():
            meta_path.unlink()

    success(f"Voice '{name}' deleted.")
    pause()


def migrate_voices_metadata():
    """Add metadata to existing voices with simple menu."""
    print_section("Migrate Voice Metadata")
    
    customs = engine.list_voices()
    if not customs:
        info("No custom voices found.")
        pause()
        return
    
    migrated = 0
    skipped = 0
    
    for name in customs:
        meta_path = VOICES_DIR / f"{name}.meta"
        
        # Skip if metadata already exists
        if meta_path.exists():
            skipped += 1
            continue
        
        print(f"\n  {CY}Voice:{R} {WH}{name}{R}")
        
        # Simple language menu
        print("\n  Select language:")
        print("    [1] 🇬🇧 English")
        print("    [2] 🇺🇸 American")
        print("    [3] 🇪🇸 Spanish")
        print("    [4] 🇫🇷 French")
        print("    [5] 🇩🇪 German")
        print("    [6] 🇮🇹 Italian")
        print("    [7] 🇵🇹 Portuguese")
        print("    [8] 🇷🇺 Russian")
        print("    [9] 🇯🇵 Japanese")
        print("    [10] 🇰🇷 Korean")
        print("    [11] 🇨🇳 Chinese")
        print("    [12] 🇮🇳 Hindi")
        print("    [13] 🇧🇩 Bengali")
        print("    [14] 🇵🇰 Urdu")
        print("    [15] 🇸🇦 Arabic")
        print("    [16] Other")
        
        lang_choice = ask("Choice", default="13")
        
        lang_map = {
            "1": ("🇬🇧", "English"),
            "2": ("🇺🇸", "American"),
            "3": ("🇪🇸", "Spanish"),
            "4": ("🇫🇷", "French"),
            "5": ("🇩🇪", "German"),
            "6": ("🇮🇹", "Italian"),
            "7": ("🇵🇹", "Portuguese"),
            "8": ("🇷🇺", "Russian"),
            "9": ("🇯🇵", "Japanese"),
            "10": ("🇰🇷", "Korean"),
            "11": ("🇨🇳", "Chinese"),
            "12": ("🇮🇳", "Hindi"),
            "13": ("🇧🇩", "Bengali"),
            "14": ("🇵🇰", "Urdu"),
            "15": ("🇸🇦", "Arabic"),
        }
        
        if lang_choice in lang_map:
            flag, lang = lang_map[lang_choice]
        else:
            flag = "👤"
            lang = ask("Custom language", default="Unknown")
        
        # Simple gender menu
        print("\n  Select gender:")
        print("    [1] Male")
        print("    [2] Female")
        print("    [3] Other")
        
        gender_choice = ask("Choice", default="1")
        gender_map = {"1": "Male", "2": "Female", "3": "Other"}
        gender = gender_map.get(gender_choice, "Other")
        
        # Save metadata
        meta_path.write_text(f"lang={lang}\ngender={gender}\nflag={flag}", encoding="utf-8")
        print(f"  {GR}✓{R} Saved: {flag} {lang} · {gender}")
        
        migrated += 1
        
        if not confirm("\n  Next voice?", default=True):
            break
    
    print(f"\n  {DONE_MARK}  {GR}Migration complete!{R}")
    print(f"  {GY}Migrated: {migrated}  ·  Skipped: {skipped}{R}")
    pause()