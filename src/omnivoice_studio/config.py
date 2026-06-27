"""
Configuration module for OmniVoice Studio.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Feature flags / Configuration
GRADIO_SHARE = os.environ.get("GRADIO_SHARE", "false").lower() in ["true", "1", "yes"]
