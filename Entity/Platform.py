from Entity.Entity import Entity
from pygame.math import Vector2
from typing import List


class Platform(Entity):
    def __init__(self, pos: Vector2, sprites: List[str], freq: int):
        super().__init__(pos, sprites, freq)
        self.collide_check = True
        self.passable = False

    def collide_player(self, player, side):
        pass
