from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import SCREEN
from typing import Tuple


class BumperPlatform(Platform):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -20
        elif side == "bottom":
            player.vel.y = 20
        elif side == "left":
            player.vel.x = -20
        elif side == "right":
            player.vel.x = 20
