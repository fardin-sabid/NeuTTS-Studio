"""
NeuTTS Studio — Streaming Mode
Real-time audio generation with live playback and progress display.
"""

import time
import numpy as np
import queue
import threading
import sys
from core.ui import (
    print_section, menu, ask, confirm,
    success, error, warning, info, working, pause, divider,
    CY, GY, WH, GR, YL, MG, B, R
)
from core.engine import engine
from core.audio import save, duration
from core.progress import Spinner
from modules.voice_selector import pick_voice


def run():
    while True:
        print_section("Streaming Mode", subtitle="real-time generation")

        if not engine.loaded:
            error("No model loaded! Go to Settings → Load Model first.")
            pause()
            return

        if not engine.supports_streaming:
            warning("Streaming requires a GGUF model (Q4 or Q8).")
            info(f"Current: {engine.model_info['name']}")
            info("Go to Settings → Load Model → Select Q4 or Q8.")
            pause()
            return

        mode = menu(
            "Streaming Options",
            {
                "1": {"label": "Stream to speakers",        "icon": "🔊", "desc": "Live playback as audio generates"},
                "2": {"label": "Stream and save",           "icon": "💾", "desc": "Generate and save without playback"},
                "3": {"label": "Stream, play, and save",    "icon": "🎙️", "desc": "Live playback + save to file"},
            },
            header_info=f"Model: {engine.model_info['name']}  ·  Streaming ready"
        )
        if mode == "0":
            return

        text = ask("Enter text to stream")
        if not text:
            continue

        voice = pick_voice()
        if not voice:
            continue
        ref_codes, ref_text, voice_name = voice

        if mode == "1":
            _stream_play(text, ref_codes, ref_text, voice_name)
        elif mode == "2":
            _stream_save(text, ref_codes, ref_text, voice_name)
        elif mode == "3":
            _stream_play_save(text, ref_codes, ref_text, voice_name)

        if not confirm("\n  Stream more?"):
            return


def _stream_play(text, ref_codes, ref_text, voice_name):
    pa = _require_pyaudio()
    if not pa:
        return

    stream, p = _open_stream(pa)
    q = queue.Queue()

    def player():
        while True:
            item = q.get()
            if item is None:
                q.task_done(); break
            _write_audio(stream, item)
            q.task_done()

    t = threading.Thread(target=player, daemon=True)
    t.start()
    _run_stream(text, ref_codes, ref_text, q, save_name=None)
    _tail(q, stream)
    t.join()
    _close_stream(stream, p)


def _stream_save(text, ref_codes, ref_text, voice_name):
    chunks = []
    q = queue.Queue()

    def collector():
        while True:
            item = q.get()
            if item is None:
                q.task_done(); break
            chunks.append(item)
            q.task_done()

    t = threading.Thread(target=collector, daemon=True)
    t.start()
    _run_stream(text, ref_codes, ref_text, q, save_name=None)
    q.put(None)
    t.join()

    if chunks:
        merged = np.concatenate(chunks)
        path   = save(merged, "streaming", name=f"stream_{voice_name}")
        success(f"Saved → {CY}{path.name}{R}  {GY}({duration(merged):.2f}s){R}")
        info("Location: data/outputs/streaming/")
    pause()


def _stream_play_save(text, ref_codes, ref_text, voice_name):
    pa = _require_pyaudio()
    if not pa:
        return

    stream, p = _open_stream(pa)
    chunks = []
    q = queue.Queue()

    def worker():
        while True:
            item = q.get()
            if item is None:
                q.task_done(); break
            chunks.append(item)
            _write_audio(stream, item)
            q.task_done()

    t = threading.Thread(target=worker, daemon=True)
    t.start()
    _run_stream(text, ref_codes, ref_text, q, save_name=None)
    _tail(q, stream)
    t.join()
    _close_stream(stream, p)

    if chunks:
        merged = np.concatenate(chunks)
        path   = save(merged, "streaming", name=f"stream_{voice_name}")
        success(f"Saved → {CY}{path.name}{R}  {GY}({duration(merged):.2f}s){R}")
        info("Location: data/outputs/streaming/")
    pause()


def _run_stream(text, ref_codes, ref_text, q, save_name):
    print(f"\n  {CY}{'─' * 54}{R}")
    print(f"  {MG}{B}Streaming...{R}\n")

    chunk_n = 0
    total_samples = 0
    total_gen = 0.0
    t_start = time.perf_counter()
    last = t_start

    try:
        for chunk in engine.infer_stream(text, ref_codes, ref_text):
            chunk_n += 1
            now = time.perf_counter()
            gen_t = now - last
            total_gen += gen_t
            last = now
            total_samples += len(chunk)

            dur_ms = len(chunk) / engine.sample_rate * 1000
            rt = gen_t / (dur_ms / 1000) * 100
            label = "TTFA" if chunk_n == 1 else "    "

            sys.stdout.write(
                f"  {CY}[{chunk_n:02d}]{R} {label}"
                f"  {WH}{dur_ms:6.1f}ms audio{R}"
                f"  {GY}gen {gen_t*1000:.0f}ms{R}"
                f"  {GR if rt < 100 else YL}{rt:.0f}% RT{R}\n"
            )
            sys.stdout.flush()
            q.put(chunk)

    except Exception as e:
        error(f"Streaming error: {e}")
        q.put(None)
        return

    total_dur = total_samples / engine.sample_rate
    wall = time.perf_counter() - t_start
    rtf  = wall / total_dur if total_dur > 0 else 0

    print(f"\n  {CY}{'─' * 54}{R}")
    print(f"  {GR}{B}✓{R}  {total_dur:.2f}s audio  ·  {wall:.2f}s wall time  ·  RTF {rtf:.2f}\n")
    q.put(None)


def _require_pyaudio():
    try:
        import pyaudio
        return pyaudio
    except ImportError:
        error("pyaudio is required for speaker playback.")
        info("Install: pip install pyaudio")
        pause()
        return None


def _open_stream(pa):
    p      = pa.PyAudio()
    stream = p.open(format=pa.paInt16, channels=1, rate=engine.sample_rate, output=True)
    return stream, p


def _write_audio(stream, chunk):
    audio = (chunk * 32767).astype(np.int16).tobytes()
    BLOCK = 2048
    for i in range(0, len(audio), BLOCK):
        stream.write(audio[i:i + BLOCK], exception_on_underflow=False)


def _tail(q, stream):
    import numpy as np
    tail = np.zeros(int(0.25 * engine.sample_rate), dtype=np.float32)
    q.put(tail)
    q.put(None)
    q.join()


def _close_stream(stream, p):
    stream.stop_stream()
    stream.close()
    p.terminate()
