import pygame
import json
from utils import draw_text

SETTINGS_FILE = 'settings.json'

# Load or create default settings
def load_settings():
    try:
        with open(SETTINGS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        default_settings = {
            "resolution": (800, 600),  # Default resolution
            "fullscreen": False,  # Windowed by default
            "volume": 50  # Volume as a percentage (0-100)
        }
        save_settings(default_settings)
        return default_settings

# Saves settings to a file
def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)

# Apply settings and update the display
def apply_settings():
    settings = load_settings()
    resolution = tuple(settings["resolution"])
    fullscreen = settings["fullscreen"]

    # Set fullscreen or windowed mode
    flags = pygame.FULLSCREEN if fullscreen else pygame.RESIZABLE
    screen = pygame.display.set_mode(resolution, flags)

    # Apply volume
    pygame.mixer.music.set_volume(settings["volume"] / 100) # Convert to range 0.0 - 1.0

    return screen, settings # Return updated screen and settings

# Displays the settings menu
def settings_menu(screen):
    settings = load_settings()
    font = pygame.font.Font(None, 40)
    running = True

    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, font, "Settings", 0.375, 0.20)
        draw_text(screen, font, f"1. Toggle Fullscreen: {'On' if settings['fullscreen'] else 'Off'}", 0.375, 0.30)
        draw_text(screen, font, f"2. Change Resolution: {settings['resolution'][0]}x{settings['resolution'][1]}", 0.375, 0.40)
        draw_text(screen, font, f"3. Adjust Volume: {settings['volume']}%", 0.375, 0.50)
        draw_text(screen, font, "4. Back", 0.375, 0.60)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    settings["fullscreen"] = not settings["fullscreen"]
                elif event.key == pygame.K_2:
                    settings["resolution"] = [1280, 720] if settings["resolution"] == [800, 600] else [800, 600]
                elif event.key == pygame.K_3:
                    settings["volume"] = max(0, min(100, settings["volume"] + 10)) # Ensure within 0-100
                elif event.key == pygame.K_4:
                    running = False

                save_settings(settings)
                screen, settings = apply_settings() # Apply settings immediately

    return screen # Return updated screen