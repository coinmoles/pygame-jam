from Item.Item import Item
from Entity.Entity import Entity
from Entity.JumpPlatform import JumpPlatform
from pygame.math import Vector2
import math
from typing import Tuple, Callable
from constants import COLORS


class JumpItem(Item):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__(size, pos)
        self.set_color(COLORS["blue"]["300"])

    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, pos: JumpPlatform(size, pos)
