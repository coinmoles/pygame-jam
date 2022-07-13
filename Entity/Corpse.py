from Entity.Platform import Platform
from constants import COLORS
from pygame.math import Vector2


class Corpse(Platform):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["400"])
