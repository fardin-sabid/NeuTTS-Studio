# 🏋️ Fine-Tuning Guide for NeuTTS Studio

This guide explains how to fine-tune NeuTTS-Nano SafeTensors models on your own voice data to improve quality and create custom voices.

---

## 📋 Table of Contents
- [Prerequisites](#prerequisites)
- [Understanding Fine-Tuning](#understanding-fine-tuning)
- [Dataset Preparation](#dataset-preparation)
- [Configuration](#configuration)
- [Running Fine-Tuning](#running-fine-tuning)
- [Monitoring Training](#monitoring-training)
- [Using Your Fine-Tuned Model](#using-your-fine-tuned-model)
- [Troubleshooting](#troubleshooting)
- [Advanced Options](#advanced-options)

---

## ✅ Prerequisites

Before starting fine-tuning, ensure you have:

### Hardware Requirements
| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **RAM** | 16GB | 32GB+ |
| **VRAM** | 8GB (GPU) | 16GB+ (GPU) |
| **Storage** | 20GB free | 50GB+ free |
| **CPU** | 4 cores | 8+ cores |

### Software Requirements
- NeuTTS Studio installed
- SafeTensors model loaded (not GGUF)
- Python 3.10+
- CUDA-capable GPU (optional but recommended)

### Data Requirements
- 30+ minutes of clean speech
- Accurate transcripts
- Variety of sentences/phrases

---

## 🧠 Understanding Fine-Tuning

Fine-tuning adapts the base NeuTTS-Nano model to your specific voice:

```
Base Model (multilingual, multi-speaker)
         ↓
[Fine-Tuning on Your Voice Data]
         ↓
Custom Model (optimized for your voice)
```

**What fine-tuning changes:**
- ✅ Voice characteristics (pitch, tone, cadence)
- ✅ Pronunciation nuances
- ✅ Speaking style
- ❌ NOT the language model architecture
- ❌ NOT the core TTS capabilities

---

## 📊 Dataset Preparation

### Step 1: Record Your Voice

**Recording Guidelines:**
- 🎙️ Use a good microphone (phone is fine)
- 🤫 Quiet environment (no background noise)
- 📏 15-30cm from microphone
- 🗣️ Natural speaking style (not robotic)
- ⏱️ Aim for 30-60 minutes total
- 📝 Read diverse content (news, stories, conversations)

### Step 2: Split into Audio Files

Create individual `.wav` files for each sentence:

```
dataset/
├── audio/
│   ├── 001.wav  (3-10 seconds)
│   ├── 002.wav  (3-10 seconds)
│   ├── 003.wav  (3-10 seconds)
│   └── ...
└── metadata.csv
```

### Step 3: Create Transcripts

**`metadata.csv` format:**
```csv
file,text
001.wav,Hello this is my first recording.
002.wav,I'm fine-tuning a TTS model on my voice.
003.wav,The quick brown fox jumps over the lazy dog.
```

**Transcript Guidelines:**
- ✅ Word-for-word accuracy
- ✅ Include punctuation
- ✅ No background noise descriptions
- ✅ Match audio exactly

### Step 4: Convert to NeuCodec Format

NeuTTS requires pre-encoded audio. Use the built-in tool:

```python
# encode_dataset.py
import torch
from neucodec import NeuCodec
import librosa
import pandas as pd
from pathlib import Path

def encode_dataset(metadata_path, output_dir):
    """Convert WAV files to NeuCodec tokens."""
    df = pd.read_csv(metadata_path)
    encoder = NeuCodec.from_pretrained("neuphonic/neucodec")
    encoder.eval()
    
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    codes_list = []
    texts = []
    
    for _, row in df.iterrows():
        # Load audio
        wav_path = Path("dataset/audio") / row['file']
        audio, sr = librosa.load(wav_path, sr=16000, mono=True)
        
        # Encode
        wav_tensor = torch.from_numpy(audio).float().unsqueeze(0).unsqueeze(0)
        with torch.no_grad():
            codes = encoder.encode_code(wav_tensor).squeeze(0).squeeze(0)
        
        # Save
        codes_path = output_dir / f"{Path(row['file']).stem}.pt"
        torch.save(codes, codes_path)
        
        codes_list.append(str(codes_path))
        texts.append(row['text'])
    
    # Create dataset JSON
    dataset = {
        "codes": codes_list,
        "texts": texts
    }
    import json
    with open(output_dir / "dataset.json", "w") as f:
        json.dump(dataset, f)
    
    print(f"✅ Encoded {len(codes_list)} files to {output_dir}")

if __name__ == "__main__":
    encode_dataset("dataset/metadata.csv", "dataset/encoded")
```

---

## ⚙️ Configuration

### Using NeuTTS Studio Menu

1. Launch NeuTTS Studio:
   ```bash
   python run.py
   ```

2. Go to `[4] Fine Tuning`

3. Select `[1] New training job`

4. Configure your training:
   ```
   Base model [neuphonic/neutts-nano]: 
   Output directory [./finetune_output]: 
   Run name [my-finetune]: my_voice_v1
   
   Dataset (HuggingFace repo or local): ./dataset/encoded/dataset.json
   Dataset split [train[:2000]]: 
   Language code [en-us]: 
   
   Learning rate [0.00004]: 
   Max steps [10000]: 5000
   Batch size per device [2]: 4
   ```

### Manual Configuration (YAML)

Create a `config.yaml` file:

```yaml
restore_from: "neuphonic/neutts-nano"
save_root: "./finetune_output"
run_name: "my_voice_v1"

# Dataset
dataset: "./dataset/encoded/dataset.json"
dataset_split: "train[:2000]"
language: "en-us"

# Model parameters
codebook_size: 65536
max_seq_len: 2048

# Training hyperparameters
lr: 0.00004
lr_scheduler_type: "cosine"
warmup_ratio: 0.0
per_device_train_batch_size: 4
max_steps: 5000
logging_steps: 100
save_steps: 2000
seed: 1337
```

---

## 🚀 Running Fine-Tuning

### From NeuTTS Studio

After configuring, select `Launch training now? [Y/n]: y`

### From Command Line

```bash
# Using the config file
python -m examples.finetune ./finetune_output/my_voice_v1_config.yaml

# With arguments directly
python -m examples.finetune \
  --restore_from neuphonic/neutts-nano \
  --save_root ./finetune_output \
  --run_name my_voice_v1 \
  --dataset ./dataset/encoded/dataset.json \
  --language en-us \
  --max_steps 5000 \
  --batch_size 4
```

### Multi-GPU Training

```bash
# Use multiple GPUs
python -m torch.distributed.launch \
  --nproc_per_node=2 \
  -m examples.finetune \
  ./finetune_output/my_voice_v1_config.yaml
```

---

## 📊 Monitoring Training

### Console Output

```
Step 100/5000 | Loss: 2.345 | LR: 4.0e-05 | Time: 12.3s
Step 200/5000 | Loss: 1.987 | LR: 3.9e-05 | Time: 24.1s
Step 300/5000 | Loss: 1.654 | LR: 3.8e-05 | Time: 36.2s
...
Step 5000/5000 | Loss: 0.456 | LR: 0.0e+00 | Time: 623.4s
✅ Training completed!
```

### TensorBoard

```bash
# Launch TensorBoard
tensorboard --logdir ./finetune_output/my_voice_v1/logs
```

Open http://localhost:6006 in your browser

### Loss Curve Expectations

- **Start**: Loss ~2.5-3.0
- **After 1000 steps**: Loss ~1.0-1.5
- **After 5000 steps**: Loss ~0.3-0.6
- **Target**: Loss < 0.5 for good quality

---

## 🎯 Using Your Fine-Tuned Model

### Step 1: Locate the Checkpoint

After training, your model is saved at:
```
./finetune_output/my_voice_v1/checkpoint-5000/
```

### Step 2: Load in NeuTTS Studio

1. Go to `[5] Settings`
2. Select `[1] Load / Switch Model`
3. Choose `Custom path` option
4. Enter the path to your checkpoint:
   ```
   ./finetune_output/my_voice_v1/checkpoint-5000
   ```

### Step 3: Test Your Model

1. Go to `[1] Text to Speech`
2. Select a sample voice (your fine-tuned model retains multi-speaker capability)
3. Generate speech and hear the improved quality!

---

## 🔧 Troubleshooting

### Common Issues

#### ❌ Out of Memory
**Error:** `CUDA out of memory`
**Solutions:**
- Reduce batch size (`batch_size: 2` or `1`)
- Use gradient accumulation
- Switch to CPU (slower but works)
- Use Q4 GGUF for inference (not training)

#### ❌ Dataset Errors
**Error:** `FileNotFoundError: dataset.json not found`
**Solutions:**
- Check path is absolute or relative correctly
- Run encoding script again
- Verify JSON format

#### ❌ Loss Not Decreasing
**Error:** Loss stuck at ~2.5
**Solutions:**
- Check learning rate (try 1e-4 or 5e-5)
- Verify dataset quality
- Increase dataset size
- Check for transcript errors

#### ❌ Overfitting
**Symptoms:** Loss near 0, but sounds robotic
**Solutions:**
- Reduce training steps
- Add more diverse data
- Use data augmentation
- Increase dropout

### Quality Checklist

| Issue | Possible Fix |
|-------|--------------|
| Robotic voice | Train longer, check data quality |
| Mispronunciations | Fix transcripts, add more examples |
| Background noise | Clean audio, use noise reduction |
| Inconsistent volume | Normalize audio files |
| Stuttering | Check audio segmentation |

---

## 🚀 Advanced Options

### Hyperparameter Tuning

```yaml
# Advanced config.yaml
restore_from: "neuphonic/neutts-nano"
save_root: "./finetune_output"
run_name: "my_voice_advanced"

# Dataset
dataset: "./dataset/encoded/dataset.json"
dataset_split: "train[:5000]"
language: "en-us"

# Model
codebook_size: 65536
max_seq_len: 2048

# Training
lr: 0.00005
lr_scheduler_type: "cosine_with_restarts"
warmup_steps: 500
per_device_train_batch_size: 4
gradient_accumulation_steps: 2
max_steps: 10000
logging_steps: 50
save_steps: 1000
eval_steps: 500
evaluation_strategy: "steps"
eval_dataset: "./dataset/encoded/validation.json"

# Optimization
adam_beta1: 0.9
adam_beta2: 0.999
adam_epsilon: 1e-8
weight_decay: 0.01
max_grad_norm: 1.0

# Regularization
dropout: 0.1
attention_dropout: 0.1

# Hardware
fp16: true
gradient_checkpointing: true
dataloader_num_workers: 4

# Logging
report_to: ["tensorboard"]
logging_first_step: true
```

### Resume from Checkpoint

```bash
# Resume training
python -m examples.finetune \
  --restore_from ./finetune_output/my_voice_v1/checkpoint-5000 \
  --save_root ./finetune_output \
  --run_name my_voice_v2 \
  --max_steps 10000
```

### Multi-Speaker Training

For multiple speakers, format your dataset as:

```json
{
  "codes": ["speaker1_001.pt", "speaker1_002.pt", "speaker2_001.pt"],
  "texts": ["Hello", "World", "Hi"],
  "speakers": ["speaker1", "speaker1", "speaker2"]
}
```

---

## 📚 References

- [NeuTTS Original Paper](https://arxiv.org/abs/neuphonic)
- [NeuCodec Documentation](https://github.com/neuphonic/neucodec)
- [HuggingFace Transformers Training Guide](https://huggingface.co/docs/transformers/training)

---

## 🎉 Success!

After fine-tuning, your model should:
- ✅ Sound more like you
- ✅ Have better pronunciation
- ✅ Maintain natural prosody
- ✅ Work with all NeuTTS Studio features

**Share your results and help improve the guide!** 

---

<div align="center">
Made with ❤️ by Fardin Sabid 🇧🇩
</div>
```