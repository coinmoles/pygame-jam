from Entity.Entity import Entity
import pygame as pg
from pygame.math import Vector2
import math
from typing import Callable, List

from constants import TRANSFORM


class Item(Entity):
    def __init__(self, pos: Vector2, sprites: List[str], freq: int):
        super().__init__(pos, sprites, freq)
        self.collide_check = True
        self.passable = True
        self.timer = 0
        self.item_id = 0

    def update(self, camera_base: Vector2, timer: int):
        self.vel = Vector2(0, math.sin(self.timer * math.pi / 20))
        self.timer += 1
        super().update(camera_base, timer)

    def collide_player(self, player, side):
        player.set_ability(self.ability_give())
        pg.event.post(pg.event.Event(TRANSFORM, item_id=self.item_id))
        self.despawn()
        

    def ability_give(self) -> Callable[[], Entity]:
        pass
