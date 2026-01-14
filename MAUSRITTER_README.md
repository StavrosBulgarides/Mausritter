# Mausritter Character Generator

A Python program that generates characters for the Mausritter tabletop RPG and creates interactive HTML character sheets.

## Features

### Character Generation
- **Attribute Rolling**: Roll 3d6, keep two highest for STR, DEX, WIL (range 2-12 per SRD 2.3)
- **Background System**: 36 unique backgrounds determined by HP and Pips rolls
- **Complete Appearance**: Birthsign with disposition, coat (color + pattern), physical detail (d66 table)
- **Smart Equipment**: Background items automatically placed (armor to body slots, others to pack)
- **Low Stats Bonus**: Additional items granted when highest attribute is 9 or less

### Interactive Character Sheet
- **Structured Inventory**: Paw slots (2), Body slots (2), Pack slots (6)
- **Item Selector**: Searchable item picker with all SRD equipment, weapons, armor, and spells
- **Usage Tracking**: 3-dot usage markers per slot (6-dot system for torches/lanterns)
- **Two-Slot Items**: Support for heavy weapons and heavy armor spanning multiple slots
- **Depleted Items**: Visual strikethrough when all usage markers are filled

### Conditions & Grit System
- **All Conditions**: Exhausted, Frightened, Hungry, Injured, Poisoned, Stunned
- **Clear Requirements**: Each condition displays how to clear it
- **Grit Tracking**: Ignore conditions using available Grit points

### Hirelings Section
- **Dynamic Hirelings**: Add and remove hirelings as needed
- **Full Stats**: STR, DEX, WIL (2d6 each), HP (1d6) with max/current tracking
- **Hireling Inventory**: 2 paw slots + 4 pack slots per hireling
- **Appearance**: Random look and disposition from SRD tables

### Additional Features
- **Dice Roller**: Custom notation support (e.g., 2d6, 4d20+2)
- **Collapsible Sections**: Stats, Inventory, Other, Hirelings
- **Value Enforcement**: Current values cannot exceed max values
- **Regenerate Flow**: Accept or regenerate new characters before applying

## Usage

Run the program:

```bash
python3 main.py
```

The program will:
1. Generate a random Mausritter character
2. Display the character details in the terminal
3. Create an HTML character sheet file
4. Automatically open the character sheet in your browser

## Character Generation Rules (SRD 2.3)

1. **Attributes**: Roll 3d6, keep two highest for each of STR, DEX, WIL
2. **Hit Protection (HP)**: Roll 1d6
3. **Pips**: Roll 1d6 for starting currency
4. **Background**: Determined by HP and Pips combination (36 backgrounds)
5. **Equipment**:
   - All characters start with Torches and Rations
   - Background provides 2 items
   - Player selects starting weapon
   - Additional items if highest attribute is 9 or less (more if 7 or less)
6. **Appearance**: Birthsign, coat color/pattern, physical detail
7. **Name**: Random first and last name from thematic tables

## Weapons Available

| Type | Weapons | Damage | Slots |
|------|---------|--------|-------|
| Light Melee | Needle, Dagger, Hatchet | d6 | 1 |
| Medium Melee | Sword, Axe, Staff, Hammer, Pickaxe | d6/d8 | 1 |
| Heavy Melee | Trashhook, Spear, Heavy hammer | d10 | 2 |
| Light Ranged | Sling, Hand crossbow | d6 | 1 |
| Heavy Ranged | Bow, Crossbow | d8 | 2 |

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Project Structure

```
mausritter/
├── __init__.py
├── browser.py          # Browser opening utilities
├── data.py             # All game data (backgrounds, items, etc.)
├── generator.py        # Character generation logic
└── templates/
    ├── __init__.py
    ├── css.py          # Character sheet styles
    ├── html_template.py # HTML structure
    └── js.py           # Interactive functionality
```

## License

This project includes material from the Mausritter SRD by Isaac Williams, used under the Creative Commons Attribution 4.0 International Licence (CC-BY 4.0).

Original work: https://mausritter.com


