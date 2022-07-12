from Item.Item import Item
from Entity.Entity import Entity
from Entity.JumpPlatform import JumpPlatform
from pygame.math import Vector2
import math
from typing import Tuple, Callable


class JumpItem(Item):
    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, center: JumpPlatform(size, (0, 100, 100), center)
