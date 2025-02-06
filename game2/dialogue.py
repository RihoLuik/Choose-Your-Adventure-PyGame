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
    clock = pygame.time.Clock()
    text_speed = 30 # Adjust this for speed (lower = faster)

    # Draw dialogue box
    pygame.draw.rect(screen, GRAY, (50, 400, 700, 150), border_radius=10)
    pygame.draw.rect(screen, WHITE, (50, 400, 700, 150), 3, border_radius=10)

    # Draw character name
    if character:
        pygame.draw.rect(screen, BLACK, (55, 370, 150, 30))
        draw_text(screen, FONT, character, 0.07, 0.63, WHITE)

    displayed_text = "" # Holds the text as it's being typed

    for i in range(len(dialogue)):
        displayed_text = dialogue[:i + 1] # Add one letter at a time

        screen.fill(BLACK)
        pygame.draw.rect(screen, GRAY, (50, 400, 700, 150), border_radius=10)
        pygame.draw.rect(screen, WHITE, (50, 400, 700, 150), 3, border_radius=10)

        # Draw name again
        if character:
            pygame.draw.rect(screen, BLACK, (55, 370, 150, 30))
            draw_text(screen, FONT, character, 0.07, 0.63, WHITE)

        # Draw the incrementally appearing dialogue
        draw_text(screen, FONT, displayed_text, 0.10, 0.75, WHITE)

        pygame.display.flip()
        clock.tick(text_speed) # Control text speed

    wait_for_keypress()

    # Draw choices if available
    if choices:
        for i, choice in enumerate(choices):
            pygame.draw.rect(screen, WHITE, (100, 450 + (i * 40), 600, 30), border_radius=5)
            draw_text(screen, FONT, f"{i + 1}. {choice}", 0.15, 0.78 + (i * 0.07), BLACK)

        pygame.display.flip()

# Waits for a key press before continuing
# Prevents skipping through text too quickly
def wait_for_keypress():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

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