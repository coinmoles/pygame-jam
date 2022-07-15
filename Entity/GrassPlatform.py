from Entity.Platform import Platform
import pygame as pg
from pygame.math import Vector2
from typing import List
from globals import GLOBALS


class GrassPlatform(Platform):
    def __init__(self, pos: Vector2, top: bool):
        if top:
            super().__init__(pos, [GLOBALS.images["grassMid"]])
        else:
            super().__init__(pos, [GLOBALS.images["grassCenter"]])
