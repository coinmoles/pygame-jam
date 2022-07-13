import pygame as pg
from pygame.math import Vector2
from constants import SCREEN, DESPAWN
from typing import Tuple


class Entity(pg.sprite.Sprite):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__()
        self.active = True
        self.collide_check = False
        self.passable = False

        self.surf = pg.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(bottomleft=pos)

        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.bottomleft = self.pos

    def set_pos(self, pos: Vector2):
        self.pos = pos
        self.rect.bottomleft = self.pos

    def set_x(self, x: int):
        self.pos.x = x
        self.rect.bottomleft = self.pos

    def set_y(self, y: int):
        self.pos.y = y
        self.rect.bottomleft = self.pos

    def despawn(self):
        pg.event.post(pg.event.Event(DESPAWN, entity=self))
