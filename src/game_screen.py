"""

"""

from pygame.sprite import GroupSingle
from screen import Screen

from game_constants import MAIN_BG_COLOR, START_STARSHIPS
from sprite_player import SpritePlayer

class GameScreen(Screen):
    """class docstring"""

    def __init__(self, resolution):
        super().__init__(resolution, 'game')
        self.starships = START_STARSHIPS
        self.starship_grp = GroupSingle(SpritePlayer())

    def handle_input(self, evt):
        super().handle_input(evt)
        self.starship_grp.sprite.handle_input(evt)

    def update(self):
        super().update()
        self.starship_grp.sprite.update()

    def draw(self, display):
        super().draw(display)
        self.fill(MAIN_BG_COLOR)

        self.starship_grp.draw(self)
