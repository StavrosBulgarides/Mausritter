# Things that I'm planning to do

## Inventory
1) Improvised weapon slots - row 266

## Weapons
1) Select weapon background should be red.

## Hirelings
1) Number hirelings as they are created #1, #2 etc
2) Sort out inventory alignment
3) Some backgrounds provide hirelings. Create those hirelings automatically where they are shown:
- Loyal beetle (Beetleherd background)
- Drunken torchbearer (Ale brewer background)
- Pack rat (Merchant background)

## Warbands
1) Include in the same section as Hirelings? Review rules to see if they are equivalent.

# Global options - Implement overarching options that affect relevant stats in one go.
1) Rest to clear relevant conditions
2) Rest to recover HP if lost
etc. 

## Dice roller
1) Relevant success rolls. e.g., against strength. Move dice icon to apply against relevant checks. Show success/fail
2) Weapon attack similar
3) Retain General dice roller but make it roll the check selected. The player can then look at the dice making up the result if they want (i) icon against the result takes the user to the dice section.

## Hit protection and damage
1) Implement

## Spells
1) Some backgrounds provide spells, but spell mechanics are not included:
- Spells provided: Magic Missile, Be Understood, Heal, Restore, Darkness
- Not implemented: Spell casting rules, spell dice, mishaps, dooms
- Spell recharge mechanics not shown
2) Impact of conditions (Exhausted, Frightened, Hungry, Injured, Drained, Freeform)


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