from settings import *
from functions import x_axis_iter, unique_id


class Term:
    def __init__(self, title: str, x_lb: int, x_rb: int, x_lt: int, x_rt: int):
        self.title = title
        self.x_lb, self.x_rb, self.x_lt, self.x_rt = x_lb, x_rb, x_lt, x_rt

    def x_axis_bottom(self) -> tuple[int, int]:
        return self.x_lb, self.x_rb

    def x_axis_top(self) -> tuple[int, int]:
        return self.x_lt, self.x_rt

    def set_x_axis_bottom(self, x_lb: int, x_rb: int):
        self.x_lb, self.x_rb = x_lb, x_rb

    def set_x_axis_top(self, x_lt: int, x_rt: int):
        self.x_lt, self.x_rt = x_lt, x_rt

    def data(self) -> tuple:
        return self.title, self.x_lb, self.x_rb, self.x_lt, self.x_rt


class LP:
    def __init__(self):
        self.id: int = 0
        self.title: str = ""
        self.x_start: int = 0
        self.x_stop: int = 0
        self.terms: list[Term] = []

    def add_term(self, title: str):
        self.update_terms(self.term_titles() + [title])

    def update_terms(self, term_titles: list[str] | None = None):
        if term_titles is None:
            term_titles = self.term_titles()

        term_count = len(term_titles)
        x_axis_bottom = x_axis_iter(False, self.x_start, self.x_stop, term_count)
        x_axis_top = x_axis_iter(True, self.x_start, self.x_stop, term_count)

        self.terms.clear()
        for i in range(term_count):
            self.terms.append(Term(term_titles[i], *next(x_axis_bottom), *next(x_axis_top)))

    def term_titles(self) -> list[str]:
        return [term.title for term in self.terms]

    def discard_term(self, i: int):
        del self.terms[i]
        self.update_terms()

    def set_title(self, title: str):
        self.title = title

    def set_x_start(self, x_start: int):
        self.x_start = x_start

    def set_x_stop(self, x_stop: int):
        self.x_stop = x_stop

    def limits(self) -> list[bool]:
        terms_count = len(self.term_titles())
        init_state = bool(terms_count)
        errors = [init_state] * 6
        if not init_state:
            return errors

        # Требование к упорядоченности термов
        for i in range(1, terms_count):
            past, future = self.terms[i - 1], self.terms[i]
            if past.x_lb > future.x_lb or past.x_lt > future.x_lt:
                errors[0] = False
                break

        # Требование к виду «крайних» функций принадлежности лингвистической переменной
        first, last = self.terms[0], self.terms[-1]
        pairs = [first.x_lb, first.x_lt, last.x_rb, last.x_rt]
        errors[1] = pairs.count(self.x_start) + pairs.count(self.x_stop) == 4

        # Требование к полноте покрытия предметной области
        x_axis_set = set(chain.from_iterable(range(*term.x_axis_bottom()) for term in self.terms))
        if len(x_axis_set) != self.x_stop - self.x_start:
            errors[2] = False

        # Требование к разграничению понятий, описанных функциями принадлежности термов лингвистической переменной
        terms_range = range(terms_count)
        set_from = lambda i: set(range(self.terms[i].x_lt, self.terms[i].x_rt + 1))
        x_axis_set = chain.from_iterable(set_from(i) & set_from(j) for j in terms_range for i in terms_range if i != j)
        if set(x_axis_set):
            errors[3] = False

        # Требование к наличию типового элемента
        # !!! Всегда истина, так как в программе нельзя менять ось Y !!!

        # Требование к ограничению предметной шкалы
        # !!! Всегда истина, так как в программе есть чёткие ограничения начала и конца !!!

        return errors

    def save(self):
        new = not bool(self.id)
        if new:
            self.id = unique_id("LPs")

        data = {
            "LPs": [(self.id, self.title, self.x_start, self.x_stop)],
            "terms": []
        }

        for term_id, term in enumerate(self.terms):
            data["terms"].append((self.id, term_id, *term.data()))

        for row in data["LPs"]:
            if new:
                sql = f"INSERT INTO LPs VALUES ({', '.join(repeat('?', len(row)))})"
                CUR.execute(sql, row)
            else:
                fields = (f"{field} = ?" for field in ("lp_id", "lp_title", "x_start", "x_stop"))
                sql = f"UPDATE LPs SET {', '.join(fields)} WHERE lp_id = ?"
                CUR.execute(sql, (*row, self.id))
            CON.commit()

        for term_id, row in enumerate(data["terms"]):
            if not new:
                sql = f"DELETE FROM terms WHERE lp_id = ? AND term_id = ?"
                CUR.execute(sql, (self.id, term_id))
                CON.commit()
            sql = f"INSERT INTO terms VALUES ({', '.join(repeat('?', len(row)))})"
            CUR.execute(sql, row)
            CON.commit()

    def load(self, lp_id: int | None = None):
        if lp_id is None:
            self.id = None
        else:
            data = {"LPs": None, "terms": None}

            for table_name in data:
                sql = f"SELECT * FROM {table_name} WHERE lp_id = ?"
                data[table_name] = CUR.execute(sql, (lp_id,)).fetchall()

            self.id, self.title, self.x_start, self.x_stop = data["LPs"].pop()
            self.terms = [Term(*term[2:]) for term in data["terms"]]
