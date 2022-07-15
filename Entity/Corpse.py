from Entity.Platform import Platform
from pygame.math import Vector2


class Corpse(Platform):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["boxEmpty"], 1)
