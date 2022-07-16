from Entity.Entity import Entity
import pygame as pg
from pygame.math import Vector2
import math
from typing import Callable, List

from constants import TRANSFORM
from globals import GLOBALS


class Item(Entity):
    def __init__(self, pos: Vector2, sprites: List[str], freq: int, item_id: int):
        super().__init__(pos, sprites, freq)
        self.collide_check = True
        self.passable = True
        self.item_id = item_id

    def update(self, camera_base: Vector2):
        self.vel = Vector2(0, math.sin(GLOBALS.timer * math.pi / 20))
        super().update(camera_base, GLOBALS.timer)

    def collide_player(self, player, side):
        player.set_ability(self.ability_give())
        pg.mixer.Sound.play(GLOBALS.sfx_dict["Powerup1"], 1)
        pg.event.post(pg.event.Event(TRANSFORM, item_id=self.item_id))
        self.despawn()
        

    def ability_give(self) -> Callable[[], Entity]:
        pass
