from Entity.Platform import Platform
from pygame.math import Vector2


class KillPlatform(Platform):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["spikes"], 1)

    def collide_player(self, player, side):
        player.despawn()
