from Entity.Entity import Entity
from constants import SCREEN, COLORS
from typing import Tuple


class Platform(Entity):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["600"])
        self.collide_check = True
        self.passable = False

    def collide_player(self, player, side):
        pass
