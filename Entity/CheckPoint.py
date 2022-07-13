import pygame as pg
from Entity.Entity import Entity
from constants import UNITSIZE, SET_SPAWN, COLORS
from pygame.math import Vector2


class CheckPoint(Entity):
    def __init__(self, size: Vector2, pos: Vector2):
        super().__init__(size, pos)
        self.set_color(COLORS["green"]["300"])
        self.collide_check = True
        self.passable = True

    def collide_player(self, player, side):
        pg.event.post(pg.event.Event(SET_SPAWN, spawn=self.pos))
        self.despawn()
