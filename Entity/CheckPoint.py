import pygame as pg
from Entity.Entity import Entity
from constants import UNITSIZE, SET_SPAWN, COLORS
from pygame.math import Vector2
from typing import List
from globals import GLOBALS


class CheckPoint(Entity):
    def __init__(self, pos: Vector2):
        super().__init__(pos, [GLOBALS.images["flagBlue"], GLOBALS.images["flagBlue2"]])
        self.collide_check = True
        self.passable = True

    def collide_player(self, player, side):
        pg.event.post(pg.event.Event(SET_SPAWN, spawn=self.pos))
        self.despawn()
