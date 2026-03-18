"""
NeuTTS Studio Modules
--------------------
Feature modules including TTS, voice cloning, streaming, fine-tuning, and settings.
"""

# Lazy imports - modules are imported only when needed
def get_tts():
    """Get TTS module."""
    from . import tts
    return tts

def get_cloning():
    """Get voice cloning module."""
    from . import cloning
    return cloning

def get_streaming():
    """Get streaming module."""
    from . import streaming
    return streaming

def get_finetuning():
    """Get fine-tuning module."""
    from . import finetuning
    return finetuning

def get_settings():
    """Get settings module."""
    from . import settings
    return settings

def get_voice_selector():
    """Get voice selector module."""
    from . import voice_selector
    return voice_selector

__all__ = [
    'get_tts',
    'get_cloning', 
    'get_streaming',
    'get_finetuning',
    'get_settings',
    'get_voice_selector',
]