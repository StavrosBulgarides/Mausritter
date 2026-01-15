"""
Player view routes.
"""

from flask import Blueprint, render_template, Response
from ..session import game_session
from ...templates.html_template import generate_character_sheet_html

player_bp = Blueprint("player", __name__)


@player_bp.route("/join")
def join():
    """Player join page - select character."""
    characters = game_session.get_all_characters()
    # Only expose names and player tokens for selection
    char_list = [
        {"name": char["name"], "token": char["player_token"]}
        for char in characters.values()
    ]
    return render_template("join.html", characters=char_list)


@player_bp.route("/player/<player_token>")
def player_view(player_token: str):
    """Player character sheet view - uses full character sheet with server connectivity."""
    character = game_session.get_character_by_token(player_token)
    if not character:
        return render_template("not_found.html"), 404

    # Generate the full character sheet HTML with server connectivity
    html = generate_character_sheet_html(character, server_mode=True, token=player_token)
    return Response(html, mimetype='text/html')
