from Entity.Platform import Platform
from pygame.math import Vector2
from globals import GLOBALS


class GrassPlatform(Platform):
    def __init__(self, pos: Vector2, top: bool):
        if top:
            super().__init__(pos, ["grassMid"], 1)
        else:
            super().__init__(pos, ["grassCenter"], 1)
