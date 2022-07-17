from typing import Dict, Final
from screeninfo import get_monitors
import pygame as pg

SCREEN = get_monitors()[0]
SCREEN.width = 1600
SCREEN.height = 900
UNITSIZE = SCREEN.height / 9
FPS = 60

CAMERA_RECT = pg.rect.Rect(SCREEN.width / 3, SCREEN.height / 3, SCREEN.width / 3, SCREEN.height / 3)

SET_SPAWN = pg.USEREVENT + 1
DESPAWN = pg.USEREVENT + 2
SPAWN = pg.USEREVENT + 3
CHANGE_SCENE = pg.USEREVENT + 4
PLAYER_JUMP = pg.USEREVENT + 5
STAGE_CLEAR = pg.USEREVENT + 6
SET_CHECKPOINT = pg.USEREVENT + 7
PLAYER_DEATH = pg.USEREVENT + 8
TRANSFORM = pg.USEREVENT + 9
TRANSFORM_END = pg.USEREVENT + 10
PLAY_SFX = pg.USEREVENT + 11
OPEN_LOAD = pg.USEREVENT + 12
OPEN_SAVE = pg.USEREVENT + 13
END_SAVELOAD = pg.USEREVENT + 14
PLAYER_RESPAWN = pg.USEREVENT + 15
OPEN_INTRO = pg.USEREVENT + 16

TOKENS: Final[Dict[str, str]] = {
    "GrassPlatform": "p",
    "DirtPlatform": "q",
    "Spike": "k",
    "CheckPoint": "c",
    "JumpItem": "j",
    "JumpPlatform": "J",
    "Goal": "d",
    "SpawnPoint": "s",
    "Cannon0": "g",
    "Cannon1": "y",
    "Cannon2": "u",
    "Cannon3": "h",
    "CannonItem": "G",
    "Control1": "!",
    "Control2": "@",
    "Control3": "#",
    "Control4": "$",
    "Control5": "%",
    "Control6": "^",
    "Control7": "&",
    "Control8": "*",
    "Control9": "(",
}

PLATFORMS = [
    TOKENS["GrassPlatform"], 
    TOKENS["DirtPlatform"],
    TOKENS["Cannon0"],
    TOKENS["Cannon1"],
    TOKENS["Cannon2"],
    TOKENS["Cannon3"],
]

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'gray': {
        '50': (247, 250, 252),
        '100': (237, 242, 247),
        '200': (226, 232, 240),
        '300': (203, 213, 224),
        '400': (160, 174, 192),
        '500': (113, 128, 150),
        '600': (74, 85, 104),
        '700': (45, 55, 72),
        '800': (26, 32, 44),
        '900': (23, 25, 35)
    },
    'red': {
        '50': (255, 245, 245),
        '100': (254, 215, 215),
        '200': (254, 178, 178),
        '300': (252, 129, 129),
        '400': (245, 101, 101),
        '500': (229, 62, 62),
        '600': (197, 48, 48),
        '700': (155, 44, 44),
        '800': (130, 39, 39),
        '900': (99, 23, 27)
    },
    'orange': {
        '50': (255, 250, 240),
        '100': (254, 235, 200),
        '200': (251, 211, 141),
        '300': (246, 173, 85),
        '400': (237, 137, 54),
        '500': (221, 107, 32),
        '600': (192, 86, 33),
        '700': (156, 66, 33),
        '800': (123, 52, 30),
        '900': (101, 43, 25)
    },
    'yellow': {
        '50': (255, 255, 240),
        '100': (254, 252, 191),
        '200': (250, 240, 137),
        '300': (246, 224, 94),
        '400': (236, 201, 75),
        '500': (214, 158, 46),
        '600': (183, 121, 31),
        '700': (151, 90, 22),
        '800': (116, 66, 16),
        '900': (95, 55, 14)
    },
    'green': {
        '50': (240, 255, 244),
        '100': (198, 246, 213),
        '200': (154, 230, 180),
        '300': (104, 211, 145),
        '400': (72, 187, 120),
        '500': (56, 161, 105),
        '600': (47, 133, 90),
        '700': (39, 103, 73),
        '800': (34, 84, 61),
        '900': (28, 69, 50)
    },
    'teal': {
        '50': (230, 255, 250),
        '100': (178, 245, 234),
        '200': (129, 230, 217),
        '300': (79, 209, 197),
        '400': (56, 178, 172),
        '500': (49, 151, 149),
        '600': (44, 122, 123),
        '700': (40, 94, 97),
        '800': (35, 78, 82),
        '900': (29, 64, 68)
    },
    'blue': {
        '50': (235, 248, 255),
        '100': (190, 227, 248),
        '200': (144, 205, 244),
        '300': (99, 179, 237),
        '400': (66, 153, 225),
        '500': (49, 130, 206),
        '600': (43, 108, 176),
        '700': (44, 82, 130),
        '800': (42, 67, 101),
        '900': (26, 54, 93)
    },
    'cyan': {
        '50': (237, 253, 253),
        '100': (196, 241, 249),
        '200': (157, 236, 249),
        '300': (118, 228, 247),
        '400': (11, 197, 234),
        '500': (0, 181, 216),
        '600': (0, 163, 196),
        '700': (9, 135, 160),
        '800': (8, 111, 131),
        '900': (6, 86, 102)
    },
    'purple': {
        '50': (250, 245, 255),
        '100': (233, 216, 253),
        '200': (214, 188, 250),
        '300': (183, 148, 244),
        '400': (159, 122, 234),
        '500': (128, 90, 213),
        '600': (107, 70, 193),
        '700': (85, 60, 154),
        '800': (68, 51, 122),
        '900': (50, 38, 89)
    },
    'pink': {
        '50': (255, 245, 247),
        '100': (254, 215, 226),
        '200': (251, 182, 206),
        '300': (246, 135, 179),
        '400': (237, 100, 166),
        '500': (213, 63, 140),
        '600': (184, 50, 128),
        '700': (151, 38, 109),
        '800': (112, 36, 89),
        '900': (82, 27, 65)
    }
}
