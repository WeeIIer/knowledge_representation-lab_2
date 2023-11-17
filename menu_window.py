# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\third_term\knowledge_representation\lab_2\ui\menu_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(503, 149)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu_window.sizePolicy().hasHeightForWidth())
        menu_window.setSizePolicy(sizePolicy)
        menu_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        menu_window.setFont(font)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(menu_window)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(menu_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.button_add_lp = QtWidgets.QPushButton(self.groupBox)
        self.button_add_lp.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_add_lp.setFont(font)
        self.button_add_lp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_add_lp.setIconSize(QtCore.QSize(24, 24))
        self.button_add_lp.setObjectName("button_add_lp")
        self.verticalLayout.addWidget(self.button_add_lp)
        self.button_load_lp = QtWidgets.QPushButton(self.groupBox)
        self.button_load_lp.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_load_lp.setFont(font)
        self.button_load_lp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_load_lp.setIconSize(QtCore.QSize(24, 24))
        self.button_load_lp.setObjectName("button_load_lp")
        self.verticalLayout.addWidget(self.button_load_lp)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "Меню"))
        self.groupBox.setTitle(_translate("menu_window", "Редактор функций принадлежности лингвистической переменной"))
        self.button_add_lp.setText(_translate("menu_window", "Создать"))
        self.button_load_lp.setText(_translate("menu_window", "Загрузить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QWidget()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec_())
