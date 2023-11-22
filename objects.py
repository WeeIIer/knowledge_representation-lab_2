from settings import *
from functions import x_axis_iter, unique_id, create_plot


class QFuzzyLabel(QtWidgets.QLabel):
    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

    def resizeEvent(self, a0):
        super(QFuzzyLabel, self).resizeEvent(a0)

        height = int(self.width() * 0.4)
        self.setMinimumHeight(height)
        self.setMaximumHeight(height)


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

    def is_fullness(self) -> bool:
        return all((self.title, isinstance(self.x_start, int), isinstance(self.x_stop, int)))

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
            self.id = unique_id("LPs", "lp_id")

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


class Attribute:
    def __init__(self, dictionary_instance, is_output=False, operation=0, lp_id=-1, connection=0, term_id=-1):
        self.__dictionary: Dictionary = dictionary_instance
        self.is_output: bool = is_output
        self.operation, self.lp_id, self.connection, self.term_id = operation, lp_id, connection, term_id

        self.__discard_outside = lambda attribute: None
        self.__combo: tuple[QtWidgets.QComboBox, ...]

        self.widget: QWidget = self.__create_widget()
        self.__set_combo_connections()

    def expression(self) -> str:
        data = map(QtWidgets.QComboBox.currentText, self.__combo)
        return " ".join(value if not i % 2 else f'"{value}"' for i, value in enumerate(data))

    def discard(self):
        self.widget.deleteLater()
        self.widget = None
        self.lp_id = None
        self.term_id = None
        self.__discard_outside(self)

    def set_discard_outside(self, func):
        self.__discard_outside = func

    def update_first_combo_operation(self):
        combo_operation = self.__combo[0]
        combo_operation.clear()
        combo_operation.addItems(["ЕСЛИ"])
        combo_operation.setCurrentIndex(0)
        combo_operation.setEnabled(False)

    def set_combo_indices(self):
        _, combo_lp, _, combo_term = self.__combo

        combo_lp.setCurrentIndex(self.__dictionary.LP_index(self.lp_id))
        combo_term.addItems(self.__dictionary.LPs[self.__dictionary.LP_index(self.lp_id)].term_titles())
        combo_term.setCurrentIndex(self.term_id)

    def is_fullness(self) -> bool:
        return all((self.widget, self.lp_id > -1, self.connection > -1))

    def data(self) -> tuple:
        return self.operation, self.lp_id, self.connection, self.term_id

    def __create_widget(self):
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
        if self.is_output:
            combo_operation.addItems(["ТО"])
            combo_operation.setCurrentIndex(0)
            combo_operation.setEnabled(False)
        else:
            combo_operation.addItems(OPERATIONS)
            combo_operation.setCurrentIndex(self.operation)
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
        combo_connection.setCurrentIndex(self.connection)
        container_layout.addWidget(combo_connection)

        combo_term = QtWidgets.QComboBox(container)
        combo_term.setMinimumSize(QtCore.QSize(0, 40))
        combo_term.setCursor(cursor)
        container_layout.addWidget(combo_term)

        if not self.is_output:
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
            button_delete.clicked.connect(self.discard)
            container_layout.addWidget(button_delete)

        main_layout.addWidget(container)
        widget = QWidget()
        widget.setLayout(main_layout)

        self.__combo = (combo_operation, combo_lp, combo_connection, combo_term)

        return widget

    def __set_combo_connections(self):
        combo_operation, combo_lp, combo_connection, combo_term = self.__combo

        def __combo_operation():
            i = combo_operation.currentIndex()
            self.operation = i if i > -1 else 0

        def __combo_lp():
            combo_term.clear()
            i = combo_lp.currentIndex()
            if i > -1:
                self.lp_id = self.__dictionary.LP(i).id
                combo_term.addItems(self.__dictionary.LP(i).term_titles())
            else:
                self.lp_id = None

        def __combo_connection():
            i = combo_connection.currentIndex()
            self.connection = i if i > -1 else 0

        def __combo_term():
            i = combo_term.currentIndex()
            self.term_id = i if i > -1 else None

        combo_operation.currentIndexChanged.connect(__combo_operation)
        combo_lp.currentIndexChanged.connect(__combo_lp)
        combo_connection.currentIndexChanged.connect(__combo_connection)
        combo_term.currentIndexChanged.connect(__combo_term)


class PP:
    def __init__(self, dictionary_instance):
        self.__dictionary: Dictionary = dictionary_instance
        self.id: int = 0
        self.expression: str = ""
        self.attributes: list[Attribute] = []
        self.output_attribute: Attribute | None = None

    def update_expression(self):
        self.expression = " ".join(map(Attribute.expression, self.__all_attributes()))

    def add_attribute(self, is_output=False, data: tuple = None):
        attribute = Attribute(self.__dictionary, is_output, *data) if data else Attribute(self.__dictionary, is_output)
        attribute.set_discard_outside(self.__discard_attribute_outside)
        if attribute.is_output:
            self.output_attribute = attribute
        else:
            self.attributes.append(attribute)
            if len(self.attributes) == 1:
                attribute.update_first_combo_operation()

    def is_attributes_fullness(self) -> bool:
        return self.attributes and all(attr.is_fullness() for attr in self.__all_attributes())

    def save(self):
        new = not bool(self.id)
        if new:
            self.id = unique_id("PPs", "pp_id")

        self.update_expression()
        data = {"PPs": (self.id, self.expression), "attributes": []}  # Данные для сохранения в БД

        for attr_id, attr in enumerate(self.__all_attributes()):  # Сформировать пакеты данных с атрибутами
            data["attributes"].append((self.id, attr_id, *attr.data()))

        if new:
            sql = f"INSERT INTO PPs VALUES ({', '.join(repeat('?', len(data['PPs'])))})"
            CUR.execute(sql, data["PPs"])
        else:
            fields = (f"{field} = ?" for field in ("pp_id", "pp_expression"))
            sql = f"UPDATE PPs SET {', '.join(fields)} WHERE pp_id = ?"
            CUR.execute(sql, (*data["PPs"], self.id))
        CON.commit()

        if not new:  # Удалить атрибуты из БД, если ПП существует
            CUR.execute("DELETE FROM attributes WHERE pp_id = ?", (self.id,))
            CON.commit()
        for attr_id, row in enumerate(data["attributes"]):  # Добавить аттрибуты ПП в БД
            sql = f"INSERT INTO attributes VALUES ({', '.join(repeat('?', len(row)))})"
            CUR.execute(sql, row)
            CON.commit()

    def load(self, pp_id: int | None = None):
        if pp_id is None:
            self.id = None
        else:
            data = {"PPs": None, "attributes": None}

            for table_name in data:
                sql = f"SELECT * FROM {table_name} WHERE pp_id = ?"
                data[table_name] = CUR.execute(sql, (pp_id,)).fetchall()

            self.id, self.expression = data["PPs"].pop()
            self.add_attribute(True, data["attributes"].pop()[2:])
            for attr in data["attributes"]:
                self.add_attribute(False, attr[2:])

    def clear(self):
        for attr in self.__all_attributes():
            attr.discard()

    def __discard_attribute_outside(self, attribute: Attribute):
        if not attribute.is_output:
            i = self.attributes.index(attribute)
            del self.attributes[i]
            if i == 0 and self.attributes:
                self.attributes[0].update_first_combo_operation()

    def __all_attributes(self) -> list[Attribute]:
        return self.attributes + [self.output_attribute]


class Dictionary:
    def __init__(self):
        self.LPs: list[LP] = []
        self.PPs: list[PP] = []

    def LP_titles(self):
        return (lp.title for lp in self.LPs)

    def PP_titles(self):
        return (pp.expression for pp in self.PPs)

    def LP(self, i: int) -> LP:
        return self.LPs[i]

    def LP_index(self, lp_id: int) -> int:
        return [lp.id for lp in self.LPs].index(lp_id)

    def PP(self, i: int) -> PP:
        return self.PPs[i]

    def discard_LP(self, i: int):
        CUR.execute("DELETE FROM LPs WHERE lp_id = ?", (self.LP(i).id,))
        CON.commit()
        self.load_LPs()

    def discard_PP(self, i: int):
        CUR.execute("DELETE FROM PPs WHERE pp_id = ?", (self.PP(i).id,))
        CON.commit()
        self.load_PPs()

    def load_LPs(self):
        self.LPs.clear()
        for _, lp_id in sorted(CUR.execute("SELECT lp_title, lp_id FROM LPs").fetchall()):
            lp = LP()
            lp.load(lp_id)
            self.LPs.append(lp)

    def load_PPs(self):
        self.PPs.clear()
        for _, pp_id in sorted(CUR.execute("SELECT pp_expression, pp_id FROM PPs").fetchall()):
            pp = PP(self)
            pp.load(pp_id)
            self.PPs.append(pp)


class FuzzyProjectAttribute:
    def __init__(self, lp: LP):
        self.lp = lp
        self.widget: QWidget = self.__create_attribute_widget()

        self.__objects: tuple[QtWidgets.QGroupBox, QFuzzyLabel, QtWidgets.QSlider]
        self.__set_connections()

    def __create_attribute_widget(self):
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        cursor = QCursor(QtCore.Qt.PointingHandCursor)

        container = QtWidgets.QGroupBox()
        container.setTitle(f'"{self.lp.title}" = {self.lp.x_start}')
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        container.setSizePolicy(sizePolicy)

        container_layout = QtWidgets.QVBoxLayout(container)
        container_layout.setContentsMargins(10, 10, 10, 10)
        container_layout.setSpacing(10)

        label_plot = QFuzzyLabel(container)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        label_plot.setSizePolicy(sizePolicy)
        label_plot.clear()
        pixmap = QPixmap(create_plot(self.lp))
        label_plot.setPixmap(pixmap)
        label_plot.setScaledContents(True)
        container_layout.addWidget(label_plot)

        slider_x_axis = QtWidgets.QSlider(container)
        slider_x_axis.setOrientation(QtCore.Qt.Horizontal)
        slider_x_axis.setRange(self.lp.x_start, self.lp.x_stop)
        slider_x_axis.setValue(self.lp.x_start)
        slider_x_axis.setCursor(cursor)
        container_layout.addWidget(slider_x_axis)

        main_layout.addWidget(container)
        widget = QWidget()
        widget.setLayout(main_layout)

        self.__objects = (container, label_plot, slider_x_axis)

        return widget

    def __set_connections(self):
        container, _, slider_x_axis = self.__objects

        def __on_value_changed_slider_x_axis():
            container.setTitle(f'"{self.lp.title}" = {slider_x_axis.value()}')

        slider_x_axis.valueChanged.connect(__on_value_changed_slider_x_axis)


class FuzzyProject:
    def __init__(self, dictionary_instance):
        self.__dictionary: Dictionary = dictionary_instance
        self.attributes: list[FuzzyProjectAttribute] = []
        self.output_attribute: FuzzyProjectAttribute | None = None

    def add_attribute(self, lp: LP, is_output=False):
        attribute = FuzzyProjectAttribute(lp)
        if is_output:
            self.output_attribute = attribute
        else:
            self.attributes.append(attribute)
        return attribute.widget
