from typing import Tuple
from Entity.Platform import Platform
from pygame.math import Vector2


class Corpse(Platform):
    def __init__(self, pos: Vector2, flip: Tuple[bool, bool]):
        super().__init__(pos, ["p1_duck"], 1)
        self.flip = flip
