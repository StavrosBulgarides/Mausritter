"""
REST API routes for character and session management.
"""

from flask import Blueprint, jsonify, request, Response
from ..session import game_session
from ...generator import generate_character

api_bp = Blueprint("api", __name__)


# Session endpoints

@api_bp.route("/session", methods=["GET"])
def get_session():
    """Get full session state (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify(game_session.get_state())


@api_bp.route("/session/save", methods=["POST"])
def save_session():
    """Export session as JSON download (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    json_data = game_session.to_json()
    session_name = game_session.get_state().get("session_name", "session")
    safe_name = "".join(c for c in session_name if c.isalnum() or c in " -_").strip().replace(" ", "_")

    return Response(
        json_data,
        mimetype="application/json",
        headers={"Content-Disposition": f"attachment; filename=mausritter_{safe_name}.json"}
    )


@api_bp.route("/session/load", methods=["POST"])
def load_session():
    """Load session from uploaded JSON (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    if "file" not in request.files:
        # Try JSON body instead
        data = request.get_json()
        if data:
            json_str = request.data.decode("utf-8")
        else:
            return jsonify({"error": "No file or JSON provided"}), 400
    else:
        json_str = request.files["file"].read().decode("utf-8")

    if game_session.from_json(json_str):
        return jsonify({
            "success": True,
            "new_gm_token": game_session.gm_token,
            "message": "Session loaded. New GM token generated."
        })
    return jsonify({"error": "Invalid session file"}), 400


@api_bp.route("/session/new", methods=["POST"])
def new_session():
    """Start a fresh session (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    game_session.reset()
    return jsonify({
        "success": True,
        "new_gm_token": game_session.gm_token,
        "message": "New session started."
    })


@api_bp.route("/session/name", methods=["PATCH"])
def update_session_name():
    """Update session name (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name required"}), 400

    game_session.set_session_name(data["name"])
    return jsonify({"success": True})


@api_bp.route("/session/data", methods=["PATCH"])
def update_session_data():
    """Update session data like turn count (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    game_session.update_session_data(data)
    return jsonify({"success": True})


@api_bp.route("/server/shutdown", methods=["POST"])
def shutdown_server():
    """Shutdown the server (GM only)."""
    import os
    import signal

    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    def shutdown():
        os.kill(os.getpid(), signal.SIGTERM)

    # Schedule shutdown after response is sent
    from threading import Timer
    Timer(0.5, shutdown).start()

    return jsonify({"success": True, "message": "Server shutting down..."})


# Character endpoints

@api_bp.route("/characters", methods=["GET"])
def list_characters():
    """List all characters (GM) or just names/IDs (players)."""
    token = request.args.get("token", "")
    is_gm = game_session.verify_gm(token)

    characters = game_session.get_all_characters()

    if is_gm:
        return jsonify(characters)
    else:
        # Players only see name and ID for the join page
        return jsonify({
            char_id: {"id": char["id"], "name": char["name"]}
            for char_id, char in characters.items()
        })


@api_bp.route("/characters", methods=["POST"])
def create_character():
    """Create a new character (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    # Check if custom data provided or generate new
    data = request.get_json(silent=True) or {}
    if data.get("name"):
        character = data
    else:
        character = generate_character()

    char_id = game_session.add_character(character)
    return jsonify({
        "success": True,
        "character": game_session.get_character(char_id)
    }), 201


@api_bp.route("/characters/<char_id>", methods=["GET"])
def get_character(char_id: str):
    """Get a specific character."""
    character = game_session.get_character(char_id)
    if not character:
        return jsonify({"error": "Character not found"}), 404

    # Check authorization - GM can see all, player needs their token
    token = request.args.get("token", "")
    is_gm = game_session.verify_gm(token)
    is_owner = character.get("player_token") == token

    if not is_gm and not is_owner:
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(character)


@api_bp.route("/characters/<char_id>", methods=["PATCH"])
def update_character(char_id: str):
    """Update a character (GM or owner)."""
    character = game_session.get_character(char_id)
    if not character:
        return jsonify({"error": "Character not found"}), 404

    # Check authorization
    token = request.args.get("token", "")
    is_gm = game_session.verify_gm(token)
    is_owner = character.get("player_token") == token

    if not is_gm and not is_owner:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if game_session.update_character(char_id, data):
        return jsonify({
            "success": True,
            "character": game_session.get_character(char_id)
        })
    return jsonify({"error": "Update failed"}), 500


@api_bp.route("/characters/<char_id>", methods=["DELETE"])
def delete_character(char_id: str):
    """Delete a character (GM only)."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return jsonify({"error": "Unauthorized"}), 401

    if game_session.delete_character(char_id):
        return jsonify({"success": True})
    return jsonify({"error": "Character not found"}), 404


# Player token endpoint

@api_bp.route("/player/<player_token>", methods=["GET"])
def get_character_by_player_token(player_token: str):
    """Get character by player token (for player view)."""
    character = game_session.get_character_by_token(player_token)
    if not character:
        return jsonify({"error": "Character not found"}), 404
    return jsonify(character)
