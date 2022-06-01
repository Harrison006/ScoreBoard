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
        self.display_gallows()

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
        point = self.ui.spinBox_2.value() 
        team1_point += int(point)
        self.ui.pushButton_14.setText(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)
    def preset2_left(self):
        team1_point = MainWindow.team_1_point
        point = self.ui.spinBox_3.value() 
        team1_point += int(point)
        self.ui.pushButton_14.setText(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)
    def preset3_left(self):
        team1_point = MainWindow.team_1_point
        point = self.ui.spinBox_4.value() 
        team1_point += int(point)
        self.ui.pushButton_14.setText(str(team1_point) + " Points")
        MainWindow.team_1_point += int(point)
    def remove_point_button_1(self):
        team1_point = MainWindow.team_1_point
        team1_point -= 1
        self.ui.pushButton_14.setText(str(team1_point) + " Points")
        MainWindow.team_1_point -= 1
    #team 2 points
    def preset1_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.spinBox_2.value() 
        team2_point += int(point)
        self.ui.pushButton_15.setText(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    def preset2_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.spinBox_3.value() 
        team2_point += int(point)
        self.ui.pushButton_15.setText(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    def preset3_right(self):
        team2_point = MainWindow.team_2_point
        point = self.ui.spinBox_4.value() 
        team2_point += int(point)
        self.ui.pushButton_15.setText(str(team2_point) + " Points")
        MainWindow.team_2_point += int(point)
    def remove_point_button_2(self):
        team2_point = MainWindow.team_2_point
        team2_point -= 1
        self.ui.pushButton_15.setText(str(team2_point) + " Points")
        MainWindow.team_2_point -= 1
    # reset scoreboard
    def reset_points(self):
        MainWindow.team_1_point = 0
        MainWindow.team_2_point = 0
        self.ui.pushButton_15.setText("0 Points")
        self.ui.pushButton_14.setText("0 Points")
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
        self.ui.pushButton_3.setEnabled(True)
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
        self.ui.pushButton_3.setEnabled(True)
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
        self.ui.pushButton_3.setEnabled(True)

    #save data
    def save_data(self):
        team_1_name = self.ui.lineEdit.text()
        team_2_name = self.ui.lineEdit_2.text()
        team_1_points = MainWindow.team_1_point 
        team_2_points = MainWindow.team_2_point 
        final_time = self.time_left_int
        final_name = (team_1_name + ", " + team_2_name)
        
        if MainWindow.thing > 0:
            with open (final_name + '.txt', 'w') as f:
                f.write(str(team_1_points))
                f.write('\n')
                f.write(str(team_2_points))
                f.write('\n')
                f.write(str(final_time))
                f.close()
        if main_win.thing == 0:
            with open(final_name + '.txt', 'a') as f:
                f.write(str(team_1_points))
                f.write('\n')
                f.write(str(team_2_points))
                f.write('\n')
                f.write(str(final_time))
                f.close()

    def load_data(self):
        MainWindow.thing = 0
        team_1_name = self.ui.lineEdit.text()
        print(team_1_name)
        team_2_name = self.ui.lineEdit_2.text()
        print(team_2_name)
        team_name = team_1_name.lower() + ", "+ team_2_name.lower()
        print(team_name)

        
        
        with open(team_name + ".txt", "r") as f:
            MainWindow.team_1_point = int(f.readline())
            print(MainWindow.team_1_point)
            self.ui.pushButton_14.setText(str(MainWindow.team_1_point) + " Points")
            MainWindow.team_2_point = int(f.readline())
            self.ui.pushButton_15.setText(str(MainWindow.team_2_point) + " Points")
            print(MainWindow.team_2_point)
            self.time_left_int = int(f.readline() )
            
            print(self.time_left_int) 
            t = self.time_left_int

            mins, secs = divmod(t, 60)
            timeformats = '{:02d}:{:02d}'.format(mins, secs)
            self.ui.Timer.setText(timeformats)
        
             
            f.close()
        MainWindow.thing += 1

    def update_gui(self):
        times = self.time_left_int
        mins, secs = divmod(times, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        self.ui.Timer.setText(timeformat)


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
