from screeninfo import get_monitors
import pygame as pg

SCREEN = get_monitors()[0]
SCREEN.width = 1600
SCREEN.height = 900
UNITSIZE = SCREEN.height / 9
FPS = 60

CAMERA_RECT = pg.rect.Rect(SCREEN.width / 3, SCREEN.height / 3, SCREEN.width / 3, SCREEN.height / 3)

SET_SPAWN = pg.USEREVENT + 1
DESPAWN = pg.USEREVENT + 2