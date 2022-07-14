from typing import Union
import pygame as pg


class GameGlobals:
    def __init__(self):
        self.screen: Union[pg.Surface, None] = None

    def set_screen(self, screen: pg.Surface):
        self.screen = screen


GLOBALS = GameGlobals()
