"""
NeuTTS Studio Core Modules
-------------------------
Core functionality including TTS engine, audio processing, chunking, and UI.
"""

# Lazy imports to avoid loading heavy dependencies at module level
def get_engine():
    """Get the TTS engine singleton instance."""
    from .engine import engine
    return engine

def get_audio():
    """Get audio utilities module."""
    from . import audio
    return audio

def get_chunker():
    """Get text chunker module."""
    from . import chunker
    return chunker

def get_ui():
    """Get UI module."""
    from . import ui
    return ui

def get_progress():
    """Get progress display module."""
    from . import progress
    return progress

__all__ = [
    'get_engine',
    'get_audio',
    'get_chunker',
    'get_ui',
    'get_progress',
]