# Mausritter Character Generator

A Python program that generates characters for the Mausritter tabletop RPG and creates interactive HTML character sheets. Includes a GM server for managing multiplayer sessions over a local network.

## Quick Start

### Standalone Mode (Single Character)
```bash
python3 main.py
```
Generates a character and opens the sheet in your browser.

### GM Server Mode (Multiplayer)
```bash
python3 run_server.py
```
Starts a local web server for GM and player access. See [GM Server](#gm-server) section below.

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

### Standalone Mode

Run the program:

```bash
python3 main.py
```

The program will:
1. Generate a random Mausritter character
2. Display the character details in the terminal
3. Create an HTML character sheet file
4. Automatically open the character sheet in your browser

---

## GM Server

The GM Server enables multiplayer sessions where:
- The GM manages all characters from a dashboard
- Players connect via browser over the local network (LAN)
- Character changes sync automatically to the server
- Sessions can be saved and loaded as JSON files

### Starting the Server

```bash
python3 run_server.py
```

On startup, the server displays:

```
============================================================
          MAUSRITTER GM SERVER
============================================================

  GM Dashboard:  http://192.168.x.x:5001/gm?token=abc123

  Player Join:   http://192.168.x.x:5001/join

------------------------------------------------------------
  Share the Player Join URL with your players.
  Keep the GM Dashboard URL secret!
------------------------------------------------------------
```

**Important URLs:**
- **GM Dashboard URL**: Contains a secret token - only share with the GM
- **Player Join URL**: Share this with your players (no token required)

The server runs on port 5001 and listens on all network interfaces, so players on the same LAN can connect using the displayed IP address.

### GM Dashboard Features

- **Create Characters**: Click "+ New Character" to generate characters
- **View All Characters**: See stats, conditions, and player tokens at a glance
- **Full Sheet View**: Click "Full Sheet" to open the complete interactive character sheet
- **Edit Any Character**: Modify stats, add/remove conditions
- **Session Management**:
  - **Save Session**: Download the current session as a JSON file
  - **Load Session**: Upload a previously saved session
  - **New Session**: Clear all characters and start fresh
  - **Stop Server**: Safely shut down the server

### Player Experience

1. Players navigate to the **Player Join URL** (e.g., `http://192.168.x.x:5001/join`)
2. They select their character from the list
3. They see the full interactive character sheet
4. Changes auto-save to the server

### Session Persistence

Sessions are stored in memory while the server runs. To preserve your session:

1. Click **Save Session** on the GM Dashboard
2. A JSON file downloads (e.g., `mausritter_session_name.json`)
3. To restore later, start the server and click **Load Session**

### Network Requirements

- GM and players must be on the same local network (LAN)
- No internet connection required
- No accounts or authentication beyond the GM token

### Server Files

```
mausritter/
└── server/
    ├── app.py              # Flask application
    ├── session.py          # Session state management
    ├── routes/
    │   ├── api.py          # REST API endpoints
    │   ├── gm.py           # GM dashboard routes
    │   └── player.py       # Player view routes
    └── templates/          # HTML templates
```

---

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
- **Standalone mode**: No external dependencies (uses only Python standard library)
- **GM Server mode**: Requires Flask (`pip install flask`)

## Project Structure

```
mausritter/
├── main.py                 # Standalone mode entry point
├── run_server.py           # GM Server entry point
├── mausritter/
│   ├── __init__.py
│   ├── browser.py          # Browser opening utilities
│   ├── data.py             # All game data (backgrounds, items, etc.)
│   ├── generator.py        # Character generation logic
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── css.py          # Character sheet styles
│   │   ├── html_template.py # HTML structure
│   │   └── js.py           # Interactive functionality
│   └── server/
│       ├── __init__.py
│       ├── app.py          # Flask application factory
│       ├── session.py      # In-memory session management
│       ├── routes/
│       │   ├── api.py      # REST API endpoints
│       │   ├── gm.py       # GM dashboard routes
│       │   └── player.py   # Player view routes
│       └── templates/      # Server HTML templates
```

## License

This project includes material from the Mausritter SRD by Isaac Williams, used under the Creative Commons Attribution 4.0 International Licence (CC-BY 4.0).

Original work: https://mausritter.com


