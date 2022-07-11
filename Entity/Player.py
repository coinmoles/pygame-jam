from Entity.Entity import Entity
from constants import SCREEN
from pygame.math import Vector2
import pygame as pg

GROUND_ACC = 0.8
AIR_ACC = 0.3
GROUND_FRIC = -0.12
AIR_FRIC = -0.05


class Player(Entity):
    def __init__(self, scene):
        super().__init__((30, 30), (128, 255, 40), (10, 420))

        self.scene = scene

        self.pos = Vector2((10, 385))
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.spawn_point = (30, 30)
        self.ability = None

        self.grounded = True

    def move(self):
        pressed_keys = pg.key.get_pressed()

        self.acc = Vector2(0, 0.5)

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
            self.vel.y = -15

    def update(self):
        if self.grounded:
            self.acc.x += self.vel.x * GROUND_FRIC
        else:
            self.acc.x += self.vel.x * AIR_FRIC

        super().update()

    def dead(self):
        pass
