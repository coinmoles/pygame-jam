from pickle import GLOBAL
from typing import Tuple
import pygame as pg
from pygame.math import Vector2
from Scene.GameScene import GameScene
from SceneData.parse_stage import parse_stage
from constants import CHANGE_SCENE, PLAY_SFX, PLAYER_DEATH, PLAYER_JUMP, SET_CHECKPOINT, STAGE_CLEAR
from globals import GLOBALS

MAX_CORPSE = 5


class StageScene(GameScene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(stage, _id)
        self.stage = parse_stage(stage, _id)
        self.set_stage()

        self.music_path = "assets/sound/music/GrasslandsTheme.mp3"
    
    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], 0)))

        if event.type == STAGE_CLEAR:
            self.stage_clear()
        
        elif event.type == PLAYER_JUMP:
            self.player.jump()

        elif event.type == PLAY_SFX:
            pg.mixer.Sound.play(GLOBALS.sfx_dict[event.sfx])
    
    def stage_clear(self):
        self.player.active = False
        self.player.vel = Vector2(0, 0)
        self.player.acc = Vector2(0, 0)
        self.player.set_animation("walk")
        GLOBALS.clear_stage(self.id)
        pg.time.set_timer(pg.event.Event(PLAY_SFX, sfx="WinJazzGuitar"), 1000, 1)
        pg.time.set_timer(PLAYER_JUMP, 2500, 1)
        pg.time.set_timer(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], 0)), 3000, 1)
