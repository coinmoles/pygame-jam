from pygame.math import Vector2
from typing import List
from Entity.KillPlatform import KillPlatform


class Spike(KillPlatform):
    def __init__(self, pos: Vector2, rotate):
        assert rotate == 0 or rotate == 1 or rotate == 2 or rotate == 3
        
        if rotate == 0:
            super().__init__(pos, ["spikes"])
        elif rotate == 1:
            super().__init__(pos, ["spikes1"])
        elif rotate == 2:
            super().__init__(pos, ["spikes2"])
        elif rotate == 3:
            super().__init__(pos, ["spikes3"])