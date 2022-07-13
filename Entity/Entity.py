import pygame as pg
from pygame.math import Vector2
from constants import SCREEN, DESPAWN, UNITSIZE, COLORS
from typing import Tuple


class Entity(pg.sprite.Sprite):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__()
        self.active = True
        self.collide_check = False
        self.passable = False

        self.surf = pg.Surface(size)
        self.rect = self.surf.get_rect(bottomleft=pos)

        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def update(self, camera_base: Vector2):
        if self.active:
            self.update_active()
        self.check_active(camera_base)

    def update_active(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.bottomleft = self.pos


    def check_active(self, camera_base):
        rel_rect = self.rect.move(-camera_base)

        if rel_rect.left > SCREEN.width + UNITSIZE or rel_rect.right < -UNITSIZE \
                or rel_rect.top > SCREEN.height + UNITSIZE or rel_rect.bottom < -UNITSIZE:
            self.active = False
        else:
            self.active = True

    def set_pos(self, pos: Vector2):
        self.pos = pos
        self.rect.bottomleft = self.pos

    def set_x(self, x: int):
        self.pos.x = x
        self.rect.bottomleft = self.pos

    def set_y(self, y: int):
        self.pos.y = y
        self.rect.bottomleft = self.pos

    def set_color(self, color: Tuple[int, int, int]):
        self.surf.fill(color)

    def despawn(self):
        pg.event.post(pg.event.Event(DESPAWN, entity=self))
