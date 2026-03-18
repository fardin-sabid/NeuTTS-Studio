"""
NeuTTS Studio — Advanced Interactive UI
Dynamic menus, color rendering, prompts, and terminal utilities.
"""

import os
import sys
import shutil
import time
from config import APP_NAME, APP_VERSION, MODELS

# ─── ANSI Color Codes ─────────────────────────────────────────────────────────
R  = "\033[0m"       # reset
B  = "\033[1m"       # bold
DM = "\033[2m"       # dim
IT = "\033[3m"       # italic
UN = "\033[4m"       # underline

# Foreground
CY  = "\033[96m"     # cyan
GR  = "\033[92m"     # green
YL  = "\033[93m"     # yellow
RD  = "\033[91m"     # red
MG  = "\033[95m"     # magenta
BL  = "\033[94m"     # blue
WH  = "\033[97m"     # white
GY  = "\033[90m"     # gray

# Background
BGC = "\033[46m"     # bg cyan
BGG = "\033[42m"     # bg green
BGR = "\033[41m"     # bg red
BGY = "\033[43m"     # bg yellow
BGM = "\033[45m"     # bg magenta
BGN = "\033[40m"     # bg black


def _term_width() -> int:
    return shutil.get_terminal_size((80, 24)).columns


def clr():
    os.system("cls" if os.name == "nt" else "clear")


# ── Persistent banner state ───────────────────────────────────────────────────
_banner_model_name: str = ""
_banner_model_type: str = ""


def set_banner_state(model_name: str = "", model_type: str = ""):
    """Call this whenever model changes so banner stays in sync."""
    global _banner_model_name, _banner_model_type
    _banner_model_name = model_name
    _banner_model_type = model_type


def _compact_banner():
    """
    Compact one-line banner always shown at top of every screen.
    Never disappears — redrawn after every clear.
    """
    w = min(_term_width(), 72)

    if _banner_model_name:
        badge_c = GR if _banner_model_type == "safetensors" else YL
        model_str = f"{badge_c}{B} {_banner_model_name} {R}"
    else:
        model_str = f"{RD} No model loaded {R}"

    left  = f"  {CY}{B}NeuTTS Studio{R}"
    right = f"Model: {model_str}"
    gap   = w - 16 - len(_banner_model_name) - 2

    print(f"{CY}{'═' * w}{R}")
    print(f"{left}  {GY}v2.0.0{R}{'  ' + right}")
    print(f"{CY}{'═' * w}{R}")


def smart_clear():
    """Clear screen and immediately redraw the persistent banner."""
    clr()
    _compact_banner()
    print()


# ─── Banner ───────────────────────────────────────────────────────────────────
def print_banner(model_name: str = None, model_type: str = None):
    set_banner_state(model_name or "", model_type or "")
    clr()
    
    # Simple colored banner without boxes - NeuTTS version
    print(f"\n{MG}{B}███╗   ██╗███████╗██╗   ██╗████████╗████████╗███████╗{R}")
    print(f"{MG}{B}████╗  ██║██╔════╝██║   ██║╚══██╔══╝╚══██╔══╝██╔════╝{R}")
    print(f"{MG}{B}██╔██╗ ██║█████╗  ██║   ██║   ██║      ██║   ███████╗{R}")
    print(f"{MG}{B}██║╚██╗██║██╔══╝  ██║   ██║   ██║      ██║   ╚════██║{R}")
    print(f"{MG}{B}██║ ╚████║███████╗╚██████╔╝   ██║      ██║   ███████║{R}")
    print(f"{MG}{B}╚═╝  ╚═══╝╚══════╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝{R}\n")
    
    # Model status line
    if model_name and model_type:
        badge_color = GR if model_type == "safetensors" else YL
        print(f"  Model: {badge_color}{B}{model_name}{R}")
    else:
        print(f"  {RD}No model loaded — go to Settings{R}")
    
    # Version
    print(f"  {GY}NeuTTS Studio v{APP_VERSION}{R}\n")


# ─── Section Headers ──────────────────────────────────────────────────────────
def print_section(title: str, subtitle: str = "", clear: bool = True):
    if clear:
        smart_clear()
    w = min(_term_width(), 64)
    line = "═" * (w - 2)
    print(f"\n  {CY}{B}╔{line}╗{R}")
    print(f"  {CY}{B}║{R}  {B}{WH}{title}{R}{'  ' + GY + subtitle + R if subtitle else ''}")
    print(f"  {CY}{B}╚{line}╝{R}\n")


def divider(style: str = "thin"):
    char = "─" if style == "thin" else "═"
    print(f"  {GY}{char * 56}{R}")


# ─── Status Messages ──────────────────────────────────────────────────────────
def success(msg: str): print(f"\n  {BGG}{B} ✓ {R} {GR}{B}{msg}{R}")
def error(msg: str):   print(f"\n  {BGR}{B} ✗ {R} {RD}{B}{msg}{R}")
def warning(msg: str): print(f"\n  {BGY}{B} ! {R} {YL}{B}{msg}{R}")
def info(msg: str):    print(f"\n  {CY}ℹ{R}  {WH}{msg}{R}")
def working(msg: str): print(f"\n  {MG}⚙{R}  {MG}{msg}{R}")


# ─── Input Prompts ────────────────────────────────────────────────────────────
def ask(label: str, default: str = "") -> str:
    """Bulletproof input function - no auto-enter, no corruption."""
    hint = f" {GY}[{default}]{R}" if default else ""
    
    # Kill any running spinners
    sys.stdout.write("\r\033[2K\033[1A\r\033[2K")  # Clear 2 lines up
    sys.stdout.flush()
    time.sleep(0.05)
    
    # Simple prompt with no special characters
    print(f"\n  > {WH}{B}{label}{R}{hint}: ", end="")
    sys.stdout.flush()
    
    try:
        # Raw input without any preprocessing
        val = sys.stdin.readline().strip()
        return val if val else default
    except (KeyboardInterrupt, EOFError):
        print()
        raise KeyboardInterrupt


def ask_multiline(label: str) -> str:
    """Multi-line input that won't trigger on paste."""
    print(f"\n  > {WH}{B}{label}{R}")
    print(f"  {GY}  (Paste your text, then press Enter, then Ctrl+D when done){R}")
    print(f"  {GY}  (Or type line by line and press Enter twice){R}")
    
    lines = []
    try:
        while True:
            line = sys.stdin.readline()
            if not line:  # EOF (Ctrl+D)
                break
            line = line.rstrip('\n')
            if not line and lines and lines[-1] == "":
                break
            lines.append(line)
    except (KeyboardInterrupt, EOFError):
        pass
    
    return " ".join(l for l in lines if l).strip()


def confirm(label: str, default: bool = True) -> bool:
    """Fixed confirm function that always works."""
    hint = f"{GR}Y{R}/{GY}n{R}" if default else f"{GY}y{R}/{RD}N{R}"
    
    # Clear any pending input
    sys.stdout.flush()
    sys.stdin.flush()
    time.sleep(0.1)
    
    try:
        val = input(f"\n  {CY}❯{R} {WH}{B}{label}{R} [{hint}]: ").strip().lower()
        if val in ("y", "yes"):
            return True
        elif val in ("n", "no"):
            return False
        return default
    except (KeyboardInterrupt, EOFError):
        print()
        raise KeyboardInterrupt


def pause(msg: str = "Press Enter to continue", clear_screen: bool = False):
    """
    Pause with optional screen clear.
    Args:
        msg: Message to display
        clear_screen: Whether to clear screen after (default False)
    """
    try:
        input(f"\n  {GY}{msg}...{R}")
    except (KeyboardInterrupt, EOFError):
        pass
    
    # Only clear if explicitly requested
    if clear_screen:
        smart_clear()


# ─── Dynamic Interactive Menu ─────────────────────────────────────────────────
def menu(
    title: str,
    options: dict,
    back_label: str = "← Back",
    header_info: str = "",
) -> str:
    """
    Render a rich interactive numbered menu.

    Args:
        title:       Section title shown at top.
        options:     {key: label} or {key: {"label": ..., "desc": ..., "icon": ..., "badge": ...}}
        back_label:  Label for option 0.
        header_info: Optional info line shown below title.

    Returns:
        Selected key string, or "0" for back/exit.
    """
    valid = set(options.keys()) | {"0"}

    while True:
        smart_clear()
        print_section(title, clear=False)

        if header_info:
            print(f"  {GY}{header_info}{R}\n")

        for key, val in options.items():
            if isinstance(val, dict):
                icon  = val.get("icon", " ")
                label = val.get("label", "")
                desc  = val.get("desc", "")
                badge = val.get("badge", "")
                badge_str = f" {BGC}{B} {badge} {R}" if badge else ""
                print(f"  {CY}{B}[{key}]{R}  {icon}  {WH}{B}{label}{R}{badge_str}")
                if desc:
                    print(f"        {GY}{desc}{R}")
                print()
            else:
                print(f"  {CY}{B}[{key}]{R}  {WH}{val}{R}")

        divider()
        print(f"\n  {GY}[0]{R}  {GY}{back_label}{R}\n")

        try:
            raw = input(f"  {CY}{B}Select ❯{R} ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            return "0"

        if raw in valid:
            return raw

        error(f"Invalid choice '{raw}'. Please enter one of: {', '.join(sorted(valid))}")
        time.sleep(1)


def radio_menu(title: str, options: list[str], default: int = 0) -> int:
    """
    A numbered list menu that returns the selected index.
    options: list of label strings
    Returns selected index (0-based), or -1 if cancelled.
    """
    opts = {str(i + 1): opt for i, opt in enumerate(options)}
    choice = menu(title, opts)
    if choice == "0":
        return -1
    return int(choice) - 1