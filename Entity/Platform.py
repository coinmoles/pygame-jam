from Entity.Entity import Entity
from constants import SCREEN


class Platform(Entity):
    def __init__(self, size, color, center):
        super().__init__(size, color, center)