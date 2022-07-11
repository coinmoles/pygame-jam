from Entity.Entity import Entity
from constants import SCREEN
from pygame.math import Vector2
import pygame as pg

ACC = 0.5
FRIC = -0.12


class Player(Entity):
    def __init__(self):
        super().__init__((30, 30), (128, 255, 40), (10, 420))

        self.pos = Vector2((10, 385))
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

    def move(self):
        pressed_keys = pg.key.get_pressed()
        if pressed_keys[pg.K_LEFT]:
            self.acc.x = -ACC
        elif pressed_keys[pg.K_RIGHT]:
            self.acc.x = ACC
        else:
            self.acc = Vector2(0, 0)

    def update(self):
        self.acc.x += self.vel.x * FRIC
        if self.vel.x * (self.vel.x+self.acc.x) < 0: self.vel.x=0
        else: self.vel += self.acc
        self.pos += self.vel

        if self.pos.x > SCREEN.width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = SCREEN.width

        self.rect.midbottom = self.pos
