from Entity.Corpse import Corpse
from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import COLORS, SCREEN
from pygame.math import Vector2
import pygame as pg
from constants import UNITSIZE, COLORS
from typing import Callable, Union

GROUND_ACC = 0.8
AIR_ACC = 0.3
GROUND_FRIC = -0.12
AIR_FRIC = -0.05


class Player(Entity):
    def __init__(self, pos: Vector2):
        super().__init__(Vector2(UNITSIZE, UNITSIZE), pos)
        self.set_color(COLORS["yellow"]["300"])
        self.collide_check = False
        self.passable = True

        self.spawn_point = Vector2(30, 30)
        self.ability: Union[Callable[[], Corpse]] = lambda size, c_pos: Corpse(size, c_pos)
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

    def update(self, camera_base: Vector2):
        self.prev_rect = self.rect.copy()

        if self.grounded:
            self.acc += self.vel * GROUND_FRIC
        else:
            self.acc += self.vel * AIR_FRIC

        super().update(camera_base)

    def check_active(self, camera_base):
        return

    def spawn_corpse(self):
        return self.ability(self.rect.size, self.pos)

    def set_ability(self, ability: Callable[[Vector2, Vector2], Entity]):
        print(ability)
        self.ability = ability
