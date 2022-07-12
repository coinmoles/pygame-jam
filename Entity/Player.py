from Entity.Entity import Entity
from Entity.Corpse import Corpse
from constants import SCREEN
from pygame.math import Vector2
import pygame as pg
from constants import UNITSIZE

GROUND_ACC = 0.8
AIR_ACC = 0.3
GROUND_FRIC = -0.12
AIR_FRIC = -0.05


class Player(Entity):
    def __init__(self):
        super().__init__((UNITSIZE, UNITSIZE), (128, 255, 40), (10, 420))
        self.collide_check = False
        self.passable = True

        self.spawn_point = Vector2(30, 30)
        self.ability = None
        self.prev_rect = self.rect.copy()

        self.grounded = True

    def move(self):
        pressed_keys = pg.key.get_pressed()

        self.acc = Vector2(0, 0.8)

        if self.grounded:
            if pressed_keys[pg.K_LEFT]:
                self.acc.x = -GROUND_ACC
            elif pressed_keys[pg.K_RIGHT]:
                self.acc.x = GROUND_ACC
        else:
            if pressed_keys[pg.K_LEFT]:
                self.acc.x = -AIR_ACC
            elif pressed_keys[pg.K_RIGHT]:
                self.acc.x = AIR_ACC

    def jump(self):
        if self.grounded:
            self.vel.y = -30

    def update(self):
        self.prev_rect = self.rect.copy()

        if self.grounded:
            self.acc += self.vel * GROUND_FRIC
        else:
            self.acc += self.vel * AIR_FRIC

        super().update()

    def spawn_corpse(self):
        corpse = Corpse(self.rect.size, self.pos)
        return corpse
