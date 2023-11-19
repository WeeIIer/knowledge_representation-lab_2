import functions
from settings import *
from objects import LP

CURRENT_LP: LP | None = None


class LPSelectionWindow(QWidget, lp_selection_window_form.Ui_lp_selection_window):
    def __init__(self):
        super(LPSelectionWindow, self).__init__()
        self.setupUi(self)

        self.LPs = None

        self.button_open.clicked.connect(self.on_clicked_button_open)
        self.button_delete.clicked.connect(self.on_clicked_button_delete)
        self.button_exit.clicked.connect(self.close)
        self.list_lps.doubleClicked.connect(self.on_clicked_button_open)

    def on_clicked_button_open(self):
        global CURRENT_LP
        i = self.list_lps.currentRow()
        if i > -1:
            lp_id = self.LPs[i][0]
            CURRENT_LP = LP()
            CURRENT_LP.load(lp_id)
            self.close()
            function_editor_window.show()

    def on_clicked_button_delete(self):
        i = self.list_lps.currentRow()
        if i > -1:
            lp_id = self.LPs[i][0]
            CUR.execute("DELETE FROM LPs WHERE lp_id = ?", (lp_id,))
            CON.commit()
            self.update_list_lps()

    def update_list_lps(self):
        self.LPs = sorted(CUR.execute("SELECT lp_id, lp_title FROM LPs").fetchall(), key=lambda lp: lp[-1].lower())
        self.list_lps.clear()
        self.list_lps.addItems(title for _, title in self.LPs)
        self.button_exit.setFocus()

    def show(self):
        super(LPSelectionWindow, self).show()
        self.button_exit.setFocus()
        self.update_list_lps()

    def closeEvent(self, a0):
        super(LPSelectionWindow, self).closeEvent(a0)
        menu_window.show()


class MenuWindow(QWidget, menu_window_form.Ui_menu_window):
    def __init__(self):
        super(MenuWindow, self).__init__()
        self.setupUi(self)

        self.button_add_lp.clicked.connect(self.on_clicked_button_add_lp)
        self.button_load_lp.clicked.connect(self.on_clicked_button_load_lp)
        self.button_exit.clicked.connect(app.closeAllWindows)

    def on_clicked_button_add_lp(self):
        global CURRENT_LP
        CURRENT_LP = None
        self.hide()
        function_editor_window.show()

    def on_clicked_button_load_lp(self):
        self.hide()
        lp_selection_window.show()


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
        self.slider_x_axis_bottom.valueChanged.connect(self.on_value_changed_slider_x_axis_bottom)
        self.slider_x_axis_top.valueChanged.connect(self.on_value_changed_slider_x_axis_top)
        self.edit_title.textChanged.connect(self.on_text_changed_edit_lp)
        self.edit_x_start.textChanged.connect(self.on_text_changed_edit_lp)
        self.edit_x_stop.textChanged.connect(self.on_text_changed_edit_lp)
        self.edit_add_term.returnPressed.connect(self.on_return_pressed_edit_add_term)

    def on_clicked_button_save(self):
        CURRENT_LP.save()

    def on_item_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        self.slider_x_axis_bottom.setValue(CURRENT_LP.terms[i].x_axis_bottom())
        self.slider_x_axis_top.setValue(CURRENT_LP.terms[i].x_axis_top())

    def on_double_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        CURRENT_LP.discard_term(i)
        self.add_terms_to_list()
        self.change_sliders_range()
        self.draw_plot()

    def on_value_changed_slider_x_axis_bottom(self):
        i = self.list_terms.currentRow()
        if i > -1:
            x_pair = self.slider_x_axis_bottom.value()
            CURRENT_LP.terms[i].set_x_axis_bottom(*x_pair)
            self.groupBox_5.setTitle(f"Редактирование нижных координат терма {x_pair}")
            self.draw_plot()

    def on_value_changed_slider_x_axis_top(self):
        i = self.list_terms.currentRow()
        if i > -1:
            x_pair = self.slider_x_axis_top.value()
            CURRENT_LP.terms[i].set_x_axis_top(*x_pair)
            self.groupBox_7.setTitle(f"Редактирование верхних координат терма {x_pair}")
            self.draw_plot()

    def on_text_changed_edit_lp(self):
        global CURRENT_LP
        title = self.edit_title.text()
        x_start, x_stop = self.edit_x_start.text(), self.edit_x_stop.text()
        try:
            x_start, x_stop = int(x_start), int(x_stop)
            if title.strip() and x_start < x_stop:
                if CURRENT_LP is None:
                    CURRENT_LP = LP()
                    CURRENT_LP.load()
                CURRENT_LP.set_title(title)
                CURRENT_LP.set_x_start(x_start)
                CURRENT_LP.set_x_stop(x_stop)
                #CURRENT_LP.update_terms()
                self.add_terms_to_list()
                self.change_sliders_range()
                self.draw_plot()
                self.edit_add_term.setEnabled(True)
            else:
                raise ValueError
        except ValueError:
            self.label_plot.clear()
            self.edit_add_term.setEnabled(False)

    def on_return_pressed_edit_add_term(self):
        term_title = self.edit_add_term.text().strip()
        self.edit_add_term.clear()
        if term_title:
            CURRENT_LP.add_term(term_title)
            self.add_terms_to_list()
            self.change_sliders_range()
            self.draw_plot()

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

    def update_limits(self):
        limits = CURRENT_LP.limits() if CURRENT_LP is not None else [False] * 6
        self.button_save.setEnabled(all(limits))
        for i, state in enumerate(limits, 1):
            self.findChild(QCheckBox, f"check_err_{i}").setChecked(state)

    def draw_plot(self):
        plt.rc("font", size=8)
        plt.rcParams["font.family"] = "Calibri"

        fig, ax = plt.subplots(figsize=(9, 6))
        ax.set(xlim=(CURRENT_LP.x_start, CURRENT_LP.x_stop), ylim=(0, 1))

        for term in CURRENT_LP.terms:
            ax.plot([term.x_lb, term.x_lt], [0, 1], linewidth=5, color="red")
            ax.plot([term.x_lt, term.x_rt], [1, 1], linewidth=5, color="red")
            ax.plot([term.x_rt, term.x_rb], [1, 0], linewidth=5, color="red")

        ax.yaxis.set_visible(False)
        ax.grid(which="major", color="k", linestyle="--")

        plt.tight_layout()
        plt.savefig("fig.png", transparent=True)
        plt.close()

        self.label_plot.clear()
        self.label_plot.setPixmap(QPixmap("fig.png"))
        self.update_limits()

    def show(self):
        super(FunctionEditorWindow, self).show()

        self.edit_title.clear()
        self.edit_x_start.clear()
        self.edit_x_stop.clear()
        self.list_terms.clear()
        self.label_plot.clear()
        self.update_limits()

        if CURRENT_LP is not None:
            self.edit_title.setText(CURRENT_LP.title)
            self.edit_x_start.setText(str(CURRENT_LP.x_start))
            self.edit_x_stop.setText(str(CURRENT_LP.x_stop))
            self.add_terms_to_list()

        self.edit_add_term.clear()
        self.change_sliders_range()

    def closeEvent(self, a0):
        super(FunctionEditorWindow, self).closeEvent(a0)

        SETTINGS.setValue("splitterSizes", self.splitter.saveState())
        SETTINGS.setValue("splitterSizes", self.splitter_3.saveState())

        menu_window.show()

    def __create_sliders(self) -> tuple[QRangeSlider, QRangeSlider]:
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
lp_selection_window = LPSelectionWindow()

menu_window.show()
app.exec_()
