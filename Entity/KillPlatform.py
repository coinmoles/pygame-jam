from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import COLORS
from pygame.math import Vector2


class KillPlatform(Platform):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size,  pos)
        self.set_color(COLORS["red"]["300"])

    def collide_player(self, player, side):
        player.despawn()
