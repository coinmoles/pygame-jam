from Entity.BackgroundObject.BackgroundObject import BackgroundObject
from pygame.math import Vector2
from globals import GLOBALS


class DoorTop(BackgroundObject):
    def __init__(self, pos: Vector2, locked: bool):
        if locked:
            super().__init__(pos, ["door_closedTop"], 1)
        else:
            super().__init__(pos, ["door_openTop"], 1)
