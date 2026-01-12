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

            // Check if any items are armor for body slots
            const packItems = [];
            const armorKeywords = ['armour', 'armor', 'jerkin'];
            let bodySlotIdx = 0;

            // Process background items (itemA and itemB at indices 3 and 4)
            [charData.equipment[3], charData.equipment[4]].forEach(item => {{
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
            const gritInput = document.querySelector('.grit-box input[type="number"]');
            if (levelInput) levelInput.value = 1;
            if (xpInput) xpInput.value = 0;
            if (gritInput) gritInput.value = 0;

            // Clear text areas
            document.querySelectorAll('.portrait-input, .conditions-box textarea, .banked-box textarea').forEach(ta => ta.value = '');

            // Reset usage markers
            resetUsageMarkers();

            // Update slot empty states
            updateAllSlotEmptyStates();
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
                    if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
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
            }});
        }}

        // Item selector state
        let currentTargetSlot = null;

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

                // Handle 2-slot items
                if (slots === 2) {{
                    currentTargetSlot.classList.add('two-slot-item');

                    // Find the paired slot
                    let pairedSlot = null;
                    const parentGrid = currentTargetSlot.parentElement;

                    if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
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
                        }}
                        // Reset paired slot markers
                        const pairedMarkers = pairedSlot.querySelectorAll('.usage-marker');
                        pairedMarkers.forEach(m => {{ m.classList.remove('used'); m.classList.remove('half-used'); }});
                        pairedSlot.classList.remove('depleted');
                        pairedSlot.classList.add('two-slot-secondary');

                        // Set up mirroring from primary to secondary
                        textarea.dataset.pairedSlotIndex = Array.from(parentGrid.querySelectorAll('.inventory-slot')).indexOf(pairedSlot);
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

            // Check if this is part of a two-slot item and clear the paired slot
            const parentGrid = slot.parentElement;
            const isTwoSlot = slot.classList.contains('two-slot-item') || slot.classList.contains('two-slot-secondary');

            if (isTwoSlot) {{
                let pairedSlot = null;
                if (parentGrid.classList.contains('paw-grid') || parentGrid.classList.contains('body-grid')) {{
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
                }}
            }}

            // Remove mirroring and readonly
            if (textarea) {{
                textarea.oninput = null;
                textarea.readOnly = false;
                delete textarea.dataset.pairedSlotIndex;
            }}

            slot.classList.remove('two-slot-item');
            slot.classList.remove('two-slot-secondary');
        }}

        // Make functions globally accessible
        window.generateNewCharacter = generateNewCharacter;
        window.closeConfirmGenerate = closeConfirmGenerate;
        window.confirmGenerate = confirmGenerate;
        window.regenerateCharacter = regenerateCharacter;
        window.acceptCharacter = acceptCharacter;
        window.toggleDiceRoller = toggleDiceRoller;
        window.rollDice = rollDice;
        window.toggleUsage = toggleUsage;
        window.resetUsageMarkers = resetUsageMarkers;
        window.openItemSelector = openItemSelector;
        window.closeItemSelector = closeItemSelector;
        window.selectItem = selectItem;
        window.clearSlot = clearSlot;

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
