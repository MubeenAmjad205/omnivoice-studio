# OmniVoice Studio

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MubeenAmjad205/omnivoice-studio/blob/main/notebooks/OmniVoice_Gradio.ipynb)

This project is a clean, maintainable GitHub repository built around [OmniVoice](https://github.com/k2-fsa/OmniVoice). It transitions a simple Google Colab notebook into a proper local and Colab-ready Python project.

## Features
- **Based on OmniVoice**: High-Quality Voice Cloning & Design.
- **Local Application Entrypoint**: Easy-to-use `app.py` wrapper.
- **Configurable Sharing**: Toggle public Gradio links via `.env`.
- **Organized Structure**: Ready for further extension and customization.

## Requirements
- Python 3.8+
- GPU Recommended (NVIDIA T4, RTX 3060 or better) for reasonable generation speeds.

## Installation & Local Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/MubeenAmjad205/omnivoice-studio.git
   cd omnivoice-studio
   ```

2. **Set up a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration**:
   Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set `GRADIO_SHARE=true` if you want to generate a public link.

5. **Run the App**:
   ```bash
   python app.py
   ```
   Or use the helper script:
   ```bash
   bash scripts/run_local.sh
   ```

## Running in Google Colab

The easiest way to run this project is by clicking the **Open in Colab** badge at the top of this page.

1. Click [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/MubeenAmjad205/omnivoice-studio/blob/main/notebooks/OmniVoice_Gradio.ipynb)
2. In Colab, go to **Runtime > Change runtime type** and select a **T4 GPU** (or better).
3. Run the single cell in the notebook. It will automatically clone the repository, install dependencies, and generate a public `xxxx.gradio.live` link for you!

## Pushing to GitHub

To push your project to GitHub (after modifying):

```bash
git init
git add .
git commit -m "Initial commit of OmniVoice Studio"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

## Safety and Ethical Usage

**⚠️ IMPORTANT**: Please read [docs/safety.md](docs/safety.md) before using this tool.

- Do not clone someone's voice without their explicit permission.
- Public Gradio share links can be accessed by anyone who has the link. Do not upload private voice recordings to public demos.
