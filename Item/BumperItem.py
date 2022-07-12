from Item.Item import Item
from Entity.Entity import Entity
from Entity.BumperPlatform import BumperPlatform
from pygame.math import Vector2
import math
from typing import Tuple, Callable


class BumperItem(Item):
    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, center: BumperPlatform(size, (0, 100, 100), center)
