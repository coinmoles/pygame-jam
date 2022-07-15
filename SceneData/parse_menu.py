from typing import Callable, Dict, Final, Tuple

import pygame as pg
from pygame.math import Vector2
from Entity.BackgroundObject.DoorTop import DoorTop
from Entity.Door import Door
from Entity.GrassPlatform import GrassPlatform
from Entity.KillPlatform import KillPlatform
from Entity.Item.JumpItem import JumpItem
from Entity.Cannon import Cannon
from constants import COLORS, UNITSIZE
from Entity.Platform import Platform
from globals import GLOBALS

TOKENS: Final[Dict[str, str]] = {
    "GrassPlatform": "p",
    "SpawnPoint": "s",
}


def parse_menu(s: str) -> Callable[[], Tuple[pg.sprite.Group, pg.Rect, Tuple[int, int]]]:
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
                if i - 1 >= 0 and m[i-1][j] == TOKENS["GrassPlatform"]:
                    entities.add(GrassPlatform(position, False))
                else:
                    entities.add(GrassPlatform(position, True))

            if m[i][j] == TOKENS["SpawnPoint"]:
                player_spawn = position

            if m[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if i - 1 >= 0 and m[i-1][j] != m[i][j]:
                    entities.add(DoorTop(position))
                else:
                    entities.add(Door(position, int(m[i][j])))

    def stage():
        return entities, stage_rect, player_spawn

    return stage