from Entity.Platform import Platform
from pygame.math import Vector2
from typing import List


class KillPlatform(Platform):
    def __init__(self, pos: Vector2, sprites: List[str]):
        super().__init__(pos, sprites, 1)

    def collide_player(self, player, side):
        player.despawn()
