# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\VADIM\Python\SFedU\third_term\knowledge_representation\lab_2\ui\pp_editor_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pp_editor_window(object):
    def setupUi(self, pp_editor_window):
        pp_editor_window.setObjectName("pp_editor_window")
        pp_editor_window.resize(1000, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pp_editor_window.sizePolicy().hasHeightForWidth())
        pp_editor_window.setSizePolicy(sizePolicy)
        pp_editor_window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        pp_editor_window.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(pp_editor_window)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(pp_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_save = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_save.sizePolicy().hasHeightForWidth())
        self.button_save.setSizePolicy(sizePolicy)
        self.button_save.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_save.setFont(font)
        self.button_save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_save.setIconSize(QtCore.QSize(24, 24))
        self.button_save.setObjectName("button_save")
        self.horizontalLayout_3.addWidget(self.button_save)
        self.button_add_attribute = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_attribute.sizePolicy().hasHeightForWidth())
        self.button_add_attribute.setSizePolicy(sizePolicy)
        self.button_add_attribute.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_add_attribute.setFont(font)
        self.button_add_attribute.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_add_attribute.setIconSize(QtCore.QSize(24, 24))
        self.button_add_attribute.setObjectName("button_add_attribute")
        self.horizontalLayout_3.addWidget(self.button_add_attribute)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.button_exit = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_exit.sizePolicy().hasHeightForWidth())
        self.button_exit.setSizePolicy(sizePolicy)
        self.button_exit.setMinimumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.button_exit.setFont(font)
        self.button_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_exit.setIconSize(QtCore.QSize(24, 24))
        self.button_exit.setObjectName("button_exit")
        self.horizontalLayout_3.addWidget(self.button_exit)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(pp_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scroll_attribute = QtWidgets.QScrollArea(self.groupBox_2)
        self.scroll_attribute.setMinimumSize(QtCore.QSize(0, 0))
        self.scroll_attribute.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.scroll_attribute.setFont(font)
        self.scroll_attribute.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scroll_attribute.setStyleSheet("")
        self.scroll_attribute.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scroll_attribute.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_attribute.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_attribute.setWidgetResizable(True)
        self.scroll_attribute.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scroll_attribute.setObjectName("scroll_attribute")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 941, 451))
        self.scrollAreaWidgetContents_2.setAutoFillBackground(True)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.layout_scroll_attribute = QtWidgets.QVBoxLayout()
        self.layout_scroll_attribute.setContentsMargins(10, 10, 10, 10)
        self.layout_scroll_attribute.setSpacing(10)
        self.layout_scroll_attribute.setObjectName("layout_scroll_attribute")
        self.verticalLayout_6.addLayout(self.layout_scroll_attribute)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.scroll_attribute.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.addWidget(self.scroll_attribute)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.group_output_attribute = QtWidgets.QGroupBox(pp_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_output_attribute.sizePolicy().hasHeightForWidth())
        self.group_output_attribute.setSizePolicy(sizePolicy)
        self.group_output_attribute.setMinimumSize(QtCore.QSize(0, 0))
        self.group_output_attribute.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.group_output_attribute.setObjectName("group_output_attribute")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.group_output_attribute)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layout_output_attribute = QtWidgets.QVBoxLayout()
        self.layout_output_attribute.setSpacing(0)
        self.layout_output_attribute.setObjectName("layout_output_attribute")
        self.horizontalLayout_2.addLayout(self.layout_output_attribute)
        self.verticalLayout_2.addWidget(self.group_output_attribute)
        self.groupBox = QtWidgets.QGroupBox(pp_editor_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edit_expression = QtWidgets.QLineEdit(self.groupBox)
        self.edit_expression.setMinimumSize(QtCore.QSize(0, 21))
        self.edit_expression.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.edit_expression.setReadOnly(True)
        self.edit_expression.setObjectName("edit_expression")
        self.horizontalLayout.addWidget(self.edit_expression)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(pp_editor_window)
        QtCore.QMetaObject.connectSlotsByName(pp_editor_window)

    def retranslateUi(self, pp_editor_window):
        _translate = QtCore.QCoreApplication.translate
        pp_editor_window.setWindowTitle(_translate("pp_editor_window", "Редактор продукционного правила"))
        self.groupBox_3.setTitle(_translate("pp_editor_window", "Панель управления"))
        self.button_save.setText(_translate("pp_editor_window", "Сохранить"))
        self.button_add_attribute.setText(_translate("pp_editor_window", "Добавить атрибут"))
        self.button_exit.setText(_translate("pp_editor_window", "Закрыть"))
        self.groupBox_2.setTitle(_translate("pp_editor_window", "Информационные атрибуты (вход)"))
        self.group_output_attribute.setTitle(_translate("pp_editor_window", "Атрибут управления (выход)"))
        self.groupBox.setTitle(_translate("pp_editor_window", "Сохранённое выражение"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    pp_editor_window = QtWidgets.QWidget()
    ui = Ui_pp_editor_window()
    ui.setupUi(pp_editor_window)
    pp_editor_window.show()
    sys.exit(app.exec_())
