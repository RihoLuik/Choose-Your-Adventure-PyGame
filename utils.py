import pygame

# Original resolution
ORIGINAL_WIDTH, ORIGINAL_HEIGHT = 800, 600

# Draws text at a position scaled based on resolution
def draw_text(screen, font, text, x_ratio, y_ratio, color=(255, 255, 255)):
    x = int(x_ratio * screen.get_width())
    y = int(y_ratio * screen.get_height())
    render = font.render(text, True, color)
    screen.blit(render, (x, y))

# Scales position dynamically based on current resolution
def scale_position(screen, x, y):
    scale_x = screen.get_width() / ORIGINAL_WIDTH
    scale_y = screen.get_height() / ORIGINAL_HEIGHT
    return int(x * scale_x), int(y * scale_y)