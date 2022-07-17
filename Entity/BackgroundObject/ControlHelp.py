from Entity.BackgroundObject.BackgroundObject import BackgroundObject
from pygame.math import Vector2


class ControlHelp(BackgroundObject):
    def __init__(self, pos: Vector2, type: int):
        super().__init__(pos, ["control_help" + str(type)], 1)
