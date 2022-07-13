from Entity.Entity import Entity
from Entity.Platform import Platform
from typing import Tuple
from constants import COLORS


class KillPlatform(Platform):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__(size,  pos)
        self.set_color(COLORS["red"]["300"])

    def collide_player(self, player, side):
        player.despawn()
