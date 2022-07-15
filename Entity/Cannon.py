import pygame as pg
from Entity.Platform import Platform
from Entity.Fireball import Fireball
from pygame.math import Vector2
from constants import SPAWN, FPS
from typing import List


class Cannon(Platform):
    def __init__(self, pos: Vector2, sprites: List[str]):
        super().__init__(pos, sprites, 1)

        self.collide_check = True
        self.passable = False

    def update_active(self, timer: int):
        if timer % (FPS * 5) == 0:
            pg.event.post(pg.event.Event(
                SPAWN, entity=Fireball(self.pos - Vector2(self.rect.width, 0), Vector2(-5, 0))
            ))
