from Entity.Entity import Entity
from Entity.KillPlatform import KillPlatform
from constants import COLORS
from pygame.math import Vector2


class Fireball(KillPlatform):
    def __init__(self, size: Vector2, pos: Vector2, vel: Vector2):
        super().__init__(size,  pos)
        self.set_color(COLORS["red"]["600"])
        self.vel = vel

    def collide_player(self, player, side):
        super().collide_player(player, side)
        self.despawn()
