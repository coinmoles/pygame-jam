from Entity.Platform import Platform


class Corpse(Platform):
    def __init__(self, size, pos):
        super().__init__(size, (30, 30, 30), pos)
