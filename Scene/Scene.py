import pygame as pg
import sys
from pygame.math import Vector2


class Scene:
    def __init__(self, screen: pg.Surface):
        self.entityList = pg.sprite.Group()
        self.screen = screen

        self.camera_base = Vector2(0, 0)

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
