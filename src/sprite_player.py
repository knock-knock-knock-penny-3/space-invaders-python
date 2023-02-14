"""
"""

from pygame.constants import KEYDOWN, KEYUP, K_LEFT, K_RIGHT
from pygame.math import Vector2
from pygame.sprite import Sprite

from game_constants import STARSHIP_COLOR, WORLD_CONSTRAINTS
from game_utils import draw_sprite

class SpritePlayer(Sprite):
    DIR_LEFT = -1
    DIR_RIGHT = 1
    DIR_STOP = 0

    def __init__(self):
        super().__init__()
        self.color = STARSHIP_COLOR
        self.constraints = WORLD_CONSTRAINTS['game']
        self.dir = self.DIR_STOP
        self.pos = Vector2(self.constraints.x // 2, self.constraints.y - 100)
        self.ship_schema = [
            '      X      ',
            '     XXX     ',
            '     XXX     ',
            ' XXXXXXXXXXX ',
            'XXXXXXXXXXXXX',
            'XXXXXXXXXXXXX',
            'XXXXXXXXXXXXX'
        ]
        self.speed = 10

        self.image = draw_sprite(self.ship_schema, self.color)
        self.rect = self.image.get_rect(center = self.pos)

    def handle_input(self, evt):
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                self.dir = self.DIR_LEFT
            elif evt.key == K_RIGHT:
                self.dir = self.DIR_RIGHT
        elif evt.type == KEYUP:
            self.dir = self.DIR_STOP

    def update(self):
        self.pos.x += self.speed * self.dir

        if self.pos.x <= self.rect.width // 2:
            self.pos.x = self.rect.width // 2
        elif self.pos.x >= self.constraints.x - self.rect.width // 2:
            self.pos.x = self.constraints.x - self.rect.width // 2

        self.rect.center = self.pos
