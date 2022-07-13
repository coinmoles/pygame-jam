from typing import Tuple
from Chapters.parse_key import build_scene
from Entity.Door import Door
from Scene.GameScene import GameScene
import pygame as pg


class ChapterScene(GameScene):
    def __init__(self, screen: pg.display, stage, _id: Tuple[int, int]):
        super().__init__(screen, stage, _id)

    def handle_event(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                self.open_door()                
                
        super().handle_event(event)

    def open_door(self):
        hits = pg.sprite.spritecollide(self.player, self.collidables, False)

        for entity in hits:
            if isinstance(entity, Door):
                print("here")
