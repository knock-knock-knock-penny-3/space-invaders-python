"""
    Game Engine Class
"""

import sys
import pygame
from pygame import display, event, time
from pygame.constants import FULLSCREEN, KEYDOWN, K_ESCAPE, QUIT

from screen_manager import ScreenManager


class GameEngine:
    """class docstring"""

    MAIN_BG_COLOR = (30, 30, 30)  # #1E1E1E

    def __init__(self):
        pygame.init()
        display_info = display.Info()
        resolution = (display_info.current_w, display_info.current_h)
        self.display = display.set_mode(resolution, FULLSCREEN)
        self.screen_manager = ScreenManager(resolution)
        self.clock = time.Clock()

    def run(self):
        """Game Engine run"""
        while True:
            self.clock.tick(60)

            self.handle_input()
            self.update()
            self.draw()

    def handle_input(self):
        """handle input"""
        for evt in event.get():
            if evt.type == QUIT:
                self.exit()
            elif evt.type == KEYDOWN and evt.key == K_ESCAPE:
                self.exit()

    def update(self):
        """update"""

    def draw(self):
        """draw"""
        self.display.fill(self.MAIN_BG_COLOR)
        self.screen_manager.draw(self.display)
        display.flip()

    def exit(self):
        """exit"""
        # to be replaced with a function that does things before closing: saves, checks, etc
        self.void()
        pygame.quit()
        sys.exit()

    def void(self):
        """ "
        void
        to be replaced with a function that does things before closing: saves, checks, etc
        """
