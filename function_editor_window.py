# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\third_term\knowledge_representation\lab_2\ui\function_editor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_function_editor_window(object):
    def setupUi(self, function_editor_window):
        function_editor_window.setObjectName("function_editor_window")
        function_editor_window.resize(1050, 683)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(function_editor_window.sizePolicy().hasHeightForWidth())
        function_editor_window.setSizePolicy(sizePolicy)
        function_editor_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        function_editor_window.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(function_editor_window)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(function_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setSpacing(5)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_20.addWidget(self.label_15)
        self.edit_term_title = QtWidgets.QLineEdit(self.groupBox)
        self.edit_term_title.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_term_title.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_term_title.setReadOnly(False)
        self.edit_term_title.setObjectName("edit_term_title")
        self.verticalLayout_20.addWidget(self.edit_term_title)
        self.verticalLayout.addLayout(self.verticalLayout_20)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSpacing(5)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_18.addWidget(self.label_13)
        self.edit_x_start = QtWidgets.QLineEdit(self.groupBox)
        self.edit_x_start.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_x_start.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_x_start.setReadOnly(False)
        self.edit_x_start.setObjectName("edit_x_start")
        self.verticalLayout_18.addWidget(self.edit_x_start)
        self.horizontalLayout.addLayout(self.verticalLayout_18)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_19.addWidget(self.label_14)
        self.edit_x_stop = QtWidgets.QLineEdit(self.groupBox)
        self.edit_x_stop.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_x_stop.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_x_stop.setReadOnly(False)
        self.edit_x_stop.setObjectName("edit_x_stop")
        self.verticalLayout_19.addWidget(self.edit_x_stop)
        self.horizontalLayout.addLayout(self.verticalLayout_19)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.button_save = QtWidgets.QPushButton(self.groupBox)
        self.button_save.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_save.setIconSize(QtCore.QSize(24, 24))
        self.button_save.setObjectName("button_save")
        self.verticalLayout.addWidget(self.button_save)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_6 = QtWidgets.QGroupBox(function_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(5)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_17.addWidget(self.label_12)
        self.edit_add_term = QtWidgets.QLineEdit(self.groupBox_6)
        self.edit_add_term.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_add_term.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_add_term.setClearButtonEnabled(True)
        self.edit_add_term.setObjectName("edit_add_term")
        self.verticalLayout_17.addWidget(self.edit_add_term)
        self.verticalLayout_2.addLayout(self.verticalLayout_17)
        self.list_terms = QtWidgets.QListWidget(self.groupBox_6)
        self.list_terms.setMinimumSize(QtCore.QSize(0, 0))
        self.list_terms.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.list_terms.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.list_terms.setObjectName("list_terms")
        self.verticalLayout_2.addWidget(self.list_terms)
        self.verticalLayout_5.addWidget(self.groupBox_6)
        self.groupBox_3 = QtWidgets.QGroupBox(function_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.check_err_1 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_1.sizePolicy().hasHeightForWidth())
        self.check_err_1.setSizePolicy(sizePolicy)
        self.check_err_1.setText("")
        self.check_err_1.setObjectName("check_err_1")
        self.horizontalLayout_3.addWidget(self.check_err_1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.check_err_2 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_2.sizePolicy().hasHeightForWidth())
        self.check_err_2.setSizePolicy(sizePolicy)
        self.check_err_2.setText("")
        self.check_err_2.setObjectName("check_err_2")
        self.horizontalLayout_5.addWidget(self.check_err_2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.check_err_3 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_3.sizePolicy().hasHeightForWidth())
        self.check_err_3.setSizePolicy(sizePolicy)
        self.check_err_3.setText("")
        self.check_err_3.setObjectName("check_err_3")
        self.horizontalLayout_6.addWidget(self.check_err_3)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.check_err_4 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_4.sizePolicy().hasHeightForWidth())
        self.check_err_4.setSizePolicy(sizePolicy)
        self.check_err_4.setText("")
        self.check_err_4.setObjectName("check_err_4")
        self.horizontalLayout_7.addWidget(self.check_err_4)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.check_err_5 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_5.sizePolicy().hasHeightForWidth())
        self.check_err_5.setSizePolicy(sizePolicy)
        self.check_err_5.setText("")
        self.check_err_5.setObjectName("check_err_5")
        self.horizontalLayout_8.addWidget(self.check_err_5)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.check_err_6 = QtWidgets.QCheckBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_err_6.sizePolicy().hasHeightForWidth())
        self.check_err_6.setSizePolicy(sizePolicy)
        self.check_err_6.setText("")
        self.check_err_6.setObjectName("check_err_6")
        self.horizontalLayout_9.addWidget(self.check_err_6)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_7 = QtWidgets.QGroupBox(function_editor_window)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_3 = QtWidgets.QSplitter(self.groupBox_7)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setHandleWidth(10)
        self.splitter_3.setObjectName("splitter_3")
        self.verticalLayout_8.addWidget(self.splitter_3)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.groupBox_2 = QtWidgets.QGroupBox(function_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_plot = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_plot.sizePolicy().hasHeightForWidth())
        self.label_plot.setSizePolicy(sizePolicy)
        self.label_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.label_plot.setText("")
        self.label_plot.setScaledContents(True)
        self.label_plot.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plot.setWordWrap(False)
        self.label_plot.setObjectName("label_plot")
        self.horizontalLayout_4.addWidget(self.label_plot)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_5 = QtWidgets.QGroupBox(function_editor_window)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.groupBox_5)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(10)
        self.splitter.setObjectName("splitter")
        self.verticalLayout_3.addWidget(self.splitter)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.retranslateUi(function_editor_window)
        QtCore.QMetaObject.connectSlotsByName(function_editor_window)

    def retranslateUi(self, function_editor_window):
        _translate = QtCore.QCoreApplication.translate
        function_editor_window.setWindowTitle(_translate("function_editor_window", "Редактор функций принадлежности лингвистической переменной"))
        self.groupBox.setTitle(_translate("function_editor_window", "Лингвистическая переменная"))
        self.label_15.setText(_translate("function_editor_window", "Название"))
        self.label_13.setText(_translate("function_editor_window", "Минимум (ось X)"))
        self.label_14.setText(_translate("function_editor_window", "Максимум (ось X)"))
        self.button_save.setText(_translate("function_editor_window", "Сохранить"))
        self.groupBox_6.setTitle(_translate("function_editor_window", "Термы"))
        self.label_12.setText(_translate("function_editor_window", "Новый терм"))
        self.groupBox_3.setTitle(_translate("function_editor_window", "Требования к виду функций принадлежности"))
        self.label.setText(_translate("function_editor_window", "Требование к упорядоченности термов"))
        self.label_2.setText(_translate("function_editor_window", "Требование к виду «крайних» функций принадлежности лингвистической переменной"))
        self.label_3.setText(_translate("function_editor_window", "Требование к полноте покрытия предметной области"))
        self.label_4.setText(_translate("function_editor_window", "Требование к разграничению понятий, описанных функциями принадлежности термов лингвистической переменной"))
        self.label_5.setText(_translate("function_editor_window", "Требование к наличию типового элемента"))
        self.label_6.setText(_translate("function_editor_window", "Требование к ограничению предметной шкалы"))
        self.groupBox_7.setTitle(_translate("function_editor_window", "Редактирование верхних координат терма"))
        self.groupBox_2.setTitle(_translate("function_editor_window", "График функций принадлежности"))
        self.groupBox_5.setTitle(_translate("function_editor_window", "Редактирование нижных координат терма"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    function_editor_window = QtWidgets.QWidget()
    ui = Ui_function_editor_window()
    ui.setupUi(function_editor_window)
    function_editor_window.show()
    sys.exit(app.exec_())
