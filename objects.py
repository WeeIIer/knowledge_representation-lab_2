from settings import *
from functions import x_axis_iter

Term = namedtuple("Term", "title x_axis_bottom x_axis_top")


class LP:
    def __init__(self, title: str, term_titles: list, x_start: int, x_stop: int):
        self.title = title
        self.x_start, self.x_stop = x_start, x_stop
        self.terms = self.create_terms(term_titles) if term_titles else term_titles

    def create_terms(self, term_titles: list = None) -> list:
        if term_titles is None:
            term_titles = self.term_titles()

        amount = len(term_titles)
        bottom_x_axis = x_axis_iter(False, self.x_start, self.x_stop, amount)
        top_x_axis = x_axis_iter(True, self.x_start, self.x_stop, amount)

        return list(map(Term, term_titles, bottom_x_axis, top_x_axis))

    def update_terms(self):
        self.terms = self.create_terms()

    def term_titles(self) -> list[str]:
        return [title for title, _, _ in self.terms]

    def set_term_x_axis_top(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_top[0], self.terms[i].x_axis_top[1] = x_1, x_2

    def set_term_x_axis_bottom(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_bottom[0], self.terms[i].x_axis_bottom[1] = x_1, x_2

    def set_title(self, title: str):
        self.title = title

    def set_x_start(self, x_start: int):
        self.x_start = x_start

    def set_x_stop(self, x_stop: int):
        self.x_stop = x_stop

    def to_discard_term(self, i: int):
        del self.terms[i]

    def add_term(self, title: str):
        self.terms = self.create_terms(self.term_titles() + [title])
