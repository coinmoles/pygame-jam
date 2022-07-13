from Entity.Entity import Entity
from constants import COLORS, SCREEN
from pygame.math import Vector2

class Potal(Entity)
    def __init__(self, size: Vector2, pos: Vector2, potal_type):
        super().__init__(size, pos)
        self.potal_type = potal_type