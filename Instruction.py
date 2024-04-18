# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Instruction.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setStyleSheet("#Frame{background-color: rgb(0, 0, 0)}")
        Frame.resize(442, 472)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 391, 371))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(110, 400, 201, 41))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        self.pushButton.clicked.connect(Frame.close)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "操作说明"))
        self.pushButton.setText(_translate("Frame", "返回"))
        self.textEdit.setText("点开转盘设置修改转盘内容:\n在弹出窗口中输入所有参与抽签的对象，输入完成后点击确定按钮。\n\n点击启动转盘以启动转盘程序:\n按下空格健不松开来开始转盘转动，松开空格健来停下转盘。" )
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Frame()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

