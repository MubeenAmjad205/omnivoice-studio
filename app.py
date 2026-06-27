"""
OmniVoice Studio - Local Entrypoint

This script provides a structured way to launch the OmniVoice web interface
locally or expose it via a temporary public link using Gradio.
"""

import os
import sys
import subprocess
from dotenv import load_dotenv

def main():
    # Load environment variables from .env if present
    load_dotenv()
    
    # Check if GRADIO_SHARE is set to 'true' (case-insensitive)
    share_env = os.environ.get("GRADIO_SHARE", "false").lower()
    share_flag = share_env in ["true", "1", "yes"]

    print("🎙️  Starting OmniVoice Studio...")
    print(f"🌍 Share Mode: {'Enabled' if share_flag else 'Disabled'}")

    # Build the command based on the share flag
    command = ["omnivoice-demo"]
    if share_flag:
        command.append("--share")

    try:
        # Launch the CLI process
        print(f"🚀 Running command: {' '.join(command)}")
        print("💡 Tip: To change share mode, set GRADIO_SHARE in your .env file.")
        
        # subprocess.run will block and stream output directly to stdout/stderr
        subprocess.run(command, check=True)
    except FileNotFoundError:
        print("❌ Error: 'omnivoice-demo' command not found.", file=sys.stderr)
        print("   Please ensure OmniVoice is installed: pip install -r requirements.txt", file=sys.stderr)
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: OmniVoice process exited with code {e.returncode}", file=sys.stderr)
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        print("\n🛑 Shutting down OmniVoice Studio. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
