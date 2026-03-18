# Contributing to NeuTTS Studio

First off, thank you for considering contributing to NeuTTS Studio! 🎉 It's people like you that make this project better for everyone.

## 📝 Table of Contents
- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Testing Guidelines](#testing-guidelines)
- [Platform-Specific Notes](#platform-specific-notes)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### 🐛 Reporting Bugs
Before creating bug reports, please check the existing issues to see if the problem has already been reported. When you create a bug report, include as many details as possible using the bug report template.

**Good bug reports include:**
- A clear and descriptive title
- Exact steps to reproduce the problem
- The exact error message or unexpected behavior
- Your environment details (platform, device, Python version)
- Screenshots or videos if applicable

### ✨ Suggesting Features
Feature requests are welcome! Use the feature request template and explain:
- What problem it solves
- How it would work
- Why it would be useful for NeuTTS Studio users

### 📝 Documentation Improvements
Found a typo? Unclear explanation? Help us improve the documentation! This includes:
- README.md improvements
- Code comments
- Docstrings
- Platform-specific guides

### 💻 Code Contributions
Looking to contribute code? Great! Here's how:

1. **Find an issue** to work on, or create one
2. **Comment on the issue** that you'd like to work on it
3. **Fork the repository** and create a branch
4. **Write your code** following our style guidelines
5. **Test your changes** on at least one platform
6. **Submit a pull request**

## Development Setup

### Prerequisites
- Python 3.10 or higher
- Git
- For Android: Termux with Ubuntu (proot-distro)
- For iOS: iSH or a-Shell

### Setting Up for Development

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/fardin-sabid/NeuTTS-Studio.git
   cd NeuTTS-Studio
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv dev-env
   source dev-env/bin/activate  # On Windows: dev-env\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install llama-cpp-python with OpenBLAS** (for ARM devices)
   ```bash
   CMAKE_ARGS="-DGGML_BLAS=ON -DGGML_BLAS_VENDOR=OpenBLAS" \
   pip install "neutts[llama]" --force-reinstall --no-cache-dir
   ```

5. **Add sample voices**
   Download sample voices from the original NeuTTS repo and place them in `data/samples/`

6. **Run the app**
   ```bash
   python run.py
   ```

## Pull Request Process

1. **Create a branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

2. **Make your changes**
   - Write clean, documented code
   - Follow the style guidelines
   - Add comments for complex logic

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
   
   **Commit Message Guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - First line: 50 characters or less
   - Follow with a blank line, then detailed description if needed

4. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Submit a pull request**
   - Use the pull request template
   - Link any related issues
   - Describe your changes in detail
   - Mention which platforms you tested on

6. **Respond to feedback**
   - Make requested changes
   - Push additional commits
   - Keep the conversation going until the PR is merged

## Style Guidelines

### Python Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 88 characters (compatible with Black)
- Use descriptive variable names
- Add docstrings to all functions, classes, and modules

### Docstring Format
Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> bool:
    """Brief description of function.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    # function body
```

### Imports Order
1. Standard library imports
2. Third-party imports
3. Local application imports

Example:
```python
import sys
import time
from pathlib import Path

import torch
import numpy as np

from core.engine import engine
from config import MODELS
```

## Testing Guidelines

### Test Your Changes
- Run the app and test the affected features
- Test on different platforms if possible
- Check for any new warnings or errors

### Platform Testing Matrix

| Change Type | Test On |
|-------------|---------|
| UI changes | All platforms |
| Core engine | Linux + one mobile platform |
| Android-specific | Termux with Ubuntu |
| iOS-specific | iSH or a-Shell |
| Documentation | N/A (just review) |

### What to Test
- Does the app start without errors?
- Do the affected features work as expected?
- Are there any performance regressions?
- Does the progress display work correctly?
- Are files saved in the correct locations?

## Platform-Specific Notes

### Android (Termux + Ubuntu)
- Always test inside Ubuntu via proot-distro
- Verify OpenBLAS compilation works
- Check storage permissions
- Test with both Q4 and Q8 models

Common Android test commands:
```bash
proot-distro login ubuntu
cd /path/to/NeuTTS-Studio
source ai-env/bin/activate
python run.py
```

### iOS (iSH)
- Test with Alpine Linux
- Check memory usage (iSH has limitations)
- Verify espeak-ng works correctly

### Linux/macOS
- Test with and without virtual environment
- Verify all dependencies install cleanly
- Test streaming with PortAudio

### Windows (WSL2)
- Test with Ubuntu WSL2
- Verify file paths work correctly
- Check that audio plays properly

## Questions?

If you have any questions, feel free to:
- Open a discussion on GitHub
- Comment on the relevant issue
- Reach out to the maintainers

Thank you for contributing to NeuTTS Studio! Your efforts help make on-device TTS accessible to everyone. 🚀
```