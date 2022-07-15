from pygame import Vector2
from Entity.Entity import Entity


class Door(Entity):
    def __init__(self, pos: Vector2, _id: int):
        super().__init__(pos, ["door_closedMid"], 1)

        self.passable = True
        self.collide_check = True
        self.id = _id

    def collide_player(self, player, side):
        super().collide_player(player, side)
