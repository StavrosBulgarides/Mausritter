# Mausritter Character Generator

A Python program that generates characters for the Mausritter tabletop RPG and creates editable HTML character sheets.

## Features

- **Automatic Character Generation**: Rolls attributes (STR, DEX, WIL), HP, Pips, and determines background
- **Complete Character Details**: Generates appearance (birthmark, fur color, fur pattern, special feature), name, and starting equipment
- **Editable HTML Character Sheet**: Creates a beautiful, editable character sheet that can be opened in any web browser
- **Print-Friendly**: The character sheet is designed to be printable

## Usage

Simply run the program:

```bash
python3 mausritter_character_generator.py
```

The program will:
1. Generate a random Mausritter character
2. Display the character details in the terminal
3. Create an HTML character sheet file (e.g., `mausritter_character_Bramble_Gnaw.html`)
4. Automatically open the character sheet in Chrome (or your default browser if Chrome is not available)

## Character Generation Rules

The program follows official Mausritter character creation rules:

1. **Attributes**: Rolls 3d6 for each of STR, DEX, and WIL
2. **Hit Protection (HP)**: Rolls 1d6
3. **Pips**: Rolls 1d6 for starting currency
4. **Background**: Determined by HP and Pips combination (36 possible backgrounds)
5. **Equipment**: 
   - All characters start with Torches and Rations
   - Background provides 2 items
   - Random weapon selection
   - Additional items if highest attribute is 9 or less
6. **Appearance**: Randomly generates birthmark, fur color, fur pattern, and special feature
7. **Name**: Randomly generates a first and last name from Mausritter-appropriate name tables

## Character Sheet Features

The generated HTML character sheet includes:

- **Editable Name**: Change your character's name
- **Attributes**: Edit STR, DEX, WIL values
- **Stats**: Edit HP and Pips
- **Background**: Editable background field
- **Appearance**: All appearance details are editable
- **Equipment**: List of starting equipment with space for additional items
- **Conditions**: Space to track character conditions
- **Notes**: Large text area for game notes

## Editing the Character Sheet

The character sheet will automatically open in Chrome when generation is complete. If Chrome is not available, it will open in your default browser.

1. Click on any field to edit it
2. Save the page (File > Save) to preserve your changes
3. The sheet can be printed directly from the browser

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Example Output

```
Generating Mausritter character...

Character Generated: Bramble Gnaw
STR: 11, DEX: 12, WIL: 12
HP: 2, Pips: 6
Background: Herbalist
Equipment: Torches, Rations, Staff, Herbs, Bandages
Character sheet saved to: mausritter_character_Bramble_Gnaw.html

Character sheet created! Open mausritter_character_Bramble_Gnaw.html in your browser to view and edit.
```

Enjoy your Mausritter adventures!


