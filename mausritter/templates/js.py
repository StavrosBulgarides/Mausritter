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

        function rollAttribute() {{
            // Roll 3d6 and keep the two highest dice (per SRD 2.3)
            // Returns a value between 2-12
            const rolls = [
                Math.floor(Math.random() * 6) + 1,
                Math.floor(Math.random() * 6) + 1,
                Math.floor(Math.random() * 6) + 1
            ];
            rolls.sort((a, b) => b - a);  // Sort descending
            return rolls[0] + rolls[1];   // Keep two highest
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

                // Roll attributes (3d6 keep two highest, per SRD 2.3)
                const str = rollAttribute();
                const dex = rollAttribute();
                const wil = rollAttribute();

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

                // Update name
                const nameInput = document.querySelector('.name-input');
                if (nameInput) nameInput.value = name;

                // Update background
                const backgroundInput = document.querySelector('.background-input');
                if (backgroundInput) backgroundInput.value = background;

                // Update attributes (STR, DEX, WIL) - each row has max and current inputs
                const attrRows = document.querySelectorAll('.attribute-row');
                if (attrRows.length >= 3) {{
                    const attrs = [str, dex, wil];
                    attrRows.forEach((row, index) => {{
                        const inputs = row.querySelectorAll('input[type="number"]');
                        if (inputs.length >= 2) {{
                            inputs[0].value = attrs[index];  // max
                            inputs[0].max = attrs[index];    // set max attribute on input
                            inputs[1].value = attrs[index];  // current starts at max
                            inputs[1].max = attrs[index];    // current can't exceed max
                        }}
                    }});
                }}

                // Update HP - row has max and current inputs
                const hpRow = document.querySelector('.hp-row');
                if (hpRow) {{
                    const hpInputs = hpRow.querySelectorAll('input[type="number"]');
                    if (hpInputs.length >= 2) {{
                        hpInputs[0].value = hp;   // max
                        hpInputs[0].max = hp;     // set max attribute on input
                        hpInputs[1].value = hp;   // current starts at max
                        hpInputs[1].max = hp;     // current can't exceed max
                    }}
                }}

                // Update Pips
                const pipsInput = document.querySelector('.pips-input');
                const pipsTotalInput = document.querySelector('.pips-total-input');
                if (pipsInput) pipsInput.value = pips;
                if (pipsTotalInput) pipsTotalInput.value = pips;

                // Update appearance
                const appearanceRows = document.querySelectorAll('.appearance-row input[type="text"]');
                if (appearanceRows.length >= 3) {{
                    appearanceRows[0].value = birthsign + ' (' + disposition + ')';
                    appearanceRows[1].value = coatColor + ', ' + coatPattern;
                    appearanceRows[2].value = physicalDetail;
                }}

                // Helper to format item text with brackets on new line
                function formatItemText(item) {{
                    if (item.includes('(') && item.includes(')')) {{
                        const idx = item.indexOf('(');
                        const name = item.substring(0, idx).trim();
                        const details = item.substring(idx);
                        return name + '\\n' + details;
                    }}
                    return item;
                }}

                // Update inventory slots (now using textareas)
                // New structure: paw-grid (main_paw, off_paw), body-grid (body[0], body[1]), pack-grid (1-6)
                const pawSlots = document.querySelectorAll('.paw-grid .slot-content textarea');
                const bodySlots = document.querySelectorAll('.body-grid .slot-content textarea');
                const packSlots = document.querySelectorAll('.pack-grid .slot-content textarea');

                // Clear all slots first
                pawSlots.forEach(slot => slot.value = '');
                bodySlots.forEach(slot => slot.value = '');
                packSlots.forEach(slot => slot.value = '');

                // Weapon goes to main paw (or off paw for heavy)
                const formattedWeapon = formatItemText(equipment[2]);
                if (pawSlots[0]) pawSlots[0].value = formattedWeapon;

                // Check if any items are armor for body slots
                const packItems = [];
                const armorKeywords = ['armour', 'armor', 'jerkin'];
                let bodySlotIdx = 0;

                // Process background items (itemA and itemB at indices 3 and 4)
                [equipment[3], equipment[4]].forEach(item => {{
                    if (item) {{
                        const isArmor = armorKeywords.some(kw => item.toLowerCase().includes(kw));
                        const formattedItem = formatItemText(item);
                        if (isArmor && bodySlotIdx < 2) {{
                            bodySlots[bodySlotIdx].value = formattedItem;
                            bodySlotIdx++;
                        }} else {{
                            packItems.push(formattedItem);
                        }}
                    }}
                }});

                // Add torches, rations to pack
                packItems.unshift(equipment[1]);  // Rations
                packItems.unshift(equipment[0]);  // Torches

                // Add additional items from low stats
                if (equipment[5]) packItems.push(formatItemText(equipment[5]));
                if (equipment[6]) packItems.push(formatItemText(equipment[6]));

                // Fill pack slots
                packItems.forEach((item, idx) => {{
                    if (packSlots[idx]) packSlots[idx].value = item;
                }});

                // Reset level, XP, grit to starting values
                const levelInput = document.querySelector('.level-box input[type="number"]');
                const xpInput = document.querySelector('.xp-box input[type="number"]');
                const gritInput = document.querySelector('.grit-box input[type="number"]');
                if (levelInput) levelInput.value = 1;
                if (xpInput) xpInput.value = 0;
                if (gritInput) gritInput.value = 0;

                // Clear text areas
                document.querySelectorAll('.portrait-input, .conditions-box textarea, .banked-box textarea').forEach(ta => ta.value = '');

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

            // Dice roller uses inline onclick="toggleDiceRoller()"

            // Enforce max values on current inputs for attributes
            const attrRows = document.querySelectorAll('.attribute-row');
            attrRows.forEach(row => {{
                const inputs = row.querySelectorAll('input[type="number"]');
                if (inputs.length >= 2) {{
                    const maxInput = inputs[0];
                    const currentInput = inputs[1];

                    // When max changes, update the current input's max attribute
                    maxInput.addEventListener('change', function() {{
                        currentInput.max = this.value;
                        if (parseInt(currentInput.value) > parseInt(this.value)) {{
                            currentInput.value = this.value;
                        }}
                    }});

                    // Enforce current can't exceed max
                    currentInput.addEventListener('change', function() {{
                        const maxVal = parseInt(maxInput.value);
                        if (parseInt(this.value) > maxVal) {{
                            this.value = maxVal;
                        }}
                        if (parseInt(this.value) < 0) {{
                            this.value = 0;
                        }}
                    }});
                }}
            }});

            // Enforce max values on HP
            const hpRow = document.querySelector('.hp-row');
            if (hpRow) {{
                const hpInputs = hpRow.querySelectorAll('input[type="number"]');
                if (hpInputs.length >= 2) {{
                    const maxHpInput = hpInputs[0];
                    const currentHpInput = hpInputs[1];

                    maxHpInput.addEventListener('change', function() {{
                        currentHpInput.max = this.value;
                        if (parseInt(currentHpInput.value) > parseInt(this.value)) {{
                            currentHpInput.value = this.value;
                        }}
                    }});

                    currentHpInput.addEventListener('change', function() {{
                        const maxVal = parseInt(maxHpInput.value);
                        if (parseInt(this.value) > maxVal) {{
                            this.value = maxVal;
                        }}
                        if (parseInt(this.value) < 0) {{
                            this.value = 0;
                        }}
                    }});
                }}
            }}

            // Enforce pips can't exceed total
            const pipsInput = document.querySelector('.pips-input');
            const pipsTotalInput = document.querySelector('.pips-total-input');
            if (pipsInput && pipsTotalInput) {{
                pipsTotalInput.addEventListener('change', function() {{
                    if (parseInt(pipsInput.value) > parseInt(this.value)) {{
                        pipsInput.value = this.value;
                    }}
                }});

                pipsInput.addEventListener('change', function() {{
                    const maxVal = parseInt(pipsTotalInput.value);
                    if (parseInt(this.value) > maxVal) {{
                        this.value = maxVal;
                    }}
                    if (parseInt(this.value) < 0) {{
                        this.value = 0;
                    }}
                }});
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
