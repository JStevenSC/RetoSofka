# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Users\jssanche\Documents\Steven\Reto\Tripuladas.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(956, 796)
        Dialog.setMinimumSize(QtCore.QSize(956, 796))
        Dialog.setMaximumSize(QtCore.QSize(956, 796))
        Dialog.setStyleSheet("background-color: rgb(91, 91, 91);")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 921, 761))
        self.frame.setSizeIncrement(QtCore.QSize(26, 0))
        self.frame.setStyleSheet("\n"
"QFrame{\n"
"background-color: rgb(0,206,151);\n"
"background-color: rgb(0, 60, 88);\n"
"border-radius:15px;\n"
"border:1px solid rgb(255, 255, 255);\n"
"\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"border-radius:0px;\n"
"background-color: rgb(211, 254, 238);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"border:1px solid whiter;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color: rgb(139, 139, 139);\n"
"font: 15pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(213, 213, 213);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"border:1px solid whiter;\n"
"\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(0, 60, 88);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;\n"
"border:2px solid rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"font: 75 19pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(211, 254, 238);\n"
"border-radius:13px;\n"
"border:2px solid whiter;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, -10, 321, 41))
        self.label.setStyleSheet("background-color:rgb(91, 91, 91);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"\n"
"border-right:3px solid rgb(255, 255, 255);\n"
"border-bottom:3px solid rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.Salir = QtWidgets.QPushButton(self.frame)
        self.Salir.setGeometry(QtCore.QRect(30, 680, 861, 70))
        self.Salir.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"border:2px solid rgb(0,0,0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:14px;\n"
"\n"
"\n"
"background-color: rgb(193, 193, 193);\n"
"border:1px solid whiter;\n"
"border-right:6px solid rgb(80,80,80);\n"
"border-bottom:6px solid rgb(80,80,80)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(156, 156, 156);\n"
"border-right:none;\n"
"border-bottom:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 156, 156)\n"
"\n"
"}")
        self.Salir.setAutoRepeatInterval(103)
        self.Salir.setObjectName("Salir")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 330, 861, 341))
        self.frame_2.setStyleSheet("\n"
"QFrame{\n"
"background-color: rgb(0,206,151);\n"
"background-color: rgb(0, 60, 88);\n"
"border-radius:15px;\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"border-radius:0px;\n"
"background-color: rgb(211, 254, 238);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border:4px solid whiter;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color: rgb(139, 139, 139);\n"
"font: 15pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(213, 213, 213);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 100, 841, 211))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setStyleSheet("")
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_3.setAutoScroll(False)
        self.tableWidget_3.setAlternatingRowColors(False)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setCornerButtonEnabled(False)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(67)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget_3.verticalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setMinimumSectionSize(29)
        self.tableWidget_3.verticalHeader().setStretchLastSection(True)
        self.Consultar_Tripuladas = QtWidgets.QPushButton(self.frame_2)
        self.Consultar_Tripuladas.setGeometry(QtCore.QRect(10, 30, 271, 70))
        self.Consultar_Tripuladas.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"border:2px solid rgb(0,0,0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:14px;\n"
"\n"
"\n"
"background-color: rgb(193, 193, 193);\n"
"border:1px solid whiter;\n"
"border-right:6px solid rgb(80,80,80);\n"
"border-bottom:6px solid rgb(80,80,80)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(156, 156, 156);\n"
"border-right:none;\n"
"border-bottom:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 156, 156)\n"
"\n"
"}")
        self.Consultar_Tripuladas.setAutoRepeatInterval(103)
        self.Consultar_Tripuladas.setObjectName("Consultar_Tripuladas")
        self.label_17 = QtWidgets.QLabel(self.frame_2)
        self.label_17.setGeometry(QtCore.QRect(690, 20, 111, 81))
        self.label_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:0px")
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("d:\\Users\\jssanche\\Documents\\Steven\\Reto\\Imagenes/tripulada-removebg-preview.png"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 60, 871, 221))
        self.frame_3.setStyleSheet("\n"
"QFrame{\n"
"background-color: rgb(0,206,151);\n"
"background-color: rgb(0, 60, 88);\n"
"border-radius:15px;\n"
"border:1px solid rgb(255, 255, 255);\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"\n"
"}\n"
"\n"
"QTableWidget{\n"
"border-radius:0px;\n"
"background-color: rgb(211, 254, 238);\n"
"font: 17pt \"MS Shell Dlg 2\";\n"
"border:4px solid whiter;\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section{\n"
"\n"
"background-color: rgb(139, 139, 139);\n"
"font: 15pt \"MS Shell Dlg 2\"\n"
"}\n"
"\n"
"QTableWidget QTableCornerButton::section{\n"
"background-color: rgb(213, 213, 213);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"border:3px solid rgb(0, 0, 0);\n"
"border-top:3px solid  rgb(255, 255, 255);\n"
"border-left:3px solid  rgb(255, 255, 255)\n"
"\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.frame_3)
        self.tableWidget_4.setEnabled(True)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 100, 851, 111))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_4.sizePolicy().hasHeightForWidth())
        self.tableWidget_4.setSizePolicy(sizePolicy)
        self.tableWidget_4.setStyleSheet("")
        self.tableWidget_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_4.setAutoScroll(False)
        self.tableWidget_4.setAlternatingRowColors(False)
        self.tableWidget_4.setShowGrid(True)
        self.tableWidget_4.setCornerButtonEnabled(False)
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(5)
        self.tableWidget_4.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setItem(0, 4, item)
        self.tableWidget_4.horizontalHeader().setVisible(True)
        self.tableWidget_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_4.horizontalHeader().setHighlightSections(False)
        self.tableWidget_4.horizontalHeader().setMinimumSectionSize(67)
        self.tableWidget_4.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_4.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_4.verticalHeader().setDefaultSectionSize(37)
        self.tableWidget_4.verticalHeader().setHighlightSections(False)
        self.tableWidget_4.verticalHeader().setMinimumSectionSize(29)
        self.tableWidget_4.verticalHeader().setStretchLastSection(True)
        self.Agregar_Tripuladas = QtWidgets.QPushButton(self.frame_3)
        self.Agregar_Tripuladas.setGeometry(QtCore.QRect(20, 20, 261, 70))
        self.Agregar_Tripuladas.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"\n"
"border:2px solid rgb(0,0,0);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"border-radius:14px;\n"
"\n"
"\n"
"background-color: rgb(193, 193, 193);\n"
"border:1px solid whiter;\n"
"border-right:6px solid rgb(80,80,80);\n"
"border-bottom:6px solid rgb(80,80,80)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(156, 156, 156);\n"
"border-right:none;\n"
"border-bottom:none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(156, 156, 156)\n"
"\n"
"}")
        self.Agregar_Tripuladas.setAutoRepeatInterval(103)
        self.Agregar_Tripuladas.setObjectName("Agregar_Tripuladas")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(690, 20, 111, 81))
        self.label_16.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;\n"
"border:0px")
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("d:\\Users\\jssanche\\Documents\\Steven\\Reto\\Imagenes/tripulada-removebg-preview.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.label_turno = QtWidgets.QLabel(self.frame)
        self.label_turno.setGeometry(QtCore.QRect(320, 310, 251, 39))
        self.label_turno.setStyleSheet("border:2px solid rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(211, 254, 238);\n"
"background-color: rgb(190, 190, 190);")
        self.label_turno.setAlignment(QtCore.Qt.AlignCenter)
        self.label_turno.setObjectName("label_turno")
        self.label_turno_2 = QtWidgets.QLabel(self.frame)
        self.label_turno_2.setGeometry(QtCore.QRect(330, 40, 251, 39))
        self.label_turno_2.setStyleSheet("border:2px solid rgb(0, 0, 0);\n"
"border-radius:12px;\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(211, 254, 238);\n"
"background-color: rgb(190, 190, 190);")
        self.label_turno_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_turno_2.setObjectName("label_turno_2")

        self.retranslateUi(Dialog)
        self.Salir.clicked.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#ffffff;\">Naves Tripuladas </span></p></body></html>"))
        self.Salir.setText(_translate("Dialog", "Salir"))
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1 "))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("Dialog", "2"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("Dialog", "3"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("Dialog", "4"))
        item = self.tableWidget_3.verticalHeaderItem(5)
        item.setText(_translate("Dialog", "5"))
        item = self.tableWidget_3.verticalHeaderItem(6)
        item.setText(_translate("Dialog", "6"))
        item = self.tableWidget_3.verticalHeaderItem(7)
        item.setText(_translate("Dialog", "7"))
        item = self.tableWidget_3.verticalHeaderItem(8)
        item.setText(_translate("Dialog", "8"))
        item = self.tableWidget_3.verticalHeaderItem(9)
        item.setText(_translate("Dialog", "9"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Pais"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "# Tripulantes"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Tipo Mision"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Orbita [Km]"))
        self.Consultar_Tripuladas.setText(_translate("Dialog", "Consultar"))
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1 "))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Nombre"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Pais"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "# Tripulantes"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Tipo Mision"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Orbita [Km]"))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        item = self.tableWidget_4.item(0, 0)
        item.setText(_translate("Dialog", " "))
        item = self.tableWidget_4.item(0, 1)
        item.setText(_translate("Dialog", " "))
        item = self.tableWidget_4.item(0, 2)
        item.setText(_translate("Dialog", "  "))
        item = self.tableWidget_4.item(0, 3)
        item.setText(_translate("Dialog", " "))
        item = self.tableWidget_4.item(0, 4)
        item.setText(_translate("Dialog", "  "))
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
        self.Agregar_Tripuladas.setText(_translate("Dialog", "Agregar"))
        self.label_turno.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Paroo</p></body></html>"))
        self.label_turno.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\">Paro oep</p></body></html>"))
        self.label_turno.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Consultar Naves</p></body></html>"))
        self.label_turno_2.setToolTip(_translate("Dialog", "<html><head/><body><p align=\"center\">Paroo</p></body></html>"))
        self.label_turno_2.setWhatsThis(_translate("Dialog", "<html><head/><body><p align=\"center\">Paro oep</p></body></html>"))
        self.label_turno_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\">Agregar Nave</p></body></html>"))
