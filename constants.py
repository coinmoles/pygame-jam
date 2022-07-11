from screeninfo import get_monitors
import pygame as pg

SCREEN = get_monitors()[0]
SCREEN.width = 1600
SCREEN.height = 900
UNITSIZE = SCREEN.height / 9
FPS = 60
