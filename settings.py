import json
import pygame
import os

# Default settings
DEFAULT_SETTINGS = {
    "resolution": [800, 600], # Default Resolution
    "fullscreen": "windowed", # Options "windowed", "fullscreen", "borderless"
    "volume": 0.5 # Default volume (50%)
}

SETTINGS_FILE = "settings.json"

def load_settings():
    """Load settings from a file or create default settings."""
    if not os.path.exists(SETTINGS_FILE):
        save_settings(DEFAULT_SETTINGS)
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    """Save settings to a file."""
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def apply_settings():
    """Apply loaded settings to the game."""
    settings = load_settings()

    # Set screen mode
    if settings["fullscreen"] == "fullscreen":
        screen = pygame.display.set_mode(settings["resolution"], pygame.FULLSCREEN)
    elif settings["fullscreen"] == "borderless":
        screen = pygame.display.set_mode(settings["resolution"], pygame.NOFRAME)
    else:
        screen = pygame.display.set_mode(settings["resolution"]) # Windowed

    return screen, settings