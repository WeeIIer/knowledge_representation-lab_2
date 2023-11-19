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

        data = {"LPs": [(self.id, self.title, self.x_start, self.x_stop)], "terms": []}  # Данные для сохранения в БД

        for term_id, term in enumerate(self.terms):  # Сформировать пакеты данных с термами
            data["terms"].append((self.id, term_id, *term.data()))

        for row in data["LPs"]:  # Добавить основную информацию о ЛП в БД
            if new:
                sql = f"INSERT INTO LPs VALUES ({', '.join(repeat('?', len(row)))})"
                CUR.execute(sql, row)
            else:
                fields = (f"{field} = ?" for field in ("lp_id", "lp_title", "x_start", "x_stop"))
                sql = f"UPDATE LPs SET {', '.join(fields)} WHERE lp_id = ?"
                CUR.execute(sql, (*row, self.id))
            CON.commit()

        if not new:  # Удалить термы из БД, если ЛП существует
            CUR.execute("DELETE FROM terms WHERE lp_id = ?", (self.id,))
            CON.commit()
        for term_id, row in enumerate(data["terms"]):  # Добавить термы ЛП в БД
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


class Dictionary:
    def __init__(self):
        self.LPs = []
        self.PPs = []

    def LP_titles(self):
        return (lp.title for lp in self.LPs)

    def LP(self, i: int) -> LP:
        return self.LPs[i]

    def del_LP(self, i: int):
        CUR.execute("DELETE FROM LPs WHERE lp_id = ?", (self.LP(i).id,))
        CON.commit()
        self.load_LPs()

    def load_LPs(self):
        self.LPs.clear()
        for _, lp_id in sorted(CUR.execute("SELECT lp_title, lp_id FROM LPs").fetchall()):
            lp = LP()
            lp.load(lp_id)
            self.LPs.append(lp)


class Attribute:
    def __init__(self, dictionary: Dictionary, not_output=True):
        self.__dictionary = dictionary
        self.widget = self.__create_widget(not_output)

        self.LP = None
        self.term_id = None

    def __create_widget(self, not_output: bool):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        cursor = QCursor(QtCore.Qt.PointingHandCursor)

        container = QtWidgets.QGroupBox()
        container.setTitle("")

        container_layout = QtWidgets.QHBoxLayout(container)
        container_layout.setContentsMargins(10, 10, 10, 10)
        container_layout.setSpacing(10)

        combo_operation = QtWidgets.QComboBox(container)
        combo_operation.setMinimumSize(QtCore.QSize(0, 40))
        combo_operation.setCursor(cursor)
        combo_operation.addItems(OPERATIONS)
        container_layout.addWidget(combo_operation)

        combo_lp = QtWidgets.QComboBox(container)
        combo_lp.setMinimumSize(QtCore.QSize(0, 40))
        combo_lp.setCursor(cursor)
        combo_lp.addItems(self.__dictionary.LP_titles())
        combo_lp.setCurrentIndex(-1)
        container_layout.addWidget(combo_lp)

        combo_connection = QtWidgets.QComboBox(container)
        combo_connection.setMinimumSize(QtCore.QSize(0, 40))
        combo_connection.setCursor(cursor)
        combo_connection.addItems(CONNECTIONS)
        container_layout.addWidget(combo_connection)

        combo_term = QtWidgets.QComboBox(container)
        combo_term.setMinimumSize(QtCore.QSize(0, 40))
        combo_term.setCursor(cursor)
        container_layout.addWidget(combo_term)

        if not_output:
            button_delete = QtWidgets.QPushButton(container)
            size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            button_delete.setSizePolicy(size_policy)
            button_delete.setMinimumSize(QtCore.QSize(80, 40))
            font = QFont()
            font.setBold(True)
            font.setWeight(75)
            button_delete.setFont(font)
            button_delete.setCursor(cursor)
            button_delete.setText("Удалить")
            button_delete.clicked.connect(self.__button_delete)
            container_layout.addWidget(button_delete)

        main_layout.addWidget(container)
        widget = QWidget()
        widget.setLayout(main_layout)

        combo_lp.currentIndexChanged.connect(lambda: self.__combo_lp(combo_lp, combo_term))
        combo_term.currentIndexChanged.connect(lambda: self.__combo_term(combo_term))

        return widget

    def __combo_lp(self, combo_lp: QtWidgets.QComboBox, combo_term: QtWidgets.QComboBox):
        combo_term.clear()
        i = combo_lp.currentIndex()
        if i > -1:
            self.LP = self.__dictionary.LP(i)
            combo_term.addItems(self.__dictionary.LP(i).term_titles())
        else:
            self.LP = None

    def __combo_term(self, combo_term: QtWidgets.QComboBox):
        i = combo_term.currentIndex()
        if i > -1:
            self.term_id = i
        else:
            self.term_id = None

    def __button_delete(self):
        self.widget.deleteLater()
        self.widget = None
        self.LP = None
