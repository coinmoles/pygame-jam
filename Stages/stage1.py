from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from Entity.Item import Item
from constants import SCREEN
import pygame as pg

def stage1() -> pg.sprite.Group: 
    entities = pg.sprite.Group()
    platform = KillPlatform((SCREEN.width, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height / 2))
    item = Item((50, 50), (0, 0, 255), (50, 50))

    entities.add(item)
    entities.add(platform)
    entities.add(Platform((SCREEN.width, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height - 10)))
    entities.add(Platform((SCREEN.width, 80), (0, 255, 0), (SCREEN.width / 2, SCREEN.height - 10)))
    return entities