import pygame as pg
from Maps.map1 import Map1
from constants import *
from Scene.GameScene import GameScene


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN.width, SCREEN.height), 0, 32)
        self.currentScene = GameScene(self.screen, Map1)
        self.clock = pg.time.Clock()

    def run(self):
        self.currentScene.scene_start()

        while True:
            self.currentScene.update()

            pg.display.update()
            self.clock.tick(FPS)
