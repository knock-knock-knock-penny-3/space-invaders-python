"""
    Screen Manager Class
"""

from screen import HighScoresScreen, SelectScreen
from game_screen import GameScreen


class ScreenManager:
    """class docstring"""

    def __init__(self, resolution):
        self.current_screen = "game"
        self.screens = {
            "select": SelectScreen(resolution),
            "game": GameScreen(resolution),
            "highscores": HighScoresScreen(resolution),
        }

    def handle_input(self, evt):
        """method docstring"""
        self.screens[self.current_screen].handle_input(evt)

    def update(self):
        """method docstring"""
        self.screens[self.current_screen].update()

    def draw(self, display):
        """method docstring"""
        self.screens[self.current_screen].draw(display)

    def switch_screen(self, screen_type):
        """method docstring"""
        if screen_type in self.screens:
            self.current_screen = screen_type
