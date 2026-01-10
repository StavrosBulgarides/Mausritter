"""Browser opening utilities for Mausritter character sheets."""

import subprocess
import webbrowser
from pathlib import Path


def open_in_browser(file_path: Path) -> None:
    """Open the HTML file in a web browser.

    Tries Chrome first, then falls back to the default browser.

    Args:
        file_path: Path to the HTML file to open
    """
    file_path = Path(file_path).resolve()
    file_url = f"file://{file_path}"

    # Try different Chrome app names on macOS
    chrome_names = [
        "Google Chrome",
        "Google Chrome Canary",
        "Chromium",
    ]

    for chrome_name in chrome_names:
        try:
            subprocess.run(
                ["open", "-a", chrome_name, file_url],
                check=True,
                capture_output=True,
                timeout=5,
            )
            print(f"Opening character sheet in {chrome_name}...")
            return
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired):
            continue

    # Fallback: try direct Chrome executable paths
    chrome_paths = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
    ]

    for chrome_path in chrome_paths:
        if Path(chrome_path).exists():
            try:
                subprocess.Popen([chrome_path, file_url])
                print("Opening character sheet in Chrome...")
                return
            except Exception:
                continue

    # Final fallback: use default browser
    try:
        webbrowser.open(file_url)
        print("Opening character sheet in default browser...")
    except Exception:
        print(f"Could not open browser automatically. Please open {file_path} manually.")
