from xmlrpc.client import Boolean
from pygame import Vector2
from Entity.Entity import Entity


class Door(Entity):
    def __init__(self, pos: Vector2, _id: int, locked: bool):
        if locked:
            super().__init__(pos, ["door_closedMid"], 1)
        else:
            super().__init__(pos, ["door_openMid"], 1)

        self.passable = True
        self.collide_check = True
        self.id = _id
        self.locked = locked

    def collide_player(self, player, side):
        super().collide_player(player, side)
