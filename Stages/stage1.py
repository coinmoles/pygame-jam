from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from Entity.CheckPoint import CheckPoint
from Item.JumpItem import JumpItem
from Stages.parser import parse_stage
from constants import SCREEN
import pygame as pg


def stage1() -> pg.sprite.Group: 
    entities = pg.sprite.Group()
    platform = KillPlatform((SCREEN.width, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height / 2))
    checkpoint = CheckPoint((120, 250, 120), (SCREEN.width / 4, SCREEN.height / 2))
    item = JumpItem((50, 50), (0, 0, 255), (SCREEN.width / 3, SCREEN.height * 2 / 3))

    entities.add(item)
    entities.add(platform)
    entities.add(checkpoint)
    entities.add(Platform((SCREEN.width, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height - 10)))
    entities.add(Platform((SCREEN.width, 80), (0, 255, 0), (SCREEN.width / 2, SCREEN.height - 10)))
    
    stage_rect = pg.Rect(0, 0, SCREEN.width * 2, SCREEN.height)
    player_spawn = (0, 0)
    
    return entities, stage_rect, player_spawn


stage2 = parse_stage("""
................................
...............c................
............ppppppp.............
......c.....p.....p.......pppppp
.....ppppkkkp.....p.......k.....
.....p............p.......k.....
.s..jp............p.......k.....
pppppp............pkkkkkkkk.....
................................
""")