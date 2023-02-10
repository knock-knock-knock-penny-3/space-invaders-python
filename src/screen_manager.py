"""
    Screen Manager Class
"""

from screen import GameScreen, HighScoresScreen, SelectScreen


class ScreenManager:
    """class docstring"""

    def __init__(self, resolution):
        self.current_screen = "highscores"
        self.screens = {
            "select": SelectScreen(resolution),
            "game": GameScreen(resolution),
            "highscores": HighScoresScreen(resolution),
        }

    def handle_input(self):
        """method docstring"""
        self.screens[self.current_screen].handle_input()

    def update(self):
        """method docstring"""
        self.screens[self.current_screen].update()

    def draw(self, display):
        """method docstring"""
        self.screens[self.current_screen].draw(display)
