#coding: utf-8

import PyQt4.QtCore as QtCore
import PyQt4.QtGui as QtGui

DEFAULT_TIME = 18000
SET_LABEL_CAPTION = "Set Time"
UNIT_LABEL_CAPTION = "Min"
EDIT_WIDTH = 100
BUTTON_LABEL = "Reflect"

class CountDownWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.interval = 10
        self.setup_ui()

    def do_countdown(self):
        self.count -= 1
        self.update_display()
        if self.count <= 0:
            self.stop_countdown()

    def update_display(self):
        self.lcd_number.display("%6.2f" % (self.count / 100))
        self.lcd_number.update()

    def start_countdown(self):
        if self.count > 0:
            self.timer.start()

    def stop_countdown(self):
        self.timer.stop()

    def reset_count(self):
        self.count = DEFAULT_TIME
        self.update_display()

    def set_time(self):
        self.count = int(self.line_edit.text()) * 6000
        self.update_display()

    def reset_edit(self):
        self.line_edit.clear()

    def setup_ui(self):

        self.set_label = QtGui.QLabel(SET_LABEL_CAPTION)
        self.unit_label = QtGui.QLabel(UNIT_LABEL_CAPTION)
        self.line_edit = QtGui.QLineEdit()
        self.line_edit.setMaxLength(1)
        self.line_edit.setFixedWidth(EDIT_WIDTH)
        self.set_button = QtGui.QPushButton(BUTTON_LABEL, parent=self)

        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.timer = QtCore.QTimer(parent=self)
        self.timer.setInterval(self.interval)
        self.timer.timeout.connect(self.do_countdown)

        self.lcd_number = QtGui.QLCDNumber(parent = self)
        self.lcd_number.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.lcd_number.setFrameStyle(QtGui.QLCDNumber.NoFrame)
        self.lcd_number.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_number.setDigitCount(6)

        #layout = QtGui.QVBoxLayout()
        layout = QtGui.QGridLayout()
        layout.addWidget(self.set_label, 0, 0)
        layout.addWidget(self.line_edit, 0, 1)
        layout.addWidget(self.unit_label, 0, 2)
        layout.addWidget(self.set_button, 0, 3)
        layout.addWidget(self.lcd_number, 1, 1)
        self.setLayout(layout)
        self.reset_count()
