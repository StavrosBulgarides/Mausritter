# Things that I'm planning to do

## Warbands
1) Include in the same section as Hirelings? Review rules to see if they are equivalent.

# Global options - Implement overarching options that affect relevant stats in one go.
1) Rest to clear relevant conditions
2) Rest to recover HP if lost
etc. 

# Advantage/disadvantage
1) Advantages/disadvantages should be indicated against the relevant stats.
2) Selecting Advantage/disadvantage on a non-stat driven dice roll shouldn't automatically roll the dice

## Conditions
1) Conditions assigned by GM need a new 'Conditions to assign' concept which allows users to move to Grit or inventory. At the moment the sheet uplift the Grit in line with the condition. Need to allow 'soft' warning - perhaps deeper red?

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

### Completed
- [x] Flask-based local server (`python run_server.py`)
- [x] GM Dashboard with character overview
- [x] Player join page (no authentication required)
- [x] Full character sheet for players and GM (with all features: usage markers, item selector, dice roller, etc.)
- [x] GM can view/edit all character sheets
- [x] Players can edit their own character sheets
- [x] Auto-save to server on changes
- [x] Session save/load (JSON files)
- [x] New session (clear all)
- [x] Stop server button
- [x] GM condition tracking - add/remove conditions from dashboard
- [x] Player tokens for character access
- [x] Full data persistence on GM -> Player -> GM cycle (conditions, inventory usage, hirelings, slot states)

### To Do
1) GM turn tracker / initiative order
2) GM only notes (per character and session-wide)
3) GM sharing area - share content with players (maps, letters, etc.)
4) Set advantages/disadvantages for a player
5) Run fights / combat tracker

### Aesthetics
1) Design a nicer background - suggest coloured banner that GM can select and acts as the colour key for the GM screen
2) Look at complimentary colour choices