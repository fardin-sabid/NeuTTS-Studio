"""
NeuTTS Studio — Fine Tuning Module
Configure and launch training jobs on NeuTTS-Nano SafeTensors.
"""

from pathlib import Path
from core.ui import (
    print_section, menu, ask, confirm,
    success, error, warning, info, working, pause, divider,
    CY, GY, WH, GR, YL, RD, B, R
)
from core.engine import engine
from core.progress import StepTracker, Spinner
from config import FINETUNE_DEFAULTS


def run():
    while True:
        print_section("Fine Tuning", subtitle="train on custom data")

        print(f"""{GY}
  Fine tuning adapts the model to new voices or languages.
  Requires: NeuTTS-Nano SafeTensors · GPU (16GB+ VRAM recommended)
{R}""")

        choice = menu(
            "Fine Tuning",
            {
                "1": {"label": "New training job",      "icon": "🚀", "desc": "Configure and launch a finetuning run"},
                "2": {"label": "Resume checkpoint",     "icon": "↩️",  "desc": "Continue training from a saved checkpoint"},
                "3": {"label": "View default config",   "icon": "⚙️",  "desc": "See all training hyperparameters"},
                "4": {"label": "Dataset guide",         "icon": "📚", "desc": "What data formats are supported"},
            }
        )
        if choice == "0":
            return
        elif choice == "1":
            _new_job()
        elif choice == "2":
            _resume()
        elif choice == "3":
            _show_config()
        elif choice == "4":
            _dataset_guide()


def _new_job():
    print_section("Configure Training Job")

    if engine.loaded and engine.is_gguf:
        warning("Fine tuning requires SafeTensors model.")
        info("Go to Settings → Load Model → NeuTTS-Nano SafeTensors.")
        pause()
        return

    cfg = {}
    cfg["restore_from"]  = ask("Base model", default="neuphonic/neutts-nano")
    cfg["save_root"]     = ask("Output directory", default="./finetune_output")
    cfg["run_name"]      = ask("Run name", default="my-finetune")
    cfg["dataset"]       = ask("Dataset (HuggingFace repo or local)", default="neuphonic/emilia-yodas-english-neucodec")
    cfg["dataset_split"] = ask("Dataset split", default="train[:2000]")
    cfg["language"]      = ask("Language code", default="en-us")
    cfg["lr"]            = ask("Learning rate", default=str(FINETUNE_DEFAULTS["lr"]))
    cfg["max_steps"]     = ask("Max steps", default=str(FINETUNE_DEFAULTS["max_steps"]))
    cfg["batch_size"]    = ask("Batch size per device", default=str(FINETUNE_DEFAULTS["batch_size"]))

    full = {
        "restore_from":               cfg["restore_from"],
        "save_root":                  cfg["save_root"],
        "run_name":                   cfg["run_name"],
        "dataset":                    cfg["dataset"],
        "dataset_split":              cfg["dataset_split"],
        "language":                   cfg["language"],
        "codebook_size":              FINETUNE_DEFAULTS["codebook_size"],
        "max_seq_len":                FINETUNE_DEFAULTS["max_seq_len"],
        "lr":                         float(cfg["lr"]),
        "lr_scheduler_type":          FINETUNE_DEFAULTS["lr_scheduler"],
        "warmup_ratio":               FINETUNE_DEFAULTS["warmup_ratio"],
        "per_device_train_batch_size": int(cfg["batch_size"]),
        "max_steps":                  int(cfg["max_steps"]),
        "logging_steps":              FINETUNE_DEFAULTS["logging_steps"],
        "save_steps":                 FINETUNE_DEFAULTS["save_steps"],
        "seed":                       FINETUNE_DEFAULTS["seed"],
    }

    config_dir  = Path(cfg["save_root"])
    config_dir.mkdir(parents=True, exist_ok=True)
    config_path = config_dir / f"{cfg['run_name']}_config.yaml"
    _write_yaml(config_path, full)

    success(f"Config saved → {CY}{config_path}{R}")
    print(f"""
  {CY}Summary:{R}
  {GY}Model    {R}  {full['restore_from']}
  {GY}Dataset  {R}  {full['dataset']} ({full['dataset_split']})
  {GY}Steps    {R}  {full['max_steps']:,}
  {GY}LR       {R}  {full['lr']}
  {GY}Output   {R}  {full['save_root']}/{full['run_name']}
""")

    if confirm("Launch training now?"):
        _launch(config_path)
    else:
        info(f"To run later:  python -m examples.finetune {config_path}")

    pause()


def _resume():
    print_section("Resume Training")
    path = ask("Path to config .yaml file")
    if not path or not Path(path).exists():
        error("Config file not found.")
        pause()
        return
    if confirm("Resume from this config?"):
        _launch(Path(path))
    pause()


def _show_config():
    print_section("Default Training Config")
    print()
    for k, v in FINETUNE_DEFAULTS.items():
        print(f"  {CY}{k:<25}{R}  {WH}{v}{R}")
    print()
    pause()


def _dataset_guide():
    print_section("Dataset Guide")
    print(f"""{GY}
  Official Datasets (HuggingFace):
  ─────────────────────────────────────────────────
  · neuphonic/emilia-yodas-english-neucodec
    English · pre-encoded with NeuCodec

  Custom Dataset Requirements:
  ─────────────────────────────────────────────────
  Must contain two columns:
  · "text"   — transcript string
  · "codes"  — NeuCodec-encoded audio tokens (int list)

  Automatic Data Filters (applied during training):
  ─────────────────────────────────────────────────
  ✗  Samples containing numbers
  ✗  Samples containing acronyms (ALL CAPS / A.B.C.)
  ✗  Samples not ending in  .  ?  !  ,
  ✗  Samples containing £ or $ symbols

  Tip: Keep samples between 3–15 seconds for best quality.
{R}""")
    pause()


def _launch(config_path: Path):
    import subprocess
    warning("Training running in foreground. Ctrl+C to stop.")
    print()
    try:
        subprocess.run(["python", "-m", "examples.finetune", str(config_path)], check=False)
        success("Training completed!")
    except KeyboardInterrupt:
        warning("Training interrupted.")
    except FileNotFoundError:
        error("Training script not found. Run from NeuTTS repo root.")


def _write_yaml(path: Path, cfg: dict):
    lines = [f'{k}: "{v}"' if isinstance(v, str) else f"{k}: {v}" for k, v in cfg.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
