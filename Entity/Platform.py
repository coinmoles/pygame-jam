from Entity.Entity import Entity
from constants import SCREEN, COLORS
from pygame.math import Vector2


class Platform(Entity):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["600"])
        self.collide_check = True
        self.passable = False

    def collide_player(self, player, side):
        pass
