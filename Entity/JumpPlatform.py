import pygame as pg
from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import COLORS, SCREEN
from pygame.math import Vector2
from typing import List


class JumpPlatform(Platform):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["blue"]["400"])

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -40
