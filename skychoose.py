# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skychoose.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from Instruction import *
from wheelset import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-color: rgb(0, 0, 0)}")
        MainWindow.resize(440, 409)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 30, 321, 61))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 110, 321, 61))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 190, 321, 61))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 270, 321, 61))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 399, 22))
        self.menubar.setObjectName("menubar")
        self.menuSKY_CHOOSE = QtWidgets.QMenu(self.menubar)
        self.menuSKY_CHOOSE.setObjectName("menuSKY_CHOOSE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSKY_CHOOSE.menuAction())

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.Start)
        self.pushButton_2.clicked.connect(self.wheelset)
        self.pushButton_3.clicked.connect(self.Instruction)
        self.pushButton_4.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SKY'CHOOSE"))
        self.pushButton.setText(_translate("MainWindow", "启动转盘"))
        self.pushButton_2.setText(_translate("MainWindow", "转盘设置"))
        self.pushButton_3.setText(_translate("MainWindow", "操作说明"))
        self.pushButton_4.setText(_translate("MainWindow", "退出游戏"))

    def wheelset(self):
        self.form2 = QtWidgets.QWidget()
        self.ui2 = Ui_Form()
        self.ui2.setupUi(self.form2)
        self.form2.show()

    def Instruction(self):
        self.form3 = QtWidgets.QWidget()
        self.ui3 = Ui_Frame()
        self.ui3.setupUi(self.form3)
        self.form3.show()

    def Start(self):
        os.system("game.py")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())