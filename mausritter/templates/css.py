"""CSS styles for the Mausritter character sheet."""

STYLES = """
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Georgia', 'Times New Roman', serif;
    background: #f5f5dc;
    color: #2c2c2c;
    padding: 20px;
    line-height: 1.6;
}

.character-sheet {
    max-width: 900px;
    margin: 0 auto;
    background: white;
    padding: 30px;
    border: 3px solid #8b4513;
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    position: relative;
}

.generate-new-btn {
    position: absolute;
    left: 20px;
    padding: 10px 20px;
    background: #8b4513;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1em;
    font-weight: bold;
    transition: background 0.3s;
}

.generate-new-btn:hover {
    background: #6b3410;
}

h1 {
    text-align: center;
    color: #8b4513;
    border-bottom: 2px solid #8b4513;
    padding-bottom: 10px;
    margin-bottom: 20px;
    font-size: 2em;
}

.section {
    margin-bottom: 25px;
    padding: 15px;
    background: #fafafa;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.section-title {
    font-size: 1.3em;
    font-weight: bold;
    color: #8b4513;
    margin-bottom: 10px;
    border-bottom: 1px solid #8b4513;
    padding-bottom: 5px;
}

.attributes-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 15px;
    margin-bottom: 15px;
}

.attribute {
    text-align: center;
    padding: 10px;
    background: white;
    border: 2px solid #8b4513;
    border-radius: 5px;
}

.attribute-label {
    font-weight: bold;
    font-size: 0.9em;
    color: #666;
    margin-bottom: 5px;
}

.attribute-value {
    font-size: 2em;
    font-weight: bold;
    color: #8b4513;
}

input[type="text"], input[type="number"], textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 3px;
    font-family: inherit;
    font-size: 1em;
}

input[type="number"] {
    text-align: center;
    font-size: 1.5em;
    font-weight: bold;
}

.stats-row {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-bottom: 15px;
}

.stat-box {
    padding: 10px;
    background: white;
    border: 2px solid #8b4513;
    border-radius: 5px;
    text-align: center;
}

.stat-label {
    font-weight: bold;
    color: #666;
    margin-bottom: 5px;
}

.equipment-list {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
}

.equipment-item {
    padding: 8px;
    background: white;
    border: 1px solid #ccc;
    border-radius: 3px;
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.equipment-name {
    width: 100%;
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 3px;
    font-family: inherit;
    font-size: 0.95em;
}

.equipment-uses {
    display: flex;
    gap: 8px;
    align-items: center;
    font-size: 0.85em;
    color: #666;
}

.equipment-uses-label {
    font-weight: bold;
    margin-right: 5px;
}

.equipment-uses-checkboxes {
    display: flex;
    gap: 5px;
}

.equipment-uses-checkboxes input[type="checkbox"] {
    width: 18px;
    height: 18px;
    cursor: pointer;
}

.equipment-uses-checkboxes label {
    display: flex;
    align-items: center;
    cursor: pointer;
    font-size: 0.9em;
}

textarea {
    min-height: 100px;
    resize: vertical;
}

.appearance-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
}

.appearance-item {
    padding: 8px;
    background: white;
    border: 1px solid #ccc;
    border-radius: 3px;
}

.appearance-label {
    font-weight: bold;
    color: #666;
    font-size: 0.9em;
    margin-bottom: 3px;
}

.conditions-list {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.condition-item {
    padding: 5px 10px;
    background: white;
    border: 1px solid #ccc;
    border-radius: 3px;
    min-width: 120px;
}

.dice-roller {
    margin-top: 30px;
    border-top: 2px solid #8b4513;
    padding-top: 20px;
}

.dice-roller-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    cursor: pointer;
    padding: 10px;
    background: #fafafa;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 15px;
    user-select: none;
}

.dice-roller-header:hover {
    background: #f0f0f0;
}

.dice-roller-header:active {
    background: #e8e8e8;
}

.dice-roller-title {
    font-size: 1.3em;
    font-weight: bold;
    color: #8b4513;
}

.dice-roller-toggle {
    font-size: 1.5em;
    color: #8b4513;
    user-select: none;
}

.dice-roller-content {
    display: none;
    padding: 15px;
    background: #fafafa;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.dice-roller-content.active {
    display: block;
}

.dice-input-section {
    display: flex;
    gap: 10px;
    align-items: center;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.dice-input {
    padding: 10px;
    border: 2px solid #8b4513;
    border-radius: 5px;
    font-size: 1.1em;
    width: 150px;
}

.roll-btn {
    padding: 10px 25px;
    background: #8b4513;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1.1em;
    font-weight: bold;
    transition: background 0.3s;
}

.roll-btn:hover {
    background: #6b3410;
}

.roll-btn:disabled {
    background: #ccc;
    cursor: not-allowed;
}

.dice-results {
    margin-top: 20px;
}

.dice-container {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 15px;
    min-height: 80px;
}

.die {
    width: 60px;
    height: 60px;
    background: white;
    border: 3px solid #8b4513;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.8em;
    font-weight: bold;
    color: #8b4513;
    position: relative;
    animation: none;
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
    margin-top: 15px;
    padding: 15px;
    background: white;
    border: 2px solid #8b4513;
    border-radius: 5px;
    font-size: 1.2em;
    font-weight: bold;
    color: #8b4513;
}

.dice-summary .total {
    font-size: 1.5em;
    color: #6b3410;
}

@media print {
    body {
        background: white;
        padding: 0;
    }
    .character-sheet {
        box-shadow: none;
        border: 2px solid #000;
    }
    .generate-new-btn {
        display: none;
    }
    .dice-roller {
        display: none;
    }
}
"""
