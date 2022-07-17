from Entity.Corpse.CannonCorpse import CannonCorpse
from Entity.Corpse.JumpCorpse import JumpCorpse
from Entity.Item.Item import Item
from Entity.Entity import Entity
from pygame.math import Vector2
from typing import Callable

from constants import UNITSIZE

class CannonItem(Item):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["gemRed"], 1, 2)

    def ability_give(self) -> Callable[[Entity], Entity]:
        return lambda player: CannonCorpse(player.pos - Vector2(UNITSIZE / 6, 0), player.flip)
