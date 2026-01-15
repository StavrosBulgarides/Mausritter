"""
Session management for Mausritter GM server.
Handles in-memory state and save/load to JSON.
"""

import json
import secrets
from datetime import datetime
from typing import Dict, Any, Optional


class GameSession:
    """Manages the current game session state."""

    def __init__(self):
        self.reset()

    def reset(self) -> None:
        """Reset to a fresh session."""
        self._state: Dict[str, Any] = {
            "session_name": "New Session",
            "created": datetime.now().isoformat(),
            "characters": {},
            "gm_notes": "",
            "combat": {
                "active": False,
                "turn_order": [],
                "current_turn": 0
            }
        }
        self._gm_token: str = secrets.token_urlsafe(8)
        self._next_char_id: int = 1

    @property
    def gm_token(self) -> str:
        """Get the GM authentication token."""
        return self._gm_token

    def verify_gm(self, token: str) -> bool:
        """Verify if the provided token matches the GM token."""
        return secrets.compare_digest(token, self._gm_token)

    def get_state(self) -> Dict[str, Any]:
        """Get the full session state."""
        return self._state.copy()

    def set_session_name(self, name: str) -> None:
        """Set the session name."""
        self._state["session_name"] = name

    def set_gm_notes(self, notes: str) -> None:
        """Set GM notes."""
        self._state["gm_notes"] = notes

    # Character management

    def add_character(self, character_data: Dict[str, Any]) -> str:
        """Add a character and return its ID."""
        char_id = f"char_{self._next_char_id:03d}"
        self._next_char_id += 1

        # Generate a player token for this character
        character_data["player_token"] = secrets.token_urlsafe(6)
        character_data["id"] = char_id

        self._state["characters"][char_id] = character_data
        return char_id

    def get_character(self, char_id: str) -> Optional[Dict[str, Any]]:
        """Get a character by ID."""
        return self._state["characters"].get(char_id)

    def get_character_by_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Get a character by player token."""
        for char in self._state["characters"].values():
            if char.get("player_token") == token:
                return char
        return None

    def get_all_characters(self) -> Dict[str, Dict[str, Any]]:
        """Get all characters."""
        return self._state["characters"].copy()

    def update_character(self, char_id: str, updates: Dict[str, Any]) -> bool:
        """Update a character's data. Returns True if successful."""
        if char_id not in self._state["characters"]:
            return False

        character = self._state["characters"][char_id]

        def deep_merge(target: dict, source: dict) -> None:
            """Recursively merge source into target."""
            for key, value in source.items():
                if key in ("id", "player_token"):
                    # Don't allow changing these
                    continue
                if isinstance(value, dict) and key in target and isinstance(target[key], dict):
                    # Recursively merge nested dicts
                    deep_merge(target[key], value)
                elif isinstance(value, list) and key in target and isinstance(target[key], list):
                    # For lists, replace entirely (inventory arrays)
                    target[key] = value
                else:
                    target[key] = value

        deep_merge(character, updates)
        return True

    def delete_character(self, char_id: str) -> bool:
        """Delete a character. Returns True if successful."""
        if char_id in self._state["characters"]:
            del self._state["characters"][char_id]
            return True
        return False

    # Save/Load

    def to_json(self) -> str:
        """Export session state to JSON string."""
        export_data = {
            "version": "1.0",
            "exported": datetime.now().isoformat(),
            "session": self._state
        }
        return json.dumps(export_data, indent=2)

    def from_json(self, json_str: str) -> bool:
        """Import session state from JSON string. Returns True if successful."""
        try:
            data = json.loads(json_str)

            if "session" not in data:
                return False

            self._state = data["session"]

            # Find the highest character ID to continue numbering
            max_id = 0
            for char_id in self._state.get("characters", {}).keys():
                try:
                    num = int(char_id.split("_")[1])
                    max_id = max(max_id, num)
                except (IndexError, ValueError):
                    pass
            self._next_char_id = max_id + 1

            # Generate new GM token for security
            self._gm_token = secrets.token_urlsafe(8)

            return True
        except (json.JSONDecodeError, KeyError):
            return False


# Global session instance
game_session = GameSession()
