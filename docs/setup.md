# Setup Guide

## Prerequisites
- Python 3.8+ installed on your system.
- An NVIDIA GPU with CUDA installed (highly recommended for performance).

## Step-by-Step Installation

1. **Create the Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. **Install Packages**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Server**:
   ```bash
   python app.py
   ```
   
## GPU Troubleshooting
If OmniVoice is running very slowly, ensure that PyTorch is installed with CUDA support. You may need to install it specifically depending on your CUDA version:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
