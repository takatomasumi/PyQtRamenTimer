#coding: utf-8

import PyQt4.QtGui as QtGui

class ButtonBoxWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.start_button = QtGui.QPushButton("Start", parent=self)
        self.stop_button = QtGui.QPushButton("Stop", parent=self)
        self.reset_button = QtGui.QPushButton("Reset", parent=self)
        self.quit_button = QtGui.QPushButton("Quit", parent=self)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.start_button, 0, 0)
        layout.addWidget(self.stop_button, 0, 1)
        layout.addWidget(self.reset_button, 1, 0)
        layout.addWidget(self.quit_button, 1, 1)

        self.setLayout(layout)
