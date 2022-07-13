from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from Entity.CheckPoint import CheckPoint
from Entity.Cannon import Cannon
from Item.JumpItem import JumpItem
from constants import SCREEN
import pygame as pg
from typing import Tuple


def stage1() -> Tuple[pg.sprite.Group, pg.rect.Rect, Tuple[int, int]]:
    entities = pg.sprite.Group()
    entities.add(
        Platform((SCREEN.width / 4, SCREEN.height / 10), (0, 0, 0), (0, SCREEN.height))
    )
    entities.add(
        Platform((SCREEN.width * 2, SCREEN.height / 10), (0, 0, 0), (SCREEN.width * 3/ 4, SCREEN.height))
    )
    entities.add(
        CheckPoint((120, 250, 120), (SCREEN.width, SCREEN.height * 9 / 10))
    )
    entities.add(
        Cannon((100, 100), (120, 100, 255), (SCREEN.width * 3 / 2, SCREEN.height * 1 / 2))
    )

    item = JumpItem((50, 50), (0, 0, 255), (SCREEN.width / 3, SCREEN.height * 2 / 3))

    # entities.add(item)
    
    stage_rect = pg.Rect(0, 0, SCREEN.width * 2, SCREEN.height)
    player_spawn = (0, 0)
    
    return entities, stage_rect, player_spawn
