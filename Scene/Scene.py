import pygame as pg
import sys


class Scene:
    def __init__(self, screen: pg.Surface):
        self.entityList = pg.sprite.Group()
        self.screen = screen

    def scene_start(self):
        pass

    def update(self):
        for event in pg.event.get():
            self.handle_event(event)

        self.screen.fill((255, 255, 255))

        for entity in self.entityList:
            self.screen.blit(entity.surf, entity.rect)

    def scene_end(self):
        pass

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
