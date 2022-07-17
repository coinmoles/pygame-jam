from Entity.BackgroundObject.BackgroundObject import BackgroundObject
from pygame.math import Vector2


class Background(BackgroundObject):
    def __init__(self):
        super().__init__(Vector2(0, 0), ["intro_bg"], 1)
