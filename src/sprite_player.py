"""
"""

from pygame import draw, Rect, SRCALPHA
from pygame.constants import KEYDOWN, K_LEFT, K_RIGHT
from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface

from game_constants import STARSHIP_COLOR, WORLD_CONSTRAINTS

class SpritePlayer(Sprite):
    DIR_LEFT = -1
    DIR_RIGHT = 1
    DIR_STOP = 0

    def __init__(self):
        super().__init__()
        self.color = STARSHIP_COLOR
        self.constraints = WORLD_CONSTRAINTS['game']
        self.dir = self.DIR_STOP
        self.pixel = Vector2(4, 4)
        self.pos = Vector2(self.constraints.x // 2, self.constraints.y - 100)
        self.schema = [
            '      X      ',
            '     XXX     ',
            '     XXX     ',
            ' XXXXXXXXXXX ',
            'XXXXXXXXXXXXX',
            'XXXXXXXXXXXXX',
            'XXXXXXXXXXXXX'
        ]
        self.speed = 10

        self.image = self._draw_ship()
        self.rect = self.image.get_rect(center = self.pos)

    def _draw_ship(self):
        width = max([len(row) for row in self.schema])
        height = len(self.schema)
        ship = Surface((width * self.pixel.x, height * self.pixel.y), SRCALPHA)

        for idx_row, row in enumerate(self.schema):
            for idx_char, char in enumerate(row):
                if char != ' ':
                    coords = Vector2(idx_char * self.pixel.x, idx_row * self.pixel.y)
                    rect = Rect(coords, self.pixel)
                    draw.rect(ship, self.color, rect)

        return ship

    def handle_input(self, evt):
        if evt.type == KEYDOWN:
            if evt.key == K_LEFT:
                self.dir = self.DIR_LEFT
            elif evt.key == K_RIGHT:
                self.dir = self.DIR_RIGHT

    def update(self):
        self.pos.x += self.speed * self.dir

        if self.pos.x <= self.rect.width // 2:
            self.pos.x = self.rect.width // 2
        elif self.pos.x >= self.constraints.x - self.rect.width // 2:
            self.pos.x = self.constraints.x - self.rect.width // 2

        self.rect.center = self.pos
