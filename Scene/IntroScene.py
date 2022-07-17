import pygame as pg
from Scene.Scene import Scene
from Entity.BackgroundObject.Background import Background
from constants import CHANGE_SCENE, COLORS, OPEN_LOAD, SCREEN
from globals import GLOBALS

class IntroScene(Scene):
    def __init__(self):
        super().__init__((-1, 0))
        self.entityList.add(Background())
        self.music_path = "assets/sound/music/IntroTheme.mp3"

        self.choice = -1
        self.titlefont = pg.font.Font("assets/font/jangmi.ttf", 144 * SCREEN.width // 1920)
        self.optionfont = pg.font.Font("assets/font/jangmi.ttf", 80 * SCREEN.width // 1920)

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.choice == 0:
                    pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=(2, 1)))
                elif self.choice == 1:
                    pg.event.post(pg.event.Event(OPEN_LOAD, current_id=(-1, 0)))
                elif self.choice == 2:
                    pg.event.post(pg.event.Event(pg.QUIT))
                else:
                    self.choice = 0

            elif event.key == pg.K_UP:
                self.choice = (self.choice + 2) % 3

            elif event.key == pg.K_DOWN:
                self.choice = (self.choice + 1) % 3

    def update(self):
        super().update()

        title = self.titlefont.render("시체 밟는 게임", True, COLORS["black"])
        title_rect = title.get_rect(center=(SCREEN.width // 2, SCREEN.height // 4))
        GLOBALS.screen.blit(title, title_rect)

        option1 = self.optionfont.render("새로하기", True, COLORS["black"] if self.choice != 0 else COLORS["yellow"]["100"])
        option1_rect = title.get_rect(center=(SCREEN.width * 29 // 30, SCREEN.height * 11 // 16))
        GLOBALS.screen.blit(option1, option1_rect)

        option2 = self.optionfont.render("이어하기", True, COLORS["black"] if self.choice != 1 else COLORS["yellow"]["100"])
        option2_rect = title.get_rect(center=(SCREEN.width * 29 // 30, SCREEN.height * 25 // 32))
        GLOBALS.screen.blit(option2, option2_rect)

        option3 = self.optionfont.render("게임 종료", True, COLORS["black"] if self.choice != 2 else COLORS["yellow"]["100"])
        option3_rect = title.get_rect(center=(SCREEN.width * 29 // 30, SCREEN.height * 14 // 16))
        GLOBALS.screen.blit(option3, option3_rect)
