from typing import Tuple
from Scene.GameScene import GameScene
from SceneData.parse_menu import parse_menu
import pygame as pg
from constants import CHANGE_SCENE


class ChapterScene(GameScene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(stage, _id)
        self.stage = parse_menu(stage)
        self.set_stage()
        self.music_path = "assets/sound/music/WorldmapTheme.mp3"

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.open_door()                
                
        super().handle_event(event)

    def open_door(self):
        hits = pg.sprite.spritecollide(self.player, self.collidables, False)
        
        if len(hits) == 0:
            return

        entity = hits[0]
        if self.id[0] == 0:
            pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(entity.id, 0)))
        else:
            pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(self.id[0], entity.id)))
