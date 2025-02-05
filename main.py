import pygame
import sys
import subprocess
from settings import settings_menu
from utils import draw_text

# Initialize PyGame
pygame.init()

# Default resolution (can be changed in settings)
# Function to create the game window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Font
font = pygame.font.Font(None, 40) # Default font, size 40

# Starts the selected game (Game1 or Game2)
def start_game(game_name):
    pygame.quit() # Close the launcher before launching the game
    subprocess.run(["python", f"{game_name}/game.py"])
    sys.exit()

# Main menu loop
def main_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, font, "Main Menu", 0.375, 0.20)
        draw_text(screen, font, "1. Select Game", 0.375, 0.30)
        draw_text(screen, font, "2. Settings", 0.375, 0.40)
        draw_text(screen, font, "3. Quit", 0.375, 0.50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    select_game_menu()
                elif event.key == pygame.K_2:
                    settings_menu(screen)
                elif event.key == pygame.K_3:
                    running = False
    pygame.quit()

# Game selection menu
def select_game_menu():
    selecting = True
    while selecting:
        screen.fill((0, 0, 0))
        draw_text(screen, font, "Select a Game", 0.375, 0.20)
        draw_text(screen, font, "1. Game1", 0.375, 0.30)
        draw_text(screen, font, "2. Game2", 0.375, 0.40)
        draw_text(screen, font, "3. Back", 0.375, 0.50)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    start_game("game1")
                elif event.key == pygame.K_2:
                    start_game("game2")
                elif event.key == pygame.K_3:
                    selecting = False

if __name__ == "__main__":
    main_menu()