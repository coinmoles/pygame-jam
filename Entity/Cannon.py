import pygame as pg
from Entity.Platform import Platform
from Entity.Fireball import Fireball
from pygame.math import Vector2
from constants import SCREEN, SPAWN, FPS, UNITSIZE
from typing import List

from globals import GLOBALS


class Cannon(Platform):
    def __init__(self, pos: Vector2, sprites: List[str]):
        super().__init__(pos, sprites, 1)

        self.collide_check = True
        self.passable = False
        self.item_id = 1

    def update_active(self):
        if GLOBALS.timer == 0:
            return
        
        if GLOBALS.timer % (FPS * 5) == 0:
            pg.event.post(pg.event.Event(
                SPAWN, entity=Fireball(self.pos - Vector2(self.rect.width, 0), Vector2(-5, 0))
            ))

    def check_active(self, camera_base):
        rel_rect = self.rect.move(-camera_base)

        if rel_rect.left > SCREEN.width + UNITSIZE or rel_rect.right < -UNITSIZE \
                or rel_rect.top > SCREEN.height + UNITSIZE or rel_rect.bottom < -UNITSIZE:
            self.active = False
        else:
            self.active = True
