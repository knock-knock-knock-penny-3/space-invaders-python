import os, sys

from pygame import draw, Rect, SRCALPHA
from pygame.math import Vector2
from pygame.mixer import Sound
from pygame.surface import Surface

from game_constants import (
    EMPTY_PIXEL,
    PIXEL_SIZE,
    RESOURCES_DIR_NAME,
    SOUNDS_DIR_NAME,
    STORE
)

def add_userevent():
    new_userevent = STORE['last_userevent'] + 1
    STORE['last_userevent'] = new_userevent
    return new_userevent

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

def load_sound(filename):
    """docstring"""
    path = os.path.join(RESOURCES_DIR_NAME, SOUNDS_DIR_NAME, filename)
    return Sound(_resource_path(path))

def _resource_path(relative_path):
    """docstring"""
    if hasattr(sys, "_MEIPASS"):
        base = getattr(sys, "_MEIPASS")
        return os.path.join(base, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
