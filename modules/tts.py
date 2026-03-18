"""
NeuTTS Studio — Text to Speech Module
Smart chunking, dynamic progress bars, flexible output options.
"""

import sys
import time
from pathlib import Path
from core.ui import (
    print_section, menu, ask, ask_multiline, confirm,
    success, error, warning, info, working, pause, divider,
    CY, GY, WH, GR, MG, B, R
)
from core.engine import engine
from core.chunker import chunk_text, chunk_summary
from core.audio import stitch, save, save_chunks, duration
from core.progress import ChunkProgress, Spinner, StepTracker, InputSafeSpinner
from modules.voice_selector import pick_voice


def run():
    while True:
        print_section("Text to Speech", subtitle="with smart chunking")

        if not engine.loaded:
            error("No model loaded! Go to Settings → Load Model first.")
            pause("Press Enter to continue", clear_screen=False)
            return

        # ── Input mode ────────────────────────────────────────────────────
        mode = menu(
            "Choose Input Mode",
            {
                "1": {"label": "Single line",        "icon": "✏️",  "desc": "Type a short sentence or paragraph"},
                "2": {"label": "Multi-paragraph",    "icon": "📝",  "desc": "Paste or type longer text (Enter twice to finish)"},
                "3": {"label": "Load from .txt file","icon": "📂",  "desc": "Read text from a file on disk"},
            },
            header_info=f"Active model: {engine.model_info['name']}"
        )
        if mode == "0":
            return

        # ── Get text ──────────────────────────────────────────────────────
        text = _get_text(mode)
        if not text:
            continue

        # ── Chunk preview ─────────────────────────────────────────────────
        summary = chunk_summary(text)
        chunks  = summary["chunks"]
        n       = summary["total_chunks"]

        print(f"\n  {CY}Chunk Preview{R}  ({n} chunk{'s' if n > 1 else ''}  ·  {len(text)} chars total)\n")
        for i, ch in enumerate(chunks, 1):
            preview = ch[:65] + "..." if len(ch) > 65 else ch
            print(f"  {GY}[{i:02d}]{R}  {GY}({len(ch):3d}c){R}  {WH}{preview}{R}")
        print()

        # Small delay before confirm
        time.sleep(0.2)
        sys.stdout.flush()
        sys.stdin.flush()

        if not confirm("Proceed with synthesis?"):
            continue

        # ── Pick voice ────────────────────────────────────────────────────
        voice = pick_voice()
        if not voice:
            info("No voice selected. Returning to menu.")
            pause("Press Enter to continue", clear_screen=False)
            continue

        ref_codes, original_ref_text, voice_name = voice

        # ── Output options ────────────────────────────────────────────────
        out_choice = menu(
            "Output Options",
            {
                "1": {"label": "Merged single file",          "icon": "🎵", "desc": "All chunks joined into one .wav"},
                "2": {"label": "Individual chunk files",      "icon": "🗂️", "desc": "Each chunk saved separately"},
                "3": {"label": "Both merged + chunk files",   "icon": "📦", "desc": "Save everything"},
            }
        )
        if out_choice == "0":
            continue

        # Stop any running spinners before asking for input
        sys.stdout.write("\r\033[K")  # Clear the line
        sys.stdout.flush()
        time.sleep(0.1)  # Give terminal a moment to settle

        out_name = ask("Output filename (no extension)", default=f"tts_{voice_name}")

        # ── Run synthesis ─────────────────────────────────────────────────
        audio_chunks = _synthesize(chunks, ref_codes, original_ref_text, voice_name)
        if not audio_chunks:
            error("Synthesis failed. No audio generated.")
            pause("Press Enter to continue", clear_screen=False)
            continue

        # ── Save output ───────────────────────────────────────────────────
        _save(audio_chunks, out_choice, out_name)

        if not confirm("\n  Generate more audio?"):
            return


def _get_text(mode: str) -> str | None:
    if mode == "1":
        t = ask("Enter your text")
        return t if t else None

    elif mode == "2":
        t = ask_multiline("Enter your text")
        return t if t else None

    elif mode == "3":
        path = ask("Path to .txt file")
        try:
            t = Path(path).read_text(encoding="utf-8").strip()
            info(f"Loaded {len(t):,} characters.")
            return t if t else None
        except Exception as e:
            error(str(e))
            return None


def _synthesize(chunks: list[str], ref_codes, original_ref_text: str, voice_name: str = "") -> list:
    print()
    prog = ChunkProgress(total_chunks=len(chunks))
    audio_chunks = []

    for i, chunk in enumerate(chunks, 1):
        prog.start_chunk(chunk, i)
        try:
            t0 = time.time()
            # Use the original transcript as reference (exactly like test does)
            audio = engine.infer(chunk, ref_codes, original_ref_text)
            dur = duration(audio)
            prog.finish_chunk(dur, chunk)
            audio_chunks.append(audio)
        except Exception as e:
            print()
            error(f"Chunk {i} failed: {e}")
            import traceback
            traceback.print_exc()
            if not confirm("  Skip and continue?"):
                return []

    prog.finish()
    return audio_chunks


def _save(audio_chunks: list, choice: str, base_name: str):
    if choice in ("1", "3"):
        # Use InputSafeSpinner instead of regular Spinner
        spinner = InputSafeSpinner("Merging chunks...")
        spinner.__enter__()
        try:
            merged = stitch(audio_chunks)
            spinner.stop_for_input()  # Stop before any potential input
        except:
            spinner.__exit__(None, None, None)
            raise
        
        path = save(merged, category="tts", name=base_name)
        dur = duration(merged)
        success(f"Saved → {CY}{path}{R}")
        print(f"  {GY}Duration: {dur:.2f}s  ·  Folder: data/outputs/tts/{R}\n")

    if choice in ("2", "3"):
        spinner = InputSafeSpinner("Saving chunk files...")
        spinner.__enter__()
        try:
            paths = save_chunks(audio_chunks, category="tts", base_name=base_name)
            spinner.stop_for_input()  # Stop before printing
        except:
            spinner.__exit__(None, None, None)
            raise
            
        success(f"Saved {len(paths)} chunk file(s) → {CY}data/outputs/tts/{R}")
        for p in paths:
            print(f"  {GY}·  {p.name}{R}")
        print()

    # Don't clear screen after saving
    pause("Press Enter to continue", clear_screen=False)