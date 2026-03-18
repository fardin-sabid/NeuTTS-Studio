import sys
"""
NeuTTS Studio — Settings Module
Model loading, output management, app info.
"""

from core.ui import (
    print_section, menu, ask, confirm,
    success, error, warning, info, working, pause, divider,
    CY, GY, WH, GR, YL, B, R
)
from core.engine import engine
from core.audio import all_outputs, list_outputs
from core.progress import StepTracker, Spinner
from config import MODELS, APP_NAME, APP_VERSION, OUTPUTS


def run():
    while True:
        print_section("Settings")

        status = (
            f"{GR}{B}{engine.model_info['name']}{R}  {GY}({engine.model_info['type'].upper()}){R}"
            if engine.loaded
            else f"{YL}No model loaded{R}"
        )
        print(f"  Model:  {status}\n")

        choice = menu(
            "Settings",
            {
                "1": {"label": "Load / Switch Model",   "icon": "🔄", "desc": "Download and activate a model"},
                "2": {"label": "View output files",     "icon": "📂", "desc": "Browse generated audio by category"},
                "3": {"label": "Clear outputs",         "icon": "🗑️",  "desc": "Delete generated audio files"},
                "4": {"label": "About",                 "icon": "ℹ️",  "desc": f"{APP_NAME} v{APP_VERSION}"},
            }
        )
        if choice == "0":
            return
        elif choice == "1":
            load_model()
        elif choice == "2":
            _view_outputs()
        elif choice == "3":
            _clear_outputs()
        elif choice == "4":
            _about()


def load_model():
    """Public — also called from main on first launch."""
    print_section("Load Model")

    opts = {
        k: {
            "label": v["name"],
            "icon":  "🔷" if v["type"] == "safetensors" else "⚡",
            "desc":  v["desc"],
            "badge": v["badge"],
        }
        for k, v in MODELS.items()
    }
    choice = menu("Select Model", opts)
    if choice == "0":
        return

    info_m = MODELS[choice]

    dev_choice = menu(
        "Select Device",
        {
            "1": {"label": "CPU", "icon": "💻", "desc": "Recommended for most devices"},
            "2": {"label": "GPU", "icon": "⚡", "desc": "CUDA GPU for faster inference"},
        }
    )
    if dev_choice == "0":
        return

    device = "cpu" if dev_choice == "1" else "gpu"

    print(f"""
  {CY}About to load:{R}
  {GY}Model   {R}  {info_m['name']}
  {GY}Repo    {R}  {info_m['repo']}
  {GY}Device  {R}  {device.upper()}
  {GY}Note    {R}  First run downloads from HuggingFace
""")

    if not confirm("Proceed?"):
        return

    # Clear once after Y — redraw banner then show loading status cleanly
    from core.ui import smart_clear
    from core.progress import DownloadSection
    smart_clear()

    print(f"""
  {CY}{'─' * 54}{R}
  {CY}{B}  Loading: {info_m['name']}{R}
  {GY}  Repo:    {info_m['repo']}{R}
  {GY}  Device:  {device.upper()}{R}
  {CY}{'─' * 54}{R}
""")
    sys.stdout.flush()

    try:
        with DownloadSection("Downloading & loading — please wait"):
            engine.load(choice, device)

        success(f"Model ready: {info_m['name']}")
        if info_m["streaming"]:
            info("Streaming mode is available with this model.")
        if info_m["finetune"]:
            info("Fine tuning is available with this model.")
    except Exception as e:
        error(f"Failed to load model: {e}")

    pause()


def _view_outputs():
    print_section("Output Files")

    outputs = all_outputs()
    total   = sum(len(v) for v in outputs.values())

    if total == 0:
        info("No output files yet. Generate some audio first!")
        pause()
        return

    for cat, files in outputs.items():
        if not files:
            continue
        print(f"\n  {CY}{B}{cat.upper()}{R}  {GY}→ data/outputs/{cat}/{R}\n")
        for f in files[:10]:
            size = f.stat().st_size / 1024
            print(f"  {GY}·{R}  {WH}{f.name:<40}{R}  {GY}{size:.1f} KB{R}")
        if len(files) > 10:
            print(f"  {GY}    ... and {len(files) - 10} more{R}")

    print(f"\n  {GY}Total: {total} file(s){R}")
    pause()


def _clear_outputs():
    print_section("Clear Outputs")

    cats = {
        "1": "tts",
        "2": "streaming",
        "3": "cloning",
        "4": "all",
    }
    choice = menu(
        "Which outputs to clear?",
        {
            "1": {"label": "TTS outputs",       "icon": "🗣️"},
            "2": {"label": "Streaming outputs",  "icon": "⚡"},
            "3": {"label": "Cloning test audio", "icon": "🎤"},
            "4": {"label": "All outputs",        "icon": "🗑️", "desc": "Clear everything"},
        }
    )
    if choice == "0":
        return

    to_clear = list(OUTPUTS.keys()) if cats[choice] == "all" else [cats[choice]]
    count    = sum(len(list_outputs(c)) for c in to_clear)

    if count == 0:
        info("Nothing to delete.")
        pause()
        return

    warning(f"Will delete {count} file(s). This cannot be undone.")
    if not confirm("Are you sure?", default=False):
        return

    deleted = 0
    with Spinner("Deleting files..."):
        for cat in to_clear:
            for f in list_outputs(cat):
                try:
                    f.unlink()
                    deleted += 1
                except Exception:
                    pass

    success(f"Deleted {deleted} file(s).")
    pause()


def _about():
    print_section(f"{APP_NAME} v{APP_VERSION}")
    print(f"""{GY}
  Built on NeuTTS by Neuphonic
  github.com/neuphonic/neutts  ·  neuphonic.com

  ─────────────────────────────────────────────
  👨‍💻  NeuTTS Studio Interface by Fardin Sabid
  🇧🇩  From Bangladesh, for the World
  ─────────────────────────────────────────────

  Models:
  · NeuTTS-Nano SafeTensors  —  Full precision · Multilingual · Finetuneable
  · NeuTTS-Nano Q8 GGUF      —  8-bit quantized · Streaming
  · NeuTTS-Nano Q4 GGUF      —  4-bit quantized · Fastest

  Architecture:
  · LLM backbone (Speech Language Model)
  · NeuCodec (50Hz neural audio codec)
  · espeak-ng (text → phonemes)

  Features:
  · Smart 4-tier text chunking (unlimited text length)
  · Instant voice cloning (3s reference minimum)
  · Real-time streaming with live RTF stats
  · Finetuning pipeline (SafeTensors only)
  · Perth watermarking on all outputs
  · Dedicated output folders per category

  ⚡  After 20+ hours of debugging — it just works!
{R}""")
    pause()


def show_model_storage():
    """Show how much space downloaded models are using."""
    from config import MODELS_DIR
    from core.ui import print_section, info, pause, CY, GY, WH, GR, R, B

    print_section("Model Storage")

    size = engine.model_cache_size()
    print(f"  {GY}Location:{R}  {CY}{MODELS_DIR}{R}")
    print(f"  {GY}Size:    {R}  {WH}{B}{size}{R}")
    print()

    files = list(MODELS_DIR.rglob("*.gguf")) + list(MODELS_DIR.rglob("*.safetensors"))
    if files:
        print(f"  {CY}Downloaded model files:{R}\n")
        for f in files:
            sz = f.stat().st_size / 1024 ** 2
            print(f"  {GY}·{R}  {WH}{f.name:<50}{R}  {GY}{sz:.1f} MB{R}")
    else:
        info("No model files downloaded yet.")

    pause()
