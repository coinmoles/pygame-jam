from Scene.Scene import Scene
from Entity.Player import Player
from Entity.Platform import Platform


class GameScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.player = Player()

        self.entityList.add(self.player)
        self.entityList.add(Platform())

    def update(self):
        super().update()
        self.player.move()
        self.player.update()
