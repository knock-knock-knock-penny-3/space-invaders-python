from pygame import draw, Rect, SRCALPHA
from pygame.math import Vector2
from pygame.surface import Surface

from game_constants import EMPTY_PIXEL, PIXEL_SIZE

def draw_sprite(schema, color):
    width = max([len(row) for row in schema])
    height = len(schema)
    sprite = Surface((width * PIXEL_SIZE.x, height * PIXEL_SIZE.y), SRCALPHA)

    for idx_row, row in enumerate(schema):
        for idx_char, char in enumerate(row):
            if char != EMPTY_PIXEL:
                coords = Vector2(idx_char * PIXEL_SIZE.x, idx_row * PIXEL_SIZE.y)
                rect = Rect(coords, PIXEL_SIZE)
                draw.rect(sprite, color, rect)

    return sprite
