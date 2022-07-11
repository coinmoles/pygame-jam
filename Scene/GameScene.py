from Scene.Scene import Scene
from Entity.Player import Player

class GameScene(Scene):
    def __init__(self, game, map):
        super().__init__(game)
        self.player = Player()

        self.entityList.add(self.player)
        for entity in map: self.entityList.add(entity)

    def update(self):
        super().update()
        self.player.move()
        self.player.update()
