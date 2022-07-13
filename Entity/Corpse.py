from Entity.Platform import Platform
from constants import COLORS


class Corpse(Platform):
    def __init__(self, size, pos):
        super().__init__(size, pos)
        self.set_color(COLORS["gray"]["400"])
