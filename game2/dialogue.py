import pygame
from game2.choices import draw_choices
from main import WIDTH
from utils import draw_text

# Load Font
pygame.font.init()
FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)

# Wrap text to fit within a given width
def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""

    for word in words:
        # Check the width of the current line with the new word
        test_line = f"{current_line} {word}" if current_line else word
        test_width, _ = font.size(test_line)

        if test_width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    # Append the last line
    if current_line:
        lines.append(current_line)

    return lines


# Displays a dialogue box with character name and choices
def display_dialogue(screen, character, dialogue, choices=None):
    clock = pygame.time.Clock()
    text_speed = 30  # Adjust this for speed (lower = faster)

    # Draw dialogue box
    pygame.draw.rect(screen, GRAY, (50, 400, 700, 150), border_radius=10)
    pygame.draw.rect(screen, WHITE, (50, 400, 700, 150), 3, border_radius=10)

    # Draw character name
    if character:
        pygame.draw.rect(screen, BLACK, (55, 370, 150, 30))
        draw_text(screen, FONT, character, 0.07, 0.63, WHITE)

    # Wrap the dialogue text into lines
    max_width = 700 - 40  # Max width for the wrapped text (subtracting some padding)
    wrapped_text = wrap_text(dialogue, FONT, max_width)

    displayed_text = [""] * len(wrapped_text)  # Initialize empty lines
    total_displayed_lines = 0  # To keep track of lines being typed

    # Display text letter by letter
    for line_index in range(len(wrapped_text)):
        line = wrapped_text[line_index]

        for i in range(len(line)):
            displayed_text[line_index] = line[:i + 1]  # Add one letter at a time to the current line

            # Redraw the entire screen content
            screen.fill(BLACK)  # Clear the screen
            pygame.draw.rect(screen, GRAY, (50, 400, 700, 150), border_radius=10)
            pygame.draw.rect(screen, WHITE, (50, 400, 700, 150), 3, border_radius=10)

            # Draw name again
            if character:
                pygame.draw.rect(screen, BLACK, (55, 370, 150, 30))
                draw_text(screen, FONT, character, 0.07, 0.63, WHITE)

            # Draw all the lines progressively
            y_offset = 0.75
            for j in range(total_displayed_lines + 1):  # Display all lines typed so far
                draw_text(screen, FONT, displayed_text[j], 0.10, y_offset + (j * 0.07), WHITE)

            pygame.display.flip()
            clock.tick(text_speed)  # Control text speed

        total_displayed_lines += 1  # After finishing a line, mark it as fully typed

    # Get the bottom of the dialogue box to place choices below it
    dialogue_box_bottom = 400 + (total_displayed_lines * FONT.get_height()) + 20

    wait_for_keypress()

    # Draw choices below the dialogue
    if choices:
        draw_choices(screen, choices, FONT, WIDTH, dialogue_box_bottom)

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