from Item.Item import Item
from Entity.Entity import Entity
from Entity.JumpPlatform import JumpPlatform
from pygame.math import Vector2
import math
from typing import Tuple, Callable


class JumpItem(Item):
    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, pos: JumpPlatform(size, pos)
