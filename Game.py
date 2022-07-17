import pygame as pg
from SceneData.main_menu import main_menu
from Scene.IntroScene import IntroScene
from constants import *
from SceneData.parse_id import parse_id
from globals import GLOBALS
import sys


class Game:
    def __init__(self):
        pg.init()
        GLOBALS.set_screen(pg.display.set_mode((SCREEN.width, SCREEN.height), 0, 32))
        GLOBALS.load_images()
        GLOBALS.load_sounds()
        self.current_scene = IntroScene()
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

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        elif event.type == CHANGE_SCENE:
            if event.next_scene_id is None:
                pg.event.post(pg.event.Event(pg.QUIT))
            else:
                self.current_scene.scene_end()
                self.current_scene = parse_id(*event.next_scene_id)
                self.current_scene.scene_start()

