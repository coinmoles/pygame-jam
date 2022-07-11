from Entity.Entity import Entity
from pygame.math import Vector2
import math


class Item(Entity):
    def __init__(self, size, color, center):
        super().__init__(size, color, center)
        self.timer = 0

    def update(self):
        self.vel = Vector2(0, math.sin(self.timer * math.pi / 20))
        self.timer += 1
        super().update()
