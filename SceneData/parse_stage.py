from typing import Callable, Tuple
import pygame as pg
from pygame.math import Vector2
from Entity.BackgroundObject.ControlHelp import ControlHelp
from Entity.DirtPlatform import DirtPlatform
from Entity.CheckPoint import CheckPoint
from Entity.GrassPlatform import GrassPlatform
from Entity.Item.CannonItem import CannonItem
from Entity.Spike import Spike
from Entity.JumpPlatform import JumpPlatform
from Entity.Item.JumpItem import JumpItem
from Entity.Goal import Goal
from Entity.Cannon import Cannon
from constants import PLATFORMS, TOKENS, UNITSIZE

def parse_stage(s: str, _id: Tuple[int, int]) -> Callable[[], Tuple[pg.sprite.Group, pg.Rect, Vector2]]:
    m = [list(l) for l in s.strip().split('\n')]
    
    assert len(m) > 0
    assert len(m[0]) > 0
    assert s.count(TOKENS["SpawnPoint"]) == 1

    height = len(m)
    width = len(m[0])

    entities = pg.sprite.Group()
    stage_rect = pg.Rect(0, 0, width * UNITSIZE, height * UNITSIZE)
    player_spawn = Vector2(0, 0)

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
            
            if m[i][j] == TOKENS["Spike"]:
                if i + 1 < height and m[i + 1][j] in PLATFORMS:
                    entities.add(Spike(position, 0))
                elif j - 1 >= 0 and m[i][j - 1] in PLATFORMS:
                    entities.add(Spike(position, 1))
                elif j + 1 < width and m[i][j + 1] in PLATFORMS:
                    entities.add(Spike(position, 3))
                else:
                    entities.add(Spike(position, 2))                 

            if m[i][j] == TOKENS["JumpPlatform"]:
                entities.add(JumpPlatform(position))

            if m[i][j] == TOKENS["JumpItem"]:
                entities.add(JumpItem(position))
            
            if m[i][j] == TOKENS["CannonItem"]:
                entities.add(CannonItem(position))

            if m[i][j] == TOKENS["CheckPoint"]:
                entities.add(CheckPoint(position))
            
            if m[i][j] == TOKENS["JumpItem"]:
                entities.add(JumpItem(position))

            if m[i][j] == TOKENS["Goal"]:
                entities.add(Goal(position, _id))
            
            for k in range(1, 10):
                if m[i][j] == TOKENS["Control" + str(k)]:
                    entities.add(ControlHelp(position, k))
        
            for k in range(4):
                if m[i][j] == TOKENS["Cannon" + str(k)]:
                    if i - 1 >= 0 and m[i-1][j] in PLATFORMS:
                        entities.add(DirtPlatform(position, False))
                    else:
                        entities.add(DirtPlatform(position, True))
                    entities.add(Cannon(position, k))

            if m[i][j] == TOKENS["SpawnPoint"]:
                player_spawn = position

    def stage():
        return entities, stage_rect, player_spawn
    
    return stage
