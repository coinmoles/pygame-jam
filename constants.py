from screeninfo import get_monitors
import pygame as pg

SCREEN = get_monitors()[0]
SCREEN.width = 1600
SCREEN.height = 900
FPS = 60
