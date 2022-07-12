import pygame as pg
from Scene.Scene import Scene
from Entity.Player import Player
from Entity.Platform import Platform
from Entity.Item import Item
from constants import SCREEN
from helper.determine_side import determine_side
from helper.try_min_max import try_max, try_min
import math


class GameScene(Scene):
    def __init__(self, screen: pg.display, map):
        super().__init__(screen)
        self.platforms = pg.sprite.Group()
        self.items = pg.sprite.Group()

        self.player = Player()
        platform = Platform((SCREEN.width, 20), (255, 0, 0), (SCREEN.width / 2, SCREEN.height - 10))
        item = Item((50, 50), (0, 0, 255), (50, 50))

        self.platforms.add(platform)
        self.items.add(item)

        self.entityList.add(self.player)
        self.entityList.add(platform)
        self.entityList.add(item)

    def update(self):
        self.player.move()
        for entity in self.entityList:
            entity.update()
        self.handle_collision()

        super().update()

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                self.player.jump()

            if event.key == pg.K_q:
                self.kill_player()

    def handle_collision(self):
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        if hits:
            collisions = zip(
                map(lambda hit: hit.rect, hits),
                map(lambda hit: determine_side(self.player.prev_rect, hit.rect), hits)
            )
            min_top = None
            max_bottom = None
            min_left = None
            max_right = None

            for (rect, side) in collisions:
                if side == "top" and (min_top is None or rect.top < min_top):
                    min_top = rect.top
                elif side == "bottom" and (max_bottom is None or rect.bottom > max_bottom):
                    max_bottom = rect.bottom
                elif side == "left" and (min_left is None or rect.left < min_left):
                    min_left = rect.left
                elif side == "right" and (max_right is None or rect.right > max_right):
                    max_right = rect.right

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

        else:
            self.player.grounded = False

        if self.player.pos.y > 800:  # 조건 변경 필요
            self.kill_player()

    def kill_player(self):
        corpse = self.player.die()
        self.entityList.add(corpse)
        self.platforms.add(corpse)
