from Entity.KillPlatform import KillPlatform
from pygame.math import Vector2
from constants import FPS

from globals import GLOBALS


class Fireball(KillPlatform):
    def __init__(self, pos: Vector2, vel: Vector2):
        super().__init__(pos, ["cannonball"])
        self.vel = vel
        self.start_time = GLOBALS.timer

    def update(self, camera_base: Vector2):
        if GLOBALS.timer - self.start_time >= FPS * 3:
            self.despawn()
        super().update(camera_base)

    def collide_player(self, player, side):
        super().collide_player(player, side)
        self.despawn()
