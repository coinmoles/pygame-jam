import pygame as pg
from Scene.Scene import Scene
from Entity.Entity import Entity
from Entity.Player import Player
from Item.BumperItem import BumperItem
from constants import SCREEN, CAMERA_RECT, SET_SPAWN, DESPAWN
from helper.determine_side import determine_side


class GameScene(Scene):
    def __init__(self, screen: pg.display, stage):
        super().__init__(screen)
        self.collidables = pg.sprite.Group()
        self.player_spawn = (0, 0)
        self.player = Player(self.player_spawn)
        self.add_entity(self.player)
        self.add_stage(stage)

        self.stage_rect = pg.rect.Rect(0, 0, SCREEN.width * 2, SCREEN.height)
        self.player_spawn = (0, 0)

    def update(self):
        # 플레이어 이동
        self.player.move()

        # 엔티티 위치 확정
        for entity in self.entityList:
            entity.update()
        self.handle_collision()

        # 카메라 이동
        self.move_camera()

        # 엔티티 그리기
        super().update()

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jump()

            if event.key == pg.K_q:
                self.player.despawn()

        if event.type == SET_SPAWN:
            self.player_spawn = event.spawn

        if event.type == DESPAWN:
            entity: Entity = event.entity
            if entity == self.player:
                self.add_entity(self.player.spawn_corpse())
                self.player = Player(self.player_spawn)
                self.add_entity(self.player)
            self.entityList.remove(entity)
            self.collidables.remove(entity)

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

        if self.player.rect.right > self.stage_rect.width:
            self.player.set_x(self.stage_rect.width - self.player.rect.width)
        elif self.player.rect.left < 0:
            self.player.set_x(0)

        if self.player.rect.bottom > self.stage_rect.bottom:
            self.player.despawn()
        elif self.player.rect.top < 0:
            self.player.set_y(self.player.rect.height)

        # if self.player.pos.y > 800:  # 조건 변경 필요
        #     self.player.despawn()

    def move_camera(self):
        if self.player.rect.right - self.camera_base.x > CAMERA_RECT.right:
            self.camera_base.x = self.player.rect.right - CAMERA_RECT.right
        elif self.player.rect.left - self.camera_base.x < CAMERA_RECT.left:
            self.camera_base.x = self.player.rect.left - CAMERA_RECT.left
        if self.player.rect.top - self.camera_base.y < CAMERA_RECT.top:
            self.camera_base.y = self.player.rect.top - CAMERA_RECT.top
        elif self.player.rect.bottom - self.camera_base.y > CAMERA_RECT.bottom:
            self.camera_base.y = self.player.rect.bottom - CAMERA_RECT.bottom

        if self.camera_base.x < 0:
            self.camera_base.x = 0
        elif self.stage_rect.width - self.camera_base.x < SCREEN.width:
            self.camera_base.x = self.stage_rect.width - SCREEN.width
        if self.camera_base.y < 0:
            self.camera_base.y = 0
        elif self.stage_rect.height - self.camera_base.y < SCREEN.height:
            self.camera_base.y = self.stage_rect.height - SCREEN.height

    def add_entity(self, entity: Entity):
        self.entityList.add(entity)
        if entity.collide_check:
            self.collidables.add(entity)

    def add_stage(self, stage):
        for entity in stage():
            self.add_entity(entity)
