# Things that I'm planning to do

## Warbands
1) Include in the same section as Hirelings? Review rules to see if they are equivalent.

# Global options - Implement overarching options that affect relevant stats in one go.
1) Rest to clear relevant conditions
2) Rest to recover HP if lost
etc. 

## Dice roller
1) Clear result
2) Weapon attack similar

## Player area
1) Notes
2) Maps  - draw

## Hit protection and damage
1) Attacks
**Attacks always hit.** Roll your weapon’s die and do that much damage to an opponent, minus their armour.

When an attack is **impaired**, such is firing into cover, or fighting while grappled, roll **d4** for damage regardless of weapon. When an attack is **enhanced** by a gambit or vulnerable opponent, roll **d12**.

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
5) GM sharing area - share content with players. One/all. Maps, letters etc.
5) Set advantages/disadvantages for a player
6) Run fights

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