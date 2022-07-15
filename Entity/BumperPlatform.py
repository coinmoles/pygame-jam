from typing import List

import pygame as pg
from constants import COLORS, SCREEN
from pygame.math import Vector2

from Entity.Platform import Platform
from pygame.math import Vector2
class BumperPlatform(Platform):
    def __init__(self, pos: Vector2, sprites: List[pg.Sprite]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["blue"]["300"])

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -20
        elif side == "bottom":
            player.vel.y = 20
        elif side == "left":
            player.vel.x = -20
        elif side == "right":
            player.vel.x = 20
