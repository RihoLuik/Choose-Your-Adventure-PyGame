import pygame
import time

# Initialize PyGame
pygame.init()

# Function to create a window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Font setup
font = pygame.font.Font(None, 40)  # Default font, size 40


# Function to display text
def draw_text(text, x, y, color=WHITE):
    render = font.render(text, True, color)
    screen.blit(render, (x, y))


def show_credits():
    screen.fill(BLACK)
    credits = [
        "Credits:",
        "",
        "Main Developer(s):",
        "NiteleeVA: Director, Coder, Artist, Writer & Musician",
        "Template: will get used when new dev joins or smth lol",
        "",
        "Press ENTER to return to the menu..."
    ]

    y_offset = 100
    typed_lines = []  # Stores completed lines

    for line in credits:
        typed_line = ""  # Store current line being typed
        for i in range(len(line) + 1):
            screen.fill(BLACK)  # Keep background black

            # Check for exit event while typing
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Draw all previous lines
            for j, prev_line in enumerate(typed_lines):
                draw_text(prev_line, 50, 100 + (j * 50))

            # Draw the current line being typed
            typed_line = line[:i]
            draw_text(typed_line, 50, y_offset)

            pygame.display.flip()
            time.sleep(0.05)  # Typing speed

        typed_lines.append(typed_line)
        y_offset += 50

    pygame.display.flip()

    # Wait for ENTER key to return to menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False


# Function to create a game window
def create_window(title, color):
    screen.fill(color)  # Change background color
    draw_text(title, 300, 250)
    draw_text("Press ENTER to return...", 250, 300)
    pygame.display.flip()

    # Wait for ENTER to return to the menu
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False


# Main menu loop
running = True
while running:
    screen.fill(BLACK)
    draw_text("Main Menu:", 300, 150)
    draw_text("1. Select Game", 300, 200)
    draw_text("2. Settings", 300, 250)
    draw_text("3. Credits", 300, 300)
    draw_text("4. Quit", 300, 350)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  # Select Game
                screen.fill(BLACK)
                draw_text("What would you like to play?", 250, 200)
                draw_text("1. Game1", 250, 250)
                draw_text("2. Game2", 250, 300)
                pygame.display.flip()

                game_selected = False
                while not game_selected:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                create_window("Game1", BLUE)
                                game_selected = True
                            elif event.key == pygame.K_2:
                                create_window("Game2", RED)
                                game_selected = True

            elif event.key == pygame.K_3:
                show_credits()

            elif event.key == pygame.K_4:
                running = False

pygame.quit()