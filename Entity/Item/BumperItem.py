from Entity.Item.Item import Item
from Entity.Entity import Entity
from Entity.BumperPlatform import BumperPlatform
from pygame.math import Vector2
from typing import Callable, List

from constants import UNITSIZE


class BumperItem(Item):
    def __init__(self, pos: Vector2, sprites: List[str]):
        super().__init__(pos, sprites, 1)
        # self.set_color(COLORS["blue"]["300"])

    def ability_give(self) -> Callable[[Entity], Entity]:
        return lambda player: BumperPlatform(player.pos - Vector2(UNITSIZE / 6, 0))
