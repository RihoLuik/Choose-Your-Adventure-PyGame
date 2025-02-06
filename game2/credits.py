import pygame
from utils import draw_text

# Displays the credits screen for Game1
def show_credits(screen):
    screen.fill((0, 0, 0)) # Black background
    font = pygame.font.Font(None, 40)

    credits_text = [
        "Game2 Credits",
        "",
        "Developer: NiteleeVA",
        "Artist: NiteleeVA",
        "Writer: NiteleeVA",
        "",
        "Press ENTER to return..."
    ]

    for i, line in enumerate(credits_text):
        draw_text(screen, font, line, 0.30, 0.20 + (i * 0.05))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False