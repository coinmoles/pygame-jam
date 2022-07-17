from Entity.Corpse.JumpCorpse import JumpCorpse
from Entity.Item.Item import Item
from Entity.Entity import Entity
from pygame.math import Vector2
from typing import Callable

from constants import UNITSIZE

class JumpItem(Item):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["gemBlue"], 1, 1)

    def ability_give(self) -> Callable[[Entity], Entity]:
        return lambda player: JumpCorpse(player.pos - Vector2(UNITSIZE / 6, 0), player.flip)
