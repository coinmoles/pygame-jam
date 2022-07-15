import pygame as pg
from Entity.Platform import Platform
from Entity.Fireball import Fireball
from pygame.math import Vector2
from constants import COLORS, SPAWN, UNITSIZE, FPS
from typing import List


class Cannon(Platform):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["gray"]["800"])

        self.collide_check = True
        self.passable = False

    def update_active(self, timer: int):
        if timer % (FPS * 5) == 0:
            pg.event.post(pg.event.Event(
                SPAWN, entity=Fireball(self.pos - Vector2(self.rect.width, 0), 
                [pg.Surface((100, 100))], Vector2(-5, 0))
            ))
