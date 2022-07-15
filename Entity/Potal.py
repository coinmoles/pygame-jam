import pygame as pg
from Entity.Entity import Entity
from constants import COLORS, SCREEN
from pygame.math import Vector2
from typing import List


class Potal(Entity):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface], potal_type):
        super().__init__(pos, sprites)
        self.potal_type = potal_type
