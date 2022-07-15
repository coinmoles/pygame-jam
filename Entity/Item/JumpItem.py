import pygame as pg
from Entity.Item.Item import Item
from Entity.Entity import Entity
from Entity.JumpPlatform import JumpPlatform
from pygame.math import Vector2
import math
from typing import Callable, List
from constants import COLORS
from globals import GLOBALS


class JumpItem(Item):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, [GLOBALS.images["gemBlue"]])
        # self.set_color(COLORS["blue"]["300"])

    def test(self, a: int):
        pass

    def ability_give(self) -> Callable[[Vector2, Vector2], Entity]:
        return lambda size, pos: JumpPlatform(pos, [pg.Surface((100, 100))])
