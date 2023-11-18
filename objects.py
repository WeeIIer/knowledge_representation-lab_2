from settings import *
from functions import x_axis_iter, unique_id


Term = namedtuple("Term", "title x_axis_bottom x_axis_top")


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

        self.terms = list(map(Term, term_titles, x_axis_bottom, x_axis_top))

    def term_titles(self) -> list[str]:
        return [title for title, _, _ in self.terms]

    def set_term_x_axis_bottom(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_bottom[0], self.terms[i].x_axis_bottom[1] = x_1, x_2

    def set_term_x_axis_top(self, i: int, x_1: int, x_2: int):
        self.terms[i].x_axis_top[0], self.terms[i].x_axis_top[1] = x_1, x_2

    def set_title(self, title: str):
        self.title = title

    def set_x_start(self, x_start: int):
        self.x_start = x_start

    def set_x_stop(self, x_stop: int):
        self.x_stop = x_stop

    def discard_term(self, i: int):
        del self.terms[i]
        self.update_terms()

    def limits(self) -> list[bool]:
        terms_count = len(self.term_titles())
        init_state = bool(terms_count)
        errors = [init_state] * 6
        if not init_state:
            return errors

        # Требование к упорядоченности термов
        for i in range(1, terms_count):
            prev, follow = self.terms[i - 1], self.terms[i]
            if prev.x_axis_bottom[0] > follow.x_axis_bottom[0] or prev.x_axis_top[0] > follow.x_axis_top[0]:
                errors[0] = False
                break

        # Требование к виду «крайних» функций принадлежности лингвистической переменной
        first, last = self.terms[0], self.terms[-1]
        pairs = [first.x_axis_bottom[0], first.x_axis_top[0], last.x_axis_bottom[1], last.x_axis_top[1]]
        errors[1] = pairs.count(self.x_start) + pairs.count(self.x_stop) == 4

        # Требование к полноте покрытия предметной области
        x_axis_set = set(chain.from_iterable(range(*x_axis_bottom) for _, x_axis_bottom, _ in self.terms))
        if len(x_axis_set) != self.x_stop - self.x_start:
            errors[2] = False

        # Требование к разграничению понятий, описанных функциями принадлежности термов лингвистической переменной
        terms_range = range(terms_count)
        set_from = lambda index: set(range(self.terms[index].x_axis_top[0], self.terms[index].x_axis_top[1] + 1))
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

        fields = [
            ("lp_id", "lp_title", "x_start", "x_stop"),
            ("lp_id", "term_id", "term_title", "x_axis_bottom_1", "x_axis_bottom_2", "x_axis_top_1", "x_axis_top_2")
        ]

        data = {
            "LPs": [(self.id, self.title, self.x_start, self.x_stop)],
            "terms": []
        }

        for term_id, term in enumerate(self.terms):
            data["terms"].append((self.id, term_id, term.title, *term.x_axis_bottom, *term.x_axis_top))

        for row in data["LPs"]:
            if new:
                sql = f"INSERT INTO LPs VALUES ({', '.join(repeat('?', len(row)))})"
                CUR.execute(sql, row)
            else:
                table_fields = (f"{field} = ?" for field in fields[0])
                sql = f"UPDATE LPs SET {', '.join(table_fields)} WHERE lp_id = ?"
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
            self.terms = [Term(term[2], [*term[3:5]], [*term[5:7]]) for term in data["terms"]]
