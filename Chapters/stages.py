from Chapters.main_menu import main_menu
from Chapters.chapter_menu.chapter1 import chapter1
from Chapters.chapter_menu.chapter2 import chapter2
from Chapters.chapter1.stage1_1 import stage1_1
from Chapters.chapter1.stage1_2 import stage1_2
from Chapters.chapter1.stage1_3 import stage1_3
from Chapters.chapter1.stage1_4 import stage1_4
from Chapters.chapter1.stage1_5 import stage1_5

stages = {
    "main_menu" : main_menu,
    "chapter_menu" : {
        "ch1": chapter1,
        "ch2": chapter2
    },
    "ch1": {
        "stage1": stage1_1,
        "stage2": stage1_2,
        "stage3": stage1_3,
        "stage4": stage1_4,
        "stage5": stage1_5,
    }
}