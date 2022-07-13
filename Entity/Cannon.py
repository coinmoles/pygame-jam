import pygame as pg
from Entity.Platform import Platform
from Entity.Fireball import Fireball
from pygame.math import Vector2
from constants import COLORS, SPAWN, UNITSIZE


class Cannon(Platform):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["800"])

        self.collide_check = True
        self.passable = False
        self.timer = 0

    def update_active(self):
        self.timer += 1
        if self.timer >= 300:
            pg.event.post(pg.event.Event(
                SPAWN, entity=Fireball(Vector2(UNITSIZE / 2, UNITSIZE / 2),
                self.pos - Vector2(self.rect.width * 3 / 4, self.rect.height * 1 / 4),  Vector2(-5, 0))
            ))
            self.timer = 0
