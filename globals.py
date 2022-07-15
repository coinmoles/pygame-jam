from typing import Union
import pygame as pg
from typing import Dict
import os
from constants import UNITSIZE


class GameGlobals:
    def __init__(self):
        self.screen: Union[pg.Surface, None] = None
        self.images: Dict[str, pg.Surface] = {}

    def set_screen(self, screen: pg.Surface):
        self.screen = screen

    def load_images(self):
        path = './assets/images'
        file_names = [f for f in os.listdir(path) if f.endswith('.png')]
        for name in file_names:
            image_name = os.path.splitext(name)[0]
            image = pg.image.load(os.path.join(path, name)).convert_alpha()
            self.images[image_name] = pg.transform.scale(image, (UNITSIZE, UNITSIZE))


GLOBALS = GameGlobals()
