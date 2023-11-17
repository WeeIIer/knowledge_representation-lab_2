import datetime
import time

from settings import *


def x_axis_iter(top: bool, start: int, stop: int, amount: int) -> Iterator:
    step = int((stop - start) / (amount * 2))
    if top:  # top
        x_1, x_2 = start, start + step
    else:  # bottom
        x_1, x_2 = start - step, start + step * 2

    yield [start, x_2]
    while True:
        x_1 += step * 2
        x_2 += step * 2
        amount -= 1
        if amount == 1:
            break
        yield [x_1, x_2]
    yield [x_1, stop]
