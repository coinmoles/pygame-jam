import imp
from Entity.Entity import Entity
import pygame as pg
from pygame.math import Vector2
from typing import List


class BackgroundObject(Entity):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface], freq: int):
        super().__init__(pos, sprites, freq)
        self.collide_check = False
