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


def _build_header(name: str) -> str:
    """Build the character sheet header with name input."""
    return f"""    <div class="character-sheet">
        <button class="generate-new-btn" onclick="generateNewCharacter()">Generate New Character</button>
        <h1>
            <input type="text" value="{name}" style="text-align: center; border: none; font-size: 1em; width: 100%; background: transparent; font-weight: bold; color: #8b4513;" />
        </h1>"""


def _build_attributes_section(attributes: Dict[str, int]) -> str:
    """Build the attributes section (STR, DEX, WIL)."""
    return f"""
        <div class="section">
            <div class="section-title">Attributes</div>
            <div class="attributes-grid">
                <div class="attribute">
                    <div class="attribute-label">Strength (STR)</div>
                    <input type="number" value="{attributes['STR']}" min="3" max="18" class="attribute-value" style="width: 100%;" />
                </div>
                <div class="attribute">
                    <div class="attribute-label">Dexterity (DEX)</div>
                    <input type="number" value="{attributes['DEX']}" min="3" max="18" class="attribute-value" style="width: 100%;" />
                </div>
                <div class="attribute">
                    <div class="attribute-label">Willpower (WIL)</div>
                    <input type="number" value="{attributes['WIL']}" min="3" max="18" class="attribute-value" style="width: 100%;" />
                </div>
            </div>
        </div>"""


def _build_stats_section(hp: int, pips: int) -> str:
    """Build the stats section (HP, Pips)."""
    return f"""
        <div class="section">
            <div class="section-title">Stats</div>
            <div class="stats-row">
                <div class="stat-box">
                    <div class="stat-label">Hit Protection (HP)</div>
                    <input type="number" value="{hp}" min="0" max="20" style="width: 100%;" />
                </div>
                <div class="stat-box">
                    <div class="stat-label">Pips</div>
                    <input type="number" value="{pips}" min="0" style="width: 100%;" />
                </div>
            </div>
        </div>"""


def _build_background_section(background: str) -> str:
    """Build the background section."""
    return f"""
        <div class="section">
            <div class="section-title">Background</div>
            <input type="text" value="{background}" style="width: 100%; font-size: 1.1em; padding: 10px;" />
        </div>"""


def _build_appearance_section(appearance: Dict[str, str]) -> str:
    """Build the appearance section."""
    return f"""
        <div class="section">
            <div class="section-title">Appearance</div>
            <div class="appearance-grid">
                <div class="appearance-item">
                    <div class="appearance-label">Birthmark</div>
                    <input type="text" value="{appearance['birthmark']}" />
                </div>
                <div class="appearance-item">
                    <div class="appearance-label">Fur Color</div>
                    <input type="text" value="{appearance['fur_color']}" />
                </div>
                <div class="appearance-item">
                    <div class="appearance-label">Fur Pattern</div>
                    <input type="text" value="{appearance['fur_pattern']}" />
                </div>
                <div class="appearance-item">
                    <div class="appearance-label">Special Feature</div>
                    <input type="text" value="{appearance['special_feature']}" />
                </div>
            </div>
        </div>"""


def _build_equipment_item(item: str, index: int) -> str:
    """Build a single equipment item."""
    item_id = f"item_{index}"
    return f"""                <div class="equipment-item">
                    <input type="text" class="equipment-name" value="{item}" />
                    <div class="equipment-uses">
                        <span class="equipment-uses-label">Uses:</span>
                        <div class="equipment-uses-checkboxes">
                            <label><input type="checkbox" name="{item_id}_use1" /> 1</label>
                            <label><input type="checkbox" name="{item_id}_use2" /> 2</label>
                            <label><input type="checkbox" name="{item_id}_use3" /> 3</label>
                        </div>
                    </div>
                </div>"""


def _build_empty_equipment_slot(index: int) -> str:
    """Build an empty equipment slot."""
    item_id = f"item_{index}"
    return f"""                <div class="equipment-item">
                    <input type="text" class="equipment-name" value="" placeholder="Additional item..." />
                    <div class="equipment-uses">
                        <span class="equipment-uses-label">Uses:</span>
                        <div class="equipment-uses-checkboxes">
                            <label><input type="checkbox" name="{item_id}_use1" /> 1</label>
                            <label><input type="checkbox" name="{item_id}_use2" /> 2</label>
                            <label><input type="checkbox" name="{item_id}_use3" /> 3</label>
                        </div>
                    </div>
                </div>"""


def _build_equipment_section(equipment: List[str], total_slots: int = 10) -> str:
    """Build the equipment section."""
    items_html = "\n".join(
        _build_equipment_item(item, idx) for idx, item in enumerate(equipment)
    )
    empty_slots_html = "\n".join(
        _build_empty_equipment_slot(idx)
        for idx in range(len(equipment), total_slots)
    )

    return f"""
        <div class="section">
            <div class="section-title">Equipment (Items have 3 uses - check boxes as you use them)</div>
            <div class="equipment-list">
{items_html}
{empty_slots_html}
            </div>
        </div>"""


def _build_conditions_section() -> str:
    """Build the conditions section."""
    return """
        <div class="section">
            <div class="section-title">Conditions</div>
            <div class="conditions-list">
                <div class="condition-item"><input type="text" value="" placeholder="Condition..." /></div>
                <div class="condition-item"><input type="text" value="" placeholder="Condition..." /></div>
                <div class="condition-item"><input type="text" value="" placeholder="Condition..." /></div>
                <div class="condition-item"><input type="text" value="" placeholder="Condition..." /></div>
            </div>
        </div>"""


def _build_notes_section() -> str:
    """Build the notes section."""
    return """
        <div class="section">
            <div class="section-title">Notes</div>
            <textarea placeholder="Add your notes here..."></textarea>
        </div>"""


def _build_dice_roller() -> str:
    """Build the dice roller section."""
    return """
        <div style="text-align: center; margin-top: 20px; color: #666; font-size: 0.9em;">
        </div>

        <div class="dice-roller">
            <div class="dice-roller-header">
                <span class="dice-roller-title">Dice Roller</span>
                <span class="dice-roller-toggle" id="diceToggle">&#x25BC;</span>
            </div>
            <div class="dice-roller-content" id="diceContent">
                <div class="dice-input-section">
                    <input type="text" class="dice-input" id="diceInput" placeholder="e.g., 2d6, 4d20" value="2d6" />
                    <button class="roll-btn" onclick="rollDice()">Roll Dice</button>
                </div>
                <div class="dice-results" id="diceResults"></div>
            </div>
        </div>"""


def _build_footer() -> str:
    """Build the closing tags and script section."""
    js_code = get_javascript_code()
    return f"""    </div>

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
        _build_header(character["name"]),
        _build_attributes_section(character["attributes"]),
        _build_stats_section(character["hp"], character["pips"]),
        _build_background_section(character["background"]),
        _build_appearance_section(character["appearance"]),
        _build_equipment_section(character["equipment"]),
        _build_conditions_section(),
        _build_notes_section(),
        _build_dice_roller(),
        _build_footer(),
    ]

    html_content = "\n".join(html_parts)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Character sheet saved to: {output_path}")
