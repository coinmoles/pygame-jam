import pygame as pg


class Entity(pg.sprite.Sprite):
    def __init__(self, size, color, center):
        super().__init__()

        self.surf = pg.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=center)
