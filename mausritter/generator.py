"""
Character generation logic for Mausritter.
"""

import random
from typing import Dict, Any, Tuple

from .data import (
    BACKGROUND_TABLE,
    BIRTHMARKS,
    FUR_COLORS,
    FUR_PATTERNS,
    SPECIAL_FEATURES,
    FIRST_NAMES,
    LAST_NAMES,
    WEAPONS,
)


def roll_dice(num_dice: int, sides: int) -> int:
    """Roll dice and return the sum."""
    return sum(random.randint(1, sides) for _ in range(num_dice))


def generate_attributes() -> Dict[str, int]:
    """Generate STR, DEX, and WIL attributes by rolling 3d6 each."""
    return {
        "STR": roll_dice(3, 6),
        "DEX": roll_dice(3, 6),
        "WIL": roll_dice(3, 6),
    }


def get_background(hp: int, pips: int) -> Tuple[str, str, str]:
    """Get background based on HP and Pips."""
    if (hp, pips) in BACKGROUND_TABLE:
        return BACKGROUND_TABLE[(hp, pips)]
    return ("Scavenger", "Rope", "Torch")


def generate_character() -> Dict[str, Any]:
    """Generate a complete Mausritter character."""
    attributes = generate_attributes()
    hp = roll_dice(1, 6)
    pips = roll_dice(1, 6)

    background, item_a, item_b = get_background(hp, pips)

    # Determine additional equipment based on highest attribute
    highest_attr = max(attributes.values())
    additional_items = []
    if highest_attr <= 9:
        additional_hp = roll_dice(1, 6)
        additional_pips = roll_dice(1, 6)
        _, add_item_a, add_item_b = get_background(additional_hp, additional_pips)
        additional_items.append(add_item_a)
        if highest_attr <= 7:
            additional_items.append(add_item_b)

    # Generate appearance
    birthmark = random.choice(BIRTHMARKS)
    fur_color = random.choice(FUR_COLORS)
    fur_pattern = random.choice(FUR_PATTERNS)
    special_feature = random.choice(SPECIAL_FEATURES)

    # Generate name
    first_name = random.choice(FIRST_NAMES)
    last_name = random.choice(LAST_NAMES)
    name = f"{first_name} {last_name}"

    # Select weapon
    weapon = random.choice(WEAPONS)

    # Starting equipment
    equipment = ["Torches", "Rations", weapon, item_a, item_b]
    equipment.extend(additional_items)

    return {
        "name": name,
        "attributes": attributes,
        "hp": hp,
        "pips": pips,
        "background": background,
        "equipment": equipment,
        "appearance": {
            "birthmark": birthmark,
            "fur_color": fur_color,
            "fur_pattern": fur_pattern,
            "special_feature": special_feature,
        },
        "weapon": weapon,
        "notes": "",
        "conditions": [],
    }
