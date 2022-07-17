from typing import Set, Tuple, Union
import pygame as pg
from typing import Dict
import os
from constants import SCREEN, UNITSIZE


class GameGlobals:
    def __init__(self):
        self.timer = 0
        self.screen: Union[pg.Surface, None] = None
        self.images: Dict[str, pg.Surface] = {}
        self.image_rect: Dict[str, pg.Rect] = {}
        self.sfx_dict: Dict[str, pg.mixer.Sound] = {}
        self.cleared_stages: Set[Tuple[int, int]] = set()

    def set_screen(self, screen: pg.Surface):
        self.screen = screen

    def reset_timer(self):
        self.timer = 0
    
    def clear_stage(self, stage_id: Tuple[int, int]):
        self.cleared_stages.add(stage_id)
        if stage_id[1] == 8:
            self.cleared_stages.add((stage_id[0], 0))

    def load_images(self):
        path = './assets/images'
        for subdir, dirs, file_names in os.walk(path):
            for name in file_names:
                if not name.endswith('.png'):
                    continue
                image_name = os.path.splitext(name)[0]
                image = pg.image.load(os.path.join(subdir, name)).convert_alpha()
                if subdir == "./assets/images\p1" or subdir == "./assets/images\p2" or subdir == "./assets/images\p3":
                    motion = image_name.split("_")[1]
                    if motion == "stand" or motion == "p1_jump":
                        image = pg.transform.scale(image, (UNITSIZE * 2 / 3, UNITSIZE))
                    else:
                        image = pg.transform.scale(image, (UNITSIZE * 2 / 3 * 1.05, UNITSIZE * 1.05))
                elif subdir == "./assets/images\\background":
                    image = pg.transform.scale(image, (SCREEN.width, SCREEN.height))
                elif subdir == "./assets/images\\control_help":
                    image = pg.transform.scale(image, (UNITSIZE * 2, UNITSIZE * 2))
                else:
                    image = pg.transform.scale(image, (UNITSIZE, UNITSIZE))
                self.images[image_name] = image
                bounding_rects = pg.mask.from_surface(image).get_bounding_rects()
                self.image_rect[image_name] = bounding_rects[0].unionall(bounding_rects[1:])

    def load_sounds(self):
        path = './assets/sound/sfx'
        for subdir, dirs, file_names in os.walk(path):
            for name in file_names:
                if not name.endswith('.wav'):
                    continue
                sound_name = os.path.splitext(name)[0]
                sound = pg.mixer.Sound(os.path.join(subdir, name))
                self.sfx_dict[sound_name] = sound
        
        self.sfx_dict["Powerup1"].set_volume(0.3)
        self.sfx_dict["Powerup"].set_volume(0.2)


GLOBALS = GameGlobals()
