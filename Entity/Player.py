from Entity.Corpse.Corpse import Corpse
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

P0_STAND = [
    "p1_stand"
]

P0_WALK = [
    "p1_walk01", "p1_walk02", "p1_walk03", "p1_walk04", "p1_walk05", 
    "p1_walk06", "p1_walk07", "p1_walk08", "p1_walk09", "p1_walk10", "p1_walk11"
]

P0_JUMP = [
    "p1_jump"
]

P0_DEATH = [
    "p1_hurt", "p1_duck"
]

P1_STAND = [
    "p2_stand"
]

P1_WALK = [
    "p2_walk01", "p2_walk02", "p2_walk03", "p2_walk04", "p2_walk05", 
    "p2_walk06", "p2_walk07", "p2_walk08", "p2_walk09", "p2_walk10", "p2_walk11"
]

P1_JUMP = [
    "p2_jump"
]

P1_DEATH = [
    "p2_hurt", "p2_duck"
]

P2_STAND = [
    "p3_stand"
]

P2_WALK = [
    "p3_walk01", "p3_walk02", "p3_walk03", "p3_walk04", "p3_walk05", 
    "p3_walk06", "p3_walk07", "p3_walk08", "p3_walk09", "p3_walk10", "p3_walk11"
]

P2_JUMP = [
    "p3_jump"
]

P2_DEATH = [
    "p3_hurt", "p3_duck"
]

ANIMS = {
    0: {
        "stand": P0_STAND,
        "walk": P0_WALK,
        "death": P0_DEATH,
        "jump": P0_JUMP
    },
    1: {
        "stand": P1_STAND,
        "walk": P1_WALK,
        "death": P1_DEATH,
        "jump": P1_JUMP
    }, 
    2: {
        "stand": P2_STAND,
        "walk": P2_WALK,
        "death": P2_DEATH,
        "jump": P2_JUMP
    },
}

class Player(Entity):
    def __init__(self, pos: Vector2):
        super().__init__(pos, P0_STAND, FPS // 10)
        self.collide_check = False
        self.passable = True

        self.spawn_point = Vector2(30, 30)
        self.ability: Callable[[], Corpse] = lambda player: Corpse(player.pos - Vector2(UNITSIZE / 6, 0), player.flip)
        self.prev_rect = self.rect.copy()
        self.drect = pg.rect.Rect(0, 0, UNITSIZE * 2 / 3, UNITSIZE)

        self.cur_animation = "stand"

        self.prev_transform = 0
        self.transform = 0

        self.grounded = True
        self.paused = False

    def move(self):
        self.acc = Vector2(0, 0.8)

        if not self.active or self.paused:
            return
        
        pressed_keys = pg.key.get_pressed()

        if self.grounded:
            if pressed_keys[pg.K_LEFT]:
                self.vel.x = GROUND_ACC / GROUND_FRIC
                self.flip = (True, False)
                self.set_animation("walk")
            elif pressed_keys[pg.K_RIGHT]:
                self.vel.x = - GROUND_ACC / GROUND_FRIC
                self.flip = (False, False)
                self.set_animation("walk")
            else:
                self.set_animation("stand")
        else:
            if pressed_keys[pg.K_LEFT]:
                self.acc.x = -AIR_ACC
            elif pressed_keys[pg.K_RIGHT]:
                self.acc.x = AIR_ACC

    def jump(self):
        if self.paused:
            return
        
        if self.grounded or not self.active:
            self.vel.y = -30
            self.grounded = False
            pg.mixer.Sound.play(GLOBALS.sfx_dict["Jump"])
            self.set_animation("jump")

    def update(self, camera_base: Vector2): 
        self.sprite_index = ((GLOBALS.timer - self.sprites_start) // self.freq) % self.sprites_len
        self.surf = GLOBALS.images[self.sprites[self.sprite_index]]

        if self.flip[0] or self.flip[0]:
            self.surf = pg.transform.flip(self.surf, self.flip[0], self.flip[1])
   
        if self.paused:
            return
        
        self.prev_rect = self.rect.copy()
    
        if self.grounded:
            self.acc += self.vel * GROUND_FRIC
        else:
            self.acc += self.vel * AIR_FRIC
        
        self.vel += self.acc
        self.set_pos(self.pos + self.vel + 0.5 * self.acc)

    def update_active(self):
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
        if animation_key == self.cur_animation:
            return
        self.cur_animation = animation_key

        if animation_key == "stand":
            self.set_sprites(ANIMS[self.transform]["stand"], 1)
        elif animation_key == "walk":
            self.set_sprites(ANIMS[self.transform]["walk"], FPS // 10)
        elif animation_key == "jump":
            self.set_sprites(ANIMS[self.transform]["jump"], 1)
        elif animation_key == "death":
            self.set_sprites(ANIMS[self.transform]["death"], FPS * 3 // 10)
        elif animation_key == "transform":
            self.set_sprites([ANIMS[self.prev_transform]["stand"][0], ANIMS[self.transform]["stand"][0]], FPS // 6)
    
    def set_transform(self, item_id: int):
        self.prev_transform = self.transform
        self.transform = item_id

    def set_ability(self, ability: Callable[[Vector2, Vector2], Entity]):
        self.ability = ability
