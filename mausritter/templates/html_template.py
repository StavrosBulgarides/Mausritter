"""HTML template generation for Mausritter character sheets."""

from pathlib import Path
from typing import Dict, Any, List

from .css import STYLES
from .js import get_javascript_code


def _build_head(character_name: str) -> str:
    """Build the HTML head section."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mausritter Character Sheet - {character_name}</title>
    <style>
{STYLES}
    </style>
</head>"""


def _build_generate_button() -> str:
    """Build the generate new character button."""
    return """
    <div class="generate-section">
        <button class="generate-btn" onclick="generateNewCharacter()">Generate New Character</button>
    </div>"""


def _build_header_section(character: Dict[str, Any]) -> str:
    """Build the header section with name, background, and appearance."""
    appearance = character["appearance"]
    return f"""
    <div class="header-section">
        <div class="name-background-box">
            <div class="name-row">
                <span class="name-label">Name</span>
                <input type="text" class="name-input" value="{character['name']}" placeholder="Enter name" />
            </div>
            <div class="background-row">
                <span class="background-label">Background</span>
                <input type="text" class="background-input" value="{character['background']}" placeholder="Enter background" />
            </div>
        </div>
        <div class="appearance-box">
            <div class="appearance-row">
                <span class="appearance-label">Birthsign</span>
                <input type="text" value="{appearance['birthsign']} ({appearance['disposition']})" placeholder="Enter birthsign" />
            </div>
            <div class="appearance-row">
                <span class="appearance-label">Coat</span>
                <input type="text" value="{appearance['coat']}" placeholder="Enter coat" />
            </div>
            <div class="appearance-row">
                <span class="appearance-label">Look</span>
                <input type="text" value="{appearance['look']}" placeholder="Enter look" />
            </div>
        </div>
    </div>"""


def _build_middle_section(character: Dict[str, Any]) -> str:
    """Build the middle section with portrait and stats."""
    attrs = character["attributes"]
    hp = character["hp"]
    pips = character["pips"]
    pips_total = character["pips_total"]

    return f"""
    <div class="middle-section">
        <div class="portrait-box">
            <div class="portrait-label">Portrait/description</div>
            <textarea class="portrait-input" placeholder="Enter description..."></textarea>
        </div>
        <div class="stats-box">
            <div class="attributes-section">
                <div class="attributes-header">
                    <span></span>
                    <span>Max</span>
                    <span>Current</span>
                </div>
                <div class="attributes-table">
                    <div class="attribute-row">
                        <span class="attribute-label">STR</span>
                        <input type="number" value="{attrs['STR']['max']}" min="1" max="12" />
                        <input type="number" value="{attrs['STR']['current']}" min="0" max="12" />
                    </div>
                    <div class="attribute-row">
                        <span class="attribute-label">DEX</span>
                        <input type="number" value="{attrs['DEX']['max']}" min="1" max="12" />
                        <input type="number" value="{attrs['DEX']['current']}" min="0" max="12" />
                    </div>
                    <div class="attribute-row">
                        <span class="attribute-label">WIL</span>
                        <input type="number" value="{attrs['WIL']['max']}" min="1" max="12" />
                        <input type="number" value="{attrs['WIL']['current']}" min="0" max="12" />
                    </div>
                </div>
            </div>
            <div class="hp-section">
                <div class="hp-table">
                    <div class="hp-row">
                        <span class="hp-label">HP</span>
                        <input type="number" value="{hp['max']}" min="1" max="20" />
                        <input type="number" value="{hp['current']}" min="0" max="20" />
                    </div>
                </div>
                <div class="hp-footer">
                    <span></span>
                    <span>Max</span>
                    <span>Current</span>
                </div>
            </div>
            <div class="pips-section">
                <div class="pips-table">
                    <div class="pips-row">
                        <span class="pips-label">Pips</span>
                        <input type="number" value="{pips}" min="0" />
                        <input type="number" value="{pips_total}" min="0" />
                    </div>
                </div>
            </div>
        </div>
    </div>"""


def _build_inventory_section(character: Dict[str, Any]) -> str:
    """Build the inventory section with slot grid."""
    inventory = character.get("inventory", {})
    main_paw = inventory.get("main_paw", "")
    off_paw = inventory.get("off_paw", "")
    body = inventory.get("body", ["", ""])
    pack = inventory.get("pack", ["", "", "", "", "", ""])

    return f"""
    <div class="inventory-section">
        <div class="inventory-header">
            <span class="inventory-title">Inventory</span>
        </div>
        <div class="inventory-container">
            <div class="paw-column">
                <div class="paw-grid">
                    <div class="inventory-slot paw-slot">
                        <div class="slot-label">Main paw</div>
                        <div class="slot-content">
                            <textarea placeholder="">{main_paw}</textarea>
                        </div>
                    </div>
                    <div class="inventory-slot paw-slot">
                        <div class="slot-label">Off paw</div>
                        <div class="slot-content">
                            <textarea placeholder="">{off_paw}</textarea>
                        </div>
                    </div>
                </div>
                <div class="inventory-legend-item"><strong>Carried:</strong> Ready to use.</div>
            </div>
            <div class="body-column">
                <div class="body-grid">
                    <div class="inventory-slot body-slot">
                        <div class="slot-label">Body</div>
                        <div class="slot-content">
                            <textarea placeholder="">{body[0]}</textarea>
                        </div>
                    </div>
                    <div class="inventory-slot body-slot">
                        <div class="slot-label">Body</div>
                        <div class="slot-content">
                            <textarea placeholder="">{body[1]}</textarea>
                        </div>
                    </div>
                </div>
                <div class="inventory-legend-item"><strong>Worn:</strong> Quick to ready.</div>
            </div>
            <div class="pack-column">
                <div class="pack-grid">
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">1</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[0]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">2</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[1]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">3</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[2]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">4</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[3]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">5</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[4]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot pack-slot">
                        <div class="slot-header">
                            <span class="slot-label">6</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{pack[5]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                </div>
                <div class="inventory-legend-item"><strong>Pack:</strong> Takes time to ready. During combat, requires an action to retrieve.</div>
            </div>
        </div>
    </div>"""


def _build_bottom_section(character: Dict[str, Any]) -> str:
    """Build the bottom section with level, grit, and banked items."""
    level = character.get("level", 1)
    xp = character.get("xp", 0)
    grit = character.get("grit", 0)

    return f"""
    <div class="bottom-section">
        <div class="level-xp-box">
            <div class="level-box">
                <div class="level-label">Level</div>
                <input type="number" value="{level}" min="1" max="10" />
            </div>
            <div class="xp-box">
                <div class="xp-label">XP</div>
                <input type="number" value="{xp}" min="0" />
            </div>
            <div class="level-note">Recovered treasure ▸ XP</div>
        </div>
        <div class="grit-conditions-box">
            <div class="grit-box">
                <div class="grit-label">Grit</div>
                <input type="number" value="{grit}" min="0" max="6" />
            </div>
            <div class="conditions-box">
                <div class="conditions-label">Ignored conditions</div>
                <textarea placeholder=""></textarea>
            </div>
            <div class="grit-note">Ignore a number of conditions equal to your Grit</div>
        </div>
        <div class="banked-box">
            <div class="banked-label">Banked items and pips</div>
            <textarea placeholder=""></textarea>
            <div class="mausritter-logo">Mausritter</div>
        </div>
    </div>"""


def _build_footer() -> str:
    """Build the footer section."""
    js_code = get_javascript_code()
    return f"""
    <div class="sheet-footer">
        This is a personal project. Original character sheet design © <a href="https://mausritter.com" target="_blank">Mausritter</a> by Losing Games.
    </div>

    <div class="item-selector-modal" id="itemSelectorModal">
        <div class="item-selector-content">
            <div class="item-selector-header">
                <span>Select Item</span>
                <button class="close-modal" onclick="closeItemSelector()">&times;</button>
            </div>
            <div class="item-selector-body" id="itemSelectorBody">
            </div>
        </div>
    </div>

    <div class="dice-roller">
        <div class="dice-roller-header" onclick="toggleDiceRoller()">
            <span class="dice-roller-title">Dice Roller</span>
            <span class="dice-roller-toggle" id="diceToggle">▼</span>
        </div>
        <div class="dice-roller-content" id="diceContent">
            <div class="dice-input-section">
                <input type="text" class="dice-input" id="diceInput" placeholder="e.g., 2d6, 4d20" value="2d6" />
                <button class="roll-btn" onclick="rollDice()">Roll Dice</button>
            </div>
            <div class="dice-results" id="diceResults"></div>
        </div>
    </div>

    </div>

    <script>
{js_code}
    </script>
</body>
</html>"""


def create_html_character_sheet(character: Dict[str, Any], output_path: Path) -> None:
    """Create an editable HTML character sheet.

    Args:
        character: Dictionary containing character data
        output_path: Path to write the HTML file
    """
    html_parts = [
        _build_head(character["name"]),
        "<body>",
        '    <div class="character-sheet">',
        _build_generate_button(),
        _build_header_section(character),
        _build_middle_section(character),
        _build_inventory_section(character),
        _build_bottom_section(character),
        _build_footer(),
    ]

    html_content = "\n".join(html_parts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Character sheet saved to: {output_path}")
