from pygame.rect import Rect
from typing import Literal

TOP: Literal["top"] = "top"
LEFT: Literal["left"] = "left"
RIGHT: Literal["right"] = "right"
BOTTOM: Literal["bottom"] = "bottom"


def determine_side(base_rect: Rect, collision_rect: Rect) -> Literal["top", "left", "right", "bottom"]:
    """
    :param base_rect: 충돌 방향을 구할 Rect
    :param collision_rect: base_rect가 충돌하는 Rect
    :return: base_rect의 collision_rect에 대한 충돌 방향
    """

    if base_rect.bottom <= collision_rect.top:
        return TOP
    elif base_rect.right <= collision_rect.left:
        return LEFT
    elif base_rect.left >= collision_rect.right:
        return RIGHT
    elif base_rect.top >= collision_rect.bottom:
        return BOTTOM
