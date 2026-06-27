"""
Script intended for execution in a Colab environment.
Provides similar functionality to the notebook but as a script.
"""

import os
import subprocess
import sys

def main():
    print("Setting up Colab environment...")
    
    # In Colab, we generally want sharing enabled
    os.environ["GRADIO_SHARE"] = "true"
    
    print("Launching OmniVoice Demo with sharing enabled...")
    try:
        subprocess.run(["omnivoice-demo", "--share"], check=True)
    except FileNotFoundError:
        print("Error: 'omnivoice-demo' not found. Ensure omnivoice is installed.", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nTerminated by user.")
        sys.exit(0)

if __name__ == "__main__":
    main()
