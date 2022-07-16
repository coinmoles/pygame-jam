from pygame import Vector2
from Entity.Entity import Entity
import pygame as pg

from constants import FPS, STAGE_CLEAR


class Goal(Entity):
    def __init__(self, pos: Vector2, _id: int):
        super().__init__(pos, ["flagRed", "flagRed2"], FPS // 5)

        self.passable = True
        self.collide_check = True
        self.id = _id

        self.checked = False

    def collide_player(self, player, side):
        if self.checked:
            return
        super().collide_player(player, side)

        if player.grounded:
            self.checked = True
            self.set_sprites(["flagGreen", "flagGreen2"], FPS // 5)
            pg.event.post(pg.event.Event(STAGE_CLEAR))
