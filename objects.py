from settings import *
from functions import x_axis_iter


Term = namedtuple("Term", "title x_axis_bottom x_axis_top")


class LP:
    def __init__(self, title: str, term_names: list, x_start: int, x_stop: int):
        self.title = title
        self.x_start, self.x_stop = x_start, x_stop
        self.terms = self.to_create_terms(term_names)


    def to_create_terms(self, term_names: list) -> list:
        amount = len(term_names)
        bottom_x_axis = x_axis_iter(False, self.x_start, self.x_stop, amount)
        top_x_axis = x_axis_iter(True, self.x_start, self.x_stop, amount)

        return list(map(Term, term_names, bottom_x_axis, top_x_axis))

    def term_titles(self) -> list[str]:
        return [title for title, _, _ in self.terms]

    def set_term_x_axis_top(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_top[0], self.terms[i].x_axis_top[1] = x_1, x_2

    def set_term_x_axis_bottom(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_bottom[0], self.terms[i].x_axis_bottom[1] = x_1, x_2

    def to_discard_term(self, i: int):
        del self.terms[i]