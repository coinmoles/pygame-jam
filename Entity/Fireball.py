from Entity.KillPlatform import KillPlatform
from pygame.math import Vector2


class Fireball(KillPlatform):
    def __init__(self, pos: Vector2, vel: Vector2):
        super().__init__(pos)
        self.vel = vel

    def collide_player(self, player, side):
        super().collide_player(player, side)
        self.despawn()
