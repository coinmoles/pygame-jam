from Entity.Entity import Entity
from Entity.Platform import Platform
from constants import COLORS, SCREEN
from pygame.math import Vector2


class JumpPlatform(Platform):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["blue"]["400"])

    def collide_player(self, player, side):
        if side == "top":
            player.vel.y = -40
