from settings import *
from objects import LP


CURRENT_LP: LP | None = None


class MenuWindow(QWidget, menu_window_form.Ui_menu_window):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)

        self.button_add_lp.clicked.connect(self.on_clicked_button_add_lp)
        self.button_load_lp.clicked.connect(self.on_clicked_button_load_lp)

    def on_clicked_button_add_lp(self):
        global CURRENT_LP
        CURRENT_LP = None

        self.hide()
        function_editor_window.show()

    def on_clicked_button_load_lp(self):
        global CURRENT_LP
        filename, _ = QFileDialog.getOpenFileName(self,
                                                  "Открыть лингвистическую переменную",
                                                  ".",
                                                  "Лингвистическая переменная (*.lp)")
        if filename:
            with open(filename, "rb") as file:
                CURRENT_LP = pickle.load(file)
            self.hide()
            function_editor_window.show()


class FunctionEditorWindow(QWidget, function_editor_window_form.Ui_function_editor_window):
    def __init__(self):
        super(FunctionEditorWindow, self).__init__()
        self.setupUi(self)

        self.slider_x_axis_top, self.slider_x_axis_bottom = self.__create_sliders()
        for i in range(1, 7):
            self.findChild(QCheckBox, f"check_err_{i}").setEnabled(False)

        self.splitter.restoreState(SETTINGS.value("splitterSizes"))
        self.splitter_3.restoreState(SETTINGS.value("splitterSizes"))

        self.button_save.clicked.connect(self.on_clicked_button_save)
        self.list_terms.itemClicked.connect(self.on_item_clicked_list_terms)
        self.list_terms.doubleClicked.connect(self.on_double_clicked_list_terms)
        self.slider_x_axis_top.valueChanged.connect(self.on_value_changed_slider_x_axis_top)
        self.slider_x_axis_bottom.valueChanged.connect(self.on_value_changed_slider_x_axis_bottom)
        self.edit_x_start.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_x_stop.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_term_title.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_add_term.returnPressed.connect(self.on_return_pressed_edit_add_term)

    def on_clicked_button_save(self):
        filename, _ = QFileDialog.getSaveFileName(self,
                                                  "Сохранить лингвистическую переменную",
                                                  fr".\{CURRENT_LP.title}.lp",
                                                  "Лингвистическая переменная (*.lp)")
        if filename:
            with open(filename, "wb") as file:
                pickle.dump(CURRENT_LP, file)
            # self.__add_log(f"Лингвистическая переменная сохранена в \"{CURRENT_LP.title}.lp\".")

    def on_return_pressed_edit_add_term(self):
        term_title = self.edit_add_term.text().strip()
        if term_title:
            CURRENT_LP.add_term(self.edit_add_term.text())
            self.add_terms_to_list()
            self.change_sliders_range()
            self.draw_plot()
            # self.__add_log(f"Добавлен терм \"{term_title}\".")

    def on_text_changed_edit_x(self):
        global CURRENT_LP
        title = self.edit_term_title.text()
        x_start, x_stop = self.edit_x_start.text(), self.edit_x_stop.text()
        self.button_save.setEnabled(False)

        if title.strip() and x_start.isdigit() and x_stop.isdigit():
            x_start, x_stop = int(x_start), int(x_stop)
            if x_stop > x_start:
                if CURRENT_LP is None:
                    CURRENT_LP = LP(title, [], x_start, x_stop)
                    self.add_terms_to_list()
                    self.change_sliders_range()
                    self.draw_plot()
                else:
                    self.list_terms.setCurrentRow(-1)
                    CURRENT_LP.set_title(title)
                    CURRENT_LP.set_x_start(x_start)
                    CURRENT_LP.set_x_stop(x_stop)
                    CURRENT_LP.update_terms()
                    self.change_sliders_range()
                    self.draw_plot()
                    self.button_save.setEnabled(True)

    def on_double_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        # term_title = CURRENT_LP.term_titles()[i]
        CURRENT_LP.discard_term(i)
        self.list_terms.takeItem(i)
        self.list_terms.setCurrentRow(-1)
        self.change_sliders_range()
        print("del here")
        self.draw_plot()
        # self.__add_log(f"Удалён терм \"{term_title}\"")

    def on_value_changed_slider_x_axis_bottom(self):
        i = self.list_terms.currentRow()
        if i > -1:
            xs = self.slider_x_axis_bottom.value()
            CURRENT_LP.set_term_x_axis_bottom(i, *xs)
            self.groupBox_5.setTitle(f"Редактирование нижных координат терма {xs}")
            self.draw_plot()

    def on_value_changed_slider_x_axis_top(self):
        i = self.list_terms.currentRow()
        if i > -1:
            xs = self.slider_x_axis_top.value()
            CURRENT_LP.set_term_x_axis_top(i, *self.slider_x_axis_top.value())
            self.groupBox_7.setTitle(f"Редактирование верхних координат терма {xs}")
            self.draw_plot()

    def on_item_clicked_list_terms(self):
        i = self.list_terms.currentRow()

        x_axis_top = CURRENT_LP.terms[i].x_axis_top
        x_axis_bottom = CURRENT_LP.terms[i].x_axis_bottom

        self.slider_x_axis_top.setValue(x_axis_top)
        self.slider_x_axis_bottom.setValue(x_axis_bottom)

    def add_terms_to_list(self):
        self.list_terms.clear()
        self.list_terms.addItems(CURRENT_LP.term_titles())

    def change_sliders_range(self):
        if CURRENT_LP is None:
            x_start, x_stop = 0, 1
        else:
            x_start, x_stop = CURRENT_LP.x_start, CURRENT_LP.x_stop

        self.slider_x_axis_bottom.setRange(x_start, x_stop)
        self.slider_x_axis_bottom.setValue([x_start, x_stop])
        self.groupBox_5.setTitle(f"Редактирование нижных координат терма ( ... )")

        self.slider_x_axis_top.setRange(x_start, x_stop)
        self.slider_x_axis_top.setValue([x_start, x_stop])
        self.groupBox_7.setTitle(f"Редактирование верхних координат терма ( ... )")

    def draw_plot(self):
        for i, state in enumerate(CURRENT_LP.limits(), 1):
            self.findChild(QCheckBox, f"check_err_{i}").setChecked(state)
        print("here")
        plt.rc("font", size=8)
        plt.rcParams["font.family"] = "Calibri"

        fig, ax = plt.subplots(figsize=(9, 6))
        ax.set(xlim=(CURRENT_LP.x_start, CURRENT_LP.x_stop), ylim=(0, 1))

        for i, data in enumerate(CURRENT_LP.terms):
            _, x_axis_bottom, x_axis_top = data

            ax.plot([x_axis_bottom[0], x_axis_top[0]], [0, 1], linewidth=5, color="red")
            ax.plot([x_axis_top[0], x_axis_top[1]], [1, 1], linewidth=5, color="red")
            ax.plot([x_axis_top[1], x_axis_bottom[1]], [1, 0], linewidth=5, color="red")

        ax.yaxis.set_visible(False)
        ax.grid(which="major", color="k", linestyle="--")

        plt.tight_layout()
        plt.savefig("fig.png", transparent=True)
        plt.close()

        self.label_plot.clear()
        self.label_plot.setPixmap(QPixmap("fig.png"))

    def closeEvent(self, a0):
        super(FunctionEditorWindow, self).closeEvent(a0)

        SETTINGS.setValue("splitterSizes", self.splitter.saveState())
        SETTINGS.setValue("splitterSizes", self.splitter_3.saveState())

        menu_window.show()

    def show(self):
        super(FunctionEditorWindow, self).show()
        # self.label_log.clear()

        if CURRENT_LP is None:
            self.edit_term_title.clear()
            self.edit_x_start.clear()
            self.edit_x_stop.clear()
            self.list_terms.clear()
            self.label_plot.clear()
            self.button_save.setEnabled(False)
            for i in range(1, 7):
                self.findChild(QCheckBox, f"check_err_{i}").setEnabled(False)
            # self.__add_log("Создание новой лингвистической переменной.")
        else:
            self.edit_term_title.setText(CURRENT_LP.title)
            self.edit_x_start.setText(str(CURRENT_LP.x_start))
            self.edit_x_stop.setText(str(CURRENT_LP.x_stop))
            self.add_terms_to_list()
            # self.__add_log(f"Редактирование лингвистической переменной \"{CURRENT_LP.title}\".")

        self.edit_add_term.clear()
        self.change_sliders_range()

    # def __add_log(self, message: str):
    #     timing = datetime.datetime.now().strftime("%H:%M")
    #     self.label_log.setText(f"Журнал: {timing} {message}")

    def __create_sliders(self):
        for splitter, slider_name in ((self.splitter_3, "slider_x_axis_top"), (self.splitter, "slider_x_axis_bottom")):
            left_frame = QtWidgets.QFrame(splitter)

            slider_x_axis = QRangeSlider(QtCore.Qt.Horizontal)
            slider_x_axis.setValue((0, 1))
            slider_x_axis.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            slider_x_axis.setObjectName(slider_name)
            splitter.addWidget(slider_x_axis)

            right_frame = QtWidgets.QFrame(splitter)
        return self.findChild(QRangeSlider, "slider_x_axis_top"), self.findChild(QRangeSlider, "slider_x_axis_bottom")


app = QApplication(sys.argv)
app.setStyle("fusion")
app.setPalette(palette())
#app.setWindowIcon(QIcon(":/logos/icons/program.png"))

menu_window = MenuWindow()
function_editor_window = FunctionEditorWindow()

menu_window.show()
app.exec_()
