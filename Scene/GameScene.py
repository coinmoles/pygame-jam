from typing import Tuple
import pygame as pg
from pygame.math import Vector2
from Scene.Scene import Scene
from Entity.Entity import Entity
from Entity.Item.Item import Item
from Entity.Player import Player
from constants import PLAYER_DEATH, SCREEN, CAMERA_RECT, SET_SPAWN, DESPAWN, SPAWN, TRANSFORM, TRANSFORM_END, UNITSIZE
from globals import GLOBALS
from helper.determine_side import determine_side
from collections import deque
from typing import Deque

MAX_CORPSE = 5


class GameScene(Scene):
    def __init__(self, stage: str, _id: Tuple[int, int]):
        super().__init__(_id)
        self.collidables = pg.sprite.Group()
        self.despawned = pg.sprite.Group()
        self.corpses: Deque[pg.sprite.Sprite] = deque()
        self.stage_rect = pg.Rect(0, 0, 0, 0)
        self.player_spawn = Vector2(0, 0)
        self.stage = lambda : (pg.sprite.Group(), pg.Rect(0, 0, 0, 0), Vector2(0, 0))

        self.player = Player(self.player_spawn)
        self.stage_rect = pg.rect.Rect(0, 0, SCREEN.width, SCREEN.height)

    def update(self):
        # 플레이어 이동
        self.player.move()

        # 엔티티 위치 확정
        for entity in self.entityList:
            entity.update(self.camera_base)
        self.handle_collision()

        # 카메라 이동
        self.move_camera()

        # 엔티티 그리기
        super().update()

    def scene_end(self):
        super().scene_end()
        self.entityList.empty()
        self.collidables.empty()
        self.despawned.empty()

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if self.player.active:
                if event.key == pg.K_SPACE:
                    if self.player.active:
                        self.player.jump()
                if event.key == pg.K_ESCAPE:
                    self.player.despawn()
                if event.key == pg.K_w:
                    self.reset_stage()
                if event.key == pg.K_q:
                    corpse = self.corpses.pop()
                    self.despawn_entity(corpse)
        
        elif event.type == SET_SPAWN:
            self.player_spawn = event.spawn

        elif event.type == SPAWN:
            entity: Entity = event.entity
            self.spawn_entity(entity)

        elif event.type == DESPAWN:
            entity: Entity = event.entity
            self.despawn_entity(entity)

        elif event.type == PLAYER_DEATH:
            if self.player.active:
                self.player_death()
        
        elif event.type == TRANSFORM:
            if self.player.active:
                self.player.active = False
                self.player.paused = True
                self.player.set_transform(event.item_id)
                self.player.set_animation("transform")
                pg.time.set_timer(TRANSFORM_END, 1000, 1)

        elif event.type == TRANSFORM_END:
            self.player.active = True
            self.player.paused = False
            self.player.set_animation("stand")

    def handle_collision(self):
        hits = pg.sprite.spritecollide(self.player, self.collidables, False)

        if hits:
            sides = list(map(lambda hit: determine_side(self.player.prev_rect, hit.rect), hits))
            min_top = None
            max_bottom = None
            min_left = None
            max_right = None

            for (entity, side) in zip(hits, sides):
                if entity.passable:
                    continue

                if side == "top" and (min_top is None or entity.rect.top < min_top):
                    min_top = entity.rect.top
                elif side == "bottom" and (max_bottom is None or entity.rect.bottom > max_bottom):
                    max_bottom = entity.rect.bottom
                elif side == "left" and (min_left is None or entity.rect.left < min_left):
                    min_left = entity.rect.left
                elif side == "right" and (max_right is None or entity.rect.right > max_right):
                    max_right = entity.rect.right

            if min_top is not None:
                self.player.set_y(min_top - UNITSIZE)
                self.player.vel.y = 0
                self.player.grounded = True
            else:
                self.player.grounded = False
            
            if min_left is not None:
                self.player.set_x(min_left - UNITSIZE * 2 / 3 - 1)
                self.player.vel.x = 0
            if max_right is not None:
                self.player.set_x(max_right)
                self.player.vel.x = 0
            if max_bottom is not None:
                self.player.set_y(max_bottom)
                self.player.vel.y = 0

            for (entity, side) in zip(hits, sides):
                entity.collide_player(self.player, side)
        else:
            self.player.grounded = False

        if self.player.rect.right > self.stage_rect.width:
            self.player.set_x(self.stage_rect.width)
        elif self.player.rect.left < 0:
            self.player.set_x(0)

        if self.player.rect.bottom > self.stage_rect.bottom:
            self.player.despawn()
        elif self.player.rect.top < 0:
            self.player.set_y(0)

        # if self.player.center.y > 800:  # 조건 변경 필요
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

    def spawn_entity(self, entity: Entity):
        self.entityList.add(entity)
        if entity.collide_check:
            self.collidables.add(entity)

    def despawn_entity(self, entity: Entity):
        if entity == self.player:
            corpse = self.player.spawn_corpse()
            self.corpses.append(corpse)
            self.spawn_entity(corpse)

            if len(self.corpses) > MAX_CORPSE:
                corpse = self.corpses.popleft()
                corpse.despawn()

            self.player = Player(self.player_spawn)
            self.spawn_entity(self.player)

        if isinstance(entity, Item):
            self.despawned.add(entity)
        
        self.collidables.remove(entity)
        self.entityList.remove(entity)

    def player_death(self):        
        self.player.active = False
        self.player.paused = True
        pg.mixer.Sound.play(GLOBALS.sfx_dict["Lose1"])
        self.player.set_animation("death")
        pg.time.set_timer(pg.event.Event(DESPAWN, entity=self.player), 500, 1)

    def set_stage(self):
        self.entityList = pg.sprite.Group()
        self.collidables = pg.sprite.Group()
        self.corpses: Deque[pg.sprite.Sprite] = deque()

        entities, stage_rect, player_spawn = self.stage()
        for entity in entities:
            self.spawn_entity(entity)

        self.stage_rect = stage_rect
        self.player_spawn = player_spawn
        self.player = Player(self.player_spawn)
        self.spawn_entity(self.player)

    def reset_stage(self):
        for corpse in self.corpses:
            self.despawn_entity(corpse)
        
        for entity in self.despawned:
            self.spawn_entity(entity)
            
        self.collidables.remove(self.player)
        self.entityList.remove(self.player)
        self.player = Player(self.player_spawn)
        self.spawn_entity(self.player)
