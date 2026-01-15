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


def _build_dice_roller() -> str:
    """Build the dice roller section."""
    return """
    <div class="dice-roller">
        <div class="dice-roller-header" onclick="toggleDiceRoller()">
            <span class="dice-roller-title">Dice Roller</span>
            <span class="dice-roller-toggle" id="diceToggle">▼</span>
        </div>
        <div class="dice-roller-content" id="diceContent">
            <div class="save-results-row" id="saveResultsRow" style="display: none;">
                <div class="save-info" id="saveInfo">
                    <div class="save-info-text">
                        <span class="save-stat-name" id="saveStatName"></span>
                        <span class="save-target" id="saveTarget"></span>
                    </div>
                    <div class="save-modifiers">
                        <button class="save-modifier-btn" id="advantageBtn" onclick="rollWithAdvantage()" title="Roll 2d20, take lowest">Advantage</button>
                        <button class="save-modifier-btn" id="disadvantageBtn" onclick="rollWithDisadvantage()" title="Roll 2d20, take highest">Disadvantage</button>
                    </div>
                </div>
                <div class="dice-results save-mode" id="saveRollResults"></div>
            </div>
            <div class="dice-input-section">
                <input type="text" class="dice-input" id="diceInput" placeholder="e.g., 2d6, 4d20" value="2d6" />
                <button class="roll-btn" onclick="manualRollDice()">Roll Dice</button>
            </div>
            <div class="dice-results" id="diceResults"></div>
        </div>
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
    <div class="stats-section">
        <div class="section-header" onclick="toggleSection('stats')">
            <span class="section-title">Stats</span>
            <span class="section-toggle" id="statsToggle">▲</span>
        </div>
        <div class="section-content active" id="statsContent">
            <div class="middle-section">
                <div class="portrait-column">
                    <div class="portrait-box">
                        <textarea class="portrait-input" placeholder="Enter description..."></textarea>
                    </div>
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
                                <span class="attribute-label save-btn" onclick="rollSave('STR')" title="Click to roll STR save">STR</span>
                                <input type="number" value="{attrs['STR']['max']}" min="1" max="12" />
                                <input type="number" value="{attrs['STR']['current']}" min="0" max="12" />
                            </div>
                            <div class="attribute-row">
                                <span class="attribute-label save-btn" onclick="rollSave('DEX')" title="Click to roll DEX save">DEX</span>
                                <input type="number" value="{attrs['DEX']['max']}" min="1" max="12" />
                                <input type="number" value="{attrs['DEX']['current']}" min="0" max="12" />
                            </div>
                            <div class="attribute-row">
                                <span class="attribute-label save-btn" onclick="rollSave('WIL')" title="Click to roll WIL save">WIL</span>
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
                    </div>
                    <div class="pips-section">
                        <div class="pips-table">
                            <div class="pips-row">
                                <span class="pips-label">Pips</span>
                                <input type="number" class="pips-total-input" value="250" readonly />
                                <input type="number" class="pips-input" value="{pips}" min="0" max="250" />
                            </div>
                        </div>
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

    # Add needs-selection class if main_paw is "Select weapon"
    main_paw_class = "needs-selection" if main_paw == "Select weapon" else ""

    return f"""
    <div class="inventory-section">
        <div class="inventory-header" onclick="toggleInventory()">
            <span class="inventory-title">Inventory</span>
            <span class="inventory-toggle" id="inventoryToggle">▲</span>
        </div>
        <div class="inventory-content active" id="inventoryContent">
        <div class="inventory-container">
            <div class="paw-column">
                <div class="paw-grid">
                    <div class="inventory-slot paw-slot">
                        <div class="slot-header">
                            <span class="slot-label">Main paw</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea class="{main_paw_class}" placeholder="">{main_paw}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot paw-slot">
                        <div class="slot-header">
                            <span class="slot-label">Off paw</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{off_paw}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                </div>
                <div class="inventory-legend-item"><strong>Carried:</strong> Ready to use.</div>
            </div>
            <div class="body-column">
                <div class="body-grid">
                    <div class="inventory-slot body-slot">
                        <div class="slot-header">
                            <span class="slot-label">Body</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{body[0]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                        </div>
                    </div>
                    <div class="inventory-slot body-slot">
                        <div class="slot-header">
                            <span class="slot-label">Body</span>
                            <span class="slot-actions">
                                <button class="slot-btn add-btn" onclick="openItemSelector(this)">+</button>
                                <button class="slot-btn clear-btn" onclick="clearSlot(this)">-</button>
                            </span>
                        </div>
                        <div class="slot-content">
                            <textarea placeholder="">{body[1]}</textarea>
                        </div>
                        <div class="usage-markers">
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
                            <span class="usage-marker" onclick="toggleUsage(this)"></span>
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
        </div>
    </div>"""


def _build_bottom_section(character: Dict[str, Any]) -> str:
    """Build the bottom section with level, grit, and banked items."""
    level = character.get("level", 1)
    xp = character.get("xp", 0)
    grit = character.get("grit", 0)

    return f"""
    <div class="other-section">
        <div class="section-header" onclick="toggleSection('other')">
            <span class="section-title">Other</span>
            <span class="section-toggle" id="otherToggle">▲</span>
        </div>
        <div class="section-content active" id="otherContent">
            <div class="bottom-section">
                <div class="level-xp-box">
                    <div class="level-row">
                        <span class="stat-label">Level</span>
                        <input type="number" value="{level}" min="1" max="10" />
                    </div>
                    <div class="xp-row">
                        <span class="stat-label">XP</span>
                        <input type="number" value="{xp}" min="0" />
                    </div>
                </div>
                <div class="grit-conditions-box">
                    <div class="grit-row">
                        <span class="stat-label">Grit</span>
                        <input type="number" class="grit-input" value="{grit}" min="0" max="6" data-max-grit="{grit}" />
                    </div>
                    <div class="conditions-area">
                        <div class="conditions-header">
                            <button class="slot-btn add-btn" onclick="addIgnoredCondition(this)">+</button>
                            <span class="conditions-label">Ignored conditions</span>
                        </div>
                        <div class="ignored-conditions-list">
                        </div>
                    </div>
                </div>
                <div class="banked-box">
                    <div class="banked-label">Banked items and pips</div>
                    <textarea placeholder=""></textarea>
                    <div class="mausritter-logo">Mausritter</div>
                </div>
                <div class="level-note">Recovered treasure ▸ XP.</div>
                <div class="grit-note">Ignore a number of conditions equal to your Grit.</div>
                <div class="banked-note"></div>
            </div>
        </div>
    </div>"""


def _build_hirelings_section() -> str:
    """Build the hirelings section with add button."""
    return """
    <div class="hirelings-section">
        <div class="section-header" onclick="toggleSection('hirelings')">
            <span class="section-title">Hirelings</span>
            <span class="section-toggle" id="hirelingsToggle">▼</span>
        </div>
        <div class="section-content" id="hirelingsContent">
            <div class="add-hireling-row">
                <button class="slot-btn add-btn" onclick="addHireling()">+</button>
                <span class="add-hireling-label">Add hireling</span>
            </div>
            <div class="hirelings-container" id="hirelingsContainer">
            </div>
        </div>
    </div>"""


def _build_footer() -> str:
    """Build the footer section."""
    js_code = get_javascript_code()
    return f"""
    <div class="custom-dialog-modal" id="gritAlertModal">
        <div class="custom-dialog-content">
            <div class="custom-dialog-header">Grit</div>
            <div class="custom-dialog-body" id="gritAlertBody">
                No Grit remaining to ignore conditions.
            </div>
            <div class="custom-dialog-buttons">
                <button class="dialog-btn dialog-btn-primary" onclick="closeGritAlert()">OK</button>
            </div>
        </div>
    </div>

    <div class="custom-dialog-modal" id="confirmGenerateModal">
        <div class="custom-dialog-content">
            <div class="custom-dialog-header">Character generation</div>
            <div class="custom-dialog-body">
                Generate a new character? This will replace all current character data.
            </div>
            <div class="custom-dialog-buttons">
                <button class="dialog-btn dialog-btn-secondary" onclick="closeConfirmGenerate()">Cancel</button>
                <button class="dialog-btn dialog-btn-primary" onclick="confirmGenerate()">OK</button>
            </div>
        </div>
    </div>

    <div class="custom-dialog-modal" id="newCharacterModal">
        <div class="custom-dialog-content">
            <div class="custom-dialog-header">New character</div>
            <div class="custom-dialog-body" id="newCharacterBody">
            </div>
            <div class="custom-dialog-buttons">
                <button class="dialog-btn dialog-btn-secondary" onclick="regenerateCharacter()">Regenerate</button>
                <button class="dialog-btn dialog-btn-primary" onclick="acceptCharacter()">Accept</button>
            </div>
        </div>
    </div>

    <div class="item-selector-modal" id="itemSelectorModal">
        <div class="item-selector-content">
            <div class="item-selector-header">
                <span>Select Item</span>
                <button class="close-modal" onclick="closeItemSelector()">&times;</button>
            </div>
            <div class="item-search-container">
                <input type="text" class="item-search-input" id="itemSearchInput" placeholder="Search items..." oninput="filterItems(this.value)" />
            </div>
            <div class="item-selector-body" id="itemSelectorBody">
            </div>
        </div>
    </div>

    <div class="hireling-type-modal" id="hirelingTypeModal">
        <div class="hireling-type-content">
            <div class="hireling-type-header">
                <span>Hire a...</span>
                <button class="close-modal" onclick="closeHirelingTypeSelector()">&times;</button>
            </div>
            <div class="hireling-type-body" id="hirelingTypeBody">
            </div>
        </div>
    </div>

    </div>

    <div class="page-footer">
        This is a personal project. Original character sheet design © <a href="https://mausritter.com" target="_blank">Mausritter</a> by Losing Games.
    </div>

    <script>
{js_code}
    </script>
</body>
</html>"""


def generate_character_sheet_html(character: Dict[str, Any], server_mode: bool = False, token: str = "") -> str:
    """Generate character sheet HTML as a string.

    Args:
        character: Dictionary containing character data
        server_mode: If True, adds server connectivity JavaScript
        token: Player token for server API authentication

    Returns:
        HTML string for the character sheet
    """
    html_parts = [
        _build_head(character["name"]),
        "<body>",
        '    <div class="character-sheet">',
    ]

    # In server mode, don't show "Generate New Character" button
    if not server_mode:
        html_parts.append(_build_generate_button())

    html_parts.extend([
        _build_header_section(character),
        _build_dice_roller(),
        _build_middle_section(character),
        _build_inventory_section(character),
        _build_bottom_section(character),
        _build_hirelings_section(),
        _build_footer(),
    ])

    # Add server connectivity script if in server mode
    if server_mode and token:
        server_script = f"""
    <script>
        // Server connectivity - auto-save changes
        const API_TOKEN = '{token}';
        const CHARACTER_ID = '{character.get("id", "")}';

        function debounce(func, wait) {{
            let timeout;
            return function(...args) {{
                clearTimeout(timeout);
                timeout = setTimeout(() => func.apply(this, args), wait);
            }};
        }}

        function getStatFromRow(statName) {{
            // Find the attribute row by looking for the span with the stat name
            const rows = document.querySelectorAll('.attribute-row');
            for (const row of rows) {{
                const label = row.querySelector('.attribute-label');
                if (label && label.textContent.trim() === statName) {{
                    const inputs = row.querySelectorAll('input[type="number"]');
                    if (inputs.length >= 2) {{
                        return {{
                            max: parseInt(inputs[0].value) || 0,
                            current: parseInt(inputs[1].value) || 0
                        }};
                    }}
                }}
            }}
            return {{ max: 0, current: 0 }};
        }}

        function getHpValues() {{
            const hpRow = document.querySelector('.hp-row');
            if (hpRow) {{
                const inputs = hpRow.querySelectorAll('input[type="number"]');
                if (inputs.length >= 2) {{
                    return {{
                        max: parseInt(inputs[0].value) || 0,
                        current: parseInt(inputs[1].value) || 0
                    }};
                }}
            }}
            return {{ max: 0, current: 0 }};
        }}

        function getInventory() {{
            const inventory = {{
                main_paw: '',
                off_paw: '',
                body: ['', ''],
                pack: ['', '', '', '', '', '']
            }};

            // Paw slots - first two .paw-slot elements
            const pawSlots = document.querySelectorAll('.paw-slot .slot-content textarea');
            if (pawSlots[0]) inventory.main_paw = pawSlots[0].value || '';
            if (pawSlots[1]) inventory.off_paw = pawSlots[1].value || '';

            // Body slots
            const bodySlots = document.querySelectorAll('.body-slot .slot-content textarea');
            bodySlots.forEach((textarea, i) => {{
                if (i < 2) inventory.body[i] = textarea.value || '';
            }});

            // Pack slots
            const packSlots = document.querySelectorAll('.pack-slot .slot-content textarea');
            packSlots.forEach((textarea, i) => {{
                if (i < 6) inventory.pack[i] = textarea.value || '';
            }});

            return inventory;
        }}

        function getHirelings() {{
            const hirelings = [];
            const hirelingCards = document.querySelectorAll('.hireling-card');

            hirelingCards.forEach(card => {{
                const hireling = {{
                    name: card.querySelector('.hireling-name-input')?.value || '',
                    type: card.querySelector('.hireling-type-display')?.textContent || '',
                    look: card.querySelector('.hireling-look-input')?.value || '',
                    disposition: card.querySelector('.hireling-disposition-input')?.value || '',
                    attributes: {{}},
                    hp: {{}},
                    inventory: {{
                        paws: ['', ''],
                        pack: ['', '', '', '']
                    }}
                }};

                // Get hireling stats
                const statRows = card.querySelectorAll('.hireling-attribute-row');
                statRows.forEach(row => {{
                    const label = row.querySelector('.hireling-attribute-label')?.textContent?.trim();
                    const inputs = row.querySelectorAll('input[type="number"]');
                    if (label && inputs.length >= 2) {{
                        hireling.attributes[label] = {{
                            max: parseInt(inputs[0].value) || 0,
                            current: parseInt(inputs[1].value) || 0
                        }};
                    }}
                }});

                // Get hireling HP
                const hpRow = card.querySelector('.hireling-hp-row');
                if (hpRow) {{
                    const inputs = hpRow.querySelectorAll('input[type="number"]');
                    if (inputs.length >= 2) {{
                        hireling.hp = {{
                            max: parseInt(inputs[0].value) || 0,
                            current: parseInt(inputs[1].value) || 0
                        }};
                    }}
                }}

                // Get hireling inventory
                const pawSlots = card.querySelectorAll('.hireling-paw-slot .slot-content textarea');
                pawSlots.forEach((textarea, i) => {{
                    if (i < 2) hireling.inventory.paws[i] = textarea.value || '';
                }});

                const packSlots = card.querySelectorAll('.hireling-pack-slot .slot-content textarea');
                packSlots.forEach((textarea, i) => {{
                    if (i < 4) hireling.inventory.pack[i] = textarea.value || '';
                }});

                hirelings.push(hireling);
            }});

            return hirelings;
        }}

        async function saveToServer() {{
            if (!CHARACTER_ID) return;

            // Collect current character state from DOM
            const data = {{
                name: document.querySelector('.name-input')?.value || '',
                background: document.querySelector('.background-input')?.value || '',
                attributes: {{
                    STR: getStatFromRow('STR'),
                    DEX: getStatFromRow('DEX'),
                    WIL: getStatFromRow('WIL')
                }},
                hp: getHpValues(),
                pips: parseInt(document.querySelector('.pips-input')?.value) || 0,
                grit: parseInt(document.querySelector('.grit-input')?.value) || 0,
                level: parseInt(document.querySelector('.level-row input')?.value) || 1,
                xp: parseInt(document.querySelector('.xp-row input')?.value) || 0,
                inventory: getInventory(),
                hirelings: getHirelings()
            }};

            // Get appearance fields
            const appearanceInputs = document.querySelectorAll('.appearance-row input');
            if (appearanceInputs.length >= 3) {{
                data.appearance = {{
                    birthsign: appearanceInputs[0]?.value || '',
                    coat: appearanceInputs[1]?.value || '',
                    look: appearanceInputs[2]?.value || ''
                }};
            }}

            // Get banked items
            const bankedTextarea = document.querySelector('.banked-box textarea');
            if (bankedTextarea) {{
                data.banked = {{
                    items: bankedTextarea.value || '',
                    pips: 0
                }};
            }}

            // Get notes/portrait
            const portraitTextarea = document.querySelector('.portrait-input');
            if (portraitTextarea) {{
                data.notes = portraitTextarea.value || '';
            }}

            try {{
                const response = await fetch(`/api/characters/${{CHARACTER_ID}}?token=${{API_TOKEN}}`, {{
                    method: 'PATCH',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify(data)
                }});
                if (response.ok) {{
                    showSaveIndicator();
                }} else {{
                    console.error('Save failed:', await response.text());
                }}
            }} catch (e) {{
                console.error('Failed to save:', e);
            }}
        }}

        const debouncedSave = debounce(saveToServer, 1000);

        function showSaveIndicator() {{
            let indicator = document.getElementById('server-save-indicator');
            if (!indicator) {{
                indicator = document.createElement('div');
                indicator.id = 'server-save-indicator';
                indicator.style.cssText = 'position:fixed;bottom:20px;right:20px;background:#4a7a4a;color:white;padding:10px 20px;border-radius:8px;opacity:0;transition:opacity 0.3s;z-index:9999;';
                indicator.textContent = 'Saved!';
                document.body.appendChild(indicator);
            }}
            indicator.style.opacity = '1';
            setTimeout(() => {{ indicator.style.opacity = '0'; }}, 1500);
        }}

        // Attach save listeners to all inputs and textareas
        document.addEventListener('DOMContentLoaded', () => {{
            function attachListeners() {{
                document.querySelectorAll('input, textarea').forEach(el => {{
                    if (!el.dataset.saveListenerAttached) {{
                        el.addEventListener('change', debouncedSave);
                        el.addEventListener('blur', debouncedSave);
                        el.addEventListener('input', debouncedSave);
                        el.dataset.saveListenerAttached = 'true';
                    }}
                }});
            }}

            // Initial attachment
            attachListeners();

            // Watch for new elements (hirelings added dynamically)
            const observer = new MutationObserver(() => {{
                attachListeners();
                debouncedSave();
            }});

            observer.observe(document.body, {{
                childList: true,
                subtree: true,
                characterData: true
            }});
        }});
    </script>
"""
        html_parts.append(server_script)

    return "\n".join(html_parts)


def create_html_character_sheet(character: Dict[str, Any], output_path: Path) -> None:
    """Create an editable HTML character sheet.

    Args:
        character: Dictionary containing character data
        output_path: Path to write the HTML file
    """
    html_content = generate_character_sheet_html(character, server_mode=False)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Character sheet saved to: {output_path}")
