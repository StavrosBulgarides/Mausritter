"""
GM dashboard routes.
"""

from flask import Blueprint, render_template, request, Response
from ..session import game_session
from ...templates.html_template import generate_character_sheet_html

gm_bp = Blueprint("gm", __name__)


@gm_bp.route("/")
def dashboard():
    """GM dashboard - view and manage all characters."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return render_template("unauthorized.html"), 401

    characters = game_session.get_all_characters()
    session_state = game_session.get_state()

    return render_template(
        "gm.html",
        token=token,
        characters=characters,
        session_name=session_state.get("session_name", "New Session"),
        gm_notes=session_state.get("gm_notes", ""),
    )


@gm_bp.route("/character/<char_id>")
def view_character(char_id: str):
    """View/edit a specific character as GM - uses full character sheet."""
    token = request.args.get("token", "")
    if not game_session.verify_gm(token):
        return render_template("unauthorized.html"), 401

    character = game_session.get_character(char_id)
    if not character:
        return render_template("not_found.html"), 404

    # Generate full character sheet HTML with server connectivity
    # GM uses their token for API auth
    html = generate_character_sheet_html(character, server_mode=True, token=token)

    # Add a back button to the GM dashboard
    back_button = f'''
    <div style="position:fixed;top:10px;left:10px;z-index:9999;">
        <a href="/gm/?token={token}" style="background:#4a4a5a;color:white;padding:10px 20px;border-radius:8px;text-decoration:none;font-weight:bold;">
            &larr; Back to Dashboard
        </a>
    </div>
    '''
    html = html.replace('<body>', '<body>' + back_button)

    return Response(html, mimetype='text/html')
