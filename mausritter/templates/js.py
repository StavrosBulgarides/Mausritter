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
        const INVENTORY_ITEMS = {json.dumps(data["INVENTORY_ITEMS"])};
        const HIRELING_LOOKS = {json.dumps(data["HIRELING_LOOKS"])};
        const HIRELING_DISPOSITIONS = {json.dumps(data["HIRELING_DISPOSITIONS"])};
        const HIRELING_TYPES = {json.dumps(data["HIRELING_TYPES"])};

        // Condition clearing requirements lookup
        const CONDITION_CLEAR = {{
            'Exhausted': 'Clear: Rest a night in camp',
            'Frightened': 'Clear: A moment\\'s rest in a safe place',
            'Hungry': 'Clear: Eat a fresh ration',
            'Injured': 'Clear: Heal 1 STR at full rest',
            'Poisoned': 'Clear: Antidote, healer\\'s care, or rest in a safe settlement',
            'Stunned': 'Clear: A moment\\'s rest in a safe place'
        }};

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

        // Store pending character data for Accept/Regenerate flow
        let pendingCharacter = null;

        function generateCharacterData() {{
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

            return {{
                name, str, dex, wil, hp, pips, background,
                birthsign, disposition, coatColor, coatPattern, physicalDetail,
                equipment
            }};
        }}

        function applyCharacterData(charData) {{
            // Update name
            const nameInput = document.querySelector('.name-input');
            if (nameInput) nameInput.value = charData.name;

            // Update background
            const backgroundInput = document.querySelector('.background-input');
            if (backgroundInput) backgroundInput.value = charData.background;

            // Update attributes (STR, DEX, WIL) - each row has max and current inputs
            const attrRows = document.querySelectorAll('.attribute-row');
            if (attrRows.length >= 3) {{
                const attrs = [charData.str, charData.dex, charData.wil];
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
                    hpInputs[0].value = charData.hp;   // max
                    hpInputs[0].max = charData.hp;     // set max attribute on input
                    hpInputs[1].value = charData.hp;   // current starts at max
                    hpInputs[1].max = charData.hp;     // current can't exceed max
                }}
            }}

            // Update Pips (only current pips, max is always 250)
            const pipsInput = document.querySelector('.pips-input');
            if (pipsInput) pipsInput.value = charData.pips;

            // Update appearance
            const appearanceRows = document.querySelectorAll('.appearance-row input[type="text"]');
            if (appearanceRows.length >= 3) {{
                appearanceRows[0].value = charData.birthsign + ' (' + charData.disposition + ')';
                appearanceRows[1].value = charData.coatColor + ', ' + charData.coatPattern;
                appearanceRows[2].value = charData.physicalDetail;
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
            const pawSlots = document.querySelectorAll('.paw-grid .slot-content textarea');
            const bodySlots = document.querySelectorAll('.body-grid .slot-content textarea');
            const packSlots = document.querySelectorAll('.pack-grid .slot-content textarea');

            // Clear all slots first
            pawSlots.forEach(slot => slot.value = '');
            bodySlots.forEach(slot => slot.value = '');
            packSlots.forEach(slot => slot.value = '');

            // Prompt user to select their weapon
            if (pawSlots[0]) {{
                pawSlots[0].value = 'Select weapon';
                pawSlots[0].classList.add('needs-selection');
            }}

            // Check if any items are armor for body/paw slots
            const packItems = [];
            let bodySlotIdx = 0;

            // Process background items (itemA and itemB at indices 3 and 4)
            [charData.equipment[3], charData.equipment[4]].forEach(item => {{
                if (item) {{
                    const formattedItem = formatItemText(item);
                    const isLightArmour = item.toLowerCase().includes('light armour');
                    const isHeavyArmour = item.toLowerCase().includes('heavy armour');

                    if (isLightArmour) {{
                        // Light armour goes in 1 paw slot + 1 body slot (same row)
                        // Use off paw (slot 1) so main paw can have weapon, paired with body slot 1
                        if (pawSlots[1]) {{
                            pawSlots[1].value = formattedItem;
                            const pawSlot = pawSlots[1].closest('.inventory-slot');
                            if (pawSlot) {{
                                pawSlot.classList.add('two-slot-item', 'light-armour-slot');
                            }}
                        }}
                        if (bodySlots[1]) {{
                            bodySlots[1].value = formattedItem;
                            bodySlots[1].readOnly = true;
                            const bodySlot = bodySlots[1].closest('.inventory-slot');
                            if (bodySlot) {{
                                bodySlot.classList.add('two-slot-secondary', 'light-armour-slot');
                            }}
                        }}
                    }} else if (isHeavyArmour && bodySlotIdx < 2) {{
                        // Heavy armour takes both body slots
                        bodySlots[0].value = formattedItem;
                        bodySlots[1].value = formattedItem;
                        bodySlots[1].readOnly = true;
                        const bodySlot0 = bodySlots[0].closest('.inventory-slot');
                        const bodySlot1 = bodySlots[1].closest('.inventory-slot');
                        if (bodySlot0) bodySlot0.classList.add('two-slot-item');
                        if (bodySlot1) bodySlot1.classList.add('two-slot-secondary');
                        bodySlotIdx = 2; // Both body slots used
                    }} else {{
                        packItems.push(formattedItem);
                    }}
                }}
            }});

            // Add torches, rations to pack
            packItems.unshift(charData.equipment[1]);  // Rations
            packItems.unshift(charData.equipment[0]);  // Torches

            // Add additional items from low stats
            if (charData.equipment[5]) packItems.push(formatItemText(charData.equipment[5]));
            if (charData.equipment[6]) packItems.push(formatItemText(charData.equipment[6]));

            // Fill pack slots
            packItems.forEach((item, idx) => {{
                if (packSlots[idx]) packSlots[idx].value = item;
            }});

            // Reset level, XP, grit to starting values
            const levelInput = document.querySelector('.level-box input[type="number"]');
            const xpInput = document.querySelector('.xp-box input[type="number"]');
            const gritInput = document.querySelector('.grit-input');
            if (levelInput) levelInput.value = 1;
            if (xpInput) xpInput.value = 0;
            if (gritInput) {{
                gritInput.value = 0;
                gritInput.dataset.maxGrit = 0;
            }}

            // Clear ignored conditions
            const ignoredConditionsList = document.querySelector('.ignored-conditions-list');
            if (ignoredConditionsList) ignoredConditionsList.innerHTML = '';

            // Clear text areas
            document.querySelectorAll('.portrait-input, .banked-box textarea').forEach(ta => ta.value = '');

            // Reset usage markers
            resetUsageMarkers();

            // Update slot empty states
            updateAllSlotEmptyStates();

            // Clear existing hirelings and create background-specific hireling if applicable
            clearAllHirelings();
            if (BACKGROUND_HIRELINGS[charData.background]) {{
                addHirelingWithType(BACKGROUND_HIRELINGS[charData.background]);
            }}
        }}

        function showNewCharacterDialog(charData) {{
            const body = document.getElementById('newCharacterBody');
            body.innerHTML = '<strong>' + charData.name + '</strong><br><br>' +
                'STR: ' + charData.str + ', DEX: ' + charData.dex + ', WIL: ' + charData.wil + '<br>' +
                'HP: ' + charData.hp + ', Pips: ' + charData.pips + '<br><br>' +
                'Background: ' + charData.background;
            document.getElementById('newCharacterModal').classList.add('active');
        }}

        function generateNewCharacter() {{
            document.getElementById('confirmGenerateModal').classList.add('active');
        }}

        function closeConfirmGenerate() {{
            document.getElementById('confirmGenerateModal').classList.remove('active');
        }}

        function confirmGenerate() {{
            document.getElementById('confirmGenerateModal').classList.remove('active');
            try {{
                pendingCharacter = generateCharacterData();
                showNewCharacterDialog(pendingCharacter);
            }} catch (error) {{
                console.error('Error generating character:', error);
                alert('Error generating character. Please check the browser console for details.');
            }}
        }}

        function regenerateCharacter() {{
            try {{
                pendingCharacter = generateCharacterData();
                showNewCharacterDialog(pendingCharacter);
            }} catch (error) {{
                console.error('Error regenerating character:', error);
                alert('Error regenerating character. Please check the browser console for details.');
            }}
        }}

        function acceptCharacter() {{
            if (pendingCharacter) {{
                applyCharacterData(pendingCharacter);
                pendingCharacter = null;
            }}
            document.getElementById('newCharacterModal').classList.remove('active');
        }}

        function toggleDiceRoller() {{
            const content = document.getElementById('diceContent');
            const toggle = document.getElementById('diceToggle');
            if (content && toggle) {{
                content.classList.toggle('active');
                toggle.textContent = content.classList.contains('active') ? '▲' : '▼';
            }}
        }}

        function toggleInventory() {{
            const content = document.getElementById('inventoryContent');
            const toggle = document.getElementById('inventoryToggle');
            if (content && toggle) {{
                content.classList.toggle('active');
                toggle.textContent = content.classList.contains('active') ? '▲' : '▼';
            }}
        }}

        function toggleSection(sectionName) {{
            const content = document.getElementById(sectionName + 'Content');
            const toggle = document.getElementById(sectionName + 'Toggle');
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

        // Save roll state
        let currentSaveRoll = null;

        function showDiceSummary(results, diceData) {{
            const total = results.reduce((a, b) => a + b, 0) + diceData.modifier;
            const diceContent = document.getElementById('diceContent');

            // Determine which results div to use
            const resultsDiv = currentSaveRoll
                ? document.getElementById('saveRollResults')
                : document.getElementById('diceResults');

            const summary = document.createElement('div');
            summary.className = 'dice-summary';

            let summaryText = '';

            // Check if this is a save roll
            if (currentSaveRoll) {{
                let effectiveResult = total;
                let rollDisplay = '';

                // Handle advantage/disadvantage
                if (currentSaveRoll.modifier && results.length === 2) {{
                    if (currentSaveRoll.modifier === 'advantage') {{
                        // Take lowest
                        effectiveResult = Math.min(results[0], results[1]);
                        const usedIndex = results[0] <= results[1] ? 0 : 1;
                        rollDisplay = results.map((r, i) =>
                            i === usedIndex ? '<strong>' + r + '</strong>' : '<span style="opacity:0.5;text-decoration:line-through">' + r + '</span>'
                        ).join(', ');
                    }} else if (currentSaveRoll.modifier === 'disadvantage') {{
                        // Take highest
                        effectiveResult = Math.max(results[0], results[1]);
                        const usedIndex = results[0] >= results[1] ? 0 : 1;
                        rollDisplay = results.map((r, i) =>
                            i === usedIndex ? '<strong>' + r + '</strong>' : '<span style="opacity:0.5;text-decoration:line-through">' + r + '</span>'
                        ).join(', ');
                    }}
                    summaryText = '<span class="total">Rolled: ' + rollDisplay + ' = ' + effectiveResult + '</span>';
                }} else {{
                    summaryText = '<span class="total">Rolled: ' + effectiveResult + '</span>';
                }}

                const isSuccess = effectiveResult <= currentSaveRoll.target;
                if (isSuccess) {{
                    summaryText += '<span class="save-result success"> — Success!</span>';
                    diceContent.classList.remove('save-fail');
                    diceContent.classList.add('save-success');
                }} else {{
                    summaryText += '<span class="save-result fail"> — Fail!</span>';
                    diceContent.classList.remove('save-success');
                    diceContent.classList.add('save-fail');
                }}
            }} else {{
                summaryText = 'Rolled: ' + results.join(', ');
                if (diceData.modifier !== 0) {{
                    summaryText += ' ' + (diceData.modifier > 0 ? '+' : '') + diceData.modifier;
                }}
                summaryText += '<br><span class="total">Total: ' + total + '</span>';
            }}

            summary.innerHTML = summaryText;
            resultsDiv.appendChild(summary);
        }}

        function clearSaveState() {{
            currentSaveRoll = null;
            const saveResultsRow = document.getElementById('saveResultsRow');
            const diceContent = document.getElementById('diceContent');
            const diceResults = document.getElementById('diceResults');
            if (saveResultsRow) saveResultsRow.style.display = 'none';
            if (diceResults) diceResults.style.display = 'block';
            if (diceContent) {{
                diceContent.classList.remove('save-success', 'save-fail');
            }}
        }}

        function manualRollDice() {{
            // Clear save state when user manually rolls
            clearSaveState();
            rollDice();
        }}

        function rollSave(stat, modifier = null) {{
            // Get current stat value
            const attrRows = document.querySelectorAll('.attribute-row');
            let targetValue = 10;

            attrRows.forEach(row => {{
                const label = row.querySelector('.attribute-label');
                if (label && label.textContent === stat) {{
                    const inputs = row.querySelectorAll('input[type="number"]');
                    if (inputs.length >= 2) {{
                        targetValue = parseInt(inputs[1].value) || 10; // Current value
                    }}
                }}
            }});

            // Set up save state
            currentSaveRoll = {{
                stat: stat,
                target: targetValue,
                modifier: modifier // 'advantage', 'disadvantage', or null
            }};

            // Update button states
            const advBtn = document.getElementById('advantageBtn');
            const disBtn = document.getElementById('disadvantageBtn');
            if (advBtn) advBtn.classList.toggle('active', modifier === 'advantage');
            if (disBtn) disBtn.classList.toggle('active', modifier === 'disadvantage');

            // Update save info display
            const saveResultsRow = document.getElementById('saveResultsRow');
            const saveStatName = document.getElementById('saveStatName');
            const saveTarget = document.getElementById('saveTarget');
            const saveRollResults = document.getElementById('saveRollResults');
            const diceResults = document.getElementById('diceResults');

            if (saveResultsRow && saveStatName && saveTarget) {{
                saveStatName.textContent = stat + ' Save';
                saveTarget.textContent = 'Target: ≤' + targetValue;
                saveResultsRow.style.display = 'flex';
            }}

            // Clear both results areas (dice graphics will show in diceResults, summary in saveRollResults)
            if (diceResults) {{
                diceResults.style.display = 'block';
                diceResults.innerHTML = '';
            }}
            if (saveRollResults) saveRollResults.innerHTML = '';

            // Set dice notation based on modifier
            const diceInput = document.getElementById('diceInput');
            if (diceInput) {{
                diceInput.value = modifier ? '2d20' : '1d20';
            }}

            // Clear previous result state
            const diceContent = document.getElementById('diceContent');
            if (diceContent) {{
                diceContent.classList.remove('save-success', 'save-fail');
            }}

            // Open dice roller if not already open
            const content = document.getElementById('diceContent');
            const toggle = document.getElementById('diceToggle');
            if (content && !content.classList.contains('active')) {{
                content.classList.add('active');
                if (toggle) toggle.textContent = '▲';
            }}

            // Auto-roll the dice
            rollDice();
        }}

        function rollWithAdvantage() {{
            if (currentSaveRoll) {{
                rollSave(currentSaveRoll.stat, 'advantage');
            }}
        }}

        function rollWithDisadvantage() {{
            if (currentSaveRoll) {{
                rollSave(currentSaveRoll.stat, 'disadvantage');
            }}
        }}

        function isTorchOrLantern(slot) {{
            const textarea = slot.querySelector('.slot-content textarea');
            if (!textarea) return false;
            const content = textarea.value.toLowerCase();
            return content.includes('torch') || content.includes('lantern');
        }}

        function updateSlotEmptyState(slot) {{
            const textarea = slot.querySelector('.slot-content textarea');
            if (!textarea) return;
            const isEmpty = !textarea.value.trim() || textarea.value.trim() === 'Select weapon';
            if (isEmpty) {{
                slot.classList.add('slot-empty');
            }} else {{
                slot.classList.remove('slot-empty');
            }}
        }}

        function updateAllSlotEmptyStates() {{
            document.querySelectorAll('.inventory-slot').forEach(slot => {{
                updateSlotEmptyState(slot);
            }});
        }}

        function toggleUsage(marker) {{
            const slot = marker.closest('.inventory-slot');
            const textarea = slot.querySelector('.slot-content textarea');

            // Don't allow marking empty slots or "Select weapon" placeholder
            if (!textarea || !textarea.value.trim() || textarea.value.trim() === 'Select weapon') {{
                return;
            }}

            const markers = Array.from(slot.querySelectorAll('.usage-marker'));
            const isSixUseItem = isTorchOrLantern(slot);

            // Determine if we're filling or unfilling based on any marker being used/half-used
            const anyUsed = markers.some(m => m.classList.contains('used') || m.classList.contains('half-used'));
            const clickedIsUsed = marker.classList.contains('used') || marker.classList.contains('half-used');

            if (isSixUseItem) {{
                // 6-use items: each marker cycles through empty → half → full → empty
                if (marker.classList.contains('used')) {{
                    // Full → Empty
                    marker.classList.remove('used');
                }} else if (marker.classList.contains('half-used')) {{
                    // Half → Full
                    marker.classList.remove('half-used');
                    marker.classList.add('used');
                }} else {{
                    // Empty → Half
                    marker.classList.add('half-used');
                }}
                // Check if all markers are fully used (depleted)
                const allFullyUsed = markers.every(m => m.classList.contains('used'));
                if (allFullyUsed) {{
                    slot.classList.add('depleted');
                }} else {{
                    slot.classList.remove('depleted');
                }}
            }} else {{
                // Standard 3-use items
                if (clickedIsUsed) {{
                    // Unfill the rightmost filled marker (3→2→1)
                    for (let i = markers.length - 1; i >= 0; i--) {{
                        if (markers[i].classList.contains('used')) {{
                            markers[i].classList.remove('used');
                            break;
                        }}
                    }}
                }} else {{
                    // Fill the leftmost empty marker (1→2→3)
                    for (let i = 0; i < markers.length; i++) {{
                        if (!markers[i].classList.contains('used')) {{
                            markers[i].classList.add('used');
                            break;
                        }}
                    }}
                }}

                // Check if all markers in this slot are used
                const allUsed = markers.every(m => m.classList.contains('used'));

                // Find paired slot if this is a two-slot item
                let pairedSlot = null;
                if (slot.classList.contains('two-slot-item')) {{
                    const parentGrid = slot.parentElement;
                    const isLightArmour = slot.classList.contains('light-armour-slot');

                    if (isLightArmour) {{
                        // Light armour: find paired slot across paw/body grids by row position
                        const pawGrid = document.querySelector('.paw-grid');
                        const bodyGrid = document.querySelector('.body-grid');

                        if (parentGrid.classList.contains('paw-grid')) {{
                            // Get same-row body slot
                            const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                            const currentIndex = Array.from(pawSlots).indexOf(slot);
                            const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                            pairedSlot = bodySlots[currentIndex];
                        }} else if (parentGrid.classList.contains('body-grid')) {{
                            // Get same-row paw slot
                            const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                            const currentIndex = Array.from(bodySlots).indexOf(slot);
                            const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                            pairedSlot = pawSlots[currentIndex];
                        }}
                    }} else if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
                        const slots = parentGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(slots).indexOf(slot);
                        pairedSlot = slots[currentIndex === 0 ? 1 : 0];
                    }} else if (parentGrid.classList.contains('pack-grid')) {{
                        const slots = parentGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(slots).indexOf(slot);
                        const pairedIndex = currentIndex < 3 ? currentIndex + 3 : currentIndex - 3;
                        pairedSlot = slots[pairedIndex];
                    }}
                }}

                if (allUsed) {{
                    slot.classList.add('depleted');
                    if (pairedSlot) pairedSlot.classList.add('depleted');
                }} else {{
                    slot.classList.remove('depleted');
                    if (pairedSlot) pairedSlot.classList.remove('depleted');
                }}
            }}
        }}

        function resetUsageMarkers() {{
            // Reset all usage markers and depleted states
            document.querySelectorAll('.usage-marker').forEach(marker => {{
                marker.classList.remove('used');
                marker.classList.remove('half-used');
            }});
            document.querySelectorAll('.inventory-slot').forEach(slot => {{
                slot.classList.remove('depleted');
                slot.classList.remove('two-slot-item');
                slot.classList.remove('two-slot-secondary');
                slot.classList.remove('light-armour-slot');
                const textarea = slot.querySelector('.slot-content textarea');
                if (textarea) textarea.readOnly = false;
            }});
        }}

        // Item selector state
        let currentTargetSlot = null;
        let currentHirelingSlot = null;
        let hirelingCounter = 0;

        function openItemSelector(button) {{
            // Find the inventory-slot that contains this button
            currentTargetSlot = button.closest('.inventory-slot');

            // Clear search input and build items
            const searchInput = document.getElementById('itemSearchInput');
            searchInput.value = '';
            buildItemList('');

            // Show the modal and focus search
            document.getElementById('itemSelectorModal').classList.add('active');
            searchInput.focus();
        }}

        function buildItemList(searchQuery) {{
            const body = document.getElementById('itemSelectorBody');
            body.innerHTML = '';
            const query = searchQuery.toLowerCase().trim();

            for (const [category, items] of Object.entries(INVENTORY_ITEMS)) {{
                // Filter items based on search query (search in name, price, slots, notes)
                const filteredItems = query ? items.filter(item => {{
                    const searchText = (item.name + ' ' + item.price + ' ' + item.slots + ' slot' + (item.slots > 1 ? 's' : '') + ' ' + (item.notes || '')).toLowerCase();
                    return searchText.includes(query);
                }}) : items;

                // Skip empty categories when searching
                if (query && filteredItems.length === 0) continue;

                const categoryDiv = document.createElement('div');
                categoryDiv.className = 'item-category';
                // Add special class for Conditions category
                if (category === 'Conditions') {{
                    categoryDiv.classList.add('conditions-category');
                }}

                const header = document.createElement('div');
                header.className = 'item-category-header';
                header.textContent = category;
                header.onclick = function() {{
                    const itemsDiv = this.nextElementSibling;
                    itemsDiv.classList.toggle('expanded');
                }};

                const itemsDiv = document.createElement('div');
                itemsDiv.className = 'item-category-items';
                // Auto-expand when searching
                if (query) itemsDiv.classList.add('expanded');

                filteredItems.forEach(item => {{
                    const itemOption = document.createElement('div');
                    itemOption.className = 'item-option';

                    const itemName = document.createElement('span');
                    itemName.className = 'item-name';
                    itemName.textContent = item.name;

                    const itemDetails = document.createElement('span');
                    itemDetails.className = 'item-details';
                    let details = item.price + ' | ' + item.slots + ' slot' + (item.slots > 1 ? 's' : '');
                    if (item.notes) details += ' | ' + item.notes;
                    itemDetails.textContent = details;

                    itemOption.appendChild(itemName);
                    itemOption.appendChild(itemDetails);
                    itemOption.onclick = function() {{
                        selectItem(item.name, item.slots);
                    }};
                    itemsDiv.appendChild(itemOption);
                }});

                categoryDiv.appendChild(header);
                categoryDiv.appendChild(itemsDiv);
                body.appendChild(categoryDiv);
            }}
        }}

        function filterItems(query) {{
            buildItemList(query);
        }}

        function closeItemSelector() {{
            document.getElementById('itemSelectorModal').classList.remove('active');
            currentTargetSlot = null;
        }}

        function selectItem(itemName, slots) {{
            // Check if this is for a hireling slot
            if (currentHirelingSlot) {{
                selectHirelingItem(itemName, slots);
                return;
            }}

            if (currentTargetSlot) {{
                // Format item text
                let itemText = itemName;
                if (itemName.includes('(') && itemName.includes(')')) {{
                    const idx = itemName.indexOf('(');
                    const name = itemName.substring(0, idx).trim();
                    const details = itemName.substring(idx);
                    itemText = name + '\\n' + details;
                }}

                const textarea = currentTargetSlot.querySelector('.slot-content textarea');
                if (textarea) {{
                    textarea.value = itemText;
                    textarea.classList.remove('needs-selection');
                }}

                // Update slot empty state
                updateSlotEmptyState(currentTargetSlot);

                // Reset usage markers for this slot
                const markers = currentTargetSlot.querySelectorAll('.usage-marker');
                markers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                currentTargetSlot.classList.remove('depleted');
                currentTargetSlot.classList.remove('two-slot-item');
                currentTargetSlot.classList.remove('two-slot-secondary');
                currentTargetSlot.classList.remove('condition-slot');

                // Remove any existing condition clear text
                const existingClear = currentTargetSlot.querySelector('.condition-clear');
                if (existingClear) existingClear.remove();

                // Check if this is a condition and apply special styling
                if (CONDITION_CLEAR[itemName]) {{
                    currentTargetSlot.classList.add('condition-slot');
                    // Add the clearing condition text
                    const clearDiv = document.createElement('div');
                    clearDiv.className = 'condition-clear';
                    clearDiv.textContent = CONDITION_CLEAR[itemName];
                    currentTargetSlot.querySelector('.slot-content').appendChild(clearDiv);
                }}

                // Handle 2-slot items
                if (slots === 2) {{
                    currentTargetSlot.classList.add('two-slot-item');

                    // Find the paired slot
                    let pairedSlot = null;
                    const parentGrid = currentTargetSlot.parentElement;

                    // Check if this is light armour (uses 1 paw + 1 body)
                    const isLightArmour = itemName.toLowerCase().includes('light armour');

                    if (isLightArmour) {{
                        // Light armour: pair across paw and body grids by row position
                        const pawGrid = document.querySelector('.paw-grid');
                        const bodyGrid = document.querySelector('.body-grid');

                        if (parentGrid.classList.contains('paw-grid')) {{
                            // Currently in paw slot, pair with same-row body slot
                            const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                            const currentIndex = Array.from(pawSlots).indexOf(currentTargetSlot);
                            const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                            pairedSlot = bodySlots[currentIndex]; // Same row position
                        }} else if (parentGrid.classList.contains('body-grid')) {{
                            // Currently in body slot, pair with same-row paw slot
                            const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                            const currentIndex = Array.from(bodySlots).indexOf(currentTargetSlot);
                            const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                            pairedSlot = pawSlots[currentIndex]; // Same row position
                        }}

                        // Mark as light armour for special handling during clear
                        currentTargetSlot.classList.add('light-armour-slot');
                    }} else if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
                        // For paw/body grids, pair with the other slot in the same grid
                        const slots = parentGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(slots).indexOf(currentTargetSlot);
                        pairedSlot = slots[currentIndex === 0 ? 1 : 0];
                    }} else if (parentGrid.classList.contains('pack-grid')) {{
                        // For pack grid (3x2), pair vertically (1-4, 2-5, 3-6)
                        const slots = parentGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(slots).indexOf(currentTargetSlot);
                        // If in top row (0,1,2), pair with bottom row (3,4,5)
                        // If in bottom row (3,4,5), pair with top row (0,1,2)
                        const pairedIndex = currentIndex < 3 ? currentIndex + 3 : currentIndex - 3;
                        pairedSlot = slots[pairedIndex];
                    }}

                    if (pairedSlot) {{
                        const pairedTextarea = pairedSlot.querySelector('.slot-content textarea');
                        if (pairedTextarea) {{
                            pairedTextarea.value = itemText;
                            pairedTextarea.readOnly = true;
                            pairedTextarea.classList.remove('needs-selection');
                        }}
                        // Reset paired slot markers
                        const pairedMarkers = pairedSlot.querySelectorAll('.usage-marker');
                        pairedMarkers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                        pairedSlot.classList.remove('depleted');
                        pairedSlot.classList.add('two-slot-secondary');
                        if (isLightArmour) {{
                            pairedSlot.classList.add('light-armour-slot');
                        }}
                        updateSlotEmptyState(pairedSlot);

                        // Set up mirroring from primary to secondary
                        textarea.dataset.pairedSlotId = pairedSlot.dataset.slotId || Array.from(pairedSlot.parentElement.querySelectorAll('.inventory-slot')).indexOf(pairedSlot);
                        textarea.dataset.pairedGridType = pairedSlot.parentElement.classList.contains('paw-grid') ? 'paw' : (pairedSlot.parentElement.classList.contains('body-grid') ? 'body' : 'pack');
                        textarea.oninput = function() {{
                            pairedTextarea.value = this.value;
                        }};
                    }}
                }}
            }}
            closeItemSelector();
        }}

        function clearSlot(button) {{
            const slot = button.closest('.inventory-slot');
            const textarea = slot.querySelector('.slot-content textarea');
            if (textarea) {{
                textarea.value = '';
                textarea.classList.remove('needs-selection');
            }}
            // Update slot empty state
            updateSlotEmptyState(slot);
            // Reset usage markers
            const markers = slot.querySelectorAll('.usage-marker');
            markers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
            slot.classList.remove('depleted');

            // Remove condition styling
            slot.classList.remove('condition-slot');
            const conditionClear = slot.querySelector('.condition-clear');
            if (conditionClear) conditionClear.remove();

            // Check if this is part of a two-slot item and clear the paired slot
            const parentGrid = slot.parentElement;
            const isTwoSlot = slot.classList.contains('two-slot-item') || slot.classList.contains('two-slot-secondary');
            const isLightArmour = slot.classList.contains('light-armour-slot');

            if (isTwoSlot) {{
                let pairedSlot = null;

                if (isLightArmour) {{
                    // Light armour: find paired slot across paw/body grids by row position
                    const pawGrid = document.querySelector('.paw-grid');
                    const bodyGrid = document.querySelector('.body-grid');

                    if (parentGrid.classList.contains('paw-grid')) {{
                        // Get same-row body slot
                        const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(pawSlots).indexOf(slot);
                        const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                        pairedSlot = bodySlots[currentIndex];
                    }} else if (parentGrid.classList.contains('body-grid')) {{
                        // Get same-row paw slot
                        const bodySlots = bodyGrid.querySelectorAll('.inventory-slot');
                        const currentIndex = Array.from(bodySlots).indexOf(slot);
                        const pawSlots = pawGrid.querySelectorAll('.inventory-slot');
                        pairedSlot = pawSlots[currentIndex];
                    }}
                }} else if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
                    const slots = parentGrid.querySelectorAll('.inventory-slot');
                    const currentIndex = Array.from(slots).indexOf(slot);
                    pairedSlot = slots[currentIndex === 0 ? 1 : 0];
                }} else if (parentGrid.classList.contains('pack-grid')) {{
                    const slots = parentGrid.querySelectorAll('.inventory-slot');
                    const currentIndex = Array.from(slots).indexOf(slot);
                    const pairedIndex = currentIndex < 3 ? currentIndex + 3 : currentIndex - 3;
                    pairedSlot = slots[pairedIndex];
                }}

                if (pairedSlot) {{
                    const pairedTextarea = pairedSlot.querySelector('.slot-content textarea');
                    if (pairedTextarea) {{
                        pairedTextarea.value = '';
                        pairedTextarea.readOnly = false;
                    }}
                    const pairedMarkers = pairedSlot.querySelectorAll('.usage-marker');
                    pairedMarkers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                    pairedSlot.classList.remove('depleted');
                    pairedSlot.classList.remove('two-slot-item');
                    pairedSlot.classList.remove('two-slot-secondary');
                    pairedSlot.classList.remove('light-armour-slot');
                    updateSlotEmptyState(pairedSlot);
                }}
            }}

            slot.classList.remove('light-armour-slot');

            // Remove mirroring and readonly
            if (textarea) {{
                textarea.oninput = null;
                textarea.readOnly = false;
                delete textarea.dataset.pairedSlotIndex;
            }}

            slot.classList.remove('two-slot-item');
            slot.classList.remove('two-slot-secondary');
        }}

        // Grit alert modal functions
        function showGritAlert(message) {{
            document.getElementById('gritAlertBody').textContent = message;
            document.getElementById('gritAlertModal').classList.add('active');
        }}

        function closeGritAlert() {{
            document.getElementById('gritAlertModal').classList.remove('active');
        }}

        // Ignored conditions functionality
        let ignoredConditionMode = false;

        function addIgnoredCondition(button) {{
            // Check if available grit is > 0
            const gritInput = document.querySelector('.grit-input');
            const availableGrit = parseInt(gritInput.value) || 0;

            if (availableGrit <= 0) {{
                showGritAlert('No Grit remaining to ignore conditions.');
                return;
            }}

            // Set mode to ignored conditions
            ignoredConditionMode = true;

            // Build conditions-only list
            buildConditionsOnlyList();

            // Show the modal
            document.getElementById('itemSelectorModal').classList.add('active');
            document.getElementById('itemSearchInput').value = '';
            document.getElementById('itemSearchInput').focus();
        }}

        function buildConditionsOnlyList() {{
            const body = document.getElementById('itemSelectorBody');
            body.innerHTML = '';

            const conditions = INVENTORY_ITEMS['Conditions'];
            if (!conditions) return;

            const categoryDiv = document.createElement('div');
            categoryDiv.className = 'item-category conditions-category';

            const header = document.createElement('div');
            header.className = 'item-category-header';
            header.textContent = 'Conditions';
            header.onclick = function() {{
                const itemsDiv = this.nextElementSibling;
                itemsDiv.classList.toggle('expanded');
            }};

            const itemsDiv = document.createElement('div');
            itemsDiv.className = 'item-category-items expanded'; // Auto-expanded

            conditions.forEach(item => {{
                const itemOption = document.createElement('div');
                itemOption.className = 'item-option';

                const itemName = document.createElement('span');
                itemName.className = 'item-name';
                itemName.textContent = item.name;

                const itemDetails = document.createElement('span');
                itemDetails.className = 'item-details';
                itemDetails.textContent = item.notes || '';

                itemOption.appendChild(itemName);
                itemOption.appendChild(itemDetails);
                itemOption.onclick = function() {{
                    selectIgnoredCondition(item.name);
                }};
                itemsDiv.appendChild(itemOption);
            }});

            categoryDiv.appendChild(header);
            categoryDiv.appendChild(itemsDiv);
            body.appendChild(categoryDiv);
        }}

        function selectIgnoredCondition(conditionName) {{
            // Get grit input
            const gritInput = document.querySelector('.grit-input');
            const availableGrit = parseInt(gritInput.value) || 0;

            if (availableGrit <= 0) {{
                showGritAlert('No Grit remaining to ignore conditions.');
                closeItemSelector();
                return;
            }}

            // Reduce available grit by 1
            gritInput.value = availableGrit - 1;

            // Get the conditions list
            const conditionsList = document.querySelector('.ignored-conditions-list');

            // Create the condition row
            const row = document.createElement('div');
            row.className = 'ignored-condition-row';
            row.dataset.condition = conditionName;

            const removeBtn = document.createElement('button');
            removeBtn.className = 'slot-btn clear-btn';
            removeBtn.textContent = '-';
            removeBtn.onclick = function() {{
                removeIgnoredCondition(this);
            }};

            const content = document.createElement('div');
            content.className = 'ignored-condition-content';

            const nameSpan = document.createElement('span');
            nameSpan.className = 'ignored-condition-name';
            nameSpan.textContent = conditionName;

            const clearSpan = document.createElement('span');
            clearSpan.className = 'ignored-condition-clear';
            clearSpan.textContent = CONDITION_CLEAR[conditionName] || '';

            content.appendChild(nameSpan);
            content.appendChild(clearSpan);

            row.appendChild(removeBtn);
            row.appendChild(content);

            conditionsList.appendChild(row);

            // Close the modal
            closeItemSelector();
            ignoredConditionMode = false;
        }}

        function removeIgnoredCondition(button) {{
            const row = button.closest('.ignored-condition-row');

            // Restore grit
            const gritInput = document.querySelector('.grit-input');
            const availableGrit = parseInt(gritInput.value) || 0;
            const maxGrit = parseInt(gritInput.dataset.maxGrit) || 0;

            // Don't exceed max grit
            if (availableGrit < maxGrit) {{
                gritInput.value = availableGrit + 1;
            }}

            // Remove the row
            row.remove();
        }}

        // Override closeItemSelector to reset mode
        const originalCloseItemSelector = closeItemSelector;
        function closeItemSelectorWithReset() {{
            document.getElementById('itemSelectorModal').classList.remove('active');
            currentTargetSlot = null;
            currentHirelingSlot = null;
            ignoredConditionMode = false;
        }}

        // ==================== HIRELING FUNCTIONS ====================

        function generateHirelingStats() {{
            // Per SRD 2.3: d6 hp, STR 2d6, DEX 2d6, WIL 2d6
            return {{
                hp: Math.floor(Math.random() * 6) + 1,
                str: rollDiceSum(2, 6),
                dex: rollDiceSum(2, 6),
                wil: rollDiceSum(2, 6),
                look: randomChoice(HIRELING_LOOKS),
                disposition: randomChoice(HIRELING_DISPOSITIONS)
            }};
        }}

        function createHirelingSlotHTML(hirelingId, slotNum, label, slotType) {{
            return `
                <div class="hireling-inventory-slot hireling-${{slotType}}-slot" data-hireling-id="${{hirelingId}}" data-slot="${{slotNum}}" data-slot-type="${{slotType}}">
                    <div class="hireling-slot-header">
                        <span class="hireling-slot-label">${{label}}</span>
                        <span class="hireling-slot-actions">
                            <button class="slot-btn add-btn" onclick="openHirelingItemSelector(this)">+</button>
                            <button class="slot-btn clear-btn" onclick="clearHirelingSlot(this)">-</button>
                        </span>
                    </div>
                    <div class="hireling-slot-content">
                        <textarea placeholder=""></textarea>
                    </div>
                    <div class="hireling-usage-markers">
                        <span class="usage-marker" onclick="toggleHirelingUsage(this)"></span>
                        <span class="usage-marker" onclick="toggleHirelingUsage(this)"></span>
                        <span class="usage-marker" onclick="toggleHirelingUsage(this)"></span>
                    </div>
                </div>
            `;
        }}

        function createHirelingCardHTML(hirelingId, stats, displayNumber, hirelingType) {{
            const titleText = hirelingType || 'Hireling';
            return `
                <div class="hireling-card" id="hireling-${{hirelingId}}" data-hireling-id="${{hirelingId}}" data-hireling-type="${{titleText}}">
                    <div class="hireling-card-header">
                        <span class="hireling-title"><span class="hireling-title-text">${{titleText}}</span> <span class="hireling-number">#${{displayNumber}}</span></span>
                        <button class="hireling-remove-btn" onclick="removeHireling(${{hirelingId}})">-</button>
                    </div>
                    <div class="hireling-info-row">
                        <div class="hireling-field">
                            <span class="hireling-field-label">Look</span>
                            <input type="text" value="${{stats.look}}" />
                        </div>
                        <div class="hireling-field">
                            <span class="hireling-field-label">Disposition</span>
                            <input type="text" value="${{stats.disposition}}" />
                        </div>
                    </div>
                    <div class="hireling-body">
                        <div class="hireling-stats">
                            <div class="hireling-stats-header">
                                <span></span>
                                <span>Max</span>
                                <span>Current</span>
                            </div>
                            <div class="hireling-stats-table">
                                <div class="hireling-stat-row">
                                    <span class="hireling-stat-label">STR</span>
                                    <input type="number" value="${{stats.str}}" min="1" max="12" />
                                    <input type="number" value="${{stats.str}}" min="0" max="12" />
                                </div>
                                <div class="hireling-stat-row">
                                    <span class="hireling-stat-label">DEX</span>
                                    <input type="number" value="${{stats.dex}}" min="1" max="12" />
                                    <input type="number" value="${{stats.dex}}" min="0" max="12" />
                                </div>
                                <div class="hireling-stat-row">
                                    <span class="hireling-stat-label">WIL</span>
                                    <input type="number" value="${{stats.wil}}" min="1" max="12" />
                                    <input type="number" value="${{stats.wil}}" min="0" max="12" />
                                </div>
                                <div class="hireling-stat-row">
                                    <span class="hireling-stat-label">HP</span>
                                    <input type="number" value="${{stats.hp}}" min="1" max="20" />
                                    <input type="number" value="${{stats.hp}}" min="0" max="20" />
                                </div>
                            </div>
                        </div>
                        <div class="hireling-inventory">
                            <div class="hireling-paw-column">
                                <div class="hireling-paw-grid">
                                    ${{createHirelingSlotHTML(hirelingId, 1, 'Main paw', 'paw')}}
                                    ${{createHirelingSlotHTML(hirelingId, 2, 'Off paw', 'paw')}}
                                </div>
                            </div>
                            <div class="hireling-pack-column">
                                <div class="hireling-pack-grid">
                                    ${{createHirelingSlotHTML(hirelingId, 3, '1', 'pack')}}
                                    ${{createHirelingSlotHTML(hirelingId, 4, '2', 'pack')}}
                                    ${{createHirelingSlotHTML(hirelingId, 5, '3', 'pack')}}
                                    ${{createHirelingSlotHTML(hirelingId, 6, '4', 'pack')}}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }}

        // Internal function to add hireling with type
        function addHirelingWithType(hirelingType) {{
            hirelingCounter++;
            const stats = generateHirelingStats();
            // Display number is count of hirelings of this type + 1
            const displayNumber = getHirelingTypeCount(hirelingType) + 1;
            const cardHTML = createHirelingCardHTML(hirelingCounter, stats, displayNumber, hirelingType);

            const container = document.getElementById('hirelingsContainer');
            container.insertAdjacentHTML('beforeend', cardHTML);

            // Add event listeners for the new hireling's stat inputs
            const hirelingCard = document.getElementById('hireling-' + hirelingCounter);
            setupHirelingStatListeners(hirelingCard);
        }}

        // Public function - opens the hireling type selector
        function addHireling() {{
            openHirelingTypeSelector();
        }}

        function getHirelingTypeCount(hirelingType) {{
            return document.querySelectorAll(`.hireling-card[data-hireling-type="${{hirelingType}}"]`).length;
        }}

        function openHirelingTypeSelector() {{
            buildHirelingTypeList();
            document.getElementById('hirelingTypeModal').classList.add('active');
        }}

        function closeHirelingTypeSelector() {{
            document.getElementById('hirelingTypeModal').classList.remove('active');
        }}

        function buildHirelingTypeList() {{
            const body = document.getElementById('hirelingTypeBody');
            body.innerHTML = '';

            HIRELING_TYPES.forEach(hireling => {{
                const option = document.createElement('div');
                option.className = 'hireling-type-option';
                option.onclick = function() {{
                    selectHirelingType(hireling.type);
                }};

                const nameSpan = document.createElement('span');
                nameSpan.className = 'hireling-type-name';
                nameSpan.textContent = hireling.type;

                const wagesSpan = document.createElement('span');
                wagesSpan.className = 'hireling-type-wages';
                wagesSpan.textContent = hireling.wages;

                option.appendChild(nameSpan);
                option.appendChild(wagesSpan);
                body.appendChild(option);
            }});
        }}

        function selectHirelingType(hirelingType) {{
            closeHirelingTypeSelector();
            addHirelingWithType(hirelingType);
        }}

        // Background to hireling mapping
        const BACKGROUND_HIRELINGS = {{
            'Beetleherd': 'Loyal beetle',
            'Ale brewer': 'Drunken torchbearer',
            'Merchant': 'Pack rat'
        }};

        function clearAllHirelings() {{
            const container = document.getElementById('hirelingsContainer');
            container.innerHTML = '';
            hirelingCounter = 0;
        }}

        function removeHireling(hirelingId) {{
            const card = document.getElementById('hireling-' + hirelingId);
            if (card) {{
                const hirelingType = card.dataset.hirelingType;
                card.remove();
                renumberHirelingsByType(hirelingType);
            }}
        }}

        function renumberHirelingsByType(hirelingType) {{
            // Get all remaining hireling cards of this type and update their display numbers
            const hirelingCards = document.querySelectorAll(`.hireling-card[data-hireling-type="${{hirelingType}}"]`);
            hirelingCards.forEach((card, index) => {{
                const numberSpan = card.querySelector('.hireling-number');
                if (numberSpan) {{
                    numberSpan.textContent = '#' + (index + 1);
                }}
            }});
        }}

        function setupHirelingStatListeners(hirelingCard) {{
            // Set up max/current enforcement for hireling stats
            const statRows = hirelingCard.querySelectorAll('.hireling-stat-row');
            statRows.forEach(row => {{
                const inputs = row.querySelectorAll('input[type="number"]');
                if (inputs.length >= 2) {{
                    const maxInput = inputs[0];
                    const currentInput = inputs[1];

                    maxInput.addEventListener('change', function() {{
                        currentInput.max = this.value;
                        if (parseInt(currentInput.value) > parseInt(this.value)) {{
                            currentInput.value = this.value;
                        }}
                    }});

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
        }}

        function openHirelingItemSelector(button) {{
            currentHirelingSlot = button.closest('.hireling-inventory-slot');

            // Clear search and build item list
            const searchInput = document.getElementById('itemSearchInput');
            searchInput.value = '';
            buildItemList('');

            // Show modal
            document.getElementById('itemSelectorModal').classList.add('active');
            searchInput.focus();
        }}

        function getHirelingPairedSlotNum(slotNum) {{
            // Paw slots 1-2 pair together
            // Pack slots pair vertically in 2x2 grid: 3-5, 4-6
            if (slotNum <= 2) {{
                return slotNum === 1 ? 2 : 1;
            }} else {{
                // Pack grid: top row (3,4) pairs with bottom row (5,6)
                return slotNum <= 4 ? slotNum + 2 : slotNum - 2;
            }}
        }}

        function clearHirelingSlot(button) {{
            const slot = button.closest('.hireling-inventory-slot');
            const textarea = slot.querySelector('.hireling-slot-content textarea');
            if (textarea) {{
                textarea.value = '';
            }}

            // Reset usage markers
            const markers = slot.querySelectorAll('.usage-marker');
            markers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
            slot.classList.remove('depleted');

            // Remove condition styling
            slot.classList.remove('condition-slot');
            const conditionClear = slot.querySelector('.condition-clear');
            if (conditionClear) conditionClear.remove();

            // Handle two-slot items
            const isTwoSlot = slot.classList.contains('two-slot-item') || slot.classList.contains('two-slot-secondary');
            if (isTwoSlot) {{
                const hirelingCard = slot.closest('.hireling-card');
                const slotNum = parseInt(slot.dataset.slot);
                const pairedSlotNum = getHirelingPairedSlotNum(slotNum);

                const pairedSlot = hirelingCard.querySelector(`.hireling-inventory-slot[data-slot="${{pairedSlotNum}}"]`);
                if (pairedSlot) {{
                    const pairedTextarea = pairedSlot.querySelector('.hireling-slot-content textarea');
                    if (pairedTextarea) {{
                        pairedTextarea.value = '';
                        pairedTextarea.readOnly = false;
                    }}
                    const pairedMarkers = pairedSlot.querySelectorAll('.usage-marker');
                    pairedMarkers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                    pairedSlot.classList.remove('depleted');
                    pairedSlot.classList.remove('two-slot-item');
                    pairedSlot.classList.remove('two-slot-secondary');
                }}
            }}

            // Clean up
            if (textarea) {{
                textarea.oninput = null;
                textarea.readOnly = false;
            }}
            slot.classList.remove('two-slot-item');
            slot.classList.remove('two-slot-secondary');
        }}

        function selectHirelingItem(itemName, slots) {{
            if (!currentHirelingSlot) return;

            // Format item text
            let itemText = itemName;
            if (itemName.includes('(') && itemName.includes(')')) {{
                const idx = itemName.indexOf('(');
                const name = itemName.substring(0, idx).trim();
                const details = itemName.substring(idx);
                itemText = name + '\\n' + details;
            }}

            const textarea = currentHirelingSlot.querySelector('.hireling-slot-content textarea');
            if (textarea) {{
                textarea.value = itemText;
            }}

            // Reset classes
            const markers = currentHirelingSlot.querySelectorAll('.usage-marker');
            markers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
            currentHirelingSlot.classList.remove('depleted');
            currentHirelingSlot.classList.remove('two-slot-item');
            currentHirelingSlot.classList.remove('two-slot-secondary');
            currentHirelingSlot.classList.remove('condition-slot');

            // Remove any existing condition clear text
            const existingClear = currentHirelingSlot.querySelector('.condition-clear');
            if (existingClear) existingClear.remove();

            // Check if this is a condition
            if (CONDITION_CLEAR[itemName]) {{
                currentHirelingSlot.classList.add('condition-slot');
                const clearDiv = document.createElement('div');
                clearDiv.className = 'condition-clear';
                clearDiv.textContent = CONDITION_CLEAR[itemName];
                currentHirelingSlot.querySelector('.hireling-slot-content').appendChild(clearDiv);
            }}

            // Handle 2-slot items
            if (slots === 2) {{
                currentHirelingSlot.classList.add('two-slot-item');

                const hirelingCard = currentHirelingSlot.closest('.hireling-card');
                const slotNum = parseInt(currentHirelingSlot.dataset.slot);
                const pairedSlotNum = getHirelingPairedSlotNum(slotNum);

                const pairedSlot = hirelingCard.querySelector(`.hireling-inventory-slot[data-slot="${{pairedSlotNum}}"]`);
                if (pairedSlot) {{
                    const pairedTextarea = pairedSlot.querySelector('.hireling-slot-content textarea');
                    if (pairedTextarea) {{
                        pairedTextarea.value = itemText;
                        pairedTextarea.readOnly = true;
                    }}
                    const pairedMarkers = pairedSlot.querySelectorAll('.usage-marker');
                    pairedMarkers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                    pairedSlot.classList.remove('depleted');
                    pairedSlot.classList.add('two-slot-secondary');

                    // Set up mirroring
                    textarea.oninput = function() {{
                        pairedTextarea.value = this.value;
                    }};
                }}
            }}

            closeItemSelector();
            currentHirelingSlot = null;
        }}

        function toggleHirelingUsage(marker) {{
            const slot = marker.closest('.hireling-inventory-slot');
            const textarea = slot.querySelector('.hireling-slot-content textarea');

            if (!textarea || !textarea.value.trim()) {{
                return;
            }}

            const markers = Array.from(slot.querySelectorAll('.usage-marker'));
            const isSixUseItem = textarea.value.toLowerCase().includes('torch') ||
                                 textarea.value.toLowerCase().includes('lantern');

            const clickedIsUsed = marker.classList.contains('used') || marker.classList.contains('half-used');

            if (isSixUseItem) {{
                if (marker.classList.contains('used')) {{
                    marker.classList.remove('used');
                }} else if (marker.classList.contains('half-used')) {{
                    marker.classList.remove('half-used');
                    marker.classList.add('used');
                }} else {{
                    marker.classList.add('half-used');
                }}
                const allFullyUsed = markers.every(m => m.classList.contains('used'));
                if (allFullyUsed) {{
                    slot.classList.add('depleted');
                }} else {{
                    slot.classList.remove('depleted');
                }}
            }} else {{
                if (clickedIsUsed) {{
                    for (let i = markers.length - 1; i >= 0; i--) {{
                        if (markers[i].classList.contains('used')) {{
                            markers[i].classList.remove('used');
                            break;
                        }}
                    }}
                }} else {{
                    for (let i = 0; i < markers.length; i++) {{
                        if (!markers[i].classList.contains('used')) {{
                            markers[i].classList.add('used');
                            break;
                        }}
                    }}
                }}

                const allUsed = markers.every(m => m.classList.contains('used'));

                // Handle paired slots for two-slot items
                let pairedSlot = null;
                if (slot.classList.contains('two-slot-item')) {{
                    const hirelingCard = slot.closest('.hireling-card');
                    const slotNum = parseInt(slot.dataset.slot);
                    const pairedSlotNum = getHirelingPairedSlotNum(slotNum);
                    pairedSlot = hirelingCard.querySelector(`.hireling-inventory-slot[data-slot="${{pairedSlotNum}}"]`);
                }}

                if (allUsed) {{
                    slot.classList.add('depleted');
                    if (pairedSlot) pairedSlot.classList.add('depleted');
                }} else {{
                    slot.classList.remove('depleted');
                    if (pairedSlot) pairedSlot.classList.remove('depleted');
                }}
            }}
        }}

        // Make functions globally accessible
        window.generateNewCharacter = generateNewCharacter;
        window.closeConfirmGenerate = closeConfirmGenerate;
        window.confirmGenerate = confirmGenerate;
        window.regenerateCharacter = regenerateCharacter;
        window.acceptCharacter = acceptCharacter;
        window.toggleDiceRoller = toggleDiceRoller;
        window.toggleInventory = toggleInventory;
        window.toggleSection = toggleSection;
        window.rollDice = rollDice;
        window.rollSave = rollSave;
        window.manualRollDice = manualRollDice;
        window.rollWithAdvantage = rollWithAdvantage;
        window.rollWithDisadvantage = rollWithDisadvantage;
        window.toggleUsage = toggleUsage;
        window.resetUsageMarkers = resetUsageMarkers;
        window.openItemSelector = openItemSelector;
        window.closeItemSelector = closeItemSelectorWithReset;
        window.selectItem = selectItem;
        window.clearSlot = clearSlot;
        window.addIgnoredCondition = addIgnoredCondition;
        window.removeIgnoredCondition = removeIgnoredCondition;
        window.showGritAlert = showGritAlert;
        window.closeGritAlert = closeGritAlert;
        window.addHireling = addHireling;
        window.removeHireling = removeHireling;
        window.closeHirelingTypeSelector = closeHirelingTypeSelector;
        window.openHirelingItemSelector = openHirelingItemSelector;
        window.clearHirelingSlot = clearHirelingSlot;
        window.toggleHirelingUsage = toggleHirelingUsage;

        document.addEventListener('DOMContentLoaded', function() {{
            console.log('Character sheet loaded');

            const diceInput = document.getElementById('diceInput');
            if (diceInput) {{
                diceInput.addEventListener('keypress', function(e) {{
                    if (e.key === 'Enter') {{
                        manualRollDice();
                    }}
                }});
                // Clear save state when user starts typing in dice input
                diceInput.addEventListener('input', function() {{
                    clearSaveState();
                }});
            }} else {{
                console.error('Could not find diceInput');
            }}

            // Dice roller uses inline onclick="toggleDiceRoller()"

            // Initialize slot empty states and add listeners for manual edits
            updateAllSlotEmptyStates();
            document.querySelectorAll('.inventory-slot .slot-content textarea').forEach(textarea => {{
                textarea.addEventListener('input', function() {{
                    const slot = this.closest('.inventory-slot');
                    updateSlotEmptyState(slot);
                }});
            }});

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

            // Enforce pips limits (max 250)
            const pipsInput = document.querySelector('.pips-input');
            const MAX_PIPS = 250;
            if (pipsInput) {{
                pipsInput.addEventListener('change', function() {{
                    if (parseInt(this.value) > MAX_PIPS) {{
                        this.value = MAX_PIPS;
                    }}
                    if (parseInt(this.value) < 0) {{
                        this.value = 0;
                    }}
                }});
            }}

            // Enforce grit limits and track max
            const gritInput = document.querySelector('.grit-input');
            if (gritInput) {{
                gritInput.addEventListener('change', function() {{
                    let val = parseInt(this.value) || 0;
                    if (val < 0) val = 0;
                    if (val > 6) val = 6;
                    this.value = val;
                    // Update max grit when user manually changes the value
                    // (only if increasing or no ignored conditions)
                    const ignoredCount = document.querySelectorAll('.ignored-condition-row').length;
                    const currentMax = parseInt(this.dataset.maxGrit) || 0;
                    // If the new value + ignored conditions > current max, update max
                    if (val + ignoredCount > currentMax) {{
                        this.dataset.maxGrit = val + ignoredCount;
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
