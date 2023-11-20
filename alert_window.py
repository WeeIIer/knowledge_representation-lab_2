# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\third_term\knowledge_representation\lab_2\ui\alert_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_alert_window(object):
    def setupUi(self, alert_window):
        alert_window.setObjectName("alert_window")
        alert_window.resize(503, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(alert_window.sizePolicy().hasHeightForWidth())
        alert_window.setSizePolicy(sizePolicy)
        alert_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        alert_window.setFont(font)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(alert_window)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(alert_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_message = QtWidgets.QLabel(self.groupBox)
        self.label_message.setText("")
        self.label_message.setAlignment(QtCore.Qt.AlignCenter)
        self.label_message.setObjectName("label_message")
        self.verticalLayout.addWidget(self.label_message)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.button_exit = QtWidgets.QPushButton(alert_window)
        self.button_exit.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_exit.setIconSize(QtCore.QSize(24, 24))
        self.button_exit.setObjectName("button_exit")
        self.verticalLayout_3.addWidget(self.button_exit)

        self.retranslateUi(alert_window)
        QtCore.QMetaObject.connectSlotsByName(alert_window)

    def retranslateUi(self, alert_window):
        _translate = QtCore.QCoreApplication.translate
        alert_window.setWindowTitle(_translate("alert_window", "Оповещение"))
        self.button_exit.setText(_translate("alert_window", "Закрыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    alert_window = QtWidgets.QWidget()
    ui = Ui_alert_window()
    ui.setupUi(alert_window)
    alert_window.show()
    sys.exit(app.exec_())
