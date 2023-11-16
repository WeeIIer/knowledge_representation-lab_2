from settings import *


def x_axis_iter(top: bool, start: float, stop: float, amount: int) -> Iterator:
    step = (stop - start) / amount
    if top:  # top
        x_1, x_2 = start - step / 2, start + step
    else:  # bottom
        x_1, x_2 = start, start + step / 2

    yield start, x_2
    while True:
        x_1 += step
        x_2 += step
        amount -= 1
        if amount == 1:
            break
        yield x_1, x_2
    yield x_1, stop