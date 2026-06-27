# Safety and Ethical Usage Guidelines

This project leverages powerful voice cloning technology provided by OmniVoice. With great power comes great responsibility.

## Ethical Voice Cloning Rules

1. **Explicit Permission**: NEVER clone someone's voice without their explicit, informed consent.
2. **No Deception**: Do not use generated audio to deceive, impersonate, or mislead others (e.g., deepfakes, scams, fake news).
3. **Respect Privacy**: Do not process or upload private or sensitive voice recordings if the environment is not entirely secure.

## Technical Security Warnings

1. **Public Gradio Links**: If you set `GRADIO_SHARE=true` in your `.env` file, the application will generate a public `xxxx.gradio.live` link.
   - **Warning**: Anyone with this link can access your app.
   - **Warning**: Anyone with the link can listen to or upload audio to your running instance.
   - Use this feature only for temporary testing or when the data is not sensitive.

2. **Local Security**: Keep your `.env` and `models/` files secure. The `.gitignore` is pre-configured to avoid accidentally committing these sensitive files to GitHub.
