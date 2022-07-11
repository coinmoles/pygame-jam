from Entity.Entity import Entity
from Entity.Corpse import Corpse
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

        self.spawn_point = Vector2(30, 30)
        self.ability = None

        self.grounded = True
        self.is_dead = False

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
        if self.pos.y > 800: #조건 변경 필요
            self.is_dead = True

        if self.grounded:
            self.acc.x += self.vel.x * GROUND_FRIC
        else:
            self.acc.x += self.vel.x * AIR_FRIC

        super().update()

        self.rect.midbottom = self.pos

        hits = pg.sprite.spritecollide(self, self.scene.platforms, False)
        if hits:
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0
            self.grounded = True
        else:
            self.grounded = False

    def spawn_corpse(self):
        corpse = Corpse(self.rect.size, self.pos)
        return corpse

    def die(self):
        corpse = self.spawn_corpse()

        self.pos = self.spawn_point.copy()
        self.is_dead = False

        return corpse
