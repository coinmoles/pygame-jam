import pygame as pg
from pygame.math import Vector2
from constants import SCREEN


class Entity(pg.sprite.Sprite):
    def __init__(self, size, color, center):
        super().__init__()

        self.surf = pg.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=center)

        self.pos = Vector2(center)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def update(self):
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > SCREEN.width:
            self.pos.x = SCREEN.width
        if self.pos.x < 0:
            self.pos.x = 0

        self.rect.midbottom = self.pos
