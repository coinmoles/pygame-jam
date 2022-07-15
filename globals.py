from typing import Union
import pygame as pg
from typing import Dict
import os
from constants import UNITSIZE


class GameGlobals:
    def __init__(self):
        self.screen: Union[pg.Surface, None] = None
        self.images: Dict[str, pg.Surface] = {}
        self.image_rect: Dict[str, pg.Rect] = {}

    def set_screen(self, screen: pg.Surface):
        self.screen = screen

    def load_images(self):
        path = './assets/images'
        for subdir, dirs, file_names in os.walk(path):
            for name in file_names:
                if not name.endswith('.png'):
                    continue
                image_name = os.path.splitext(name)[0]
                image = pg.transform.scale(pg.image.load(os.path.join(subdir, name)).convert_alpha(), (UNITSIZE, UNITSIZE))
                self.images[image_name] = image
                self.image_rect[image_name] = pg.mask.from_surface(image).get_bounding_rects()[0]
        


GLOBALS = GameGlobals()
