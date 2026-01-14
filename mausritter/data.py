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

# Hireling Looks (from SRD 2.3 NPC Details d20 table - Appearance column)
HIRELING_LOOKS = [
    "Soulful eyes",
    "Bright, patched clothes",
    "Wreath of daisies",
    "Grubby clothes",
    "Large floppy hat",
    "Pockets full of seed",
    "Bent twig walking stick",
    "Carries rusted pinsword",
    "Long, wild fur",
    "Very, very old",
    "Bandaged tail",
    "Tail tied with a bow",
    "Missing an ear",
    "Long whiskers",
    "Twinkling eyes",
    "Huge, heavy black cloak",
    "Old battle scars",
    "Very young",
    "Shaved fur",
    "Braided fur",
]

# Hireling Dispositions (from SRD 2.3 - same as Birthsign dispositions)
HIRELING_DISPOSITIONS = [
    "Brave / Reckless",
    "Industrious / Unimaginative",
    "Inquisitive / Stubborn",
    "Generous / Wrathful",
    "Wise / Mysterious",
    "Nurturing / Worrying",
]

# Hireling Types with wages (from SRD 2.3)
HIRELING_TYPES = [
    {"type": "Torchbearer", "wages": "1p/day"},
    {"type": "Labourer", "wages": "2p/day"},
    {"type": "Tunnel digger", "wages": "5p/day"},
    {"type": "Armourer/blacksmith", "wages": "8p/day"},
    {"type": "Local guide", "wages": "10p/day"},
    {"type": "Mouse-at-arms", "wages": "10p/day"},
    {"type": "Scholar", "wages": "20p/day"},
    {"type": "Knight", "wages": "25p/day"},
    {"type": "Interpreter", "wages": "30p/day"},
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


# Inventory items available for selection (from SRD 2.3)
# Format: {"name": str, "price": str, "slots": int, "notes": str (optional)}
INVENTORY_ITEMS = {
    "Weapons": [
        {"name": "Improvised (d6)", "price": "1p", "slots": 1, "notes": "Twig, rock, etc."},
        {"name": "Needle (Light, d6)", "price": "10p", "slots": 1},
        {"name": "Dagger (Light, d6)", "price": "10p", "slots": 1},
        {"name": "Hatchet (Light, d6)", "price": "10p", "slots": 1},
        {"name": "Sword (Medium, d6/d8)", "price": "20p", "slots": 1},
        {"name": "Axe (Medium, d6/d8)", "price": "20p", "slots": 1},
        {"name": "Staff (Medium, d6/d8)", "price": "20p", "slots": 1},
        {"name": "Hammer (Medium, d6/d8)", "price": "20p", "slots": 1},
        {"name": "Pickaxe (Medium, d6/d8)", "price": "20p", "slots": 1},
        {"name": "Trashhook (Heavy, d10)", "price": "40p", "slots": 2, "notes": "Two paws"},
        {"name": "Spear (Heavy, d10)", "price": "40p", "slots": 2, "notes": "Two paws"},
        {"name": "Heavy hammer (Heavy, d10)", "price": "40p", "slots": 2, "notes": "Two paws"},
        {"name": "Sling (Light ranged)", "price": "10p", "slots": 1},
        {"name": "Hand crossbow (Light ranged)", "price": "10p", "slots": 1},
        {"name": "Bow (Heavy ranged)", "price": "40p", "slots": 2, "notes": "Two paws"},
        {"name": "Crossbow (Heavy ranged)", "price": "40p", "slots": 2, "notes": "Two paws"},
        {"name": "Arrows, quiver", "price": "5p", "slots": 1, "notes": "Body slot"},
        {"name": "Stones, pouch", "price": "1p", "slots": 1, "notes": "Body slot"},
    ],
    "Armour": [
        {"name": "Shield & jerkin (Light armour)", "price": "150p", "slots": 2, "notes": "Paw + Body"},
        {"name": "Lead coat (Heavy armour)", "price": "500p", "slots": 2, "notes": "Two body slots"},
    ],
    "Adventuring Gear": [
        {"name": "Bedroll", "price": "10p", "slots": 1},
        {"name": "Bellows", "price": "10p", "slots": 1},
        {"name": "Book, blank", "price": "300p", "slots": 1},
        {"name": "Book, reading", "price": "600p", "slots": 1},
        {"name": "Bottle", "price": "1p", "slots": 1},
        {"name": "Bucket", "price": "5p", "slots": 1},
        {"name": "Caltrops, bag", "price": "10p", "slots": 1},
        {"name": "Chalk", "price": "1p", "slots": 1},
        {"name": "Chisel", "price": "5p", "slots": 1},
        {"name": "Cookpots", "price": "10p", "slots": 1},
        {"name": "Crowbar", "price": "10p", "slots": 1},
        {"name": "Drill", "price": "10p", "slots": 1},
        {"name": "Glue", "price": "5p", "slots": 1},
        {"name": "Grease", "price": "5p", "slots": 1},
        {"name": "Hammer", "price": "10p", "slots": 1},
        {"name": "Horn", "price": "10p", "slots": 1},
        {"name": "Hourglass", "price": "300p", "slots": 1},
        {"name": "Lockpicks", "price": "100p", "slots": 1},
        {"name": "Metal file", "price": "5p", "slots": 1},
        {"name": "Mirror", "price": "200p", "slots": 1},
        {"name": "Musical instrument", "price": "200p", "slots": 1},
        {"name": "Net", "price": "10p", "slots": 1},
        {"name": "Padlock and key, small", "price": "20p", "slots": 1},
        {"name": "Perfume", "price": "50p", "slots": 1},
        {"name": "Pick", "price": "10p", "slots": 1},
        {"name": "Set of loaded dice", "price": "5p", "slots": 1},
        {"name": "Shovel", "price": "10p", "slots": 1},
        {"name": "Tent", "price": "80p", "slots": 1},
        {"name": "Waterskin", "price": "5p", "slots": 1},
        {"name": "Whistle", "price": "5p", "slots": 1},
        {"name": "Wooden pole, 6\"", "price": "1p", "slots": 1},
        {"name": "Wooden spikes", "price": "1p", "slots": 1},
    ],
    "Human-made Tools": [
        {"name": "Fishing hook", "price": "20p", "slots": 1},
        {"name": "Incense stick", "price": "20p", "slots": 1},
        {"name": "Lens", "price": "200p", "slots": 1},
        {"name": "Necklace chain", "price": "40p", "slots": 1},
        {"name": "Needle", "price": "20p", "slots": 1},
        {"name": "Matches, packet", "price": "80p", "slots": 1},
        {"name": "Padlock and key, large", "price": "100p", "slots": 1},
        {"name": "Twine, roll", "price": "40p", "slots": 1},
        {"name": "Soap", "price": "10p", "slots": 1},
        {"name": "Thread, spool", "price": "20p", "slots": 1},
        {"name": "Mouse trap", "price": "100p", "slots": 1},
        {"name": "Poison", "price": "100p", "slots": 1},
    ],
    "Light Sources": [
        {"name": "Torches", "price": "10p", "slots": 1},
        {"name": "Lantern", "price": "50p", "slots": 1},
        {"name": "Oil, for lantern", "price": "10p", "slots": 1},
        {"name": "Electric lantern", "price": "200p", "slots": 1, "notes": "6 usage dots"},
        {"name": "Batteries", "price": "50p", "slots": 1},
    ],
    "Provisions": [
        {"name": "Rations", "price": "5p", "slots": 1},
        {"name": "Travel rations", "price": "5p", "slots": 1},
        {"name": "Waterskin", "price": "5p", "slots": 1},
        {"name": "Bottle of milk", "price": "2p", "slots": 1},
        {"name": "Flask of coffee", "price": "2p", "slots": 1},
        {"name": "Jar of honey", "price": "10p", "slots": 1},
        {"name": "Small barrel of ale", "price": "10p", "slots": 1},
        {"name": "Block of cheese", "price": "5p", "slots": 1},
        {"name": "Dried mushroom", "price": "5p", "slots": 1},
    ],
    "Miscellaneous": [
        {"name": "Purse", "price": "1p", "slots": 1, "notes": "Holds 250 pips"},
        {"name": "Rope, 6\"", "price": "5p", "slots": 1},
        {"name": "Chain, 6\"", "price": "20p", "slots": 1},
        {"name": "Wire, spool", "price": "20p", "slots": 1},
        {"name": "Compass", "price": "50p", "slots": 1},
        {"name": "Quill & ink", "price": "10p", "slots": 1},
        {"name": "Goggles", "price": "20p", "slots": 1},
        {"name": "Spore mask", "price": "20p", "slots": 1},
        {"name": "Disguise kit", "price": "50p", "slots": 1},
        {"name": "Holy symbol", "price": "20p", "slots": 1},
        {"name": "Bag of bat teeth", "price": "10p", "slots": 1},
        {"name": "Felt hat", "price": "10p", "slots": 1},
        {"name": "Documents, sealed", "price": "5p", "slots": 1},
        {"name": "Treasure map, dubious", "price": "10p", "slots": 1},
        {"name": "20p IOU from a noblemouse", "price": "20p", "slots": 1},
        {"name": "Scrap of obscure book", "price": "5p", "slots": 1},
    ],
    "Spells": [
        {"name": "Spell: Fireball", "price": "-", "slots": 1, "notes": "Deal [SUM]+[DICE] damage to all within 6\""},
        {"name": "Spell: Heal", "price": "-", "slots": 1, "notes": "Heal [SUM] STR, remove Injured"},
        {"name": "Spell: Magic missile", "price": "-", "slots": 1, "notes": "Deal [SUM]+[DICE] damage to creature in sight"},
        {"name": "Spell: Fear", "price": "-", "slots": 1, "notes": "Give Frightened to [DICE] creatures"},
        {"name": "Spell: Darkness", "price": "-", "slots": 1, "notes": "Create [SUM]x2\" sphere of darkness for [DICE] Turns"},
        {"name": "Spell: Restore", "price": "-", "slots": 1, "notes": "Remove Exhausted/Frightened from [DICE]+1 creatures"},
        {"name": "Spell: Be understood", "price": "-", "slots": 1, "notes": "Communicate with [DICE] creatures for [DICE] Turns"},
        {"name": "Spell: Ghost beetle", "price": "-", "slots": 1, "notes": "Create illusory beetle (6 slots) for [DICE]x6 Turns"},
        {"name": "Spell: Light", "price": "-", "slots": 1, "notes": "Stun [DICE] creatures or create torchlight [SUM] Turns"},
        {"name": "Spell: Invisible ring", "price": "-", "slots": 1, "notes": "Create [DICE]x6\" invisible force ring for [DICE] Turns"},
        {"name": "Spell: Knock", "price": "-", "slots": 1, "notes": "Open door/container as STR 10+[DICE]x4"},
        {"name": "Spell: Grease", "price": "-", "slots": 1, "notes": "Cover [DICE]x6\" in slippery grease"},
        {"name": "Spell: Grow", "price": "-", "slots": 1, "notes": "Grow creature to [DICE]+1 times size for 1 Turn"},
        {"name": "Spell: Invisibility", "price": "-", "slots": 1, "notes": "Invisible for [DICE] Turns, movement reduces duration"},
        {"name": "Spell: Catnip", "price": "-", "slots": 1, "notes": "Object becomes irresistible to cats for [DICE] Turns"},
    ],
    "Conditions": [
        {
            "name": "Exhausted",
            "price": "-",
            "slots": 1,
            "notes": "Body slot | Clear: Rest a night in camp",
        },
        {
            "name": "Frightened",
            "price": "-",
            "slots": 1,
            "notes": "Paw slot | Clear: A moment's rest in a safe place",
        },
        {
            "name": "Hungry",
            "price": "-",
            "slots": 1,
            "notes": "Body slot | Clear: Eat a fresh ration",
        },
        {
            "name": "Injured",
            "price": "-",
            "slots": 1,
            "notes": "Body slot | Clear: Heal 1 STR at full rest",
        },
        {
            "name": "Poisoned",
            "price": "-",
            "slots": 1,
            "notes": "Body slot | Clear: Antidote, healer's care, or rest in a safe settlement",
        },
        {
            "name": "Stunned",
            "price": "-",
            "slots": 1,
            "notes": "Paw slot | Clear: A moment's rest in a safe place",
        },
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
        "INVENTORY_ITEMS": INVENTORY_ITEMS,
        "HIRELING_LOOKS": HIRELING_LOOKS,
        "HIRELING_DISPOSITIONS": HIRELING_DISPOSITIONS,
        "HIRELING_TYPES": HIRELING_TYPES,
    }
