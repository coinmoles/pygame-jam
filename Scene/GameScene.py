import pygame as pg
from Scene.Scene import Scene
from Entity.Player import Player
from Entity.Platform import Platform
from Entity.Item import Item


class GameScene(Scene):
    def __init__(self, game, map):
        super().__init__(game)
        self.platforms = pg.sprite.Group()
        self.items = pg.sprite.Group()

        self.player = Player(self)
        platform = Platform()
        item = Item((50, 50), (0, 0, 255), (50, 50))

        self.platforms.add(platform)
        self.items.add(item)
        self.entityList.add(self.player)
        self.entityList.add(platform)
        self.entityList.add(item)

    def update(self):
        super().update()
        self.player.move()
        for entity in self.entityList:
            entity.update()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jump()
