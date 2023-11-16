from settings import *
from functions import x_axis_iter


Term = namedtuple("Term", "title x_axis_bottom x_axis_top")


class LP:
    def __init__(self, title: str, terms: list[str], x_start: float, x_stop: float):
        self.title = title
        self.x_start, self.x_stop = x_start, x_stop
        self.terms = self.to_create_terms(terms)
        # print(*self.terms, sep="\n")

    def to_create_terms(self, term_names: list) -> list:
        amount = len(term_names)
        bottom_x_axis = x_axis_iter(False, self.x_start, self.x_stop, amount)
        top_x_axis = x_axis_iter(True, self.x_start, self.x_stop, amount)

        return list(map(Term, term_names, bottom_x_axis, top_x_axis))
