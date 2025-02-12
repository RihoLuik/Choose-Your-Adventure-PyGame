import pygame
import time

def run_chapter(screen):
    font = pygame.font.Font(None, 40)
    screen.fill((0,0,0)) # Black background

    print("Starting Neutral Chapter 2...")

    text = font.render("Chapter 2: New Discovery...", True, (255,255,255))
    screen.blit(text, (250, 250))
    pygame.display.flip()

    time.sleep(3)
    pygame.quit()