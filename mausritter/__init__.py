"""
Mausritter Character Generator Package
Generates characters for the Mausritter tabletop RPG
"""

from .generator import generate_character
from .templates.html_template import create_html_character_sheet
from .browser import open_in_browser

__all__ = ['generate_character', 'create_html_character_sheet', 'open_in_browser']
