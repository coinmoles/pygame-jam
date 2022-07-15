import pygame as pg
from Entity.Platform import Platform
from constants import COLORS
from pygame.math import Vector2
from typing import List


class Corpse(Platform):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["gray"]["400"])
