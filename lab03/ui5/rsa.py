# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plain = QtWidgets.QTextEdit(self.centralwidget)
        self.plain.setGeometry(QtCore.QRect(80, 150, 291, 71))
        self.plain.setObjectName("plain")
        self.cptext = QtWidgets.QTextEdit(self.centralwidget)
        self.cptext.setGeometry(QtCore.QRect(80, 240, 291, 71))
        self.cptext.setObjectName("cptext")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(390, 150, 291, 71))
        self.txt_info.setObjectName("txt_info")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(390, 240, 291, 71))
        self.txt_sign.setObjectName("txt_sign")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 130, 47, 13))
        self.label.setObjectName("label")
        self.cc = QtWidgets.QLabel(self.centralwidget)
        self.cc.setGeometry(QtCore.QRect(80, 220, 47, 13))
        self.cc.setObjectName("cc")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 130, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(390, 220, 47, 13))
        self.label_4.setObjectName("label_4")
        self.btn_gen_keys = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(80, 330, 75, 23))
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.en = QtWidgets.QPushButton(self.centralwidget)
        self.en.setGeometry(QtCore.QRect(80, 360, 75, 23))
        self.en.setObjectName("en")
        self.den = QtWidgets.QPushButton(self.centralwidget)
        self.den.setGeometry(QtCore.QRect(80, 390, 75, 23))
        self.den.setObjectName("den")
        self.btn_sign = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(80, 420, 75, 23))
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(80, 450, 75, 23))
        self.btn_verify.setObjectName("btn_verify")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ptext"))
        self.cc.setText(_translate("MainWindow", "cptext"))
        self.label_3.setText(_translate("MainWindow", "info"))
        self.label_4.setText(_translate("MainWindow", "sign"))
        self.btn_gen_keys.setText(_translate("MainWindow", "genkey"))
        self.en.setText(_translate("MainWindow", "en"))
        self.den.setText(_translate("MainWindow", "den"))
        self.btn_sign.setText(_translate("MainWindow", "sign"))
        self.btn_verify.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
