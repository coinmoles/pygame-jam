from abc import ABCMeta
from typing import Union, Optional, Sized, Iterable


class SizedIterable(Sized, Iterable, metaclass=ABCMeta):
    pass


def try_min(iterable: SizedIterable) -> Union[int, float, None]:
    if len(iterable) == 0:
        return None
    else:
        return min(iterable)


def try_max(iterable: SizedIterable) -> Union[int, float, None]:
    if len(iterable) == 0:
        return None
    else:
        return max(iterable)
