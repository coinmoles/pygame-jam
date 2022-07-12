from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import SCREEN
from typing import Tuple


class JumpPlatform(Platform):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -40
