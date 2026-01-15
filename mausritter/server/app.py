"""
Flask application factory for Mausritter GM server.
"""

from flask import Flask
from pathlib import Path


def create_app() -> Flask:
    """Create and configure the Flask application."""
    app = Flask(
        __name__,
        template_folder=str(Path(__file__).parent / "templates"),
        static_folder=str(Path(__file__).parent / "static"),
    )

    # Configuration
    app.config["SECRET_KEY"] = "mausritter-local-dev"  # Only for local LAN use
    app.config["JSON_SORT_KEYS"] = False

    # Register blueprints
    from .routes.api import api_bp
    from .routes.gm import gm_bp
    from .routes.player import player_bp

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(gm_bp, url_prefix="/gm")
    app.register_blueprint(player_bp)

    # Root route
    @app.route("/")
    def index():
        from flask import render_template
        from .session import game_session
        return render_template("index.html", gm_token=game_session.gm_token)

    return app
