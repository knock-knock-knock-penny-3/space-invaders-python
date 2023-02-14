"""
"""

from pygame import draw, Rect, SRCALPHA
from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface

from game_constants import WORLD_CONSTRAINTS
from game_utils import draw_sprite

class SpriteAlien(Sprite):
    def __init__(self, pos, color, type):
        super().__init__()
        self.color = color
        self.constraints = WORLD_CONSTRAINTS['game']
        self.explosion_schema = [
            '    X   X    ',
            ' X   X X   X ',
            '  X       X  ',
            '   X     X   ',
            'XX         XX',
            '   X     X   ',
            '  X  X X  X  ',
            ' X  X   X  X '
        ]
        self.pos = pos
        self.speed = 10
        self.type = type

        self.images = [draw_sprite(schema, self.color) for schema in self.alien_schemas]
        self.image = self.images[0]
        self.rect = self.image.get_rect(center = self.pos)


class SpriteAlienCrab(SpriteAlien):
    def __init__(self, pos, color):
        self.alien_schema = [
            [
                '  X     X  ',
                '   X   X   ',
                '  XXXXXXX  ',
                ' XX XXX XX ',
                'XXXXXXXXXXX',
                'X XXXXXXX X',
                'X X     X X',
                '   XX XX   '
            ],
            [
                '  X     X  ',
                'X  X   X  X',
                'X XXXXXXX X',
                'XXX XXX XXX',
                'XXXXXXXXXXX',
                ' XXXXXXXXX ',
                '  X     X  ',
                ' X       X '
            ]
        ]
        super().__init__(pos, color, 'crab')


class SpriteAlienMartian(SpriteAlien):
    def __init__(self, pos, color):
        self.alien_schema = [
            [
                '    XXXX    ',
                ' XXXXXXXXXX ',
                'XXXXXXXXXXXX',
                'XXX  XX  XXX',
                'XXXXXXXXXXXX',
                '   XX  XX   ',
                '  XX    XX  ',
                'XX   XX   XX'
            ],
            [
                '    XXXX    ',
                ' XXXXXXXXXX ',
                'XXXXXXXXXXXX',
                'XXX  XX  XXX',
                'XXXXXXXXXXXX',
                '  XXX  XXX  ',
                ' XX  XX  XX ',
                '  XX    XX  '
            ]
        ]
        super().__init__(pos, color, 'martian')


class SpriteAlienSquid(SpriteAlien):
    def __init__(self, pos, color):
        self.alien_schema = [
            [
                '   XX   ',
                '  XXXX  ',
                ' XXXXXX ',
                'XX XX XX',
                'XXXXXXXX',
                '  X  X  ',
                ' X XX X ',
                'X X  X X'
            ],
            [
                '   XX   ',
                '  XXXX  ',
                ' XXXXXX ',
                'XX XX XX',
                'XXXXXXXX',
                ' X XX X ',
                'X      X',
                ' X    X '
            ]
        ]
        super().__init__(pos, color, 'squid')
