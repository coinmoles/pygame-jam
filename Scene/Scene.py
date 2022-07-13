from __future__ import annotations
from typing import Tuple, Union
import pygame as pg
import sys
from pygame.math import Vector2


class Scene:
    def __init__(self, screen: pg.Surface, id: Tuple[int, int]):
        self.entityList: pg.sprite.Group = pg.sprite.Group()
        self.screen:pg.Surface = screen

        self.active:bool = True
        self.next_scene : Union[Scene, None] = None
        self.id: Tuple[int, int] = id

        self.camera_base:Vector2 = Vector2(0, 0)

    def scene_start(self):
        pass

    def update(self):
        self.screen.fill((255, 255, 255))

        for entity in self.entityList:
            self.screen.blit(entity.surf, entity.rect.move(-self.camera_base))

    def scene_end(self):
        pass

    def handle_event(self, event: pg.event.Event):
        pass

    def set_next_scene(self, scene: Union[Scene, None]):
        self.next_scene = scene
    
    def deactivate(self):
        self.active = False