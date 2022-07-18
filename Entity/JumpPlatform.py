from Entity.Platform import Platform
from constants import FPS, UNITSIZE
from pygame.math import Vector2
import pygame as pg
from globals import GLOBALS


class JumpPlatform(Platform):
    def __init__(self, pos: Vector2):
        super().__init__(pos, ["springboardDown", "springboardUp"], FPS // 5)
        
    def collide_player(self, player, side):
        if side == "top" or side == "left" or side == "right":
            player.vel.y = - UNITSIZE // 2
            pg.mixer.Sound.play(GLOBALS.sfx_dict["Jump"])
