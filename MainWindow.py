import imp
import sys
import time
from PyQt6 import uic
from Ui_scoreboard import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QPixmap
class MainWindow:
    def __init__(self):
        #ui elements
        self.main_win = QMainWindow()
        self.ui =Ui_MainWindow
        self.ui.setupUi(self.main_win)
        #init ui with values
        self.leftscore()
        self.rightscore()
        self.timer()
        self.leftteam()
        self.rightteam()
        self.settimer()

# time part

starttime = time.time()
timevalue = ""



    def show(self):
        self.main_win.show()

    def leftscore(self):
        self.ui

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())