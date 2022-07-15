import pygame as pg
from Entity.Entity import Entity
from pygame.math import Vector2
import math
from typing import Callable, List


class Item(Entity):
    def __init__(self, pos: Vector2, sprites: List[pg.Surface]):
        super().__init__(pos, sprites)
        self.collide_check = True
        self.passable = True
        self.timer = 0

    def update(self, camera_base: Vector2, timer: int):
        self.vel = Vector2(0, math.sin(self.timer * math.pi / 20))
        self.timer += 1
        super().update(camera_base, timer)

    def collide_player(self, player, side):
        player.set_ability(self.ability_give())
        self.despawn()

    def ability_give(self) -> Callable[[], Entity]:
        pass
