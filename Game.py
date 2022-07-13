import pygame as pg
from Stages.stage1 import stage1, stage2
from constants import *
from Scene.GameScene import GameScene
import sys


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN.width, SCREEN.height), 0, 32)
        self.currentScene = GameScene(self.screen, stage2)
        self.clock = pg.time.Clock()

    def run(self):
        self.currentScene.scene_start()

        while True:
            for event in pg.event.get():
                self.handle_event(event)
                self.currentScene.handle_event(event)
            self.currentScene.update()

            pg.display.update()
            self.clock.tick(FPS)

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT: pg.quit(); sys.exit()
