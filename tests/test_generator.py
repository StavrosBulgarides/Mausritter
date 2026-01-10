"""Unit tests for the Mausritter character generator."""

import random
import pytest

from mausritter.generator import (
    roll_dice,
    generate_attributes,
    get_background,
    generate_character,
)
from mausritter.data import (
    BACKGROUND_TABLE,
    BIRTHMARKS,
    FUR_COLORS,
    FUR_PATTERNS,
    SPECIAL_FEATURES,
    FIRST_NAMES,
    LAST_NAMES,
    WEAPONS,
)


class TestRollDice:
    """Tests for the roll_dice function."""

    def test_single_d6_range(self):
        """Rolling 1d6 should return values between 1 and 6."""
        for _ in range(100):
            result = roll_dice(1, 6)
            assert 1 <= result <= 6

    def test_multiple_d6_range(self):
        """Rolling 3d6 should return values between 3 and 18."""
        for _ in range(100):
            result = roll_dice(3, 6)
            assert 3 <= result <= 18

    def test_single_d20_range(self):
        """Rolling 1d20 should return values between 1 and 20."""
        for _ in range(100):
            result = roll_dice(1, 20)
            assert 1 <= result <= 20

    def test_deterministic_with_seed(self):
        """Results should be reproducible with a fixed seed."""
        random.seed(42)
        result1 = roll_dice(3, 6)
        random.seed(42)
        result2 = roll_dice(3, 6)
        assert result1 == result2


class TestGenerateAttributes:
    """Tests for the generate_attributes function."""

    def test_returns_all_attributes(self):
        """Should return STR, DEX, and WIL."""
        attrs = generate_attributes()
        assert "STR" in attrs
        assert "DEX" in attrs
        assert "WIL" in attrs
        assert len(attrs) == 3

    def test_attributes_in_valid_range(self):
        """All attributes should be between 3 and 18 (3d6 range)."""
        for _ in range(100):
            attrs = generate_attributes()
            for attr_name, value in attrs.items():
                assert 3 <= value <= 18, f"{attr_name} was {value}, expected 3-18"

    def test_deterministic_with_seed(self):
        """Results should be reproducible with a fixed seed."""
        random.seed(42)
        attrs1 = generate_attributes()
        random.seed(42)
        attrs2 = generate_attributes()
        assert attrs1 == attrs2


class TestGetBackground:
    """Tests for the get_background function."""

    def test_valid_lookup(self):
        """Should return correct background for known HP/Pips combinations."""
        # Test a few known combinations from the table
        assert get_background(1, 1) == ("Scavenger", "Rope", "Torch")
        assert get_background(1, 5) == ("Cook", "Pot", "Spices")
        assert get_background(3, 3) == ("Tailor", "Thread", "Needle")
        assert get_background(6, 6) == ("Guard", "Spear", "Shield")

    def test_all_table_entries(self):
        """All entries in the background table should be retrievable."""
        for (hp, pips), expected in BACKGROUND_TABLE.items():
            result = get_background(hp, pips)
            assert result == expected

    def test_fallback_for_invalid_values(self):
        """Should return fallback background for invalid HP/Pips."""
        assert get_background(0, 0) == ("Scavenger", "Rope", "Torch")
        assert get_background(7, 7) == ("Scavenger", "Rope", "Torch")
        assert get_background(-1, 3) == ("Scavenger", "Rope", "Torch")

    def test_returns_tuple_of_three_strings(self):
        """Should return a tuple of (background, item_a, item_b)."""
        result = get_background(3, 3)
        assert isinstance(result, tuple)
        assert len(result) == 3
        assert all(isinstance(s, str) for s in result)


class TestGenerateCharacter:
    """Tests for the generate_character function."""

    def test_returns_dict_with_required_keys(self):
        """Character should have all required fields."""
        character = generate_character()
        required_keys = [
            "name", "attributes", "hp", "pips", "background",
            "equipment", "appearance", "weapon", "notes", "conditions"
        ]
        for key in required_keys:
            assert key in character, f"Missing key: {key}"

    def test_name_format(self):
        """Name should be 'FirstName LastName' format."""
        character = generate_character()
        name_parts = character["name"].split()
        assert len(name_parts) == 2
        assert name_parts[0] in FIRST_NAMES
        assert name_parts[1] in LAST_NAMES

    def test_attributes_structure(self):
        """Attributes should contain STR, DEX, WIL in valid range."""
        character = generate_character()
        attrs = character["attributes"]
        assert "STR" in attrs
        assert "DEX" in attrs
        assert "WIL" in attrs
        for value in attrs.values():
            assert 3 <= value <= 18

    def test_hp_and_pips_range(self):
        """HP and Pips should be between 1 and 6."""
        for _ in range(50):
            character = generate_character()
            assert 1 <= character["hp"] <= 6
            assert 1 <= character["pips"] <= 6

    def test_background_is_valid(self):
        """Background should be from the background table."""
        valid_backgrounds = {bg for bg, _, _ in BACKGROUND_TABLE.values()}
        for _ in range(50):
            character = generate_character()
            assert character["background"] in valid_backgrounds

    def test_equipment_contains_basics(self):
        """Equipment should always contain Torches and Rations."""
        character = generate_character()
        assert "Torches" in character["equipment"]
        assert "Rations" in character["equipment"]

    def test_equipment_contains_weapon(self):
        """Equipment should contain a valid weapon."""
        character = generate_character()
        weapon = character["weapon"]
        assert weapon in WEAPONS
        assert weapon in character["equipment"]

    def test_equipment_minimum_items(self):
        """Equipment should have at least 5 items (basics + weapon + 2 background items)."""
        character = generate_character()
        assert len(character["equipment"]) >= 5

    def test_appearance_structure(self):
        """Appearance should have all required fields with valid values."""
        character = generate_character()
        appearance = character["appearance"]

        assert "birthmark" in appearance
        assert "fur_color" in appearance
        assert "fur_pattern" in appearance
        assert "special_feature" in appearance

        assert appearance["birthmark"] in BIRTHMARKS
        assert appearance["fur_color"] in FUR_COLORS
        assert appearance["fur_pattern"] in FUR_PATTERNS
        assert appearance["special_feature"] in SPECIAL_FEATURES

    def test_notes_and_conditions_initialized(self):
        """Notes should be empty string, conditions should be empty list."""
        character = generate_character()
        assert character["notes"] == ""
        assert character["conditions"] == []

    def test_deterministic_with_seed(self):
        """Character generation should be reproducible with a fixed seed."""
        random.seed(42)
        char1 = generate_character()
        random.seed(42)
        char2 = generate_character()
        assert char1 == char2

    def test_low_attributes_get_extra_equipment(self):
        """Characters with highest attribute <= 9 should get extra items."""
        random.seed(12345)  # Seed that produces low attributes
        # Generate many characters and check the rule
        found_extra_equipment = False
        for seed in range(1000):
            random.seed(seed)
            character = generate_character()
            highest_attr = max(character["attributes"].values())
            if highest_attr <= 9:
                # Should have at least 6 items (5 base + 1 extra)
                assert len(character["equipment"]) >= 6
                found_extra_equipment = True
                break
        assert found_extra_equipment, "Could not find a character with low enough attributes"

    def test_very_low_attributes_get_two_extra_items(self):
        """Characters with highest attribute <= 7 should get 2 extra items."""
        found_very_low = False
        for seed in range(10000):
            random.seed(seed)
            character = generate_character()
            highest_attr = max(character["attributes"].values())
            if highest_attr <= 7:
                # Should have at least 7 items (5 base + 2 extra)
                assert len(character["equipment"]) >= 7
                found_very_low = True
                break
        assert found_very_low, "Could not find a character with attributes <= 7"
