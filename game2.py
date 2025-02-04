import pygame
import importlib
import settings

pygame.init()

screen, game_settings = settings.apply_settings()

pygame.display.set_caption("Game 2")

# List of chapter for Game 2
chapters = ["chapter1", "chapter2"]

def start_game():
    for chapter in chapters:
        module = importlib.import_module(f"game2Chapters.{chapter}") # Load dynamically
        module.run_chapter(screen) # Run the chapter

    pygame.quit()

start_game()