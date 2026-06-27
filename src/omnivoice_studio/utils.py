"""
Utility functions for OmniVoice Studio.
"""

def setup_directories():
    """Ensure required directories exist."""
    import os
    dirs = ["outputs", "models"]
    for d in dirs:
        os.makedirs(d, exist_ok=True)
