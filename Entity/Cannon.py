import pygame as pg
from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from typing import Tuple
from pygame.math import Vector2
from constants import SPAWN


class Cannon(Platform):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)
        self.collide_check = True
        self.passable = False
        self.timer = 0

    def update_active(self):
        self.timer += 1
        if self.timer >= 500:
            self.despawn()
            pg.event.post(pg.event.Event(SPAWN, entity=KillPlatform((10, 10), (30, 30, 30), (40, 40))))
            self.timer = 0
