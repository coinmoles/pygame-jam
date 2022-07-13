from Chapters.stages import stages

def build_scene(chapter: int, stage: int):
    if chapter == 0:
        return stages['main_menu']
    if stage == 0:
        return stages['chapter_menu']['ch'+str(chapter)]
    return stages['ch'+str(chapter)]['stage'+str(stage)]