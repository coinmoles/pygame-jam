from Entity.Entity import Entity
from pygame.math import Vector2
import math
from typing import Tuple, Callable


class Item(Entity):
    def __init__(self, size: Tuple[int, int], color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__(size, color, pos)
        self.collide_check = True
        self.passable = True
        self.timer = 0

    def update(self):
        self.vel = Vector2(0, math.sin(self.timer * math.pi / 20))
        self.timer += 1
        super().update()

    def collide_player(self, player, side):
        player.set_ability(self.ability_give())
        self.despawn()

    def ability_give(self) -> Callable[[], Entity]:
        pass
