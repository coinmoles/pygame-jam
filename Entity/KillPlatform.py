import pygame as pg
from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import COLORS
from pygame.math import Vector2
from typing import List


class KillPlatform(Platform):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["red"]["300"])

    def collide_player(self, player, side):
        player.despawn()
