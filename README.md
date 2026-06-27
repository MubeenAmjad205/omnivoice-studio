# OmniVoice Studio

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
   git clone <your-repo-url>
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

Since you will be running this from a public repository, you can easily use it in Google Colab:

1. Open a new [Google Colab Notebook](https://colab.research.google.com/).
2. Go to **Runtime > Change runtime type** and select a **T4 GPU** (or better).
3. Create a new code cell and run the following commands to clone the repo, install dependencies, and launch the app:

```python
!git clone https://github.com/<your-username>/omnivoice-studio.git
%cd omnivoice-studio
!pip install -r requirements.txt
!python scripts/run_colab.py
```
*(Replace `<your-username>` with your actual GitHub username)*

4. A public `xxxx.gradio.live` link will appear in the output. Click it to open your UI!

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
