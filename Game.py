from errno import EEXIST
import imp
from typing import Tuple
import pygame as pg
# from SceneData.chapter1 import chapter1, main_menu, stages
from SceneData.chapter_menu.chapter1 import chapter1
from Scene.ChapterScene import ChapterScene
from constants import *
from Scene.GameScene import GameScene
from globals import GLOBALS
import sys


class Game:
    def __init__(self):
        pg.init()
        GLOBALS.set_screen(pg.display.set_mode((SCREEN.width, SCREEN.height), 0, 32))
        # self.currentScene = GameScene(self.screen, chapter1[0])
        self.current_scene = ChapterScene(chapter1, (1, 1))
        self.clock = pg.time.Clock()

    def run(self):
        self.current_scene.scene_start()

        while True:
            for event in pg.event.get():
                self.handle_event(event)
                self.current_scene.handle_event(event)
            self.current_scene.update()

            pg.display.update()
            self.clock.tick(FPS)

# pygame Event 이용해서 다시 구현해야됨
    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pass
        elif event.type == CHANGE_SCENE:
            if event.next_scene is None:
                pg.event.post(pg.event.Event(pg.QUIT))
            else:
                self.current_scene.scene_end()
                self.current_scene = event.next_scene
