# Things that I'm planning to do

## Attributes
1) Characters can swap any two attributes. Easiest way is to allow max to go up/down

## Inventory
1)Improvised weapon slots - row 266

## Conditions
1) Implement conditions in the inventory list (search)- they are included as items affecting the inventory
2) List clear requirement in search
3) For each point of Grit you have, you may place one Condition into the Grit space on your character sheet. Once placed into the Grit space, a Condition cannot be removed until cleared. Preuambly reduces remaining grit.

### Conditions
Conditions are **negative effects** suffered by your mouse. Each Condition must be placed in an **inventory slot**. Mice may have multiple copies of the same condition. Some Conditions have additional effects, which apply as long as the Condition remains in your inventory. Conditions can only be **removed** by meeting their **clear** requirement—usually a short, long or full rest.

## Dice roller
1) Relevant success rolls. e.g., against strength. Icon against each one?
2) Weapon attack similar
3) General dice roller needed? After a roll compare the result to the condition and mark the roll as successful or not

## Hit protection and damage
1) Implement

## Spells
1) Inventory - add as items
2) Impact (Exhausted, Frightened, Hungry, Injured, Drained, Freeform)

## Hirelings
1) Implement hireling character sheets. Nest these?
2) Add an option to add hirelings (per character) - Player option. Rules review

## General Rule review
1) Look for rule exceptions not catered for by the current implementation

## GM view / LAN implementation
1) GM should be able to see the character sheets of each individual player - with a  summary page and the ability to navigate to other pages from this, and to be able to make changes to the sheet. Determine how this will work in practice prior to implementation, looking to other projects for inspiration. Suggestion is Flask app and local area LAN
2) GM turn tracker
3) GM Condition tracking - flag all conditions applied
4) GM only notes

### High-level approach

Create a small local web server: Python backend (Flask)
One server runs on the GM’s machine
Players connect via browser over LAN

Each character has:
a private player view
a GM view / dashboard that allows them to view and amend player pages (e.g., add conditions)
No accounts, no internet, no cloud, no heavy auth.

### Aesthetics
1) Design a nicer background - suggest coloured banner that GM can select and acts as the colour key for the GM screen
2) Look at complimentary colour choices