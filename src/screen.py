"""
    Screen Class
"""

import pygame
from pygame.math import Vector2
from pygame.surface import Surface

from game_constants import WORLD_CONSTRAINTS


class Screen(Surface):
    """class docstring"""

    def __init__(self, resolution, screen_type):
        super().__init__(resolution)
        self.screen_type = screen_type
        WORLD_CONSTRAINTS[screen_type] = Vector2(resolution)

    def handle_input(self, evt):
        """mehod docstring"""

    def update(self):
        """mehod docstring"""

    def draw(self, display):
        """mehod docstring"""
        display.blit(self, (0, 0))


class HighScoresScreen(Screen):
    """class docstring"""

    def __init__(self, resolution):
        super().__init__(resolution, "highscores")
        self.fill("green")

    def draw(self, display):
        rect = pygame.Rect((900, 100), (250, 75))
        pygame.draw.ellipse(self, (119, 217, 98), rect)
        super().draw(display)


class SelectScreen(Screen):
    """class docstring"""

    def __init__(self, resolution):
        super().__init__(resolution, "select")
        self.fill("blue")

    def draw(self, display):
        pygame.draw.circle(self, (217, 98, 119), (200, 200), 50)
        super().draw(display)
