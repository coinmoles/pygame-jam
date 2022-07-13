from typing import Callable, Dict, Final, Tuple

import pygame as pg
from Entity.CheckPoint import CheckPoint
from Entity.KillPlatform import KillPlatform
from Item.JumpItem import JumpItem
from constants import COLORS, UNITSIZE
from Entity.Platform import Platform

TOKENS: Final[Dict[str, str]] = {
    "Platform": "p",
    "KillPlatform": "k",
    "CheckPoint": "c",
    "JumpItem": "j",
    "SpawnPoint": "s"
}


def parse_stage(s: str) -> Callable[[], Tuple[pg.sprite.Group, pg.Rect, Tuple[int, int]]]:
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
            size = (UNITSIZE, UNITSIZE)
            item_size = (UNITSIZE / 2, UNITSIZE / 2)
            position = (UNITSIZE * j, UNITSIZE * i + UNITSIZE)

            if m[i][j] == TOKENS["Platform"]:
                entities.add(Platform(size, position))

            if m[i][j] == TOKENS["KillPlatform"]:
                entities.add(KillPlatform(size, position))

            if m[i][j] == TOKENS["CheckPoint"]:
                entities.add(CheckPoint(size, position))
            
            if m[i][j] == TOKENS["JumpItem"]:
                entities.add(JumpItem(item_size, position))

            if m[i][j] == TOKENS["SpawnPoint"]:
                player_spawn = position
    

    def stage():
        return entities, stage_rect, player_spawn
    
    return stage