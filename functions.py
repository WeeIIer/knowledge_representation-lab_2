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


def unique_id(table_name: str, id_name: str) -> int:
    used_ids = {i[0] for i in CUR.execute(f"SELECT {id_name} FROM {table_name}").fetchall()}
    if len(used_ids):
        available_ids = set(range(1, max(used_ids) + 2))
        return min(available_ids - used_ids)
    return 1


def create_plot(lp, figure_path="fig.png"):
    plt.rc("font", size=12)
    plt.rcParams["font.family"] = "Calibri"

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set(xlim=(lp.x_start, lp.x_stop), ylim=(0, 1))

    for term in lp.terms:
        ax.plot([term.x_lb, term.x_lt], [0, 1], linewidth=5, color="red")
        ax.plot([term.x_lt, term.x_rt], [1, 1], linewidth=5, color="red")
        ax.plot([term.x_rt, term.x_rb], [1, 0], linewidth=5, color="red")

        # a, b = (term.x_lb, 0), (term.x_lt, 1)
        # c, d = (10, 0), (10, 1)
        # ax.plot([10, 10], [0, 1], linewidth=5, color="blue")
        # line1 = shapely.LineString([a, b])
        # line2 = shapely.LineString([c, d])
        # point = line1.intersection(line2)
        # print(point)

    ax.yaxis.set_visible(False)
    ax.grid(which="major", color="k", linestyle="--")

    plt.tight_layout()
    plt.savefig(figure_path, transparent=True)
    plt.close()

    return figure_path
