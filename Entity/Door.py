import pygame as pg
from pygame import Vector2
from Entity.Entity import Entity
from typing import Tuple, List
from constants import COLORS, CHANGE_SCENE
from SceneData.stages import stages


class Door(Entity):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface], _id: int):
        super().__init__(pos, sprites)
        # self.set_color(COLORS["orange"]["600"])

        self.passable = True
        self.collide_check = True
        self.id = _id

    def collide_player(self, player, side):
        super().collide_player(player, side)
        # self.set_color(COLORS["orange"]["800"])
