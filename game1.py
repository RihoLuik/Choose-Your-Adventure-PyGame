import pygame
import importlib
import os
import settings

# Initialize Pygame
pygame.init()

screen, game_settings = settings.apply_settings()

pygame.display.set_caption("Game 1")

# Automatically get all chapter files in game1Chapters
chapter_files = [f[:-3] for f in os.listdir("game1Chapters") if f.endswith(".py")]

def start_game():
    for chapter in sorted(chapter_files): # Ensure correct order
        module = importlib.import_module(f"game1Chapters.{chapter}") # Load chapter dynamically
        module.run_chapter(screen) # Run the chapter

    pygame.quit()

start_game()