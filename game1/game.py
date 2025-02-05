import pygame
import subprocess
import sys
from settings import settings_menu, apply_settings
from credits import show_credits
from utils import draw_text

# Initialize Pygame
pygame.init()

# Apply settings and create the screen
screen, settings = apply_settings()
pygame.display.set_caption("Game 1")

# Font setup
font = pygame.font.Font(None, 40)

# Starts the game from Chapter 1
def start_game():
    subprocess.run(["python", "game1/chapters/chapter1.py"])
    sys.exit()

# Loads a saved game
def load_game():
    subprocess.run(["python", "game1/save.py"])
    sys.exit()

# Game1 menu loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_text(screen, font, "Game1 Menu", 0.375, 0.20)
    draw_text(screen, font, "1. Continue", 0.375, 0.30)
    draw_text(screen, font, "2. New Game", 0.375, 0.40)
    draw_text(screen, font, "3. Settings", 0.375, 0.50)
    draw_text(screen, font, "4. Credits", 0.375, 0.60)
    draw_text(screen, font, "5. Quit", 0.375, 0.70)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                load_game() # Continue game from save
            elif event.key == pygame.K_2:
                start_game() # Start from Chapter 1
            elif event.key == pygame.K_3:
                settings_menu(screen) # Calls settings menu
            elif event.key == pygame.K_4:
                show_credits(screen) # Calls credits screen
            elif event.key == pygame.K_5:
                running = False

pygame.quit()