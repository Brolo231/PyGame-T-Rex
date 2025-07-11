import random

import pygame


def draw_text(surface, text, font_size, color, position, center=True, font_name=None):
    """
    Draws text onto the given surface.

    Args:
        surface (pygame.Surface): The surface to draw on (e.g. screen).
        text (str): The text string to display.
        font_size (int): Font size.
        color (tuple): RGB color (e.g., (255, 255, 255)).
        position (tuple): (x, y) coordinates.
        center (bool): If True, text will be centered on position. Otherwise, topleft.
        font_name (str or None): Optional font path or name.
    """
    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()

    if center:
        text_rect.center = position
    else:
        text_rect.topleft = position

    surface.blit(text_surface, text_rect)


