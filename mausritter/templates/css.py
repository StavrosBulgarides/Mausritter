"""CSS styles for the Mausritter character sheet."""

STYLES = """
@import url('https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&display=swap');

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: #e8e8e8;
    color: #4a4a5a;
    padding: 20px;
    line-height: 1.4;
}

.character-sheet {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Generate Button */
.generate-section {
    margin-bottom: 20px;
}

.generate-btn {
    padding: 12px 24px;
    background: #4a4a5a;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background 0.2s, transform 0.1s;
}

.generate-btn:hover {
    background: #3a3a4a;
}

.generate-btn:active {
    transform: scale(0.98);
}

/* Blackletter font class */
.blackletter {
    font-family: 'UnifrakturMaguntia', 'Times New Roman', serif;
}

/* Header Section */
.header-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

.name-background-box {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    padding: 15px 20px;
    min-width: 0;
    overflow: hidden;
}

.name-row {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 12px;
    padding-bottom: 12px;
    border-bottom: 1px solid #e0e0e0;
}

.name-label {
    font-weight: bold;
    font-size: 1.3em;
    color: #4a4a5a;
    min-width: 120px;
}

.name-input {
    flex: 1;
    border: none;
    background: transparent;
    font-size: 1.1em;
    color: #6a6a7a;
    padding: 5px;
}

.name-input:focus {
    outline: none;
    background: #f8f8f8;
    border-radius: 4px;
}

.background-row {
    display: flex;
    align-items: center;
    gap: 15px;
    padding-bottom: 12px;
    border-bottom: 1px solid #e0e0e0;
}

.background-label {
    font-weight: bold;
    font-size: 1.2em;
    color: #4a4a5a;
    min-width: 120px;
}

.background-input {
    flex: 1;
    border: none;
    background: transparent;
    font-size: 1em;
    color: #6a6a7a;
    padding: 5px;
}

.background-input:focus {
    outline: none;
    background: #f8f8f8;
    border-radius: 4px;
}

.appearance-box {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 15px 20px;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    min-width: 0;
    overflow: hidden;
}

.appearance-row {
    display: grid;
    grid-template-columns: 100px 1fr;
    align-items: center;
    gap: 10px;
}

.appearance-row .appearance-label {
    font-weight: bold;
    color: #4a4a5a;
    font-size: 1.3em;
}

.appearance-row input {
    border: none;
    border-bottom: 1px solid #d0d0d0;
    background: transparent;
    padding: 5px;
    font-size: 0.95em;
    color: #6a6a7a;
}

.appearance-row input:focus {
    outline: none;
    border-bottom-color: #4a4a5a;
}

/* Middle Section - Portrait and Stats */
.middle-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 20px;
}

.stats-section,
.other-section {
    margin-bottom: 20px;
}

.portrait-column {
    display: flex;
    flex-direction: column;
    min-width: 0;
}

.portrait-box {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    padding: 15px 20px;
    background: linear-gradient(135deg, #f5f5f5 0%, #e8e8e8 100%);
    flex: 1;
    min-width: 0;
    min-height: 150px;
    display: flex;
    flex-direction: column;
}

.portrait-input {
    flex: 1;
    border: none;
    background: transparent;
    resize: none;
    font-family: inherit;
    font-size: 0.95em;
    color: #6a6a7a;
    padding: 0;
    text-align: left;
}

.portrait-input:focus {
    outline: none;
}

.stats-box {
    display: flex;
    flex-direction: column;
    gap: 15px;
    min-width: 0;
}

/* Attributes Section */
.attributes-section {
    display: flex;
    flex-direction: column;
}

.attributes-header {
    display: grid;
    grid-template-columns: 70px 1fr 1fr;
    padding: 5px 2px;
    font-size: 0.85em;
    color: #6a6a7a;
    font-style: italic;
}

.attributes-header span {
    text-align: center;
}

.attributes-header span:first-child {
    text-align: left;
}

.attributes-table {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.attribute-row {
    display: grid;
    grid-template-columns: 70px 1fr 1fr;
    border-bottom: 1px solid #d0d0d0;
}

.attribute-row:last-child {
    border-bottom: none;
}

.attribute-label {
    font-weight: bold;
    font-size: 1.3em;
    background: #f0f0f0;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #d0d0d0;
    color: #4a4a5a;
}

.attribute-row input {
    border: none;
    background: white;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    border-right: 1px solid #d0d0d0;
    width: 100%;
    min-width: 0;
}

.attribute-row input:last-child {
    border-right: none;
}

.attribute-row input:focus {
    outline: none;
    background: #f8f8f8;
}

/* HP Section */
.hp-section {
    display: flex;
    flex-direction: column;
}

.hp-table {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.hp-row {
    display: grid;
    grid-template-columns: 70px 1fr 1fr;
}

.hp-label {
    font-weight: bold;
    font-size: 1.3em;
    background: #f0f0f0;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #d0d0d0;
    color: #4a4a5a;
}

.hp-row input {
    border: none;
    background: white;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    border-right: 1px solid #d0d0d0;
    width: 100%;
    min-width: 0;
}

.hp-row input:last-child {
    border-right: none;
}

.hp-row input:focus {
    outline: none;
    background: #f8f8f8;
}

.hp-footer {
    display: grid;
    grid-template-columns: 70px 1fr 1fr;
    padding: 5px 2px;
    font-size: 0.85em;
    color: #6a6a7a;
    font-style: italic;
}

.hp-footer span {
    text-align: center;
}

.hp-footer span:first-child {
    text-align: left;
}

/* Pips Section */
.pips-section {
    display: flex;
    flex-direction: column;
}

.pips-table {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.pips-row {
    display: grid;
    grid-template-columns: 70px 1fr 1fr;
}

.pips-label {
    font-weight: bold;
    font-size: 1.3em;
    background: #f0f0f0;
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #d0d0d0;
    color: #4a4a5a;
}

.pips-row input {
    border: none;
    background: white;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    border-right: 1px solid #d0d0d0;
    width: 100%;
    min-width: 0;
}

.pips-row input:last-child {
    border-right: none;
}

.pips-row input:focus {
    outline: none;
    background: #f8f8f8;
}

.pips-row input[readonly] {
    background: #f0f0f0;
    color: #6a6a7a;
    cursor: not-allowed;
}

/* Inventory Section */
.inventory-section {
    margin-bottom: 20px;
}

/* Generic collapsible section styles */
.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    padding: 10px 15px;
    background: #f8f8f8;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
    margin-bottom: 10px;
    user-select: none;
}

.section-header:hover {
    background: #f0f0f0;
}

.section-title {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a4a5a;
}

.section-toggle {
    font-size: 1em;
    color: #6a6a7a;
}

.section-content {
    display: none;
}

.section-content.active {
    display: block;
}

/* Inventory section - uses generic section styles */
.inventory-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    padding: 10px 15px;
    background: #f8f8f8;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
    margin-bottom: 10px;
    user-select: none;
}

.inventory-header:hover {
    background: #f0f0f0;
}

.inventory-title {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a4a5a;
}

.inventory-toggle {
    font-size: 1em;
    color: #6a6a7a;
}

.inventory-content {
    display: none;
}

.inventory-content.active {
    display: block;
}

.inventory-container {
    display: flex;
    gap: 15px;
    margin-bottom: 10px;
}

.paw-column,
.body-column {
    display: flex;
    flex-direction: column;
    width: 170px;
}

.pack-column {
    display: flex;
    flex-direction: column;
    flex: 1;
}

.paw-grid {
    display: flex;
    flex-direction: column;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.paw-grid .paw-slot {
    border: none;
    border-radius: 0;
    flex: 1;
}

.paw-grid .paw-slot:first-child {
    border-bottom: 1px solid #d0d0d0;
}

.body-grid {
    display: flex;
    flex-direction: column;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.body-grid .body-slot {
    border: none;
    border-radius: 0;
    flex: 1;
}

.body-grid .body-slot:first-child {
    border-bottom: 1px solid #d0d0d0;
}

.pack-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.pack-grid .pack-slot {
    border: none;
    border-radius: 0;
    border-right: 1px solid #d0d0d0;
    border-bottom: 1px solid #d0d0d0;
}

.pack-grid .pack-slot:nth-child(3),
.pack-grid .pack-slot:nth-child(6) {
    border-right: none;
}

.pack-grid .pack-slot:nth-child(4),
.pack-grid .pack-slot:nth-child(5),
.pack-grid .pack-slot:nth-child(6) {
    border-bottom: none;
}

.inventory-legend-item {
    font-size: 0.85em;
    color: #6a6a7a;
    padding: 8px 0;
}

.inventory-legend-item strong {
    color: #4a4a5a;
}

.inventory-slot {
    border: 2px solid #d0d0d0;
    border-radius: 8px;
    padding: 10px;
    min-height: 155px;
    display: flex;
    flex-direction: column;
    background: white;
}

.slot-label {
    text-align: center;
    margin-bottom: 8px;
    color: #6a6a7a;
}

.paw-slot .slot-label,
.body-slot .slot-label,
.pack-slot .slot-label {
    font-weight: bold;
    font-size: 1.3em;
    color: #4a4a5a;
    margin-bottom: 0;
}

.slot-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}

.slot-actions {
    display: flex;
    gap: 4px;
}

.slot-btn {
    width: 20px;
    height: 20px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    background: #f8f8f8;
    cursor: pointer;
    font-size: 14px;
    font-weight: bold;
    color: #6a6a7a;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0;
    line-height: 1;
}

.slot-btn:hover {
    background: #e8e8e8;
    border-color: #4a4a5a;
}

.add-btn {
    color: #2a7a2a;
}

.clear-btn {
    color: #aa2a2a;
}

.usage-markers {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin-top: 8px;
}

.usage-marker {
    width: 18px;
    height: 18px;
    border: 2px solid #4a4a5a;
    border-radius: 50%;
    cursor: pointer;
    transition: background-color 0.2s;
}

.usage-marker:hover {
    background-color: #e0e0e0;
}

.slot-empty .usage-marker {
    opacity: 0.3;
    cursor: not-allowed;
}

.slot-empty .usage-marker:hover {
    background-color: transparent;
}

.usage-marker.used {
    background-color: #4a4a5a;
}

.usage-marker.half-used {
    background: linear-gradient(to right, #4a4a5a 50%, transparent 50%);
}

.pack-slot.depleted .slot-content textarea,
.paw-slot.depleted .slot-content textarea,
.body-slot.depleted .slot-content textarea {
    opacity: 0.7;
    text-decoration: line-through;
    background: #fce4e4;
    border-color: #e8a0a0;
}

/* "Select weapon" placeholder - red background */
.slot-content textarea.needs-selection {
    background: #fce4e4;
    color: #904040;
    font-style: italic;
    border-color: #e8a0a0;
}

.two-slot-secondary .usage-markers {
    display: none;
}

.two-slot-secondary .slot-header {
    opacity: 0.5;
}

.two-slot-secondary .slot-content textarea {
    background: #f0f0f0;
    cursor: not-allowed;
}

/* Condition slots - contrasting background to highlight they are bad */
.inventory-slot.condition-slot {
    background: #fce4e4;
}

.inventory-slot.condition-slot .slot-content textarea {
    background: #fef0f0;
    border-color: #e8a0a0;
}

.inventory-slot.condition-slot .slot-content textarea:focus {
    background: #fff8f8;
    border-color: #c07070;
}

.inventory-slot.condition-slot .slot-content {
    flex-direction: column;
}

.inventory-slot.condition-slot .slot-content textarea {
    flex: 1;
    min-height: 40px;
}

.inventory-slot.condition-slot .condition-clear {
    font-size: 0.75em;
    color: #905050;
    text-align: center;
    margin-top: 4px;
    font-style: italic;
    line-height: 1.2;
    flex-shrink: 0;
}

.slot-content {
    flex: 1;
    display: flex;
    align-items: stretch;
}

.slot-content textarea {
    width: 100%;
    padding: 6px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    text-align: center;
    font-size: 0.85em;
    background: #fafafa;
    resize: none;
    font-family: inherit;
}

.slot-content textarea:focus {
    outline: none;
    border-color: #4a4a5a;
    background: white;
}

.slot-content textarea.needs-selection {
    background: #f0f0f0;
    color: #6a6a7a;
    font-style: italic;
}


/* Bottom Section */
.bottom-section {
    display: grid;
    grid-template-columns: 1fr 2.5fr 2fr;
    gap: 15px;
    margin-bottom: 20px;
    align-items: stretch;
}

.level-xp-column {
    display: flex;
    flex-direction: column;
}

.level-xp-box {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
}

.level-row, .xp-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

.level-row {
    border-bottom: 1px solid #d0d0d0;
}

.xp-row {
    flex: 1;
    min-height: 60px;
}

.xp-row .stat-label,
.xp-row input {
    display: flex;
    align-items: center;
    justify-content: center;
}

.level-xp-box .stat-label {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a4a5a;
    padding: 10px;
    background: #f0f0f0;
    display: flex;
    align-items: center;
    border-right: 1px solid #d0d0d0;
}

.level-xp-box input {
    border: none;
    background: white;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    width: 100%;
    min-width: 0;
}

.level-xp-box input:focus {
    outline: none;
    background: #f8f8f8;
}

.level-note {
    font-size: 0.8em;
    color: #6a6a7a;
    margin-top: 8px;
}

.grit-conditions-column {
    display: flex;
    flex-direction: column;
}

.grit-conditions-box {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
    display: flex;
    flex-direction: column;
    min-width: 0;
}

.grit-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border-bottom: 1px solid #d0d0d0;
}

.grit-row .stat-label {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a4a5a;
    padding: 10px;
    background: #f0f0f0;
    display: flex;
    align-items: center;
    border-right: 1px solid #d0d0d0;
}

.grit-row input {
    border: none;
    background: white;
    text-align: center;
    font-size: 1em;
    padding: 10px;
    width: 100%;
    min-width: 0;
}

.grit-row input:focus {
    outline: none;
    background: #f8f8f8;
}

.conditions-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    min-height: 60px;
    padding: 8px;
    background: #fafafa;
}

.conditions-header {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 8px;
}

.conditions-label {
    font-size: 0.85em;
    color: #6a6a7a;
    font-style: italic;
}

.ignored-conditions-list {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.ignored-condition-row {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    background: #fce4e4;
    border-radius: 4px;
    padding: 6px 8px;
}

.ignored-condition-row .slot-btn {
    flex-shrink: 0;
    margin-top: 2px;
}

.ignored-condition-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.ignored-condition-name {
    font-weight: 500;
    font-size: 0.9em;
    color: #904040;
}

.ignored-condition-clear {
    font-size: 0.75em;
    color: #905050;
    font-style: italic;
}

.grit-note {
    font-size: 0.8em;
    color: #6a6a7a;
    margin-top: 8px;
}

.banked-box {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    min-width: 0;
    overflow: hidden;
}

.banked-label {
    font-weight: bold;
    color: #4a4a5a;
    margin-bottom: 8px;
}

.banked-box textarea {
    flex: 1;
    min-height: 80px;
    padding: 8px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    resize: none;
    font-family: inherit;
    font-size: 0.9em;
    background: #fafafa;
}

.banked-box textarea:focus {
    outline: none;
    border-color: #4a4a5a;
}

.mausritter-logo {
    font-family: 'UnifrakturMaguntia', 'Times New Roman', serif;
    font-size: 1.5em;
    color: #4a4a5a;
    text-align: right;
    margin-top: 10px;
}

/* Page Footer */
.page-footer {
    max-width: 900px;
    margin: 20px auto 0;
    padding: 15px 25px;
    border-top: 1px solid #d0d0d0;
    text-align: center;
    font-size: 0.85em;
    color: #8a8a9a;
}

.page-footer a {
    color: #4a4a5a;
    text-decoration: underline;
}

/* Dice Roller - collapsible */
.dice-roller {
    margin-top: 20px;
    border-top: 1px solid #e0e0e0;
    padding-top: 15px;
}

.dice-roller-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    padding: 10px 15px;
    background: #f8f8f8;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
    margin-bottom: 10px;
    user-select: none;
}

.dice-roller-header:hover {
    background: #f0f0f0;
}

.dice-roller-title {
    font-weight: bold;
    font-size: 1.1em;
    color: #4a4a5a;
}

.dice-roller-toggle {
    font-size: 1em;
    color: #6a6a7a;
}

.dice-roller-content {
    display: none;
    padding: 15px;
    background: #f8f8f8;
    border: 1px solid #d0d0d0;
    border-radius: 8px;
}

.dice-roller-content.active {
    display: block;
}

.dice-input-section {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 15px;
}

.dice-input {
    padding: 10px;
    border: 1px solid #d0d0d0;
    border-radius: 6px;
    font-size: 1em;
    width: 150px;
}

.dice-input:focus {
    outline: none;
    border-color: #4a4a5a;
}

.roll-btn {
    padding: 10px 20px;
    background: #4a4a5a;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: background 0.2s;
}

.roll-btn:hover {
    background: #3a3a4a;
}

.dice-results {
    margin-top: 15px;
}

.dice-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 10px;
}

.die {
    width: 50px;
    height: 50px;
    background: white;
    border: 2px solid #4a4a5a;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4em;
    font-weight: bold;
    color: #4a4a5a;
}

.die.rolling {
    animation: rollDice 0.6s ease-in-out;
}

@keyframes rollDice {
    0% { transform: rotate(0deg); }
    25% { transform: rotate(90deg) scale(1.1); }
    50% { transform: rotate(180deg) scale(0.9); }
    75% { transform: rotate(270deg) scale(1.1); }
    100% { transform: rotate(360deg); }
}

.dice-summary {
    padding: 10px;
    background: white;
    border: 1px solid #d0d0d0;
    border-radius: 6px;
    font-weight: bold;
    color: #4a4a5a;
}

/* Item Selector Modal */
.item-selector-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.item-selector-modal.active {
    display: flex;
}

.item-selector-content {
    background: white;
    border-radius: 12px;
    max-width: 500px;
    width: 90%;
    max-height: 80vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
}

.item-selector-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 20px;
    border-bottom: 1px solid #e0e0e0;
    font-weight: bold;
    font-size: 1.2em;
    color: #4a4a5a;
}

.close-modal {
    background: none;
    border: none;
    font-size: 1.5em;
    cursor: pointer;
    color: #6a6a7a;
    padding: 0;
    line-height: 1;
}

.close-modal:hover {
    color: #4a4a5a;
}

.item-search-container {
    padding: 10px 15px;
    border-bottom: 1px solid #e0e0e0;
}

.item-search-input {
    width: 100%;
    padding: 10px 12px;
    border: 1px solid #d0d0d0;
    border-radius: 6px;
    font-size: 0.95em;
    box-sizing: border-box;
}

.item-search-input:focus {
    outline: none;
    border-color: #8a8a9a;
    box-shadow: 0 0 0 2px rgba(138, 138, 154, 0.2);
}

.item-search-input::placeholder {
    color: #9a9aaa;
}

.item-selector-body {
    overflow-y: auto;
    padding: 10px;
}

.item-category {
    margin-bottom: 15px;
}

.item-category-header {
    font-weight: bold;
    color: #4a4a5a;
    padding: 8px 10px;
    background: #f0f0f0;
    border-radius: 6px;
    margin-bottom: 8px;
    cursor: pointer;
}

.item-category-header:hover {
    background: #e8e8e8;
}

/* Conditions category - red styling to indicate these are bad */
.item-category.conditions-category .item-category-header {
    background: #fce4e4;
    color: #904040;
}

.item-category.conditions-category .item-category-header:hover {
    background: #f8d4d4;
}

.item-category.conditions-category .item-category-items {
    background: #fef8f8;
    border-radius: 0 0 6px 6px;
    margin-top: -4px;
    padding-top: 8px;
}

.item-category.conditions-category .item-option:hover {
    background: #fce4e4;
}

.item-category-items {
    display: none;
    padding-left: 10px;
}

.item-category-items.expanded {
    display: block;
}

.item-option {
    padding: 8px 12px;
    cursor: pointer;
    border-radius: 4px;
    color: #5a5a6a;
    font-size: 0.95em;
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.item-option:hover {
    background: #f0f0f0;
    color: #4a4a5a;
}

.item-name {
    font-weight: 500;
}

.item-details {
    font-size: 0.85em;
    color: #8a8a9a;
}

/* Custom Dialog Modal */
.custom-dialog-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    z-index: 1000;
    justify-content: center;
    align-items: center;
}

.custom-dialog-modal.active {
    display: flex;
}

.custom-dialog-content {
    background: white;
    border-radius: 12px;
    max-width: 400px;
    width: 90%;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
}

.custom-dialog-header {
    padding: 15px 20px;
    border-bottom: 1px solid #e0e0e0;
    font-weight: bold;
    font-size: 1.2em;
    color: #4a4a5a;
}

.custom-dialog-body {
    padding: 20px;
    color: #5a5a6a;
    line-height: 1.5;
}

.custom-dialog-buttons {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    padding: 15px 20px;
    border-top: 1px solid #e0e0e0;
    background: #f8f8f8;
}

.dialog-btn {
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    font-size: 0.95em;
    transition: background 0.2s, transform 0.1s;
}

.dialog-btn:active {
    transform: scale(0.98);
}

.dialog-btn-primary {
    background: #4a4a5a;
    color: white;
}

.dialog-btn-primary:hover {
    background: #3a3a4a;
}

.dialog-btn-secondary {
    background: #e0e0e0;
    color: #4a4a5a;
}

.dialog-btn-secondary:hover {
    background: #d0d0d0;
}

/* Hirelings Section */
.hirelings-section {
    margin-bottom: 20px;
}

.hirelings-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.add-hireling-row {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
}

.add-hireling-label {
    font-size: 0.95em;
    color: #6a6a7a;
}

/* Individual Hireling Card */
.hireling-card {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    padding: 15px;
    background: white;
}

.hireling-card-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: 15px;
    padding-bottom: 10px;
    border-bottom: 1px solid #d0d0d0;
}

.hireling-title {
    font-family: 'UnifrakturMaguntia', 'Times New Roman', serif;
    font-size: 1.8em;
    color: #4a4a5a;
}

.hireling-remove-btn {
    width: 24px;
    height: 24px;
    border: 1px solid #d0d0d0;
    border-radius: 4px;
    background: #f8f8f8;
    cursor: pointer;
    font-size: 16px;
    font-weight: bold;
    color: #aa2a2a;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hireling-remove-btn:hover {
    background: #fce4e4;
    border-color: #aa2a2a;
}

.hireling-info-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-bottom: 15px;
}

.hireling-field {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.hireling-field-label {
    font-size: 0.85em;
    color: #6a6a7a;
    font-style: italic;
}

.hireling-field input {
    border: none;
    border-bottom: 1px solid #d0d0d0;
    padding: 5px;
    font-size: 0.95em;
    color: #4a4a5a;
    background: transparent;
}

.hireling-field input:focus {
    outline: none;
    border-bottom-color: #4a4a5a;
}

.hireling-body {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 15px;
}

/* Hireling Stats */
.hireling-stats {
    display: flex;
    flex-direction: column;
    min-width: 160px;
    max-width: 180px;
}

.hireling-stats-header {
    display: grid;
    grid-template-columns: 50px 1fr 1fr;
    padding: 5px 2px;
    font-size: 0.75em;
    color: #6a6a7a;
    font-style: italic;
}

.hireling-stats-header span {
    text-align: center;
}

.hireling-stats-header span:first-child {
    text-align: left;
}

.hireling-stats-table {
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
}

.hireling-stat-row {
    display: grid;
    grid-template-columns: 50px 1fr 1fr;
    border-bottom: 1px solid #d0d0d0;
}

.hireling-stat-row:last-child {
    border-bottom: none;
}

.hireling-stat-label {
    font-weight: bold;
    font-size: 0.95em;
    background: #f0f0f0;
    padding: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #d0d0d0;
    color: #4a4a5a;
}

.hireling-stat-row input {
    border: none;
    background: white;
    text-align: center;
    font-size: 0.85em;
    padding: 6px;
    border-right: 1px solid #d0d0d0;
    width: 100%;
    min-width: 0;
}

.hireling-stat-row input:last-child {
    border-right: none;
}

.hireling-stat-row input:focus {
    outline: none;
    background: #f8f8f8;
}

/* Hireling Inventory (6 slots: 2 paw, 4 pack) */
.hireling-inventory {
    display: flex;
    gap: 10px;
    flex: 1;
}

.hireling-paw-column {
    display: flex;
    flex-direction: column;
    width: 120px;
    flex-shrink: 0;
}

.hireling-pack-column {
    display: flex;
    flex-direction: column;
    flex: 1;
}

.hireling-paw-grid {
    display: flex;
    flex-direction: column;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
}

.hireling-pack-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    grid-template-rows: 1fr 1fr;
    border: 2px solid #4a4a5a;
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
}

.hireling-inventory-slot {
    padding: 8px;
    min-height: 70px;
    display: flex;
    flex-direction: column;
    background: white;
}

/* Paw slots stack vertically with divider */
.hireling-paw-grid .hireling-inventory-slot:first-child {
    border-bottom: 1px solid #d0d0d0;
}

/* Pack grid internal borders */
.hireling-pack-grid .hireling-inventory-slot {
    border-right: 1px solid #d0d0d0;
    border-bottom: 1px solid #d0d0d0;
}

.hireling-pack-grid .hireling-inventory-slot:nth-child(2),
.hireling-pack-grid .hireling-inventory-slot:nth-child(4) {
    border-right: none;
}

.hireling-pack-grid .hireling-inventory-slot:nth-child(3),
.hireling-pack-grid .hireling-inventory-slot:nth-child(4) {
    border-bottom: none;
}

.hireling-slot-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 6px;
}

.hireling-slot-label {
    font-weight: bold;
    font-size: 1em;
    color: #4a4a5a;
}

.hireling-slot-actions {
    display: flex;
    gap: 4px;
}

.hireling-slot-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: stretch;
}

.hireling-slot-content textarea {
    width: 100%;
    flex: 1;
    padding: 4px;
    border: 1px solid #e0e0e0;
    border-radius: 4px;
    text-align: center;
    font-size: 0.8em;
    background: #fafafa;
    resize: none;
    font-family: inherit;
}

.hireling-slot-content textarea:focus {
    outline: none;
    border-color: #4a4a5a;
    background: white;
}

.hireling-usage-markers {
    display: flex;
    justify-content: center;
    gap: 6px;
    margin-top: 6px;
}

.hireling-usage-markers .usage-marker {
    width: 14px;
    height: 14px;
}

/* Hireling inventory slot - condition styling */
.hireling-inventory-slot.condition-slot {
    background: #fce4e4;
}

.hireling-inventory-slot.condition-slot .hireling-slot-content textarea {
    background: #fef0f0;
    border-color: #e8a0a0;
}

.hireling-inventory-slot.condition-slot .condition-clear {
    font-size: 0.7em;
    color: #905050;
    text-align: center;
    margin-top: 2px;
    font-style: italic;
}

/* Hireling depleted state - cross through text with red background */
.hireling-inventory-slot.depleted .hireling-slot-content textarea {
    opacity: 0.7;
    text-decoration: line-through;
    background: #fce4e4;
    border-color: #e8a0a0;
}

/* Hireling two-slot item secondary styling */
.hireling-inventory-slot.two-slot-secondary .hireling-usage-markers {
    display: none;
}

.hireling-inventory-slot.two-slot-secondary .hireling-slot-header {
    opacity: 0.5;
}

.hireling-inventory-slot.two-slot-secondary .hireling-slot-content textarea {
    background: #f0f0f0;
    cursor: not-allowed;
}

@media print {
    body {
        background: white;
        padding: 0;
    }
    .character-sheet {
        box-shadow: none;
        border-radius: 0;
    }
    .dice-roller {
        display: none;
    }
    .page-footer {
        display: none;
    }
    .item-selector-modal {
        display: none;
    }
    .custom-dialog-modal {
        display: none;
    }
    .slot-actions {
        display: none;
    }
}
"""
