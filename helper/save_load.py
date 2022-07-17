import os
import pickle
from typing import Tuple
from globals import GLOBALS


def save_game(current_id: Tuple[int, int], file_id: int):
    with open("saves/save{:02d}.pickle".format(file_id), "wb") as fw:
        pickle.dump({
            "current_id": current_id,
            "cleared_stages": GLOBALS.cleared_stages
        }, fw)


def load_game(file_id: int):
    if not os.path.isfile("saves/save{:02d}.pickle".format(file_id)):
        return None

    with open("saves/save{:02d}.pickle".format(file_id), "rb") as fr:
        savedata = pickle.load(fr)
        GLOBALS.cleared_stages = savedata["cleared_stages"]
    
    return savedata["current_id"]
