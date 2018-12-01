# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lotteryGUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from lotteryApp.lotteryGUI import Ui_MainWindow
from PyQt5 import QtWidgets

import random



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def menu():
    user_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    matched_numbers = user_numbers.intersection(lottery_numbers)
    ui.outputTxt.setText("You guessed {}. You won ${}!".format(matched_numbers, 100 ** len(matched_numbers)))
    ui.numbersLbl.setText("The Winners: " + str(lottery_numbers))


def get_player_numbers():
    number_csv = ui.inputTxt.toPlainText()
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    # ui.numbersLbl.setText("function working")
    print(integer_set)
    return integer_set


def create_lottery_numbers():
    # ui.numbersLbl.setText("function working")
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    print(values)
    return values



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.gameBtn.clicked.connect(menu)
    ui.exitBtn.clicked.connect(app.quit)

    MainWindow.show()
    sys.exit(app.exec_())

