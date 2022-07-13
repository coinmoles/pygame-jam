import pygame as pg
from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from pygame.math import Vector2
from constants import COLORS, SPAWN


class Cannon(Platform):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["600"])

        self.collide_check = True
        self.passable = False
        self.timer = 0

    def update_active(self):
        self.timer += 1
        if self.timer >= 500:
            self.despawn()
            pg.event.post(pg.event.Event(SPAWN, entity=KillPlatform((10, 10), (40, 40))))
            self.timer = 0
