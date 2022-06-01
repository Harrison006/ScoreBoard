import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from qt import *
import time
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

DURATION_INT = 60
DURATION_INT_2 = 0

class MainWindow:
    team_1_point = 0
    team_2_point = 0
    timers = 60
    ver = 0
    thing = 0
    
    

    def __init__(self):
        
        self.time_left_int = DURATION_INT
        self.widget_counter_int = 0
        self.time_left_int_2 = DURATION_INT_2
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.signals()

    def show(self):
        self.main_win.show()

    def signals(self):
        """
        Connects the UI buttons to the corresponding functions (see slots)
        """
        #team 1 points
        self.ui.preset1_left.clicked.connect(self.preset1_left)
        self.ui.preset2_left.clicked.connect(self.preset2_left)
        self.ui.preset3_left.clicked.connect(self.preset3_left)
        #team 2 points 
        self.ui.preset1_right.clicked.connect(self.preset1_right)
        self.ui.preset2_right.clicked.connect(self.preset2_right)
        self.ui.preset3_right.clicked.connect(self.preset3_right)
        #timer buttons
        self.ui.Pause_timer.clicked.connect(self.pause_timer)
        #self.ui.Timer.valueChanged.connect(self.spin)
        self.ui.Set_time.clicked.connect(self.add)
        #name change
        
    #team 1 point
    def preset1_left(self):
        team1_point = MainWindow.team_1_point
        point = self.ui.preset1Spin_left.value() 
        team1_point += int(point)
        self.ui.LeftTeamNumber.setNumDigits(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)
    def preset2_left(self):
        team1_point = MainWindow.team_1_point
        point = self.ui.preset2Spin_left.value() 
        team1_point += int(point)
        self.ui.LeftTeamNumber.setNumDigits(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)
    def preset3_left(self):
        team1_point = MainWindow.team_1_point
        point = self.ui.preset3Spin_left.value() 
        team1_point += int(point)
        self.ui.LeftTeamNumber.setNumDigits(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)

    #team 2 points
    def preset1_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.preset1spin_right.value() 
        team2_point += int(point)
        self.ui.RightTeamNumber.setNumDigits(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    def preset2_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.preset2spin_right.value() 
        team2_point += int(point)
        self.ui.RightTeamNumber.setNumDigits(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    def preset3_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.preset3spin_right.value() 
        team2_point += int(point)
        self.ui.RightTeamNumber.setNumDigits(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    #timer
    def add(self):

        self.time_left_int_2 += 3
        self.ui.pushButton_3.setEnabled(False)
        self.startin()

    def timer_start(self):

        MainWindow.ver += 1
        self.my_qtimer = QtCore.QTimer()
        
        self.my_qtimer.timeout.connect(self.timer_timeout)
        self.my_qtimer.start(1000)
        
        self.update_gui()
    def startin(self):
        self.my_ctimer = QtCore.QTimer()
        self.my_ctimer.timeout.connect(self.timer_timeout_2)
        self.my_ctimer.start(1000)
        self.update_gui_2()


    def timer_timeout(self):
        self.time_left_int -= 1

        if self.time_left_int == 0:
            self.ui.Timer.setText("0:0")
            self.my_qtimer.stop()
            self.ui.pushButton_3.setEnabled(True)
            
  

        self.update_gui()
    
    def pause_timer(self):
        self.my_qtimer.stop()
        self.ui.Pause_timer.setEnabled(True)
    def spin(self):
        t = self.ui.spinBox.value()
        int_t = t*10
        int(int_t)
        display_timer = int(int_t*6)
        mins, secs = divmod(display_timer, 60)
        timeformats = '{:02d}:{:02d}'.format(mins, secs)
        self.ui.Timer.setText(timeformats)
        self.time_left_int = display_timer
        if MainWindow.ver == 1:
            self.my_qtimer.stop()
        self.ui.Set_time.setEnabled(True)
    def reset_timer(self):
        self.my_qtimer.stop()
        t = self.ui.spinBox.value()
        int_t = t*10
        int(int_t)
        display_timer = int(int_t*6)
        mins, secs = divmod(display_timer, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        self.ui.Timer.setText(timeformat)
        self.time_left_int = display_timer
        self.ui.Reset_timer.setEnabled(True)
    def timer_timeout_2(self):
    
        self.time_left_int_2 -= 1
        
        if self.time_left_int_2 == 0:
            self.ui.count_start.setText(str(" "))
            self.my_ctimer.stop()
            self.timer_start()
            MainWindow.DURATION_INT_2 = 0
        self.update_gui_2()
    def update_gui_2(self):
       t = self.time_left_int_2 
     
       self.ui.count_start.setText(str(t))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())