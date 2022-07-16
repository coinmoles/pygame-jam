import pygame as pg
from Entity.Entity import Entity
from constants import FPS, SET_SPAWN
from pygame.math import Vector2


class CheckPoint(Entity):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["flagBlue", "flagBlue2"], FPS // 5)
        self.collide_check = True
        self.passable = True
        self.checked = False

    def collide_player(self, player, side):
        if self.checked:
            return
        
        pg.event.post(pg.event.Event(SET_SPAWN, spawn=self.pos))
        self.set_sprites(["flagGreen", "flagGreen2"], FPS // 5)
        self.checked = True
