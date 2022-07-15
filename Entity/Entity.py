import pygame as pg
from pygame.math import Vector2
from globals import GLOBALS
from constants import SCREEN, DESPAWN, UNITSIZE
from typing import List


class Entity(pg.sprite.Sprite):
    def __init__(self, pos: Vector2, sprites: List[str], freq: int):
        super().__init__()
        assert len(sprites) >= 1

        self.active = True
        self.collide_check = False
        self.passable = False

        self.sprites = sprites
        self.sprites_len = len(sprites)
        self.sprites_start = 0
        self.sprite_index = 0

        self.surf = GLOBALS.images[sprites[0]]
        self.rect = GLOBALS.image_rect[sprites[0]]
        self.drect = self.surf.get_rect()
        self.freq = freq

        self.pos = Vector2(0, 0)
        self.set_pos(pos)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def update(self, camera_base: Vector2, timer: int):
        if self.active:
            self.update_active(timer)
        self.check_active(camera_base)
        

    def update_active(self, timer):
        self.sprite_index = ((timer - self.sprites_start) // self.freq) % self.sprites_len
        self.surf = GLOBALS.images[self.sprites[self.sprite_index]]
        
        self.vel += self.acc
        self.set_pos(self.pos + self.vel + 0.5 * self.acc)

    def collide_player(self, player, side):
        pass

    def check_active(self, camera_base):
        rel_rect = self.rect.move(-camera_base)

        if rel_rect.left > SCREEN.width + UNITSIZE or rel_rect.right < -UNITSIZE \
                or rel_rect.top > SCREEN.height + UNITSIZE or rel_rect.bottom < -UNITSIZE:
            self.active = False
        else:
            self.active = True

    def set_pos(self, pos: Vector2):
        self.pos = pos
        self.rect = GLOBALS.image_rect[self.sprites[self.sprite_index]].move(self.pos)

    def set_x(self, x: int):
        self.pos.x = x
        self.rect = GLOBALS.image_rect[self.sprites[self.sprite_index]].move(self.pos)

    def set_y(self, y: int):
        self.pos.y = y
        self.rect = GLOBALS.image_rect[self.sprites[self.sprite_index]].move(self.pos)

    def set_sprites(self, sprites: List[pg.Surface], timer: int):
        self.sprites = sprites
        self.sprites_len = len(sprites)
        self.sprites_start = 0

    def despawn(self):
        pg.event.post(pg.event.Event(DESPAWN, entity=self))

    def draw(self, camera_base, timer: int):
        GLOBALS.screen.blit(self.surf, self.drect.move(self.pos - camera_base))
