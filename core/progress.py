"""
NeuTTS Studio — True Real-Time Progress
Updates continuously so you can watch it fill up!
"""

import sys
import time
import threading
import shutil

# ─── Colors ───────────────────────────────────────────────────────────────────
CY = "\033[96m"
GR = "\033[92m"
YL = "\033[93m"
RD = "\033[91m"
MG = "\033[95m"
GY = "\033[90m"
WH = "\033[97m"
B  = "\033[1m"
R  = "\033[0m"

DONE_MARK = f"{GR}✓{R}"
FAIL_MARK = f"{RD}✗{R}"
SPINNER_FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]

# Force unbuffered output - CRITICAL for real-time updates
sys.stdout.reconfigure(line_buffering=True)


def _term_width() -> int:
    return shutil.get_terminal_size((80, 24)).columns


# ─── Step Tracker ───────────────────────────────────────────────────────────
class StepTracker:
    """Track named steps with clean status lines."""
    
    def __init__(self, steps: list[str]):
        self.steps = steps
        self.current = 0
        print()
        for i, s in enumerate(steps, 1):
            print(f"  {GY}[{i}]{R}  {GY}{s}{R}")
        print()
        sys.stdout.flush()

    def step(self, label: str):
        return _StepContext(self, label)


class _StepContext:
    def __init__(self, tracker, label):
        self.tracker = tracker
        self.label = label

    def __enter__(self):
        idx = self.tracker.current + 1
        total = len(self.tracker.steps)
        sys.stdout.write(f"  {CY}[{idx}/{total}]{R}  {WH}{self.label}...\n")
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, *_):
        idx = self.tracker.current + 1
        total = len(self.tracker.steps)
        mark = DONE_MARK if exc_type is None else FAIL_MARK
        sys.stdout.write(f"  {mark}  {GY}[{idx}/{total}]{R}  {WH}{self.label}\033[K\n")
        sys.stdout.flush()
        self.tracker.current += 1


# ─── Spinner ─────────────────────────────────────────────────────────────────
class Spinner:
    """Simple spinner for short operations."""
    
    def __init__(self, label: str = "Working", color: str = CY):
        self.label = label
        self.color = color
        self._stop = threading.Event()
        self._thread = None
        self._frames = SPINNER_FRAMES
    
    def _spin(self):
        i = 0
        while not self._stop.is_set():
            frame = self._frames[i % len(self._frames)]
            sys.stdout.write(f"\r  {self.color}{frame}{R}  {self.label} ")
            sys.stdout.flush()
            time.sleep(0.08)
            i += 1
    
    def start(self):
        self._stop.clear()
        self._thread = threading.Thread(target=self._spin, daemon=True)
        self._thread.start()
        return self
    
    def stop(self, success: bool = True):
        self._stop.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        mark = DONE_MARK if success else FAIL_MARK
        sys.stdout.write(f"\r  {mark}  {self.label}\033[K\n")
        sys.stdout.flush()
    
    def __enter__(self):
        self.start()
        return self
    
    def __exit__(self, exc_type, *_):
        self.stop(success=exc_type is None)


class InputSafeSpinner:
    """Spinner that stops automatically before input()."""
    
    def __init__(self, label: str = "Working", color: str = CY):
        self.label = label
        self.color = color
        self._spinner = None
    
    def __enter__(self):
        self._spinner = Spinner(self.label, self.color)
        self._spinner.start()
        return self
    
    def __exit__(self, exc_type, *_):
        if self._spinner:
            self._spinner.stop(success=exc_type is None)
    
    def stop_for_input(self):
        """Call this before input() to prevent corruption."""
        if self._spinner:
            self._spinner.stop(success=True)
            self._spinner = None
        # Clear the line completely
        sys.stdout.write("\r\033[K")
        sys.stdout.flush()


# ─── TRUE REAL-TIME PROGRESS BAR ─────────────────────────────────────────────
class RealTimeProgress:
    """
    Progress bar that updates continuously so you can watch it fill up.
    Shows percentage, bar, elapsed time, and estimated time remaining.
    Updates every 0.1 seconds for smooth animation.
    """
    
    BAR_FILL = "█"
    BAR_EMPTY = "░"
    BAR_WIDTH = 30  # Nice wide bar for satisfying filling effect
    
    def __init__(self, total: int, label: str = "Generating"):
        self.total = max(total, 1)
        self.label = label
        self.current = 0
        self.start_time = time.time()
        self.last_update = 0
        self._running = True
        self._update_thread = None
        
        # Start the auto-update thread
        self._start_auto_update()
        
        # Initial display
        self._render()
    
    def _start_auto_update(self):
        """Start a thread that updates the display continuously."""
        def updater():
            while self._running and self.current < self.total:
                self._render()
                time.sleep(0.1)  # Update 10 times per second for smooth animation
        self._update_thread = threading.Thread(target=updater, daemon=True)
        self._update_thread.start()
    
    def _render(self):
        """Render the progress bar with current stats."""
        pct = (self.current / self.total) * 100
        filled = int(self.BAR_WIDTH * self.current / self.total)
        empty = self.BAR_WIDTH - filled
        
        # Create the bar with gradient effect
        bar = ""
        for i in range(self.BAR_WIDTH):
            if i < filled:
                if i < filled - 2:
                    bar += f"{GR}{self.BAR_FILL}{R}"
                else:
                    bar += f"{YL}{self.BAR_FILL}{R}"  # Leading edge in yellow
            else:
                bar += f"{GY}{self.BAR_EMPTY}{R}"
        
        # Calculate times
        elapsed = time.time() - self.start_time
        if self.current > 0:
            rate = self.current / elapsed
            eta = (self.total - self.current) / rate if rate > 0 else 0
            eta_str = f" ETA: {eta:.1f}s"
        else:
            eta_str = " ETA: --"
        
        # Build the progress line
        line = (f"\r  {self.label} [{bar}] "
                f"{WH}{pct:3.1f}%{R} "
                f"{GY}[{self.current}/{self.total}]{R} "
                f"{GY}{elapsed:.1f}s{R}{eta_str}")
        
        # Ensure we don't exceed terminal width
        w = _term_width() - 2
        sys.stdout.write(line[:w] + "\033[K")
        sys.stdout.flush()
    
    def update(self, n: int = 1):
        """Update progress by n steps."""
        self.current = min(self.current + n, self.total)
        # Immediate render on update for responsiveness
        self._render()
    
    def finish(self, msg: str = "Complete!"):
        """Finish and show final message."""
        self._running = False
        if self._update_thread and self._update_thread.is_alive():
            self._update_thread.join(timeout=1.0)
        
        self.current = self.total
        self._render()
        
        elapsed = time.time() - self.start_time
        sys.stdout.write(f"\n  {DONE_MARK}  {msg} ({elapsed:.1f}s)\n\n")
        sys.stdout.flush()


# ─── Chunk Progress with Real-Time Updates ────────────────────────────────────
class ChunkProgress:
    """
    Shows each chunk with its own real-time progress.
    You can watch each chunk generate in real-time!
    """
    
    def __init__(self, total_chunks: int):
        self.total = total_chunks
        self.current = 0
        self.start_time = time.time()
        self.chunk_times = []
        self.chunk_durs = []
        self.current_chunk_progress = None
        self.pulse_thread = None
        self.chunk_start = 0  # Initialize chunk_start
        
        print(f"\n  {CY}Processing {total_chunks} chunk(s)...{R}\n")
        sys.stdout.flush()
    
    def start_chunk(self, chunk_text: str, idx: int):
        """Start a new chunk with its own real-time progress."""
        preview = chunk_text[:30] + "..." if len(chunk_text) > 30 else chunk_text
        print(f"  {CY}[Chunk {idx}/{self.total}]{R}  {WH}{preview}{R}")
        
        # Set chunk start time
        self.chunk_start = time.time()
        self.current_chunk_progress = True
        
        # Create a real-time progress bar for this chunk
        self._start_pulse(f"    Generating...")
        sys.stdout.flush()
    
    def _start_pulse(self, label):
        """Start a pulsing indicator for the current chunk."""
        def pulse():
            frames = ["█", "▉", "▊", "▋", "▌", "▍", "▎", "▏", "▎", "▍", "▌", "▋", "▊", "▉"]
            i = 0
            while self.current_chunk_progress:
                frame = frames[i % len(frames)]
                # Use local reference to chunk_start to avoid threading issues
                elapsed = time.time() - self.chunk_start
                sys.stdout.write(f"\r  {label} {GR}{frame}{R} {elapsed:.1f}s\033[K")
                sys.stdout.flush()
                time.sleep(0.1)
                i += 1
        
        self.pulse_thread = threading.Thread(target=pulse, daemon=True)
        self.pulse_thread.start()
    
    def finish_chunk(self, audio_dur: float, chunk_text: str = ""):
        """Finish current chunk and show stats."""
        self.current_chunk_progress = False
        if self.pulse_thread and self.pulse_thread.is_alive():
            self.pulse_thread.join(timeout=1.0)
        
        elapsed = time.time() - self.chunk_start
        rtf = elapsed / audio_dur if audio_dur > 0 else 0
        self.current += 1
        self.chunk_times.append(elapsed)
        self.chunk_durs.append(audio_dur)
        
        # Color code based on performance
        time_color = GR if rtf < 5 else YL if rtf < 10 else RD
        
        # Update the line with completion info
        sys.stdout.write(f"\r  {GR}✓{R}  {time_color}{elapsed:.1f}s{R}  "
                        f"audio:{audio_dur:.2f}s  RTF:{rtf:.1f}\033[K\n")
        sys.stdout.flush()
    
    def finish(self):
        """Show final summary."""
        total_audio = sum(self.chunk_durs)
        total_gen = sum(self.chunk_times)
        rtf = total_gen / total_audio if total_audio > 0 else 0
        total_time = time.time() - self.start_time
        
        print(f"\n  {DONE_MARK}  {GR}Generated {total_audio:.2f}s{R} audio in "
              f"{WH}{total_gen:.1f}s{R}  ·  RTF {YL if rtf > 10 else GR}{rtf:.1f}{R}")
        print(f"  {GY}Total time: {total_time:.1f}s{R}\n")
        sys.stdout.flush()


# ─── Download Section ─────────────────────────────────────────────────────────
class DownloadSection:
    """Lets HuggingFace's tqdm show through."""
    
    def __init__(self, label: str = "Downloading from HuggingFace"):
        self.label = label
    
    def __enter__(self):
        try:
            import tqdm
            tqdm.tqdm.monitor_interval = 0
        except:
            pass
        
        sys.stdout.flush()
        print(f"  {GY}First run only — cached locally after this{R}")
        sys.stdout.flush()
        return self
    
    def __exit__(self, exc_type, *_):
        sys.stdout.flush()
        if exc_type is None:
            print(f"\n  {DONE_MARK}  {GR}Download complete{R}\n")
        else:
            print(f"\n  {FAIL_MARK}  {RD}Failed{R}\n")
        sys.stdout.flush()


# For backward compatibility - alias RealTimeProgress as ProgressBar
ProgressBar = RealTimeProgress