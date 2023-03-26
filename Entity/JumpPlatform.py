from Entity.Platform import Platform
from constants import FPS, UNITSIZE
from pygame.math import Vector2
import pygame as pg
from globals import GLOBALS


class JumpPlatform(Platform):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["springboardDown", "springboardUp"], FPS // 5)
        self.jump_active = True
        self.jump_cooldown = 0
    
    def update_active(self):
        super().update_active()
        if GLOBALS.timer == 0:
            return
        
        self.jump_cooldown -= 1

        if self.jump_active == False and self.jump_cooldown <= 0:
            self.jump_active = True
            

    def collide_player(self, player, side):
        if self.jump_active == False:
            return

        if side == "top" or side == "left" or side == "right":
            player.vel.y = - UNITSIZE // 2
            pg.mixer.Sound.play(GLOBALS.sfx_dict["Jump"])
            self.jump_active = False
            self.jump_cooldown = 10
