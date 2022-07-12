import pygame as pg
from pygame.math import Vector2
from constants import SCREEN
from typing import Tuple


class Entity(pg.sprite.Sprite):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__()

        self.surf = pg.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(bottomleft=pos)

        self.pos = Vector2(pos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > SCREEN.width:
            self.pos.x = SCREEN.width
        if self.pos.x < 0:
            self.pos.x = 0

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
