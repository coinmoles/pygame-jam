from Entity.Item.Item import Item
from Entity.Entity import Entity
from Entity.JumpPlatform import JumpPlatform
from pygame.math import Vector2
from typing import Callable

class JumpItem(Item):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["gemBlue"], 1)

    def test(self, a: int):
        pass

    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, pos: JumpPlatform(pos)
