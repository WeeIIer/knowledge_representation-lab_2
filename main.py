from settings import *
from objects import LP


class MainWindow(QWidget, main_window_form.Ui_main_window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.slider_x_axis_top, self.slider_x_axis_bottom = self.__to_create_sliders()

        self.lp = LP("Скорость", ["Очень низкая", "Низкая", "Средняя", "Высокая", "Очень высокая"], 0, 100)

        self.splitter.restoreState(SETTINGS.value("splitterSizes"))
        self.splitter_3.restoreState(SETTINGS.value("splitterSizes"))

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.starting)

        self.button_start.clicked.connect(self.to_draw)

        #self.edit_add_event.returnPressed.connect(self.on_return_pressed_edit_add_event)


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
