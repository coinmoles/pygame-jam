import pygame as pg
from Scene.Scene import Scene
from Entity.Player import Player
from Entity.Platform import Platform


class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.platforms = pg.sprite.Group()

        self.player = Player(self)
        platform = Platform()

        self.platforms.add(platform)
        self.entityList.add(self.player)
        self.entityList.add(platform)

    def update(self):
        super().update()
        self.player.move()
        self.player.update()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jump()
