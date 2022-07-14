from SceneData.stages import stages
from Scene.ChapterScene import ChapterScene
from Scene.GameScene import GameScene


def parse_id(chapter: int, stage: int):
    print(chapter, stage)

    if chapter == 0:
        return ChapterScene(stages['main_menu'], (chapter, stage))
    if stage == 0:
        return ChapterScene(stages['chapter_menu']['ch'+str(chapter)], (chapter, stage))
    return GameScene(stages['ch'+str(chapter)]['stage'+str(stage)], (chapter, stage))
