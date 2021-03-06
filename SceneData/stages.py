from SceneData.main_menu import main_menu
from SceneData.chapter_menu.chapter1 import chapter1
from SceneData.chapter_menu.chapter2 import chapter2
from SceneData.chapter1.stage1_1 import stage1_1
from SceneData.chapter1.stage1_2 import stage1_2
from SceneData.chapter1.stage1_3 import stage1_3
from SceneData.chapter1.stage1_4 import stage1_4
from SceneData.chapter1.stage1_5 import stage1_5
from SceneData.chapter1.stage1_6 import stage1_6
from SceneData.chapter1.stage1_7 import stage1_7
from SceneData.chapter1.stage1_8 import stage1_8
from SceneData.chapter2.stage2_1 import stage2_1
from SceneData.chapter2.stage2_2 import stage2_2
from SceneData.chapter2.stage2_3 import stage2_3
from SceneData.chapter2.stage2_4 import stage2_4
from SceneData.chapter2.stage2_5 import stage2_5
from SceneData.chapter2.stage2_6 import stage2_6
from SceneData.chapter2.stage2_7 import stage2_7
from SceneData.chapter2.stage2_8 import stage2_8


stages = {
    "main_menu": main_menu,
    "chapter_menu": {
        "ch1": chapter1,
        "ch2": chapter2
    },
    "ch1": {
        "stage1": stage1_1,
        "stage2": stage1_2,
        "stage3": stage1_3,
        "stage4": stage1_4,
        "stage5": stage1_5,
        "stage6": stage1_6,
        "stage7": stage1_7,
        "stage8": stage1_8,
    },
    "ch2": {
        "stage1": stage2_1,
        "stage2": stage2_2,
        "stage3": stage2_3,
        "stage4": stage2_4,
        "stage5": stage2_5,
        "stage6": stage2_6,
        "stage7": stage2_7,
        "stage8": stage2_8,
    }
}