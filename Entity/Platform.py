from Entity.Entity import Entity
from constants import SCREEN
from typing import Tuple


class Platform(Entity):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)
