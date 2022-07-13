from errno import EEXIST
import imp
from typing import Tuple
import pygame as pg
# from Chapters.chapter1 import chapter1, main_menu, stages
from Chapters.chapter_menu.chapter1 import chapter1
from Scene.ChapterScene import ChapterScene
from constants import *
from Scene.GameScene import GameScene
import sys


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN.width, SCREEN.height), 0, 32)
        # self.currentScene = GameScene(self.screen, chapter1[0])
        self.current_scene = ChapterScene(self.screen, chapter1, (1, 1))
        self.clock = pg.time.Clock()

    def run(self):
        while True:
            self.current_scene.scene_start()

            while self.current_scene.active:
                for event in pg.event.get():
                    self.handle_event(event)
                    self.current_scene.handle_event(event)
                self.current_scene.update()

                pg.display.update()
                self.clock.tick(FPS)

            self.current_scene.scene_end()

            if self.current_scene.next_scene == None: pg.quit(); sys.exit()
            self.current_scene = self.current_scene.next_scene

# pygame Event 이용해서 다시 구현해야됨


    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT: pg.quit(); sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pass
