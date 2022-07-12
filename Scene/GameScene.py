import pygame as pg
from Scene.Scene import Scene
from Entity.Entity import Entity
from Entity.Player import Player
from Entity.Platform import Platform
from Entity.KillPlatform import KillPlatform
from Entity.Item import Item
from constants import SCREEN
from helper.determine_side import determine_side
from helper.try_min_max import try_max, try_min
import math


class GameScene(Scene):
    def __init__(self, screen: pg.display, stage):
        super().__init__(screen)
        self.collidables = pg.sprite.Group()

        self.player = Player()
        self.add_entity(self.player)
        self.add_stage(stage)

    def update(self):
        self.player.move()
        for entity in self.entityList:
            entity.update()
        self.handle_collision()
        self.handle_despawn()
        super().update()

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jump()

            if event.key == pg.K_q:
                self.player.despawn()

    def handle_collision(self):
        hits = pg.sprite.spritecollide(self.player, self.collidables, False)

        if hits:
            sides = list(map(lambda hit: determine_side(self.player.prev_rect, hit.rect), hits))
            min_top = None
            max_bottom = None
            min_left = None
            max_right = None

            for (platform, side) in zip(hits, sides):
                if platform.passable:
                    continue
                if side == "top" and (min_top is None or platform.rect.top < min_top):
                    min_top = platform.rect.top
                elif side == "bottom" and (max_bottom is None or platform.rect.bottom > max_bottom):
                    max_bottom = platform.rect.bottom
                elif side == "left" and (min_left is None or platform.rect.left < min_left):
                    min_left = platform.rect.left
                elif side == "right" and (max_right is None or platform.rect.right > max_right):
                    max_right = platform.rect.right

            if min_top is not None:
                self.player.set_y(min_top)
                self.player.vel.y = 0
                self.player.grounded = True
            if min_left is not None:
                self.player.set_x(min_left - self.player.rect.width- 1)
                self.player.vel.x = 0
            if max_right is not None:
                self.player.set_x(max_right + 1)
                self.player.vel.x = 0
            if max_bottom is not None:
                self.player.set_y(max_bottom + self.player.rect.height + 1)
                self.player.vel.y = 0

            for (platform, side) in zip(hits, sides):
                platform.collide_player(self.player, side)

        else:
            self.player.grounded = False

        if self.player.pos.y > 800:  # 조건 변경 필요
            self.player.despawn()

    def handle_despawn(self):
        if not self.player.active:
            self.add_entity(self.player.spawn_corpse())
            self.player = Player()
            self.add_entity(self.player)
        self.entityList.remove(filter(lambda entity: not entity.active, self.entityList))

    def add_entity(self, entity: Entity):
        self.entityList.add(entity)
        if entity.collide_check:
            self.collidables.add(entity)

    def add_stage(self, stage):
        for entity in stage():
            self.add_entity(entity)
