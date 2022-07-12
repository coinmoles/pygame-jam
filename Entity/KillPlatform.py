from Entity.Entity import Entity
from Entity.Platform import Platform
from typing import Tuple


class KillPlatform(Platform):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)

    def collide_player(self, player, side):
        player.despawn()
