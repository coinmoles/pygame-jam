from re import S
from tkinter import UNITS
from typing import Tuple
from Entity.Door import Door
from Entity.BackgroundObject.ControlHelp import ControlHelp
from Scene.GameScene import GameScene
from SceneData.parse_menu import parse_menu
import pygame as pg
from constants import CHANGE_SCENE, OPEN_LOAD, OPEN_SAVE, UNITSIZE
from globals import GLOBALS


class ChapterScene(GameScene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(stage, _id)
        self.stage = parse_menu(stage, _id[0])
        self.set_stage()
        self.music_path = "assets/sound/music/WorldmapTheme.mp3"

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.open_door()
            elif event.key == pg.K_d:
                pg.event.post(pg.event.Event(OPEN_SAVE, current_id=self.id))
            elif event.key == pg.K_f:
                pg.event.post(pg.event.Event(OPEN_LOAD, current_id=self.id))

            if event.key == pg.K_ESCAPE:
                if self.id[0] == 0:
                    return
                else:
                    pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(0, 0)))
            
        super().handle_event(event)

    def open_door(self):
        hits = list(filter(lambda hit: isinstance(hit, Door), pg.sprite.spritecollide(self.player, self.collidables, False)))
        
        if len(hits) == 0:
            return

        entity = hits[0]

        if entity.locked:
            return
        
        self.player.active = False

        if self.id[0] == 0:
            pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(entity.id, 0)))
        else:
            if entity.id == 9:
                GLOBALS.clear_stage((self.id, 0))
                pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(0, 0)))   
            else:
                pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], entity.id)))
