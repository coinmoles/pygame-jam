import pygame as pg
from Entity.Entity import Entity
from constants import UNITSIZE, SET_SPAWN, COLORS
from typing import Tuple


class CheckPoint(Entity):
    def __init__(self, size: Tuple[int, int], pos: Tuple[int, int]):
        super().__init__(size, pos)
        self.set_color(COLORS["green"]["300"])
        self.collide_check = True
        self.passable = True

    def collide_player(self, player, side):
        pg.event.post(pg.event.Event(SET_SPAWN, spawn=self.pos))
        self.despawn()
