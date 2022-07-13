from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import SCREEN, COLORS
from typing import Tuple


class BumperPlatform(Platform):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__(size, pos)
        self.set_color(COLORS["blue"]["300"])

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -20
        elif side == "bottom":
            player.vel.y = 20
        elif side == "left":
            player.vel.x = -20
        elif side == "right":
            player.vel.x = 20
