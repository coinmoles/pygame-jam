from Entity.Platform import Platform
from pygame.math import Vector2


class DirtPlatform(Platform):
    def __init__(self, pos: Vector2, top: bool):
        if top:
            super().__init__(pos, ["dirtMid"], 1)
        else:
            super().__init__(pos, ["dirtCenter"], 1)
