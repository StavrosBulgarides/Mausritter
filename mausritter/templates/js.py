"""JavaScript code for the Mausritter character sheet."""

import json
from ..data import get_all_data_as_json


def get_javascript_code() -> str:
    """Generate JavaScript code with game data injected from Python."""
    data = get_all_data_as_json()

    return f"""
        // Game data (single source of truth from Python - SRD 2.3)
        const BACKGROUND_TABLE = {json.dumps(data["BACKGROUND_TABLE"])};
        const BIRTHSIGNS = {json.dumps(data["BIRTHSIGNS"])};
        const COAT_COLORS = {json.dumps(data["COAT_COLORS"])};
        const COAT_PATTERNS = {json.dumps(data["COAT_PATTERNS"])};
        const PHYSICAL_DETAILS = {json.dumps(data["PHYSICAL_DETAILS"])};
        const FIRST_NAMES = {json.dumps(data["FIRST_NAMES"])};
        const LAST_NAMES = {json.dumps(data["LAST_NAMES"])};
        const WEAPONS = {json.dumps(data["WEAPONS"])};

        function rollDiceSum(numDice, sides) {{
            let total = 0;
            for (let i = 0; i < numDice; i++) {{
                total += Math.floor(Math.random() * sides) + 1;
            }}
            return total;
        }}

        function randomChoice(array) {{
            return array[Math.floor(Math.random() * array.length)];
        }}

        function getBackground(hp, pips) {{
            const key = hp + ',' + pips;
            return BACKGROUND_TABLE[key] || ["Test subject", "Spell: Magic missile", "Lead coat (Heavy armour)"];
        }}

        function rollD66() {{
            // Roll d66: first d6 is tens digit, second is ones digit
            const tens = Math.floor(Math.random() * 6) + 1;
            const ones = Math.floor(Math.random() * 6) + 1;
            return tens * 10 + ones;
        }}

        function getRandomWeapon() {{
            // Get random weapon category, then random weapon from that category
            const categories = Object.keys(WEAPONS);
            const category = categories[Math.floor(Math.random() * categories.length)];
            const weapons = WEAPONS[category];
            const weapon = weapons[Math.floor(Math.random() * weapons.length)];
            // Format: "Name (Category, Damage)"
            return weapon[0] + ' (' + category.charAt(0).toUpperCase() + category.slice(1) + ', ' + weapon[1] + ')';
        }}

        function generateNewCharacter() {{
            try {{
                if (!confirm('Generate a new character? This will replace all current character data.')) {{
                    return;
                }}

                // Roll attributes
                const str = rollDiceSum(3, 6);
                const dex = rollDiceSum(3, 6);
                const wil = rollDiceSum(3, 6);

                // Roll HP and Pips
                const hp = Math.floor(Math.random() * 6) + 1;
                const pips = Math.floor(Math.random() * 6) + 1;

                // Get background
                const [background, itemA, itemB] = getBackground(hp, pips);

                // Determine additional equipment
                const highestAttr = Math.max(str, dex, wil);
                const equipment = ["Torches", "Rations", getRandomWeapon(), itemA, itemB];

                if (highestAttr <= 9) {{
                    const addHp = Math.floor(Math.random() * 6) + 1;
                    const addPips = Math.floor(Math.random() * 6) + 1;
                    const [addBg, addItemA, addItemB] = getBackground(addHp, addPips);
                    equipment.push(addItemA);
                    if (highestAttr <= 7) {{
                        equipment.push(addItemB);
                    }}
                }}

                // Generate appearance
                const birthsignData = randomChoice(BIRTHSIGNS);
                const birthsign = birthsignData[0];
                const disposition = birthsignData[1];
                const coatColor = randomChoice(COAT_COLORS);
                const coatPattern = randomChoice(COAT_PATTERNS);
                const detailRoll = rollD66();
                const physicalDetail = PHYSICAL_DETAILS[detailRoll.toString()];

                // Generate name
                const firstName = randomChoice(FIRST_NAMES);
                const lastName = randomChoice(LAST_NAMES);
                const name = firstName + ' ' + lastName;

                // Update the form fields
                const nameInput = document.querySelector('h1 input[type="text"]');
                if (nameInput) nameInput.value = name;

                // Update attributes (STR, DEX, WIL)
                const attrInputs = document.querySelectorAll('.attribute input[type="number"]');
                if (attrInputs.length >= 3) {{
                    attrInputs[0].value = str;
                    attrInputs[1].value = dex;
                    attrInputs[2].value = wil;
                }} else {{
                    console.error('Could not find attribute inputs');
                }}

                // Update stats (HP, Pips)
                const statInputs = document.querySelectorAll('.stat-box input[type="number"]');
                if (statInputs.length >= 2) {{
                    statInputs[0].value = hp;
                    statInputs[1].value = pips;
                }} else {{
                    console.error('Could not find stat inputs');
                }}

                // Update background - find section with "Background" title
                const allSections = document.querySelectorAll('.section');
                let backgroundUpdated = false;
                for (let section of allSections) {{
                    const title = section.querySelector('.section-title');
                    if (title && title.textContent.trim() === 'Background') {{
                        const bgInput = section.querySelector('input[type="text"]');
                        if (bgInput) {{
                            bgInput.value = background;
                            backgroundUpdated = true;
                            break;
                        }}
                    }}
                }}
                if (!backgroundUpdated) {{
                    console.error('Could not find background input');
                }}

                // Update appearance
                const appearanceInputs = document.querySelectorAll('.appearance-item input[type="text"]');
                if (appearanceInputs.length >= 5) {{
                    appearanceInputs[0].value = birthsign;
                    appearanceInputs[1].value = disposition;
                    appearanceInputs[2].value = coatColor;
                    appearanceInputs[3].value = coatPattern;
                    appearanceInputs[4].value = physicalDetail;
                }} else if (appearanceInputs.length >= 4) {{
                    // Legacy 4-field format
                    appearanceInputs[0].value = birthsign + ' (' + disposition + ')';
                    appearanceInputs[1].value = coatColor;
                    appearanceInputs[2].value = coatPattern;
                    appearanceInputs[3].value = physicalDetail;
                }} else {{
                    console.error('Could not find appearance inputs');
                }}

                // Update equipment
                const equipmentItems = document.querySelectorAll('.equipment-item');
                equipment.forEach((item, index) => {{
                    if (equipmentItems[index]) {{
                        const nameInput = equipmentItems[index].querySelector('.equipment-name');
                        if (nameInput) {{
                            nameInput.value = item;
                        }}
                        // Reset usage checkboxes
                        equipmentItems[index].querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
                    }}
                }});

                // Clear remaining equipment slots
                for (let i = equipment.length; i < equipmentItems.length; i++) {{
                    if (equipmentItems[i]) {{
                        const nameInput = equipmentItems[i].querySelector('.equipment-name');
                        if (nameInput) {{
                            nameInput.value = '';
                        }}
                        equipmentItems[i].querySelectorAll('input[type="checkbox"]').forEach(cb => cb.checked = false);
                    }}
                }}

                alert('New character generated: ' + name + '\\nSTR: ' + str + ', DEX: ' + dex + ', WIL: ' + wil + '\\nHP: ' + hp + ', Pips: ' + pips + '\\nBackground: ' + background);
            }} catch (error) {{
                console.error('Error generating character:', error);
                alert('Error generating character. Please check the browser console for details.');
            }}
        }}

        function toggleDiceRoller() {{
            const content = document.getElementById('diceContent');
            const toggle = document.getElementById('diceToggle');
            if (content && toggle) {{
                content.classList.toggle('active');
                toggle.textContent = content.classList.contains('active') ? '▲' : '▼';
            }}
        }}

        function parseDiceNotation(notation) {{
            const regex = /^(\\d+)d(\\d+)([+-]\\d+)?$/i;
            const match = notation.trim().match(regex);
            if (!match) {{
                return null;
            }}
            return {{
                count: parseInt(match[1]),
                sides: parseInt(match[2]),
                modifier: match[3] ? parseInt(match[3]) : 0
            }};
        }}

        function rollDie(sides) {{
            return Math.floor(Math.random() * sides) + 1;
        }}

        function rollDice() {{
            const input = document.getElementById('diceInput');
            const notation = input.value.trim();
            const diceData = parseDiceNotation(notation);

            if (!diceData) {{
                alert('Invalid dice notation! Please use format like: 2d6, 4d20, 1d10+2');
                return;
            }}

            if (diceData.count > 20) {{
                if (!confirm('You are rolling ' + diceData.count + ' dice. This may take a moment. Continue?')) {{
                    return;
                }}
            }}

            const resultsDiv = document.getElementById('diceResults');
            resultsDiv.innerHTML = '';

            // Create dice containers
            const diceContainer = document.createElement('div');
            diceContainer.className = 'dice-container';

            const dice = [];
            for (let i = 0; i < diceData.count; i++) {{
                const die = document.createElement('div');
                die.className = 'die rolling';
                die.textContent = '?';
                diceContainer.appendChild(die);
                dice.push(die);
            }}

            resultsDiv.appendChild(diceContainer);

            // Roll animation
            const rollDuration = 600;
            const results = [];

            // Animate and roll
            dice.forEach((die, index) => {{
                setTimeout(() => {{
                    let result = rollDie(diceData.sides);
                    results.push(result);
                    die.textContent = result;
                    die.classList.remove('rolling');

                    // Show final results
                    if (index === dice.length - 1) {{
                        setTimeout(() => {{
                            showDiceSummary(results, diceData);
                        }}, 100);
                    }}
                }}, (index * 50) + (rollDuration / 2));
            }});
        }}

        function showDiceSummary(results, diceData) {{
            const resultsDiv = document.getElementById('diceResults');
            const total = results.reduce((a, b) => a + b, 0) + diceData.modifier;

            const summary = document.createElement('div');
            summary.className = 'dice-summary';

            let summaryText = 'Rolled: ' + results.join(', ');
            if (diceData.modifier !== 0) {{
                summaryText += ' ' + (diceData.modifier > 0 ? '+' : '') + diceData.modifier;
            }}
            summaryText += '<br><span class="total">Total: ' + total + '</span>';

            summary.innerHTML = summaryText;
            resultsDiv.appendChild(summary);
        }}

        // Make functions globally accessible
        window.generateNewCharacter = generateNewCharacter;
        window.toggleDiceRoller = toggleDiceRoller;
        window.rollDice = rollDice;

        document.addEventListener('DOMContentLoaded', function() {{
            console.log('Character sheet loaded');

            const diceInput = document.getElementById('diceInput');
            if (diceInput) {{
                diceInput.addEventListener('keypress', function(e) {{
                    if (e.key === 'Enter') {{
                        rollDice();
                    }}
                }});
            }} else {{
                console.error('Could not find diceInput');
            }}

            // Ensure dice roller header is clickable
            const diceHeader = document.querySelector('.dice-roller-header');
            if (diceHeader) {{
                diceHeader.addEventListener('click', function(e) {{
                    e.preventDefault();
                    e.stopPropagation();
                    toggleDiceRoller();
                }});
                console.log('Dice roller header click handler attached');
            }} else {{
                console.error('Could not find dice roller header');
            }}

            // Test if functions are accessible
            if (typeof generateNewCharacter === 'function') {{
                console.log('generateNewCharacter function is available');
            }} else {{
                console.error('generateNewCharacter function is NOT available');
            }}

            if (typeof toggleDiceRoller === 'function') {{
                console.log('toggleDiceRoller function is available');
            }} else {{
                console.error('toggleDiceRoller function is NOT available');
            }}
        }});
"""
