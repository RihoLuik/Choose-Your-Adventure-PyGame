import pygame
import sys
import importlib
import json
from settings import settings_menu
from credits import show_credits
from utils import draw_text
from game2.chapters import chapter1

SAVE_FILE = "game2/save.json" # Adjust if necessary

# Initialize Pygame
pygame.init()

# Load settings
settings = {"resolution": (800, 600), "fullscreen": False} # Replace with actual settings loading
WIDTH, HEIGHT = settings["resolution"]
FLAGS = pygame.FULLSCREEN if settings.get("fullscreen", False) else 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS)
pygame.display.set_caption("Game2")

# Font setup
font = pygame.font.Font(None, 40)

# Load saved progress from save.json
def load_saved_progress():
    try:
        with open(SAVE_FILE, "r") as file:
            save_data = json.load(file)
            return save_data.get("current_chapter", "chapter1") # Default to Chapter 1 if no save exists
    except (FileNotFoundError, json.JSONDecodeError):
        return "chapter1" # Default if no save file is found

# Starts Chapter 1 inside the same window
def start_game():
    next_chapter = chapter1.run_chapter(screen) # Runs Chapter 1
    load_chapter(next_chapter)

# Dynamically load and run the next chapter
def load_chapter(chapter_name):
    chapter_module = importlib.import_module(f"game2.chapters.{chapter_name}")
    chapter_module.run_chapter(screen)

# Save progress to save.json
def save_progress(chapter_name):
    save_data = {"current_chapter": chapter_name}
    with open(SAVE_FILE, "w") as file:
        json.dump(save_data, file, indent=4)

# Game2 menu loop
running = True
while running:
    screen.fill((0, 0, 0))
    draw_text(screen, font, "Game2", 0.375, 0.20)
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
                # Load saved progress from save.json and continue
                saved_chapter = load_saved_progress()
                load_chapter(saved_chapter)
            elif event.key == pygame.K_2:
                start_game() # Starts a new game (Chapter 1
            elif event.key == pygame.K_3:
                settings_menu(screen) # Calls settings menu
            elif event.key == pygame.K_4:
                show_credits(screen) # Calls credits screen
            elif event.key == pygame.K_5:
                running = False

pygame.quit()