from typing import Callable, Tuple
import pygame as pg
from pygame.math import Vector2
from Entity.BackgroundObject.ControlHelp import ControlHelp
from Entity.BackgroundObject.DoorTop import DoorTop
from Entity.Door import Door
from Entity.GrassPlatform import GrassPlatform
from Entity.DirtPlatform import DirtPlatform
from Entity.JumpPlatform import JumpPlatform
from constants import PLATFORMS, TOKENS, UNITSIZE
from globals import GLOBALS


def parse_menu(s: str, cur_id: int) -> Callable[[], Tuple[pg.sprite.Group, pg.Rect, Tuple[int, int]]]:
    m = [list(l) for l in s.strip().split('\n')]

    assert len(m) > 0
    assert len(m[0]) > 0
    assert s.count(TOKENS["SpawnPoint"]) == 1

    height = len(m)
    width = len(m[0])

    entities = pg.sprite.Group()
    stage_rect = pg.Rect(0, 0, width * UNITSIZE, height * UNITSIZE)
    player_spawn = (0, 0)

    for i in range(height):
        for j in range(width):
            position = Vector2(UNITSIZE * j, UNITSIZE * i)

            if m[i][j] == TOKENS["GrassPlatform"]:
                if i - 1 >= 0 and m[i-1][j] in PLATFORMS:
                    entities.add(GrassPlatform(position, False))
                else:
                    entities.add(GrassPlatform(position, True))

            if m[i][j] == TOKENS["DirtPlatform"]:
                if i - 1 >= 0 and m[i-1][j] in PLATFORMS:
                    entities.add(DirtPlatform(position, False))
                else:
                    entities.add(DirtPlatform(position, True))

            if m[i][j] == TOKENS["JumpPlatform"]:
                entities.add(JumpPlatform(position))

            if m[i][j] == TOKENS["SpawnPoint"]:
                player_spawn = position
            
            for k in range(1, 10):
                if m[i][j] == TOKENS["Control" + str(k)]:
                    entities.add(ControlHelp(position, k))

            if m[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                locked = True
                if cur_id == 0:
                    if int(m[i][j]) == 1 or (int(m[i][j]) - 1, 0) in GLOBALS.cleared_stages:
                        locked = False
                else:
                    if int(m[i][j]) == 1 or (cur_id, int(m[i][j]) - 1) in GLOBALS.cleared_stages:
                        locked = False
                
                entities.add(DoorTop(position - Vector2(0, UNITSIZE), locked))
                entities.add(Door(position, int(m[i][j]), locked))

    def stage():
        return entities, stage_rect, player_spawn

    return stage