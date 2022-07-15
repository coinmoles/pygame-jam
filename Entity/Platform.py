import pygame as pg
from Entity.Entity import Entity
from constants import SCREEN, COLORS
from pygame.math import Vector2
from typing import List


class Platform(Entity):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["gray"]["600"])
        self.collide_check = True
        self.passable = False

    def collide_player(self, player, side):
        pass
