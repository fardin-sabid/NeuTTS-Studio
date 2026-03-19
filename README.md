<div align="center">

# 🎙️ NeuTTS Studio

```diff
+ ███╗   ██╗████████╗███████╗
+ ████╗  ██║╚══██╔══╝██╔════╝
+ ██╔██╗ ██║   ██║   ███████╗
+ ██║╚██╗██║   ██║   ╚════██║
+ ██║ ╚████║   ██║   ███████║
+ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝
       
+       ⚡ NeuTTS Studio ⚡
```

> **The original NeuTTS** is built for researchers and developers.  
> **NeuTTS Studio** is built for everyone — especially mobile users.

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Android](https://img.shields.io/badge/Android-Optimised-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://android.com)
[![iOS](https://img.shields.io/badge/iOS-Optimised-000000?style=for-the-badge&logo=apple&logoColor=white)](https://apple.com)
[![Linux](https://img.shields.io/badge/Linux-Ready-FCC624?style=for-the-badge&logo=linux&logoColor=black)](https://kernel.org)
[![macOS](https://img.shields.io/badge/macOS-Supported-000000?style=for-the-badge&logo=apple&logoColor=white)](https://apple.com)
[![Windows](https://img.shields.io/badge/Windows-WSL2-0078D6?style=for-the-badge&logo=windows&logoColor=white)](https://microsoft.com)
[![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-Ready-C51A4A?style=for-the-badge&logo=raspberry-pi&logoColor=white)](https://raspberrypi.com)
[![NeuTTS](https://img.shields.io/badge/Powered%20by-NeuTTS%20Nano-FF6B6B?style=for-the-badge)](https://github.com/neuphonic/neutts)
[![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)](LICENSE)

</div>

## 📌 Table of Contents

- [Why I Built This](#-why-i-built-this)
- [Credits & Attribution](#-credits--attribution)
- [Platform Support](#-platform-support)
- [Model Recommendations](#-model-recommendations)
- [Features](#-features)
- [Smart Chunking](#-smart-chunking--unlimited-text-length)
- [Project Structure](#-project-structure)
- [Installation Guides](#-installation-guides)
  - [Android (Termux + Ubuntu)](#-android--termux--ubuntu-)
  - [iOS (iSH)](#-ios-ish)
  - [Linux](#-linux)
  - [macOS](#-macos)
  - [Windows (WSL2)](#-windows-wsl2)
  - [Raspberry Pi](#-raspberry-pi)
- [How to Use](#-how-to-use)
- [A-to-Z Troubleshooting](#-a-to-z-troubleshooting)
- [Responsible Use](#-responsible-use)
- [License](#-license)
- [Links](#-links)

---

## 📌 Why I Built This

The original [NeuTTS](https://github.com/neuphonic/neutts) by **Neuphonic** is an incredible open-source project — state-of-the-art text-to-speech that runs on-device. But it was built for developers who are comfortable with command-line flags and technical setups.

I asked myself: *"Why should only developers get to use this?"*

So I reverse-engineered the interface to create a **user-friendly shell** that anyone can use — no terminal expertise required. Just pick numbers from a menu and go.

**What the original looks like:**
```bash
python -m examples.basic_example \
  --input_text "Hello world" \
  --ref_audio ./samples/jo.wav \
  --ref_text ./samples/jo.txt \
  --backbone neuphonic/neutts-nano-q4-gguf \
  --output_path ./output.wav
```

**What NeuTTS Studio looks like:**
```bash
python run.py
# Then just pick numbers from a menu!
```

| Original NeuTTS | NeuTTS Studio |
|-----------------|---------------|
| Command-line flags | Interactive numbered menus |
| Manual model each run | Load once, use everywhere |
| No progress feedback | Animated progress bars with RTF stats |
| 30-second text limit | Unlimited text — auto-chunking |
| Manual audio encoding | Auto-encode + save voice profiles |
| Files save anywhere | Organized `data/outputs/` folders |
| Requires developer knowledge | Anyone can use it |
| Hidden cache (`~/.cache`) | Models inside project folder |

---

## 📌 Credits & Attribution

> ⚠️ **This project does NOT claim ownership of any AI model.**

All TTS models, the NeuCodec audio codec, and the core inference engine are the intellectual property of **[Neuphonic](https://neuphonic.com)**.

NeuTTS Studio is purely an **interface layer** — a user-friendly shell built around their open-source work. The models have not been modified, retrained, or redistributed in any way.

| Component | Owner | License |
|---|---|---|
| NeuTTS-Nano models | [Neuphonic](https://neuphonic.com) | NeuTTS Open License 1.0 |
| NeuCodec audio codec | [Neuphonic](https://neuphonic.com) | NeuTTS Open License 1.0 |
| Core inference engine | [neuphonic/neutts](https://github.com/neuphonic/neutts) | See repo |
| espeak-ng phonemizer | [espeak-ng](https://github.com/espeak-ng/espeak-ng) | GPL v3 |
| Perth watermarking | [resemble-ai/perth](https://github.com/resemble-ai/perth) | MIT |
| llama.cpp GGUF backend | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | MIT |
| **NeuTTS Studio interface** | **This project** | **MIT** |

**💛 Huge thanks to the entire Neuphonic team** for open-sourcing such high-quality on-device TTS and making it accessible to the community.

**👨‍💻 My contribution:** 20+ hours of debugging, reverse-engineering, and optimizing to make this work seamlessly on mobile devices — especially Android via Termux.

---

## 📱 Platform Support

| Platform | Status | Requirements | Tested On |
|----------|--------|--------------|-----------|
| **Android** | ✅ Optimised | Termux + Ubuntu (via proot-distro) | Galaxy A25, S23, Pixel 7 |
| **iOS** | ✅ Optimised | iSH or a-Shell | iPhone 14, iPad Pro |
| **Linux** | ✅ Supported | Python 3.10+, build-essential | Ubuntu 22.04+, Debian, Arch |
| **macOS** | ✅ Supported | Python 3.10+, Xcode CLT | Intel & Apple Silicon |
| **Windows** | ⚠️ WSL2 Required | WSL2 with Ubuntu | Windows 10/11 |
| **Raspberry Pi** | ✅ Supported | Raspberry Pi OS | Pi 4, Pi 5 |

---

## 👍 Model Recommendations

| Platform | Recommended Model | Why |
|----------|-------------------|-----|
| **Android (High-end)** 8GB+ RAM | `NeuTTS-Nano Q8 GGUF` | Better quality while staying fast on devices like S23, Pixel 7 Pro |
| **Android (Mid-range)** 4-6GB RAM | `NeuTTS-Nano Q4 GGUF` | Optimized for most phones, fastest on ARM, streaming ready |
| **iOS (High-end)** iPhone Pro Max / iPad Pro | `NeuTTS-Nano Q8 GGUF` | Take advantage of more RAM for better quality |
| **iOS (Mid-range)** Standard iPhone/iPad | `NeuTTS-Nano Q4 GGUF` | Smooth performance, lowest resource usage |
| **Linux (High-end)** 16GB+ RAM, modern CPU | `NeuTTS-Nano SafeTensors` | Best quality, finetuning capable |
| **Linux (Mid-range)** 8-16GB RAM | `NeuTTS-Nano Q8 GGUF` | Good balance of quality and speed |
| **Linux (Low-end)** 4-8GB RAM, older hardware | `NeuTTS-Nano Q4 GGUF` | If you have limited resources |
| **macOS (Apple Silicon)** M1/M2/M3 | `NeuTTS-Nano Q8 GGUF` | Optimized for Apple Silicon, great performance |
| **macOS (Intel)** | `NeuTTS-Nano SafeTensors` | Works natively on Intel Macs |
| **Windows (WSL2)** | `NeuTTS-Nano SafeTensors` | Full performance via Ubuntu WSL2 |
| **Raspberry Pi 4/5** | `NeuTTS-Nano Q4 GGUF` | Only model that runs smoothly on ARM SBCs |

**Quick Guide:**
- **Q4 GGUF** = Fastest, lowest memory, streaming ready — **Best for mid-range mobile**
- **Q8 GGUF** = Better quality, needs more RAM — **Great for high-end mobile and Apple Silicon**
- **SafeTensors** = Best quality, requires more RAM, finetuning capable — **Best for desktops**

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🗣️ Text to Speech
- Type, paste, or load text from file
- **No length limit** — smart auto-chunking
- Live progress bar per chunk with RTF stats
- Merge chunks OR save individually OR both
- Output saved to `data/outputs/tts/`

</td>
<td width="50%">

### 🎤 Voice Cloning
- Clone any voice from 3+ seconds of audio
- Save as named reusable `.pt` profiles
- Test cloned voice with any phrase
- Add language & gender metadata with flags
- Output saved to `data/outputs/cloning/`

</td>
</tr>
<tr>
<td width="50%">

### ⚡ Streaming Mode
- Audio plays as it generates — no waiting
- Live chunk stats: duration, gen time, RTF
- Stream to speakers only
- Stream + save simultaneously
- Output saved to `data/outputs/streaming/`

</td>
<td width="50%">

### 🔧 Fine Tuning
- Train on your own voice data
- Interactive config builder
- Launch training from inside the app
- Resume from checkpoints
- Dataset guide built in

</td>
</tr>
</table>

---

## 🧠 Smart Chunking — Unlimited Text Length

The NeuTTS model has a **2048 token context window** (~30 seconds per call). NeuTTS Studio solves this automatically with a **4-tier chunking strategy**:

```
Your text (any length — sentence, page, chapter, book)
                         ↓
     ┌─────────────────────────────────────────────┐
     │  Tier 1  ·  Split at sentence endings       │  .  !  ?
     │  Tier 2  ·  Split at clause boundaries      │  ,  ;  :
     │  Tier 3  ·  Split at word boundaries        │  spaces
     │  Tier 4  ·  Hard cut at 250 characters      │  last resort
     └─────────────────────────────────────────────┘
                         ↓
      [chunk 1]  [chunk 2]  [chunk 3]  ...  [chunk N]
                         ↓
         Same voice applied to every single chunk
                         ↓
       All chunks stitched with smooth 200ms gaps
                         ↓
              ✅  One seamless final .wav file
```

**Example — 10,000 character input:**
- Splits into ~40 chunks automatically
- Generates ~15 minutes of audio
- Zero manual intervention needed

---

## 🗂️ Project Structure

```
NeuTTS-Studio/
│
├── 🚀 run.py                    ← Entry point — run this to start
├── ⚙️  config.py                 ← All settings, paths, model definitions
├── 📋 requirements.txt          ← Python dependencies
├── 📖 README.md                 ← You are here
│
├── 🧠 core/
│   ├── engine.py                ← NeuTTS wrapper (model loading & inference)
│   ├── chunker.py               ← Smart 4-tier text splitting system
│   ├── audio.py                 ← Audio stitching, saving, file management
│   ├── ui.py                    ← Interactive menus, colors, input prompts
│   └── progress.py              ← Animated progress bars & spinners
│
├── 📦 modules/
│   ├── tts.py                   ← Text to Speech module
│   ├── cloning.py               ← Voice Cloning module
│   ├── streaming.py             ← Streaming Mode module
│   ├── finetuning.py            ← Fine Tuning module
│   ├── settings.py              ← Settings & model management
│   └── voice_selector.py        ← Shared voice picker
│
└── 💾 data/
    ├── voices/                  ← Your cloned voice profiles (.pt + .txt + .wav)
    ├── samples/                  ← Built-in reference voices (.wav + .txt)
    ├── models/                   ← Downloaded models cached here (NOT hidden)
    └── outputs/
        ├── tts/                  ← Audio from Text to Speech
        ├── streaming/            ← Recordings from Streaming sessions
        └── cloning/              ← Test audio from Voice Cloning
```

---

## 🤖 Android Installation (Termux + Ubuntu)

### ⚠️ IMPORTANT — Read Before Starting

Default Termux uses its own package system (`pkg`) which is **missing many packages** required by NeuTTS Studio such as `libopenblas-dev`, `portaudio19-dev`, `pkg-config`, `cmake` and more.

**You MUST set up a full Ubuntu environment inside Termux first.** This gives you access to the complete `apt-get` ecosystem.

---

### Step 0 — Install Termux

**Install Termux from F-Droid** (NOT the Play Store — F-Droid version is actively maintained):
```
https://f-droid.org/packages/com.termux/
```

Open Termux and run:

```bash
# Update Termux base packages
pkg update && pkg upgrade -y

# Install proot-distro — the Ubuntu manager for Termux
pkg install proot-distro -y

# Install Ubuntu
proot-distro install ubuntu

# Enter Ubuntu environment
proot-distro login ubuntu
```

Your prompt will change to:
```
root@localhost:~#
```

You are now inside a full Ubuntu environment with complete `apt-get` access.

> 💡 **Every time you open Termux**, you must re-enter Ubuntu before using NeuTTS Studio:
> ```bash
> proot-distro login ubuntu
> ```

**Create a shortcut so you never forget:**
```bash
# Run this in regular Termux (NOT inside Ubuntu)
echo "alias ubuntu='proot-distro login ubuntu'" >> ~/.bashrc
source ~/.bashrc

# Now just type this to enter Ubuntu anytime:
ubuntu
```

---

### Step 1 — Update system packages
```bash
apt-get update && apt-get upgrade -y
```

### Step 2 — Install Python
```bash
apt-get install python3 python3-pip python3-venv -y
python3 --version   # Must be 3.10+
```

### Step 3 — Install espeak-ng
```bash
apt-get install espeak-ng -y
espeak-ng --version   # Must be 1.52+
```

### Step 4 — Install build tools
```bash
apt-get install build-essential cmake git pkg-config -y
```

### Step 5 — Install OpenBLAS
```bash
apt-get install libopenblas-dev -y
```

### Step 6 — Install PortAudio (for streaming)
```bash
apt-get install portaudio19-dev -y
```

### Step 7 — Install ffmpeg (for audio conversion)
```bash
apt-get install ffmpeg -y
```

### Step 8 — Create virtual environment
```bash
python3 -m venv ai-env
source ai-env/bin/activate
```

> 💡 Always run `source ai-env/bin/activate` before using the app.

### Step 9 — Clone NeuTTS Studio
```bash
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
```

### Step 10 — Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 11 — Install llama-cpp-python with OpenBLAS (CRITICAL for ARM)
```bash
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir
```

### Step 12 — Add sample voices
Download from [original NeuTTS samples](https://github.com/neuphonic/neutts/tree/main/samples) and copy into `data/samples/`:
```
data/samples/
├── dave.wav  +  dave.txt     ← English male
├── jo.wav    +  jo.txt       ← English female
├── mateo.wav +  mateo.txt    ← Spanish male
├── greta.wav +  greta.txt    ← German female
└── juliette.wav + juliette.txt  ← French female
```

### Step 13 — Launch! 🚀
```bash
python run.py
```

---

## 🍎 iOS Installation (iSH)

### Step 1 — Install iSH from App Store
Search: **iSH Shell** → Download → Open

### Step 2 — Setup Alpine Linux
```bash
apk update && apk upgrade
apk add python3 py3-pip cmake build-base git pkgconfig
apk add espeak-ng espeak-ng-dev
apk add portaudio-dev
apk add openblas-dev
apk add ffmpeg
```

### Step 3 — Clone and install
```bash
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
pip install -r requirements.txt
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir
```

### Step 4 — Launch
```bash
python run.py
```

---

## 🐧 Linux Installation

```bash
# Install system dependencies
sudo apt update
sudo apt install python3 python3-pip python3-venv espeak-ng \
  build-essential cmake git pkg-config libopenblas-dev portaudio19-dev \
  ffmpeg -y

# Clone and setup
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# Optional: For better performance on Linux
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir

# Launch
python run.py
```

---

## 🍎 macOS Installation

```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install python3 espeak-ng cmake pkg-config openblas portaudio ffmpeg

# Clone and setup
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# For Apple Silicon (M1/M2/M3), this is optimized automatically
# Launch
python run.py
```

---

## 🪟 Windows Installation (WSL2)

```powershell
# In PowerShell (Admin)
wsl --install -d Ubuntu

# Restart your computer when prompted

# Open Ubuntu WSL terminal
# Follow Linux instructions above
```

---

## 🥧 Raspberry Pi Installation

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv espeak-ng \
  build-essential cmake git pkg-config libopenblas-dev portaudio19-dev \
  ffmpeg -y

git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio
python3 -m venv ai-env
source ai-env/bin/activate
pip install -r requirements.txt

# CRITICAL for Raspberry Pi ARM
CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir

# Launch
python run.py
```

---

## 🚀 How to Use

### Main Menu
```
╔══════════════════════════════════════════════════════════════╗
║  Main Menu
╚══════════════════════════════════════════════════════════════╝

  [1]  🗣️   Text to Speech     — convert text to audio with chunking
  [2]  🎤   Voice Cloning      — clone & manage voice profiles
  [3]  ⚡   Streaming Mode     — real-time audio generation
  [4]  🔧   Fine Tuning        — train on custom voice data
  [5]  ⚙️   Settings           — load model, manage outputs
  [0]  Exit

  ────────────────────────────────────────────────────────

  [0]  ← Back

  Select ❯
```

### 📝 Text to Speech
1. Select `[1] Text to Speech`
2. Choose input mode:
   - `[1] Single line` — short sentences
   - `[2] Multi-paragraph` — paste long text (Enter twice to finish)
   - `[3] Load from .txt file` — read from file
3. Preview chunk breakdown
4. Pick a voice (sample or your cloned voice)
5. Choose output format:
   - `[1] Merged single file` — one seamless audio
   - `[2] Individual chunk files` — per-chunk files
   - `[3] Both` — everything!
6. Watch real-time progress:
```
  Generating [████████████████████████████] 100.0% [1/1] 12.5s ETA: 0.0s
  ✓  Generated 2.44s audio in 12.5s  ·  RTF 5.1
```
7. Audio saved to `data/outputs/tts/`

### 🎤 Voice Cloning
1. Record 3–15 seconds of clear speech on your phone
2. Convert to WAV if needed:
```bash
ffmpeg -i recording.m4a -ar 16000 -ac 1 -sample_fmt s16 voice.wav
```
3. Select `[2] Voice Cloning → [1] Clone new voice`
4. Provide:
   - Path to WAV file
   - Exact transcript (word-for-word)
   - Voice name
   - Language (with flag support! 🇧🇩)
   - Gender
5. Watch encoding progress:
```
    Loading encoder model...
    ✓ Encoder loaded in 16.1s
    Loading audio file...
    ✓ Audio loaded: 32000Hz, 8.9s in 10.1s
    Encoding voice...
        ✓ Encoding complete in 207.9s
```
6. Test immediately with `[3] Test a voice`

### ⚡ Streaming Mode
1. Select `[3] Streaming Mode` (GGUF model required)
2. Choose mode:
   - `[1] Stream to speakers` — live playback
   - `[2] Stream and save` — generate + save
   - `[3] Stream, play, and save` — both!
3. Type your text
4. Watch real-time chunk stats:
```
  [01] TTFA   512ms audio  gen 920ms  ✅ 55% RT
  [02]        480ms audio  gen 460ms  ✅ 96% RT
  [03]        495ms audio  gen 480ms  ✅ 97% RT
```

### 🎵 Converting Any Audio Format to WAV

NeuTTS requires `.wav` format. Use `ffmpeg` for conversion:

```bash
# Universal command — works for ALL formats
ffmpeg -i input_file.m4a -ar 16000 -ac 1 -sample_fmt s16 output.wav

# Examples:
ffmpeg -i recording.mp3  -ar 16000 -ac 1 voice.wav
ffmpeg -i audio.ogg      -ar 16000 -ac 1 voice.wav
ffmpeg -i sound.aac      -ar 16000 -ac 1 voice.wav
ffmpeg -i music.flac     -ar 16000 -ac 1 voice.wav
```

**What each flag means:**

| Flag | Meaning | Why |
|---|---|---|
| `-i input.m4a` | Input file | Your original recording |
| `-ar 16000` | Sample rate = 16kHz | What NeuTTS expects |
| `-ac 1` | Mono channel | Single speaker, no stereo |
| `-sample_fmt s16` | 16-bit PCM | Standard WAV format |
| `output.wav` | Output filename | The file for NeuTTS |

**Check your converted file:**
```bash
ffprobe output.wav
# Should show: Audio: pcm_s16le, 16000 Hz, mono
```

**Trim to optimal length (3-15 seconds):**
```bash
# Trim from 0s to 10s
ffmpeg -i output.wav -ss 0 -t 10 trimmed.wav
```

---

## 🔧 A-to-Z Troubleshooting

### 🟢 Installation Issues

#### Q: `proot-distro: command not found`
**Cause:** proot-distro not installed in Termux.
```bash
# In regular Termux (NOT Ubuntu)
pkg update && pkg install proot-distro -y
```

#### Q: Ubuntu won't start after `proot-distro login ubuntu`
**Cause:** Ubuntu installation corrupted.
```bash
proot-distro remove ubuntu
proot-distro install ubuntu
proot-distro login ubuntu
```

#### Q: Confused between `pkg` and `apt-get`
- `pkg` = Termux (outside Ubuntu)
- `apt-get` = Ubuntu (inside proot-distro)

```bash
# ✅ Correct — in regular Termux
pkg install proot-distro

# ✅ Correct — inside Ubuntu
apt-get install python3

# ❌ Wrong — apt-get in regular Termux
# ❌ Wrong — pkg inside Ubuntu
```

#### Q: Can't access Android storage from Ubuntu
```bash
# In regular Termux (NOT Ubuntu) first
termux-setup-storage
# Grant permission when prompted

# Then inside Ubuntu, access files at:
ls /storage/emulated/0/
```

#### Q: Files not visible between Termux and Ubuntu
**Cause:** Ubuntu's home directory is separate.
```bash
# Work directly in Android storage
cd /storage/emulated/0/Repository/NeuTTS-Studio
python run.py
```

---

### 🟡 Python & Package Issues

#### Q: `No module named 'resampy'`
```bash
pip install resampy
```

#### Q: `PySoundFile failed` warning
```bash
pip install soundfile
```

#### Q: `Failed building wheel for llama-cpp-python`
**Cause:** Build tools or OpenBLAS missing.
```bash
apt-get install build-essential cmake pkg-config libopenblas-dev -y

CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
pip install "neutts[llama]" --force-reinstall --no-cache-dir
```

#### Q: `ModuleNotFoundError: No module named 'torch'`
```bash
source ai-env/bin/activate  # Activate venv first!
pip install -r requirements.txt
```

#### Q: `Could NOT find PkgConfig (missing: PKG_CONFIG_EXECUTABLE)`
```bash
# Android / Ubuntu
apt-get install pkg-config -y

# iOS / Alpine
apk add pkgconfig
```

#### Q: `portaudio.h: No such file or directory`
```bash
# Android / Ubuntu
apt-get install portaudio19-dev -y

# iOS / Alpine
apk add portaudio-dev
```

---

### 🔴 Model Loading Issues

#### Q: Download hangs or times out
```bash
# Increase timeout
export HF_HUB_DOWNLOAD_TIMEOUT=60

# Or use mirror if blocked
export HF_ENDPOINT=https://hf-mirror.com

# Then run again
python run.py
```

#### Q: `out of memory` during model loading
- Switch to Q4 GGUF model (smallest)
- Close all other apps
- Restart Termux/Ubuntu session
- On Android: disable background apps in system settings

#### Q: `Streaming requires a GGUF model`
**Cause:** SafeTensors model doesn't support streaming.
Go to: `[5] Settings → [1] Load Model → Select [2] Q8 or [3] Q4`

#### Q: `FileNotFoundError: Sample 'jo.wav' not found`
**Cause:** Sample voices missing.
Download from: `https://github.com/neuphonic/neutts/tree/main/samples`
Copy to `NeuTTS-Studio/data/samples/`

---

### 🎤 Voice Cloning Issues

#### Q: Cloned voice sounds robotic or wrong
**Checklist:**
- [ ] Audio is 3-15 seconds long
- [ ] Format is WAV (not MP3/M4A)
- [ ] Sample rate 16-44kHz
- [ ] Mono channel (not stereo)
- [ ] No background noise
- [ ] Transcript matches EXACTLY word for word

**Fix audio:**
```bash
ffmpeg -i input.m4a -ar 16000 -ac 1 -sample_fmt s16 output.wav
```

#### Q: Voice cloning takes forever
Normal for first time:
- Downloads `facebook/w2v-bert-2.0` (~2-3GB)
- Takes 3-5 minutes on mobile
- **Only happens once!**

#### Q: `list index out of range` error during cloning
Fixed in v2.0.0 — update your code.

#### Q: Cloned voice sounds like it's mixing with sample voices
Fixed! Now uses original transcript as reference.

#### Q: Converted WAV sounds distorted or too quiet
```bash
# Normalize audio levels
ffmpeg -i input.m4a -ar 16000 -ac 1 -af "loudnorm" output.wav
```

#### Q: `Invalid data found when processing input`
```bash
# Check actual format
ffprobe your_file.m4a

# Try forcing format
ffmpeg -f mp4 -i your_file.m4a -ar 16000 -ac 1 output.wav
```

---

### 🟣 Terminal & Input Issues

#### Q: Input prompt shows garbage (e ❯)
Fixed in v2.0.0 — now uses `>` instead of special chars.

#### Q: Spinner keeps running during input
Fixed with `InputSafeSpinner` class.

#### Q: Paste triggers auto-enter
Fixed with custom `ask_multiline()` function.

#### Q: Progress bar stuck at 0%
```bash
export PYTHONUNBUFFERED=1
# Already set in run.py
```

#### Q: `permission denied` on storage path
```bash
# Work from home directory instead
cd ~
git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
cd NeuTTS-Studio && python run.py
```

---

### 🟠 Performance Issues

#### Q: Generation is very slow
Normal for mobile:
- 50-100x real-time is expected
- 2s audio = 100-200s on mobile CPU
- Switch to Q4 GGUF for 2-3x speedup

#### Q: Audio has clicks/pops between chunks
Edit `config.py`:
```python
CHUNK_SILENCE_MS = 300  # Increase from 200ms
```

#### Q: `PyAudio` stream underflow warning
**Cause:** CPU too slow to feed audio buffer.
- Switch to Q4 GGUF for faster generation
- This is a warning, not an error

#### Q: `antlr4` deprecation warning
Safe to ignore completely — just a packaging warning.

---

### 🔵 Expected Performance

| Device | Model | Speed | RTF |
|--------|-------|-------|-----|
| Galaxy A25 (Mid-range) | Q4 GGUF | 45 tok/s | 50-60x |
| Galaxy S23 (High-end) | Q4 GGUF | 80 tok/s | 30-40x |
| Galaxy S23 | Q8 GGUF | 70 tok/s | 35-45x |
| Pixel 7 | Q4 GGUF | 70 tok/s | 35-45x |
| iPhone 14 (iSH) | Q4 GGUF | 60 tok/s | 40-50x |
| iPad Pro | Q8 GGUF | 90 tok/s | 25-35x |
| Raspberry Pi 4 | Q4 GGUF | 30 tok/s | 80-100x |
| PC (i5, no GPU) | SafeTensors | 150 tok/s | 15-20x |
| PC (with GPU) | SafeTensors | 500+ tok/s | <5x |

> **RTF = Real-Time Factor** (lower is better)  
> 50 tok/s ≈ 1 second of audio per second of generation

---

## 🔒 Responsible Use

Every audio file generated includes an invisible **[Perth watermark](https://github.com/resemble-ai/perth)** that cryptographically identifies it as AI-generated.

- ❌ Do not impersonate real people without explicit consent
- ❌ Do not generate deceptive, harmful, or fraudulent audio
- ✅ Respect the privacy and dignity of all individuals
- ✅ Follow all applicable laws in your jurisdiction
- ✅ Use for creative, educational, and personal projects

---

## 📄 License

| Component | License |
|-----------|---------|
| **NeuTTS Studio Interface** | MIT |
| **NeuTTS-Nano Models** | [NeuTTS Open License 1.0](https://github.com/neuphonic/neutts/blob/main/LICENSE) |
| **NeuCodec** | NeuTTS Open License 1.0 |
| **espeak-ng** | GPL v3 |
| **Perth** | MIT |
| **llama.cpp** | MIT |

---

## 🌐 Links

| | |
|---|---|
| 🏠 Original NeuTTS repo | [github.com/neuphonic/neutts](https://github.com/neuphonic/neutts) |
| 🌍 Neuphonic website | [neuphonic.com](https://neuphonic.com) |
| 🤗 HuggingFace models | [huggingface.co/neuphonic](https://huggingface.co/neuphonic) |
| 🎮 Try online | [HuggingFace Space](https://huggingface.co/spaces/neuphonic/neutts-nano-multilingual-collection) |
| 🐛 Report issues | [GitHub Issues](https://github.com/fardin-sabid/NeuTTS-Studio/issues) |

---

<div align="center">

**Made with ❤️ by Fardin Sabid**  
**🇧🇩 From Bangladesh, for the World 🌍**

<br>

```
If you can dream it, you can speak it.
```

<br>
After 20+ hours of debugging, reverse-engineering, and optimizing — it's finally here.

<br>

[![GitHub stars](https://img.shields.io/github/stars/fardin-sabid/NeuTTS-Studio?style=for-the-badge&logo=github)](https://github.com/fardin-sabid/NeuTTS-Studio)
[![Follow](https://img.shields.io/github/followers/fardin-sabid?style=for-the-badge&logo=github)](https://github.com/fardin-sabid)

**If you find this project useful, please ⭐ star it on GitHub!**

</div>