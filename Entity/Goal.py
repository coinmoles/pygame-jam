from pygame import Vector2
from Entity.Entity import Entity
import pygame as pg
from constants import CHANGE_SCENE, FPS


class Goal(Entity):
    def __init__(self, pos: Vector2, _id: int):
        super().__init__(pos, ["flagRed", "flagRed2"], FPS // 5)

        self.passable = True
        self.collide_check = True
        self.id = _id

    def collide_player(self, player, side):
        super().collide_player(player, side)
        pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], 0)))
