# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '../platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 302)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plain = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plain.setGeometry(QtCore.QRect(250, 70, 321, 71))
        self.plain.setObjectName("plain")
        self.key = QtWidgets.QTextEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(250, 150, 281, 31))
        self.key.setObjectName("key")
        self.cptext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.cptext.setGeometry(QtCore.QRect(250, 190, 321, 71))
        self.cptext.setObjectName("cptext")
        self.en = QtWidgets.QPushButton(self.centralwidget)
        self.en.setGeometry(QtCore.QRect(600, 110, 75, 23))
        self.en.setObjectName("en")
        self.de = QtWidgets.QPushButton(self.centralwidget)
        self.de.setGeometry(QtCore.QRect(600, 130, 75, 23))
        self.de.setObjectName("de")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 90, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 190, 47, 13))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
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
        self.en.setText(_translate("MainWindow", "PushButton"))
        self.de.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "plain"))
        self.label_2.setText(_translate("MainWindow", "key"))
        self.label_3.setText(_translate("MainWindow", "cptext"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
