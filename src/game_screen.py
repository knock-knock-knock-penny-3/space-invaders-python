"""

"""

from pygame.constants import MOUSEBUTTONDOWN
from pygame.sprite import GroupSingle
from pygame.time import get_ticks
from screen import Screen

from game_constants import MAIN_BG_COLOR, START_STARSHIPS
from game_utils import load_sound
from sprite_player import SpritePlayer

class GameScreen(Screen):
    """class docstring"""

    def __init__(self, resolution):
        super().__init__(resolution, 'game')
        self.aliens_heartbeat_sounds = [load_sound(f'beat_{n}.wav') for n in range(4)]
        [sound.set_volume(.1) for sound in self.aliens_heartbeat_sounds]
        self.current_aliens_heartbeat = 0
        self.starships = START_STARSHIPS
        self.starship_grp = GroupSingle(SpritePlayer())

        self.gap = 100
        self.tick = None
        self.aliens = 40

    def handle_input(self, evt):
        super().handle_input(evt)

        if evt.type == MOUSEBUTTONDOWN:
            self.aliens -= 1

        self.starship_grp.sprite.handle_input(evt)

    def update(self):
        super().update()

        current_tick = get_ticks()
        if self.tick is None or current_tick >= self.tick + self.gap + (self.aliens * 25):
            self._aliens_heartbeat()
            print(current_tick)
            self.tick = current_tick


        self.starship_grp.sprite.update()

    def draw(self, display):
        super().draw(display)
        self.fill(MAIN_BG_COLOR)

        self.starship_grp.draw(self)

    def _aliens_heartbeat(self):
        self.aliens_heartbeat_sounds[self.current_aliens_heartbeat].play()
        self.current_aliens_heartbeat = (self.current_aliens_heartbeat + 1) % len(self.aliens_heartbeat_sounds)
