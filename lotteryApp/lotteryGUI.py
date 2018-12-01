# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lotteryGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLbl = QtWidgets.QLabel(self.centralwidget)
        self.mainLbl.setGeometry(QtCore.QRect(150, 10, 501, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.mainLbl.setFont(font)
        self.mainLbl.setObjectName("mainLbl")
        self.inputTxt = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputTxt.setGeometry(QtCore.QRect(200, 140, 381, 87))
        self.inputTxt.setObjectName("inputTxt")
        self.inpuLbl = QtWidgets.QLabel(self.centralwidget)
        self.inpuLbl.setGeometry(QtCore.QRect(130, 230, 511, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inpuLbl.setFont(font)
        self.inpuLbl.setObjectName("inpuLbl")
        self.outputTxt = QtWidgets.QTextBrowser(self.centralwidget)
        self.outputTxt.setGeometry(QtCore.QRect(140, 400, 521, 192))
        self.outputTxt.setObjectName("outputTxt")
        self.gameBtn = QtWidgets.QPushButton(self.centralwidget)
        self.gameBtn.setGeometry(QtCore.QRect(140, 640, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.gameBtn.setFont(font)
        self.gameBtn.setObjectName("gameBtn")
        self.exitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitBtn.setGeometry(QtCore.QRect(532, 640, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.exitBtn.setFont(font)
        self.exitBtn.setObjectName("exitBtn")
        self.numbersLbl = QtWidgets.QLabel(self.centralwidget)
        self.numbersLbl.setGeometry(QtCore.QRect(150, 300, 491, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.numbersLbl.setFont(font)
        self.numbersLbl.setText("")
        self.numbersLbl.setObjectName("numbersLbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 26))
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
        self.mainLbl.setText(_translate("MainWindow", "Python Lottery Game"))
        self.inpuLbl.setText(_translate("MainWindow", "Please enter your six numbers above separated by a comma"))
        self.gameBtn.setText(_translate("MainWindow", "Play"))
        self.exitBtn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

