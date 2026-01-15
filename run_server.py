#!/usr/bin/env python3
"""
Mausritter GM Server
Run this to start the local server for multiplayer sessions.
"""

import socket
import sys


def get_local_ip() -> str:
    """Get the local IP address for LAN connections."""
    try:
        # Create a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def main():
    # Import here to avoid import errors if Flask not installed
    try:
        from mausritter.server import create_app
        from mausritter.server.session import game_session
    except ImportError as e:
        print(f"Error: Could not import required modules: {e}")
        print("Make sure Flask is installed: pip install flask")
        sys.exit(1)

    app = create_app()

    # Get network info
    host = "0.0.0.0"  # Listen on all interfaces
    port = 5001  # Using 5001 as 5000 is often used by macOS AirPlay
    local_ip = get_local_ip()
    gm_token = game_session.gm_token

    # Print startup info
    print()
    print("=" * 60)
    print("          MAUSRITTER GM SERVER")
    print("=" * 60)
    print()
    print(f"  GM Dashboard:  http://{local_ip}:{port}/gm?token={gm_token}")
    print()
    print(f"  Player Join:   http://{local_ip}:{port}/join")
    print()
    print("-" * 60)
    print("  Share the Player Join URL with your players.")
    print("  Keep the GM Dashboard URL secret!")
    print("-" * 60)
    print()
    print("Press Ctrl+C to stop the server.")
    print()

    # Run the server
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    main()
