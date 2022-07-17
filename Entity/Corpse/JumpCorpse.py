from typing import Tuple
from pygame import Vector2
from Entity.JumpPlatform import JumpPlatform
from constants import FPS


class JumpCorpse(JumpPlatform):
    def __init__(self, pos: Vector2, flip: Tuple[bool, bool]):
        super().__init__(pos)
        self.flip = flip
        self.set_sprites(["p2_duck", "p2_duck2"], FPS // 5)
