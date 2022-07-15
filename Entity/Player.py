from Entity.Corpse import Corpse
from Entity.Entity import Entity
from constants import FPS, UNITSIZE
from pygame.math import Vector2
import pygame as pg
from typing import Callable, List

from globals import GLOBALS

GROUND_ACC = 1.0
AIR_ACC = 0.3
GROUND_FRIC = -0.15
AIR_FRIC = -0.05

P1_WALK = [
    "p1_walk01", "p1_walk02", "p1_walk03", "p1_walk04", "p1_walk05", 
    "p1_walk06", "p1_walk07", "p1_walk08", "p1_walk09", "p1_walk10", "p1_walk11"
]

P1_DEATH = [
    "p1_hurt"
]


class Player(Entity):
    def __init__(self, pos: Vector2):
        super().__init__(pos, P1_WALK, FPS // 10)
        self.collide_check = False
        self.passable = True

        self.spawn_point = Vector2(30, 30)
        self.ability: Callable[[], Corpse] = lambda player: Corpse(player.pos - Vector2(UNITSIZE / 6, 0))
        self.prev_rect = self.rect.copy()
        self.drect = pg.rect.Rect(0, 0, UNITSIZE * 2 / 3, UNITSIZE)

        self.grounded = True
        self.dead = False
        self.last_direction = "r"

    def move(self):
        if self.dead:
            self.acc = Vector2(0, 0)
            return
        
        self.acc = Vector2(0, 0.8)

        if not self.active:
            return
        
        pressed_keys = pg.key.get_pressed()

        if self.grounded:
            if pressed_keys[pg.K_LEFT]:
                self.vel.x = GROUND_ACC / GROUND_FRIC
                self.last_direction = "l"
                self.set_animation("walkLeft")
            elif pressed_keys[pg.K_RIGHT]:
                self.vel.x = - GROUND_ACC / GROUND_FRIC
                self.last_direction = "r"
                self.set_animation("walkRight")
            else:
                if self.last_direction == "r":
                    self.set_animation("standRight")
                else:
                    self.set_animation("standLeft")
        else:
            if pressed_keys[pg.K_LEFT]:
                self.acc.x = -AIR_ACC
            elif pressed_keys[pg.K_RIGHT]:
                self.acc.x = AIR_ACC

    def jump(self):
        if self.grounded or not self.active:
            self.vel.y = -30
            self.grounded = False
            if self.last_direction == "r":
                self.set_animation("jumpRight")
            else:
                self.set_animation("jumpLeft")

    def update(self, camera_base: Vector2, timer: int):
        self.prev_rect = self.rect.copy()
        
        if self.grounded:
            self.acc += self.vel * GROUND_FRIC
        else:
            self.acc += self.vel * AIR_FRIC

        self.sprite_index = ((timer - self.sprites_start) // self.freq) % self.sprites_len
        self.surf = GLOBALS.images[self.sprites[self.sprite_index]]
        if self.flip[0] or self.flip[0]:
            self.surf = pg.transform.flip(self.surf, self.flip[0], self.flip[1])
        
        self.vel += self.acc
        self.set_pos(self.pos + self.vel + 0.5 * self.acc)

    def update_active(self, timer: int):
        pass

    def check_active(self, camera_base):
        return

    def spawn_corpse(self):
        return self.ability(self)

    def set_pos(self, pos: Vector2):
        self.pos = pos
        self.rect = pg.rect.Rect(self.pos, (UNITSIZE * 2 / 3, UNITSIZE))

    def set_x(self, x: int):
        self.pos.x = x
        self.rect = pg.rect.Rect(self.pos, (UNITSIZE * 2 / 3, UNITSIZE))

    def set_y(self, y: int):
        self.pos.y = y
        self.rect = pg.rect.Rect(self.pos, (UNITSIZE * 2 / 3 , UNITSIZE))

    def set_animation(self, animation_key: str):
        if (animation_key == "standRight"):
            self.set_sprites(["p1_stand"], 1)
            self.flip = (False, False)
        elif (animation_key == "jumpRight"):
            self.set_sprites(["p1_jump"], 1)
            self.flip = (False, False)
        elif (animation_key == "walkRight"):
            self.set_sprites(P1_WALK, FPS // 10)
            self.flip = (False, False)
        elif (animation_key == "standLeft"):
            self.set_sprites(["p1_stand"], 1)
            self.flip = (True, False)
        elif (animation_key == "jumpLeft"):
            self.set_sprites(["p1_jump"], 1)
            self.flip = (True, False)
        elif (animation_key == "walkLeft"):
            self.set_sprites(P1_WALK, FPS // 10)
            self.flip = (True, False)
        elif (animation_key == "death"):
            self.set_sprites(P1_DEATH, 1)

    def set_ability(self, ability: Callable[[Vector2, Vector2], Entity]):
        self.ability = ability
