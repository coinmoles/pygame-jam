import pygame as pg
from Entity.Entity import Entity
from Entity.KillPlatform import KillPlatform
from constants import COLORS
from pygame.math import Vector2
from typing import List


class Fireball(KillPlatform):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface], vel: Vector2):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["red"]["600"])
        self.vel = vel

    def collide_player(self, player, side):
        super().collide_player(player, side)
        self.despawn()
