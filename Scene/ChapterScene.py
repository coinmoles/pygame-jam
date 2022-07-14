from typing import Tuple
from SceneData.parse_id import parse_id
from Entity.Door import Door
from Scene.Scene import Scene
from Scene.GameScene import GameScene
from SceneData.parse_menu import parse_menu
import pygame as pg
from constants import CHANGE_SCENE


class ChapterScene(GameScene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(stage, _id)
        self.stage = parse_menu(stage)
        self.reset_stage()

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.open_door()                
                
        super().handle_event(event)

    def open_door(self):
        hits = pg.sprite.spritecollide(self.player, self.collidables, False)

        assert len(hits) <= 1
        for entity in hits:
            next_scene: Scene
            if self.id[0] == 0:
                next_scene = ChapterScene(parse_id(entity.id, 0), (entity.id, 0))
            else:
                next_scene = GameScene(parse_id(self.id[0], entity.id), (self.id[0], entity.id))

            pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene=next_scene))