from pygame import Vector2
from Entity.Cannon import Cannon
from constants import FPS

class CannonCorpse(Cannon):
    def __init__(self, pos: Vector2, flip: bool):
        super().__init__(pos, 0 if flip[0] else 2)
        self.flip = flip
        self.set_sprites(["p3_duck"], 1)
