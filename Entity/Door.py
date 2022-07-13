from pygame import Vector2
from Entity.Entity import Entity
import pygame as pg

from constants import COLORS


class Door(Entity):
    def __init__(self, size: Vector2, pos: Vector2, id:int):
        super().__init__(size, pos)
        self.set_color(COLORS["orange"]["600"])

        self.passable = True
        self.collide_check = True
        self.id = id

    def collide_player(self, player, side):
        super().collide_player(player, side)
        self.set_color(COLORS["orange"]["800"])
