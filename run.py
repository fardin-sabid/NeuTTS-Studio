"""
NeuTTS Studio — Entry Point
Run this file to launch the interactive studio.

Usage:
    python -u run.py        ← recommended (unbuffered, real-time progress)
    python run.py           ← also works
"""

import sys
import os
import warnings
import atexit
import termios
import tty
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

# ── Fix terminal settings for bulletproof input ─────────────────────────────
def fix_terminal():
    """Reset terminal to sane settings."""
    sys.stdout.write("\033[?25h")  # Show cursor
    sys.stdout.flush()

atexit.register(fix_terminal)

# Save original terminal settings and restore on exit
try:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    def restore_terminal():
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    atexit.register(restore_terminal)
except:
    pass  # Skip if not a TTY

# ── Force unbuffered output — fixes tqdm/progress not updating in real time ──
os.environ["PYTHONUNBUFFERED"] = "1"
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(line_buffering=True)
    sys.stderr.reconfigure(line_buffering=True)

# ── Force tqdm to render properly in Termux terminal ─────────────────────────
os.environ["TQDM_DYNAMIC_NCOLS"]     = "1"
os.environ["TQDM_MININTERVAL"]       = "0.1"   # update every 100ms minimum
os.environ["HF_HUB_DISABLE_PROGRESS_BARS"] = "0"  # ensure HF bars are ON
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "60"  # Increase timeout to 60 seconds

# ── Silence known non-critical warnings ──────────────────────────────────────
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=UserWarning, message=".*flock.*")
warnings.filterwarnings("ignore", category=UserWarning, message=".*symlinks.*")

from core.ui import (print_banner, print_section, menu, confirm,
                     info, success, pause, smart_clear, set_banner_state)
from core.ui import CY, GY, WH, GR, YL, B, R
from core.engine import engine
from config import MODELS, APP_NAME, APP_VERSION


def main():
    # First launch: guide user to load a model
    _welcome()

    while True:
        try:
            choice = _main_menu()

            if choice == "0":
                _exit()

            elif choice == "1":
                from modules.tts import run
                run()

            elif choice == "2":
                from modules.cloning import run
                run()

            elif choice == "3":
                from modules.streaming import run
                run()

            elif choice == "4":
                from modules.finetuning import run
                run()

            elif choice == "5":
                from modules.settings import run
                run()

        except KeyboardInterrupt:
            print()
            _exit()
        except Exception as e:
            from core.ui import error
            error(f"Unexpected error: {e}")
            pause("Press Enter to return to menu")


def _main_menu() -> str:
    # Always clear and redraw for a clean interactive feel
    if engine.loaded:
        print_banner(engine.model_info["short"], engine.model_info["type"])
    else:
        print_banner()

    streaming_note = f"{GY}(GGUF only){R}" if engine.loaded and not engine.supports_streaming else ""
    finetune_note  = f"{GY}(SafeTensors only){R}" if engine.loaded and not engine.supports_finetune else ""

    options = {
        "1": {
            "label": "Text to Speech",
            "icon":  "🗣️",
            "desc":  "Convert any length of text to audio with smart chunking",
        },
        "2": {
            "label": "Voice Cloning",
            "icon":  "🎤",
            "desc":  "Clone a voice from 3s of audio · manage voice profiles",
        },
        "3": {
            "label": f"Streaming Mode  {streaming_note}",
            "icon":  "⚡",
            "desc":  "Real-time audio generation with live playback",
        },
        "4": {
            "label": f"Fine Tuning  {finetune_note}",
            "icon":  "🔧",
            "desc":  "Train on custom voice data to improve quality",
        },
        "5": {
            "label": "Settings",
            "icon":  "⚙️",
            "desc":  "Load model · manage outputs · app info",
        },
    }

    return menu("Main Menu", options, back_label="Exit NeuTTS Studio")


def _welcome():
    """On first run, show welcome and prompt model load."""
    if engine.loaded:
        return

    print_banner()
    print(f"""  {CY}{B}Welcome to {APP_NAME} v{APP_VERSION}!{R}

  {WH}Before you start, you need to load a model.{R}
  {GY}First run will download it from HuggingFace automatically.{R}

  {CY}Available models:{R}

""")
    for k, m in MODELS.items():
        badge_c = GR if m["type"] == "safetensors" else YL
        print(f"  {CY}[{k}]{R}  {badge_c}{B}{m['badge']}{R}  {WH}{m['name']}{R}")
        print(f"       {GY}{m['desc']}{R}\n")

    if confirm("\n  Load a model now?", default=True):
        from modules.settings import load_model
        smart_clear()   # keep banner, clear welcome text
        load_model()
    else:
        info("You can load a model anytime from Settings [5].")
        pause()


def _exit():
    fix_terminal()  # Ensure terminal is clean before exit
    print(f"\n  {CY}Goodbye! 👋{R}\n")
    sys.exit(0)


if __name__ == "__main__":
    main()