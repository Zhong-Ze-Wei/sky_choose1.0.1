# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wheelset.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setStyleSheet("#Form{background-color: rgb(0, 0, 0)}")
        Form.resize(500, 450)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 451, 341))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 360, 201, 51))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 360, 201, 51))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:rgb(0, 0, 0);boder:4px solid red;font-family:\'宋体\';font-size:30px;color:rgb(225,225,225,255);\n"
"}\n"
"QPushButton:hover{background-color:rgb(100, 100, 100)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.Print)
        self.pushButton.clicked.connect(Form.close)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "抽签对象写入程序"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.pushButton_2.setText(_translate("Form", "取消"))
        self.textEdit.setPlaceholderText("请输入参与抽签对象,一行写一个，写完后点确认即可关闭")

    def Print(self):
        str = self.textEdit.toPlainText()
        doc = open('name.txt','w',encoding="utf-8")
        print(str,file=doc)
        doc.close()
'''        self.pushButton().information(self, "提示", "定义成功！", QMessageBox.Yes)
        dialog = QDialog()
		pushButton = QPushButton("ok", dialog )
		pushButton.move(50,50)
		dialog.setWindowTitle("Dialog")
		dialog.setWindowModality(Qt.ApplicationModal)
		dialog.exec_()'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())