# Mausritter Character Generator

A character generator and interactive character sheet for the Mausritter tabletop RPG. Includes a GM server for multiplayer sessions over LAN.

## Quick Start

### Standalone (Single Character)
```bash
python3 main.py
```

### GM Server (Multiplayer)
```bash
pip install flask  # First time only
python3 run_server.py
```

The server displays two URLs on startup:
- **GM Dashboard**: `http://192.168.x.x:5001/gm?token=...` (keep secret)
- **Player Join**: `http://192.168.x.x:5001/join` (share with players)

## Features

- Character generation following SRD 2.3 rules
- Interactive HTML character sheet with inventory management
- Item selector with all weapons, armor, spells, and equipment
- Usage tracking with depleted item indicators
- Conditions system with Grit-based ignoring
- Hirelings section with full stats and inventory
- Dice roller with custom notation
- **GM Server**: Manage multiple players over local network
- **Session Save/Load**: Preserve sessions as JSON files

See [MAUSRITTER_README.md](MAUSRITTER_README.md) for detailed documentation.

## License

This project includes material from the Mausritter SRD
by Isaac Williams, used under the Creative Commons
Attribution 4.0 International Licence (CC-BY 4.0).

Original work: https://mausritter.com
