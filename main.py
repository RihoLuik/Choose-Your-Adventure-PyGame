import pygame
import subprocess
import settings # Import settings handler

# Initialize PyGame
pygame.init()

# Load settings
screen, game_settings = settings.apply_settings()

# Function to create a window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Colors & Font
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 40) # Default font, size 40

# Function to display text
ORIGINAL_WIDTH, ORIGINAL_HEIGHT = 800, 600

def draw_text(text, x, y, color=WHITE):
    scale_x = screen.get_width() / ORIGINAL_WIDTH
    scale_y = screen.get_height() / ORIGINAL_HEIGHT
    render = font.render(text, True, color)
    screen.blit(render, (int(x * scale_x), int(y * scale_y)))

def start_game(file_name):
    pygame.quit() # Close the menu window
    subprocess.run(["python", file_name]) # Run the selected game
    exit() # Exit after the game closes

# Function for the game selection menu
def select_game():
    game_selecting = True
    while game_selecting:
        screen.fill(BLACK)
        draw_text("Select Game:", 300, 150)
        draw_text("1. Game1", 300, 200)
        draw_text("2. Game2", 300, 250)
        draw_text("3. Back to Menu", 300, 300)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_game("game1.py")
                elif event.key == pygame.K_2:
                    start_game("game2.py")
                elif event.key == pygame.K_3:
                    game_selecting = False # Return to the main menu

# Settings menu loop
def settings_menu():
    global screen, game_settings

    options = ["1. Change Resolution", "2. Toggle Fullscreen", "3. Adjust Volume", "4. Back"]
    running = True

    while running:
        screen.fill(BLACK)
        draw_text("Settings Menu", 300, 150)
        draw_text("1. Change Resolution", 300, 200)
        draw_text("2. Toggle Fullscreen", 300, 250)
        draw_text("3. Adjust Volume", 300, 300)
        draw_text("4. Back", 300, 400)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    change_resolution()
                elif event.key == pygame.K_2:
                    toggle_fullscreen()
                elif event.key == pygame.K_3:
                    adjust_volume()
                elif event.key == pygame.K_4:
                    running = False # Go back to menu

# Change screen resolution
def change_resolution():
    global screen, game_settings

    resolutions = [(800, 600), (1280, 720), (1920, 1080)]
    current_res = game_settings["resolution"]
    index = resolutions.index(tuple(current_res))
    index = (index + 1) % len(resolutions) # Cycle through options

    game_settings["resolution"] = list(resolutions[index])
    settings.save_settings(game_settings)
    screen, game_settings = settings.apply_settings() # Reapply settings

# Toggle between fullscreen modes
def toggle_fullscreen():
    global screen, game_settings

    modes = ["windowed", "fullscreen", "borderless"]
    index = modes.index(game_settings["fullscreen"])
    index = (index + 1) % len(modes)

    game_settings["fullscreen"] = modes[index]
    settings.save_settings(game_settings)
    screen, game_settings = settings.apply_settings()

# Increase/decrease volume
def adjust_volume():
    global game_settings

    game_settings["volume"] += 0.1
    if game_settings["volume"] > 1.0:
        game_settings["volume"] = 0.0 # Reset volume if it exceeds max

    pygame.mixer.music.set_volume(game_settings["volume"]) # Apply volume
    settings.save_settings(game_settings)

# Main menu loop
running = True
while running:
    screen.fill(BLACK)
    draw_text("Main Menu", 300, 150)
    draw_text("1. Select Game", 300, 200)
    draw_text("2. Settings", 300, 250)
    draw_text("3. Quit", 300, 300)
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                select_game()
            elif event.key == pygame.K_2:
                settings_menu()
            elif event.key == pygame.K_3:
                running = False

pygame.quit()