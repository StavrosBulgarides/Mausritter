#!/usr/bin/env python3
"""
Mausritter Character Generator
Generates a character and creates an editable HTML character sheet.
"""

import tempfile
from pathlib import Path

from mausritter import generate_character, create_html_character_sheet, open_in_browser


def main() -> None:
    """Generate a character and create an HTML character sheet."""
    print("Generating Mausritter character...")
    character = generate_character()

    print(f"\nCharacter Generated: {character['name']}")
    print(f"STR: {character['attributes']['STR']}, DEX: {character['attributes']['DEX']}, WIL: {character['attributes']['WIL']}")
    print(f"HP: {character['hp']}, Pips: {character['pips']}")
    print(f"Background: {character['background']}")
    print(f"Equipment: {', '.join(character['equipment'])}")

    # Create temp file (OS cleans these up automatically)
    safe_name = "".join(
        c for c in character["name"] if c.isalnum() or c in (" ", "-", "_")
    ).strip().replace(" ", "_")

    temp_file = tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.html',
        prefix=f'mausritter_{safe_name}_',
        delete=False  # Keep file so browser can load it
    )
    output_path = Path(temp_file.name)
    temp_file.close()

    create_html_character_sheet(character, output_path)
    print("\nCharacter sheet created in temp directory! Opening in browser...")

    open_in_browser(output_path)


if __name__ == "__main__":
    main()
