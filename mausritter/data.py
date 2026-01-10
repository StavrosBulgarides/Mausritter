"""
Game data tables for Mausritter character generation.
Single source of truth for all character creation data.
"""

import json

# Background table based on HP and Pips (from SRD 2.3)
# Format: (HP, Pips) -> (Background, Item A, Item B)
BACKGROUND_TABLE = {
    (1, 1): ("Test subject", "Spell: Magic missile", "Lead coat (Heavy armour)"),
    (1, 2): ("Kitchen forager", "Shield & jerkin (Light armour)", "Cookpots"),
    (1, 3): ("Cage dweller", "Spell: Be understood", "Bottle of milk"),
    (1, 4): ("Hedge witch", "Spell: Heal", "Incense stick"),
    (1, 5): ("Leatherworker", "Shield & jerkin (Light armour)", "Shears"),
    (1, 6): ("Street tough", "Dagger (Light, d6)", "Flask of coffee"),
    (2, 1): ("Mendicant priest", "Spell: Restore", "Holy symbol"),
    (2, 2): ("Beetleherd", "Hireling: Loyal beetle", "Pole, 6\""),
    (2, 3): ("Ale brewer", "Hireling: Drunken torchbearer", "Small barrel of ale"),
    (2, 4): ("Fishermouse", "Net", "Needle (Light, d6)"),
    (2, 5): ("Blacksmith", "Hammer (Medium, d6/d8)", "Metal file"),
    (2, 6): ("Wireworker", "Wire, spool", "Electric lantern"),
    (3, 1): ("Woodcutter", "Axe (Medium, d6/d8)", "Twine, roll"),
    (3, 2): ("Bat cultist", "Spell: Darkness", "Bag of bat teeth"),
    (3, 3): ("Tin miner", "Pickaxe (Medium, d6/d8)", "Lantern"),
    (3, 4): ("Trash collector", "Trashhook (Heavy, d10)", "Mirror"),
    (3, 5): ("Wall rover", "Fishhook", "Thread, spool"),
    (3, 6): ("Merchant", "Hireling: Pack rat", "20p IOU from a noblemouse"),
    (4, 1): ("Raft crew", "Hammer (Medium, d6/d8)", "Wooden spikes"),
    (4, 2): ("Worm wrangler", "Pole, 6\"", "Soap"),
    (4, 3): ("Sparrow rider", "Fishhook", "Goggles"),
    (4, 4): ("Sewer guide", "Metal file", "Thread, spool"),
    (4, 5): ("Prison guard", "Chain, 6\"", "Spear (Heavy, d10)"),
    (4, 6): ("Fungus farmer", "Dried mushroom (as rations)", "Spore mask"),
    (5, 1): ("Dam builder", "Shovel", "Wooden spikes"),
    (5, 2): ("Cartographer", "Quill & ink", "Compass"),
    (5, 3): ("Trap thief", "Block of cheese", "Glue"),
    (5, 4): ("Vagabond", "Tent", "Treasure map, dubious"),
    (5, 5): ("Grain farmer", "Spear (Heavy, d10)", "Whistle"),
    (5, 6): ("Message runner", "Bedroll", "Documents, sealed"),
    (6, 1): ("Troubadour", "Musical instrument", "Disguise kit"),
    (6, 2): ("Gambler", "Set of loaded dice", "Mirror"),
    (6, 3): ("Sap tapper", "Bucket", "Wooden spikes"),
    (6, 4): ("Bee keeper", "Jar of honey", "Net"),
    (6, 5): ("Librarian", "Scrap of obscure book", "Quill & ink"),
    (6, 6): ("Pauper noblemouse", "Felt hat", "Perfume"),
}

# Birthsign table (from SRD 2.3)
# Format: (Sign, Disposition)
BIRTHSIGNS = [
    ("Star", "Brave / Reckless"),
    ("Wheel", "Industrious / Unimaginative"),
    ("Acorn", "Inquisitive / Stubborn"),
    ("Storm", "Generous / Wrathful"),
    ("Moon", "Wise / Mysterious"),
    ("Mother", "Nurturing / Worrying"),
]

# Coat colors (from SRD 2.3)
COAT_COLORS = [
    "Chocolate",
    "Black",
    "White",
    "Tan",
    "Grey",
    "Blue",
]

# Coat patterns (from SRD 2.3)
COAT_PATTERNS = [
    "Solid",
    "Brindle",
    "Patchy",
    "Banded",
    "Marbled",
    "Flecked",
]

# Physical details d66 table (from SRD 2.3)
# Indexed by d66 roll (11-66)
PHYSICAL_DETAILS = {
    # Body (11-16)
    11: "Scarred body",
    12: "Corpulent body",
    13: "Skeletal body",
    14: "Willowy body",
    15: "Tiny body",
    16: "Massive body",
    # Clothes (21-26)
    21: "War paint",
    22: "Foreign clothes",
    23: "Elegant clothes",
    24: "Patched clothes",
    25: "Fashionable clothes",
    26: "Unwashed clothes",
    # Face/Ear (31-36)
    31: "Missing ear",
    32: "Lumpy face",
    33: "Beautiful face",
    34: "Round face",
    35: "Delicate face",
    36: "Elongated face",
    # Fur (41-46)
    41: "Groomed fur",
    42: "Dreadlocks",
    43: "Dyed fur",
    44: "Shaved fur",
    45: "Frizzy fur",
    46: "Silky fur",
    # Eyes (51-56)
    51: "Night black eyes",
    52: "Eye patch",
    53: "Blood red eyes",
    54: "Wise eyes",
    55: "Sharp eyes",
    56: "Luminous eyes",
    # Tail (61-66)
    61: "Cropped tail",
    62: "Whip-like tail",
    63: "Tufted tail",
    64: "Stubby tail",
    65: "Prehensile tail",
    66: "Curly tail",
}

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

# Weapons by category (from SRD 2.3)
# Format: (Name, Damage, Slots, Special)
WEAPONS = {
    "light": [
        ("Needle", "d6", 1, "If dual-wielding, roll both dice and use best"),
        ("Dagger", "d6", 1, "If dual-wielding, roll both dice and use best"),
        ("Hatchet", "d6", 1, "If dual-wielding, roll both dice and use best"),
    ],
    "medium": [
        ("Sword", "d6/d8", 1, "d6 one-handed, d8 two-handed"),
        ("Axe", "d6/d8", 1, "d6 one-handed, d8 two-handed"),
        ("Staff", "d6/d8", 1, "d6 one-handed, d8 two-handed"),
        ("Hammer", "d6/d8", 1, "d6 one-handed, d8 two-handed"),
        ("Pickaxe", "d6/d8", 1, "d6 one-handed, d8 two-handed"),
    ],
    "heavy": [
        ("Trashhook", "d10", 2, "Requires both paws"),
        ("Spear", "d10", 2, "Requires both paws"),
        ("Heavy hammer", "d10", 2, "Requires both paws"),
    ],
}


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
        "BIRTHSIGNS": BIRTHSIGNS,
        "COAT_COLORS": COAT_COLORS,
        "COAT_PATTERNS": COAT_PATTERNS,
        "PHYSICAL_DETAILS": PHYSICAL_DETAILS,
        "FIRST_NAMES": FIRST_NAMES,
        "LAST_NAMES": LAST_NAMES,
        "WEAPONS": WEAPONS,
    }
