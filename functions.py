import datetime
import time

from settings import *


def x_axis_iter(top: bool, start: int, stop: int, amount: int) -> Iterator[list[int, int]]:
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


def unique_id(table_name: str) -> int:
    used_ids = {i[0] for i in CUR.execute(f"SELECT lp_id FROM {table_name}").fetchall()}
    available_ids = set(range(0, max(used_ids) + 2))

    return min(available_ids - used_ids)
