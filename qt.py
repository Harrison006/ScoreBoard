# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.preset2_left = QtWidgets.QPushButton(self.centralwidget)
        self.preset2_left.setGeometry(QtCore.QRect(640, 888, 111, 41))
        self.preset2_left.setObjectName("preset2_left")
        self.preset3_left = QtWidgets.QPushButton(self.centralwidget)
        self.preset3_left.setGeometry(QtCore.QRect(640, 938, 111, 41))
        self.preset3_left.setObjectName("preset3_left")
        self.preset1_left = QtWidgets.QPushButton(self.centralwidget)
        self.preset1_left.setGeometry(QtCore.QRect(640, 838, 111, 41))
        self.preset1_left.setObjectName("preset1_left")
        self.preset2_right = QtWidgets.QPushButton(self.centralwidget)
        self.preset2_right.setGeometry(QtCore.QRect(1210, 888, 111, 41))
        self.preset2_right.setObjectName("preset2_right")
        self.preset3_right = QtWidgets.QPushButton(self.centralwidget)
        self.preset3_right.setGeometry(QtCore.QRect(1210, 938, 111, 41))
        self.preset3_right.setObjectName("preset3_right")
        self.preset1_right = QtWidgets.QPushButton(self.centralwidget)
        self.preset1_right.setGeometry(QtCore.QRect(1210, 838, 111, 41))
        self.preset1_right.setObjectName("preset1_right")
        self.Start_timer = QtWidgets.QPushButton(self.centralwidget)
        self.Start_timer.setGeometry(QtCore.QRect(800, 888, 101, 41))
        self.Start_timer.setObjectName("Start_timer")
        self.Reset_timer = QtWidgets.QPushButton(self.centralwidget)
        self.Reset_timer.setGeometry(QtCore.QRect(1050, 888, 101, 41))
        self.Reset_timer.setObjectName("Reset_timer")
        self.Pause_timer = QtWidgets.QPushButton(self.centralwidget)
        self.Pause_timer.setGeometry(QtCore.QRect(930, 888, 101, 41))
        self.Pause_timer.setObjectName("Pause_timer")
        self.Left_Team_name = QtWidgets.QPushButton(self.centralwidget)
        self.Left_Team_name.setGeometry(QtCore.QRect(650, 988, 75, 23))
        self.Left_Team_name.setObjectName("Left_Team_name")
        self.Timer = QtWidgets.QLCDNumber(self.centralwidget)
        self.Timer.setGeometry(QtCore.QRect(720, 100, 451, 191))
        self.Timer.setDigitCount(4)
        self.Timer.setObjectName("Timer")
        self.LeftTeamNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.LeftTeamNumber.setGeometry(QtCore.QRect(200, 270, 401, 251))
        self.LeftTeamNumber.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";")
        self.LeftTeamNumber.setLineWidth(0)
        self.LeftTeamNumber.setDigitCount(1)
        self.LeftTeamNumber.setObjectName("LeftTeamNumber")
        self.Set_time = QtWidgets.QPushButton(self.centralwidget)
        self.Set_time.setGeometry(QtCore.QRect(940, 948, 75, 23))
        self.Set_time.setObjectName("Set_time")
        self.RightTeamNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.RightTeamNumber.setGeometry(QtCore.QRect(1310, 260, 401, 251))
        self.RightTeamNumber.setStyleSheet("font: 50pt \"MS Shell Dlg 2\";")
        self.RightTeamNumber.setLineWidth(0)
        self.RightTeamNumber.setDigitCount(1)
        self.RightTeamNumber.setObjectName("RightTeamNumber")
        self.Left_Team_name_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Left_Team_name_2.setGeometry(QtCore.QRect(1230, 988, 75, 23))
        self.Left_Team_name_2.setObjectName("Left_Team_name_2")
        self.timervalset = QtWidgets.QSpinBox(self.centralwidget)
        self.timervalset.setGeometry(QtCore.QRect(950, 980, 51, 21))
        self.timervalset.setObjectName("timervalset")
        self.LeftTeamName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.LeftTeamName.setGeometry(QtCore.QRect(50, 140, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.LeftTeamName.setFont(font)
        self.LeftTeamName.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.LeftTeamName.setStyleSheet("background-color: rgb(0, 174, 239);")
        self.LeftTeamName.setBackgroundVisible(False)
        self.LeftTeamName.setObjectName("LeftTeamName")
        self.preset1Spin_left = QtWidgets.QSpinBox(self.centralwidget)
        self.preset1Spin_left.setGeometry(QtCore.QRect(580, 850, 51, 21))
        self.preset1Spin_left.setObjectName("preset1Spin_left")
        self.preset2spin_left = QtWidgets.QSpinBox(self.centralwidget)
        self.preset2spin_left.setGeometry(QtCore.QRect(580, 900, 51, 21))
        self.preset2spin_left.setObjectName("preset2spin_left")
        self.preset3spin_left = QtWidgets.QSpinBox(self.centralwidget)
        self.preset3spin_left.setGeometry(QtCore.QRect(580, 950, 51, 21))
        self.preset3spin_left.setObjectName("preset3spin_left")
        self.preset1spin_right = QtWidgets.QSpinBox(self.centralwidget)
        self.preset1spin_right.setGeometry(QtCore.QRect(1330, 850, 51, 21))
        self.preset1spin_right.setObjectName("preset1spin_right")
        self.preset2spin_right = QtWidgets.QSpinBox(self.centralwidget)
        self.preset2spin_right.setGeometry(QtCore.QRect(1330, 900, 51, 21))
        self.preset2spin_right.setObjectName("preset2spin_right")
        self.preset3spin_right = QtWidgets.QSpinBox(self.centralwidget)
        self.preset3spin_right.setGeometry(QtCore.QRect(1330, 950, 51, 21))
        self.preset3spin_right.setObjectName("preset3spin_right")
        self.set1_left = QtWidgets.QPushButton(self.centralwidget)
        self.set1_left.setGeometry(QtCore.QRect(500, 850, 75, 23))
        self.set1_left.setObjectName("set1_left")
        self.set2_left = QtWidgets.QPushButton(self.centralwidget)
        self.set2_left.setGeometry(QtCore.QRect(500, 900, 75, 23))
        self.set2_left.setObjectName("set2_left")
        self.set3_left = QtWidgets.QPushButton(self.centralwidget)
        self.set3_left.setGeometry(QtCore.QRect(500, 950, 75, 23))
        self.set3_left.setObjectName("set3_left")
        self.set1_right = QtWidgets.QPushButton(self.centralwidget)
        self.set1_right.setGeometry(QtCore.QRect(1390, 850, 75, 23))
        self.set1_right.setObjectName("set1_right")
        self.set2_right = QtWidgets.QPushButton(self.centralwidget)
        self.set2_right.setGeometry(QtCore.QRect(1390, 900, 75, 23))
        self.set2_right.setObjectName("set2_right")
        self.set3_right = QtWidgets.QPushButton(self.centralwidget)
        self.set3_right.setGeometry(QtCore.QRect(1390, 950, 75, 23))
        self.set3_right.setObjectName("set3_right")
        self.RightTeamName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.RightTeamName.setGeometry(QtCore.QRect(1310, 140, 551, 121))
        font = QtGui.QFont()
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.RightTeamName.setFont(font)
        self.RightTeamName.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.RightTeamName.setStyleSheet("background-color: rgb(186, 1, 78);")
        self.RightTeamName.setBackgroundVisible(False)
        self.RightTeamName.setObjectName("RightTeamName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menuScoreboard = QtWidgets.QMenu(self.menubar)
        self.menuScoreboard.setObjectName("menuScoreboard")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionScore_Settings = QtGui.QAction(MainWindow)
        self.actionScore_Settings.setObjectName("actionScore_Settings")
        self.actionTeam_Names = QtGui.QAction(MainWindow)
        self.actionTeam_Names.setObjectName("actionTeam_Names")
        self.menubar.addAction(self.menuScoreboard.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.preset2_left.setText(_translate("MainWindow", "Preset 2"))
        self.preset3_left.setText(_translate("MainWindow", "Preset 3"))
        self.preset1_left.setText(_translate("MainWindow", "Preset 1"))
        self.preset2_right.setText(_translate("MainWindow", "Preset 2"))
        self.preset3_right.setText(_translate("MainWindow", "Preset 3"))
        self.preset1_right.setText(_translate("MainWindow", "Preset 1"))
        self.Start_timer.setText(_translate("MainWindow", "Start"))
        self.Reset_timer.setText(_translate("MainWindow", "Reset"))
        self.Pause_timer.setText(_translate("MainWindow", "Pause"))
        self.Left_Team_name.setText(_translate("MainWindow", "Team Name"))
        self.Set_time.setText(_translate("MainWindow", "Set Timer"))
        self.Left_Team_name_2.setText(_translate("MainWindow", "Team Name"))
        self.LeftTeamName.setPlainText(_translate("MainWindow", "Team Name"))
        self.set1_left.setText(_translate("MainWindow", "set"))
        self.set2_left.setText(_translate("MainWindow", "set"))
        self.set3_left.setText(_translate("MainWindow", "set"))
        self.set1_right.setText(_translate("MainWindow", "set"))
        self.set2_right.setText(_translate("MainWindow", "set"))
        self.set3_right.setText(_translate("MainWindow", "set"))
        self.RightTeamName.setPlainText(_translate("MainWindow", "Team Name"))
        self.menuScoreboard.setTitle(_translate("MainWindow", "Scoreboard"))
        self.actionScore_Settings.setText(_translate("MainWindow", "Score Settings"))
        self.actionTeam_Names.setText(_translate("MainWindow", "Team Names"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
