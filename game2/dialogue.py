import pygame
from utils import draw_text
import time

# Load Font
pygame.font.init()
FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Displays a dialogue box with character name and choices
def display_dialogue(screen, character, dialogue, choices=None):
    screen.fill(BLACK) # Clear the screen

    # Draw dialogue box
    pygame.draw.rect(screen, GRAY, (50, 400, 700, 150), border_radius=10)
    pygame.draw.rect(screen, WHITE, (50, 400, 700, 150), 3, border_radius=10)

    # Draw character name
    if character:
        pygame.draw.rect(screen, BLACK, (55, 370, 150, 30))
        draw_text(screen, FONT, character, 0.07, 0.63, WHITE)

    # Draw dialogue
    draw_text(screen, FONT, dialogue, 0.10, 0.75, WHITE)

    # Draw choices if available
    if choices:
        for i, choice in enumerate(choices):
            pygame.draw.rect(screen, WHITE, (100, 450 + (i * 40), 600, 30), border_radius=5)
            draw_text(screen, FONT, f"{i+1}. {choice}", 0.15, 0.78 + (i * 0.07), BLACK)

    pygame.display.flip()
    time.sleep(0.2)

# Waits for player's choice input
def get_choice():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 0
                elif event.key == pygame.K_2:
                    return 1