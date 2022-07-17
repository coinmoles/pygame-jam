import pygame as pg
from Scene.Scene import Scene
from constants import CHANGE_SCENE, COLORS, SCREEN
from globals import GLOBALS
from helper.get_background_color import get_background_color
from helper.save_load import save_game

class SaveScene(Scene):
    def __init__(self, current_id):
        super().__init__((-1, 0))
        self.music_path = "assets/sound/music/IcelandTheme.mp3"
        self.background_color = get_background_color(current_id)
        self.saving = False
        self.choice = -1
        self.current_id = current_id
        self.titlefont = pg.font.Font("assets/font/jangmi.ttf", 144 * SCREEN.width // 1920)
        self.optionfont = pg.font.Font("assets/font/jangmi.ttf", 80 * SCREEN.width // 1920)

    def handle_event(self, event: pg.event.Event):
        super().handle_event(event)
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.saving:
                    self.saving = False
                elif self.choice in [0, 1, 2]:
                    save_game(self.current_id, self.choice)
                    self.saving = True
                else:
                    self.choice = 0

            elif event.key == pg.K_UP:
                self.choice = (self.choice + 2) % 3

            elif event.key == pg.K_DOWN:
                self.choice = (self.choice + 1) % 3
            
            elif event.key == pg.K_ESCAPE:
                pg.event.post(pg.event.Event(CHANGE_SCENE, next_scene_id=self.current_id))

    def update(self):
        super().update()

        if self.saving:
            message = self.titlefont.render("저장 완료!", True, COLORS["black"])
            message_rect = message.get_rect(center=(SCREEN.width // 2, SCREEN.height // 2))
            GLOBALS.screen.blit(message, message_rect)

        else:
            title = self.titlefont.render("저장하기", True, COLORS["black"])
            title_rect = title.get_rect(center=(SCREEN.width // 2, SCREEN.height // 4))
            GLOBALS.screen.blit(title, title_rect)
            
            help = self.optionfont.render("나가기: ESC", True, COLORS["black"])
            help_rect = help.get_rect(topleft=(SCREEN.width * 1 // 30, SCREEN.height * 1 // 30))
            GLOBALS.screen.blit(help, help_rect)

            option1 = self.optionfont.render("파일 1", True, COLORS["black"] if self.choice != 0 else COLORS["yellow"]["100"])
            option1_rect = option1.get_rect(center=(SCREEN.width // 2, SCREEN.height * 9 // 16))
            GLOBALS.screen.blit(option1, option1_rect)

            option2 = self.optionfont.render("파일 2", True, COLORS["black"] if self.choice != 1 else COLORS["yellow"]["100"])
            option2_rect = option2.get_rect(center=(SCREEN.width // 2, SCREEN.height * 21 // 32))
            GLOBALS.screen.blit(option2, option2_rect)

            option3 = self.optionfont.render("파일 3", True, COLORS["black"] if self.choice != 2 else COLORS["yellow"]["100"])
            option3_rect = option3.get_rect(center=(SCREEN.width // 2, SCREEN.height * 12 // 16))
            GLOBALS.screen.blit(option3, option3_rect)
