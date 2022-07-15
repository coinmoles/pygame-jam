from pygame import Vector2
from Entity.Entity import Entity
import pygame as pg
from typing import Tuple, List
from constants import COLORS, CHANGE_SCENE
from globals import GLOBALS


class Goal(Entity):
    def __init__(self, pos: Vector2, _id: int):
        super().__init__(pos, [GLOBALS.images["flagRed"], GLOBALS.images["flagRed2"]])
        # self.set_color(COLORS["orange"]["600"])

        self.passable = True
        self.collide_check = True
        self.id = _id

    def collide_player(self, player, side):
        super().collide_player(player, side)
        pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], 0)))
