import pygame as pg
import sys


class Scene:
    def __init__(self, game):
        self.entityList = pg.sprite.Group()
        self.game = game

    def scene_start(self):
        pass

    def update(self):
        for event in pg.event.get():
            self.handle_event(event)

        self.game.screen.fill((255, 255, 255))

        for entity in self.entityList:
            self.game.screen.blit(entity.surf, entity.rect)

    def scene_end(self):
        pass

    def handle_event(self, event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
