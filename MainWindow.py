import imp
import sys
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


    def show(self):
        self.main_win.show()

    def leftscore(self):
        self.ui