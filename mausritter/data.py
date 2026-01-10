"""
Game data tables for Mausritter character generation.
Single source of truth for all character creation data.
"""

import json

# Background table based on HP and Pips
# Format: (HP, Pips) -> (Background, Item A, Item B)
BACKGROUND_TABLE = {
    (1, 1): ("Scavenger", "Rope", "Torch"),
    (1, 2): ("Scavenger", "Rope", "Torch"),
    (1, 3): ("Farmer", "Sickle", "Seed Pouch"),
    (1, 4): ("Farmer", "Sickle", "Seed Pouch"),
    (1, 5): ("Cook", "Pot", "Spices"),
    (1, 6): ("Cook", "Pot", "Spices"),
    (2, 1): ("Scavenger", "Rope", "Torch"),
    (2, 2): ("Farmer", "Sickle", "Seed Pouch"),
    (2, 3): ("Fisher", "Net", "Hook"),
    (2, 4): ("Fisher", "Net", "Hook"),
    (2, 5): ("Herbalist", "Herbs", "Bandages"),
    (2, 6): ("Herbalist", "Herbs", "Bandages"),
    (3, 1): ("Farmer", "Sickle", "Seed Pouch"),
    (3, 2): ("Fisher", "Net", "Hook"),
    (3, 3): ("Tailor", "Thread", "Needle"),
    (3, 4): ("Tailor", "Thread", "Needle"),
    (3, 5): ("Craftsman", "Hammer", "Nails"),
    (3, 6): ("Craftsman", "Hammer", "Nails"),
    (4, 1): ("Fisher", "Net", "Hook"),
    (4, 2): ("Tailor", "Thread", "Needle"),
    (4, 3): ("Mason", "Chisel", "Stone"),
    (4, 4): ("Mason", "Chisel", "Stone"),
    (4, 5): ("Merchant", "Scale", "Coin Purse"),
    (4, 6): ("Merchant", "Scale", "Coin Purse"),
    (5, 1): ("Tailor", "Thread", "Needle"),
    (5, 2): ("Mason", "Chisel", "Stone"),
    (5, 3): ("Merchant", "Scale", "Coin Purse"),
    (5, 4): ("Scholar", "Book", "Ink & Quill"),
    (5, 5): ("Scholar", "Book", "Ink & Quill"),
    (5, 6): ("Scout", "Map", "Compass"),
    (6, 1): ("Mason", "Chisel", "Stone"),
    (6, 2): ("Merchant", "Scale", "Coin Purse"),
    (6, 3): ("Scholar", "Book", "Ink & Quill"),
    (6, 4): ("Scout", "Map", "Compass"),
    (6, 5): ("Guard", "Spear", "Shield"),
    (6, 6): ("Guard", "Spear", "Shield"),
}

BIRTHMARKS = [
    "Star-shaped", "Crescent moon", "Circle", "Triangle", "Line", "Dot",
    "Heart-shaped", "Diamond", "Cross", "Spiral", "Arrow", "Leaf"
]

FUR_COLORS = [
    "Brown", "Gray", "Black", "White", "Tan", "Cream",
    "Golden", "Silver", "Rust", "Charcoal", "Beige", "Cinnamon"
]

FUR_PATTERNS = [
    "Solid", "Spotted", "Striped", "Patched", "Brindled", "Ticked",
    "Banded", "Mottled", "Piebald", "Sable", "Agouti", "Roan"
]

SPECIAL_FEATURES = [
    "Eye patch", "Scar", "Missing ear tip", "Notched ear", "White paw",
    "Crooked tail", "Long whiskers", "Short whiskers", "One white eye",
    "Tattoo", "Jewelry", "Distinctive gait"
]

FIRST_NAMES = [
    "Acorn", "Bramble", "Chestnut", "Daisy", "Elder", "Fern", "Ginger",
    "Hazel", "Ivy", "Juniper", "Kestrel", "Laurel", "Maple", "Nettle",
    "Oak", "Pip", "Quill", "Rowan", "Sage", "Thistle", "Willow", "Yarrow",
    "Berry", "Clover", "Dandelion", "Fennel", "Hawthorn", "Moss", "Poppy",
    "Reed", "Sorrel", "Tansy", "Violet", "Wheat"
]

LAST_NAMES = [
    "Whiskers", "Tail", "Paw", "Ear", "Fur", "Nose", "Tooth", "Claw",
    "Squeak", "Scamper", "Nibble", "Gnaw", "Scratch", "Dig", "Burrow",
    "Nest", "Hollow", "Branch", "Leaf", "Root", "Bark", "Twig", "Seed",
    "Berry", "Nut", "Acorn", "Chestnut", "Hazel", "Oak", "Maple", "Willow"
]

WEAPONS = [
    "Dagger", "Shortsword", "Spear", "Bow", "Sling", "Club", "Rapier",
    "Sword", "Axe", "Mace", "Staff", "Knife", "Sickle", "Hammer"
]


def get_background_table_as_json() -> str:
    """Convert background table to JSON format for JavaScript use."""
    js_table = {}
    for (hp, pips), (bg, item_a, item_b) in BACKGROUND_TABLE.items():
        js_table[f"{hp},{pips}"] = [bg, item_a, item_b]
    return json.dumps(js_table, ensure_ascii=False)


def get_all_data_as_json() -> dict:
    """Return all game data as a dictionary for JSON serialization."""
    return {
        "BACKGROUND_TABLE": {f"{hp},{pips}": list(val) for (hp, pips), val in BACKGROUND_TABLE.items()},
        "BIRTHMARKS": BIRTHMARKS,
        "FUR_COLORS": FUR_COLORS,
        "FUR_PATTERNS": FUR_PATTERNS,
        "SPECIAL_FEATURES": SPECIAL_FEATURES,
        "FIRST_NAMES": FIRST_NAMES,
        "LAST_NAMES": LAST_NAMES,
        "WEAPONS": WEAPONS,
    }
