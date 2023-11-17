from settings import *
from functions import x_axis_iter

Term = namedtuple("Term", "title x_axis_bottom x_axis_top")


class LP:
    def __init__(self, title: str, term_titles: list, x_start: int, x_stop: int):
        self.title = title
        self.x_start, self.x_stop = x_start, x_stop
        self.terms = self.create_terms(term_titles) if term_titles else term_titles
        self.terms_amount = 0

    def create_terms(self, term_titles: list = None) -> list:
        if term_titles is None:
            term_titles = self.term_titles()

        self.terms_amount = len(term_titles)
        bottom_x_axis = x_axis_iter(False, self.x_start, self.x_stop, self.terms_amount)
        top_x_axis = x_axis_iter(True, self.x_start, self.x_stop, self.terms_amount)

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

    def discard_term(self, i: int):
        del self.terms[i]
        self.update_terms()

    def add_term(self, title: str):
        self.terms = self.create_terms(self.term_titles() + [title])

    def limits(self):
        errors = [*repeat(True if self.terms_amount else False, 6)]

        # Требование к упорядоченности термов
        for i in range(1, self.terms_amount):
            prev, follow = self.terms[i - 1], self.terms[i]
            if prev.x_axis_bottom[0] > follow.x_axis_bottom[0] or prev.x_axis_top[0] > follow.x_axis_top[0]:
                errors[0] = False
                break

        # Требование к виду «крайних» функций принадлежности лингвистической переменной
        for i in range(1, self.terms_amount):
            first, last = self.terms[0], self.terms[-1]
            if first.x_axis_bottom[0] != self.x_start or first.x_axis_top[0] != self.x_start \
                    or last.x_axis_bottom[1] != self.x_stop or last.x_axis_top[1] != self.x_stop:
                errors[1] = False
                break

        # Требование к полноте покрытия предметной области
        x_axis_set = set(chain.from_iterable(range(*x_axis_bottom) for _, x_axis_bottom, _ in self.terms))
        if len(x_axis_set) != self.x_stop - self.x_start:
            errors[2] = False

        # Требование к разграничению понятий, описанных функциями принадлежности термов лингвистической переменной
        terms_range = range(self.terms_amount)
        set_from = lambda index: set(range(self.terms[index].x_axis_top[0], self.terms[index].x_axis_top[1] + 1))
        x_axis_set = chain.from_iterable(set_from(i) & set_from(j) for j in terms_range for i in terms_range if i != j)
        if set(x_axis_set):
            errors[3] = False

        # Требование к наличию типового элемента
        # !!! Всегда истина, так как в программе нельзя менять ось Y !!!

        # Требование к ограничению предметной шкалы
        # !!! Всегда истина, так как в программе есть чёткие ограничения начала и конца !!!

        return errors
