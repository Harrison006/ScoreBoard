import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from pip import main
from PyQt6 import QtCore, QtGui, QtWidgets
from qt import *
import time
from PyQt6.QtGui import QPixmap
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *


def set_button_enabled(self,val):

    self.ui.preset2_left.setEnabled(val)
