"""
    Game Engine Class
"""

import sys
import pygame
from pygame import display, event, time
from pygame.constants import FULLSCREEN, KEYDOWN, K_ESCAPE, K_1, K_2, K_3, QUIT

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

            if evt.type == KEYDOWN:
                if evt.key == K_1:
                    self.screen_manager.switch_screen("game")
                elif evt.key == K_2:
                    self.screen_manager.switch_screen("highscores")
                elif evt.key == K_3:
                    self.screen_manager.switch_screen("select")

    def update(self):
        """update"""
        self.screen_manager.update()

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
