---
name: 🐛 Bug Report
about: Report something that's not working correctly in NeuTTS Studio
title: '[BUG] '
labels: bug
assignees: ''

---

## 🐛 Describe the Bug
A clear and concise description of what the bug is.

## 🔄 Steps To Reproduce
1. Go to '...' menu option
2. Select '....' model
3. Enter text: '....'
4. See error

## ✅ Expected Behavior
What should have happened instead?

## 📸 Screenshots / Error Logs
Here's a **fake error log example** for the bug report:

## 📸 Screenshots / Error Logs
```
Traceback (most recent call last):
  File "/storage/emulated/0/NeuTTS-Studio/run.py", line 45, in <module>
    main()
  File "/storage/emulated/0/NeuTTS-Studio/run.py", line 38, in main
    choice = _main_menu()
  File "/storage/emulated/0/NeuTTS-Studio/run.py", line 82, in _main_menu
    return menu("Main Menu", options, back_label="Exit NeuTTS Studio")
  File "/storage/emulated/0/NeuTTS-Studio/core/ui.py", line 245, in menu
    raw = input(f"  {CY}{B}Select ❯{R} ").strip()
  File "/root/ai-env/lib/python3.11/site-packages/termios.py", line 45, in input
    return sys.__stdin__.readline()
KeyboardInterrupt
```

Or a more detailed one:

```
Loading encoder model...
    ✓ Encoder loaded in 16.5s

    Loading audio file...
    ✓ Audio loaded: 48000Hz, 12.3s in 8.2s

    Resampling from 48000Hz to 16000Hz...
    ✗ Error during resampling: 'resampy' not installed

    Failed to encode voice: No module named 'resampy'

----------------------------------------
  ✗  Voice cloning failed: 'resampy' not installed
  Please install: pip install resampy
```

Or for TTS generation:

```
Processing 3 chunk(s)...

  [Chunk 1/3] Hello, this is a test of the text to speech system.
    Generating... ⠋ 2.3s
  ✓  2.3s  audio:1.8s  RTF:1.28

  [Chunk 2/3] The model should generate natural sounding speech.
    Generating... ⠙ 45.6s
  ✗  Chunk 2 failed: CUDA out of memory. Tried to allocate 2.5 GiB

  ❯  Skip and continue? [Y/n]: n

  Generation stopped by user.
```

## 🖥️ Environment Details
| | |
|---|---|
| **Platform** | [e.g. Android/Termux, iOS/iSH, Linux, macOS, Windows/WSL2] |
| **Device** | [e.g. Galaxy S23, iPhone 14, Raspberry Pi 4, PC] |
| **OS Version** | [e.g. Android 14, iOS 17, Ubuntu 22.04] |
| **Python Version** | [e.g. 3.10, 3.11, 3.12, 3.13] |
| **NeuTTS Studio Version** | [e.g. v2.0.0] |
| **Model Used** | [e.g. SafeTensors, Q8 GGUF, Q4 GGUF] |

## 📱 Android-Specific Details (if applicable)
- **Termux Version:**
- **Ubuntu via proot-distro?** [Yes/No]
- **Storage Permission Granted?** [Yes/No]
- **RAM Available:**

## 🍎 iOS-Specific Details (if applicable)
- **iSH or a-Shell:**
- **Alpine Linux Version:**

## 🔧 Attempted Solutions
What have you tried to fix the issue?

## 📝 Additional Context
Add any other context about the problem here.