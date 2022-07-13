import pygame as pg
from Entity.Entity import Entity
from constants import UNITSIZE, SET_SPAWN
from typing import Tuple


class CheckPoint(Entity):
    def __init__(self, color: Tuple[int, int, int], pos: Tuple[int, int]):
        super().__init__((UNITSIZE, UNITSIZE), color, pos)
        self.collide_check = True
        self.passable = True

    def collide_player(self, player, side):
        pg.event.post(pg.event.Event(SET_SPAWN, spawn=self.pos))
        self.despawn()
