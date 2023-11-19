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
    available_ids = set(range(1, max(used_ids) + 2))

    return min(available_ids - used_ids)


def create_attribute_widget(lp_id_list: int) -> QWidget:
    container = QtWidgets.QGroupBox()
    container.setTitle("")

    container_layout = QtWidgets.QHBoxLayout(container)
    container_layout.setContentsMargins(10, 10, 10, 10)
    container_layout.setSpacing(10)

    combo_operation = QtWidgets.QComboBox(container)
    combo_operation.setMinimumSize(QtCore.QSize(0, 40))
    combo_operation.addItems(OPERATIONS)
    container_layout.addWidget(combo_operation)

    combo_lp = QtWidgets.QComboBox(container)
    combo_lp.setMinimumSize(QtCore.QSize(0, 40))
    combo_lp.addItems(lps)
    container_layout.addWidget(combo_lp)

    combo_connection = QtWidgets.QComboBox(container)
    combo_connection.setMinimumSize(QtCore.QSize(0, 40))
    combo_connection.addItems(OPERATIONS)
    container_layout.addWidget(combo_connection)

    combo_term = QtWidgets.QComboBox(container)
    combo_term.setMinimumSize(QtCore.QSize(0, 40))
    combo_term.addItems(terms)
    container_layout.addWidget(combo_term)

    button_delete = QtWidgets.QPushButton(container)
    size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    button_delete.setSizePolicy(size_policy)
    button_delete.setMinimumSize(QtCore.QSize(80, 40))
    font = QFont()
    font.setBold(True)
    font.setWeight(75)
    button_delete.setFont(font)
    button_delete.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    container_layout.addWidget(button_delete)

    widget = QWidget()
    widget.setLayout(container_layout)

    return widget
