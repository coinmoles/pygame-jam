from Entity.Entity import Entity
from constants import SCREEN


class Platform(Entity):
    def __init__(self):
        super().__init__((SCREEN.width / 2, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height - 10))
