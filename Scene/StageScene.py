from typing import Tuple
import pygame as pg
from pygame.math import Vector2
from Scene.GameScene import GameScene
from SceneData.parse_stage import parse_stage
from constants import CHANGE_SCENE, PLAYER_DEATH, PLAYER_JUMP, SET_CHECKPOINT, STAGE_CLEAR

MAX_CORPSE = 5


class StageScene(GameScene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(stage, _id)
        self.stage = parse_stage(stage, _id)
        self.set_stage(True)

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == STAGE_CLEAR:
            self.stage_clear()
        
        if event.type == PLAYER_JUMP:
            self.player.jump()
    
    def stage_clear(self):
        self.player.active = False
        self.player.vel = Vector2(0, 0)
        self.player.acc = Vector2(0, 0)
        self.player.set_animation("stand")
        pg.time.set_timer(PLAYER_JUMP, 200, 1)
        pg.time.set_timer(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], 0)), 1000, 1)
