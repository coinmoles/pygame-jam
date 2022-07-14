from __future__ import annotations
from typing import Tuple, Union
import pygame as pg
import sys
from pygame.math import Vector2
from globals import GLOBALS


class Scene:
    def __init__(self, _id: Tuple[int, int]):
        self.entityList: pg.sprite.Group = pg.sprite.Group()

        self.id: Tuple[int, int] = _id
        self.timer = 0

        self.camera_base: Vector2 = Vector2(0, 0)

    def scene_start(self):
        pass

    def update(self):
        GLOBALS.screen.fill((255, 255, 255))

        for entity in self.entityList:
            entity.draw(self.camera_base)

        self.timer += 1

    def scene_end(self):
        pass

    def handle_event(self, event: pg.event.Event):
        pass
