from settings import *
from objects import LP


class MainWindow(QWidget, main_window_form.Ui_main_window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.slider_x_axis_top, self.slider_x_axis_bottom = self.__to_create_sliders()

        self.splitter.restoreState(SETTINGS.value("splitterSizes"))
        self.splitter_3.restoreState(SETTINGS.value("splitterSizes"))

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.starting)

        self.button_to_draw.clicked.connect(self.on_clicked_button_to_draw)
        self.list_terms.itemClicked.connect(self.on_item_clicked_list_terms)
        self.list_terms.doubleClicked.connect(self.on_double_clicked_list_terms)
        self.slider_x_axis_top.valueChanged.connect(self.on_value_changed_slider_x_axis_top)
        self.slider_x_axis_bottom.valueChanged.connect(self.on_value_changed_slider_x_axis_bottom)
        self.edit_x_start.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_x_stop.textChanged.connect(self.on_text_changed_edit_x)
        self.edit_term_title.textChanged.connect(self.on_text_changed_edit_x)

        self.button_to_draw.setEnabled(False)
        self.lp = None

        #self.edit_add_event.returnPressed.connect(self.on_return_pressed_edit_add_event)

    def on_clicked_button_to_draw(self):
        title = self.edit_term_title.text()
        x_start, x_stop = self.edit_x_start.text(), self.edit_x_stop.text()

        if self.lp is None:
            self.lp = LP(title, ["Низкая", "Средняя", "Высокая"], int(x_start), int(x_stop))
            self.add_terms_to_list()
            self.to_draw()

    def on_text_changed_edit_x(self):
        title = self.edit_term_title.text()
        x_start, x_stop = self.edit_x_start.text(), self.edit_x_stop.text()
        conditions = (x_start.isdigit(), x_stop.isdigit(), bool(title.strip()))
        if all(conditions):
            self.button_to_draw.setEnabled(True)
        else:
            self.button_to_draw.setEnabled(False)

    def on_double_clicked_list_terms(self):
        i = self.list_terms.currentRow()
        self.lp.to_discard_term(i)
        self.list_terms.takeItem(i)
        self.list_terms.setCurrentRow(-1)
        self.to_change_sliders_range()
        self.to_draw()

    def on_value_changed_slider_x_axis_bottom(self):
        i = self.list_terms.currentRow()
        if i > -1:
            xs = self.slider_x_axis_bottom.value()
            self.lp.set_term_x_axis_bottom(i, *xs)
            self.groupBox_5.setTitle(f"Редактирование нижных координат терма {xs}")
            self.to_draw()

    def on_value_changed_slider_x_axis_top(self):
        i = self.list_terms.currentRow()
        if i > -1:
            xs = self.slider_x_axis_top.value()
            self.lp.set_term_x_axis_top(i, *self.slider_x_axis_top.value())
            self.groupBox_7.setTitle(f"Редактирование верхних координат терма {xs}")
            self.to_draw()

    def on_item_clicked_list_terms(self):
        i = self.list_terms.currentRow()

        x_axis_top = self.lp.terms[i].x_axis_top
        x_axis_bottom = self.lp.terms[i].x_axis_bottom

        self.slider_x_axis_top.setValue(x_axis_top)
        self.slider_x_axis_bottom.setValue(x_axis_bottom)

    def add_terms_to_list(self):
        self.list_terms.addItems(self.lp.term_titles())
        self.to_change_sliders_range()

    def to_change_sliders_range(self):
        self.slider_x_axis_bottom.setRange(self.lp.x_start, self.lp.x_stop)
        self.slider_x_axis_bottom.setValue([self.lp.x_start, self.lp.x_stop])
        self.groupBox_5.setTitle(f"Редактирование нижных координат терма ( ... )")

        self.slider_x_axis_top.setRange(self.lp.x_start, self.lp.x_stop)
        self.slider_x_axis_top.setValue([self.lp.x_start, self.lp.x_stop])
        self.groupBox_7.setTitle(f"Редактирование верхних координат терма ( ... )")

    def to_draw(self):
        # titles = [data.title for data in self.events.plots]
        # y_axis = range(1, self.events.amount + 1)

        plt.rc("font", size=8)
        plt.rcParams["font.family"] = "Calibri"

        fig, ax = plt.subplots(figsize=(9, 6))

        # plt.setp(ax, yticks=[*y_axis], yticklabels=titles)

        # ticks_count, now = 20, self.events.now
        # past = now - ticks_count if now > ticks_count else 0

        ax.set(xlim=(self.lp.x_start, self.lp.x_stop), ylim=(0, 1))
        # ax.locator_params(axis="x", nbins=now - past)

        for data in self.lp.terms:
            _, x_axis_bottom, x_axis_top = data

            ax.plot([x_axis_bottom[0], x_axis_top[0]], [0, 1], linewidth=5, color="red")
            ax.plot([x_axis_top[0], x_axis_top[1]], [1, 1], linewidth=5, color="red")
            ax.plot([x_axis_top[1], x_axis_bottom[1]], [1, 0], linewidth=5, color="red")

        #ax.yaxis.tick_right()
        ax.yaxis.set_visible(False)
        ax.grid(which="major", color="k", linestyle="--")

        plt.tight_layout()
        plt.savefig("fig.png", transparent=True)
        plt.close()

        self.label_plot.clear()
        self.label_plot.setPixmap(QPixmap("fig.png"))

    def starting(self):
        self.events.next()
        self.tempors.update_values()

        self.plot_timeline()

    def closeEvent(self, a0):
        super(MainWindow, self).closeEvent(a0)

        SETTINGS.setValue("splitterSizes", self.splitter.saveState())
        SETTINGS.setValue("splitterSizes", self.splitter_3.saveState())

    def show(self):
        super(MainWindow, self).show()
        self.showMaximized()

    def __to_create_sliders(self):
        for splitter, slider_name in ((self.splitter_3, "slider_x_axis_top"), (self.splitter, "slider_x_axis_bottom")):
            left_frame = QtWidgets.QFrame(splitter)
            # left_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            # left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            # left_frame.setObjectName("frame_5")

            slider_x_axis_top = QRangeSlider(QtCore.Qt.Horizontal)
            slider_x_axis_top.setValue((20, 80))
            slider_x_axis_top.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
            slider_x_axis_top.setObjectName(slider_name)
            splitter.addWidget(slider_x_axis_top)

            right_frame = QtWidgets.QFrame(splitter)
            # right_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
            # right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
            # right_frame.setObjectName("frame_6")

        return self.findChild(QRangeSlider, "slider_x_axis_top"), self.findChild(QRangeSlider, "slider_x_axis_bottom")


app = QApplication(sys.argv)
app.setStyle("fusion")
app.setPalette(palette())
#app.setWindowIcon(QIcon(":/logos/icons/program.png"))

main_window = MainWindow()

main_window.show()
app.exec_()
