#coding: utf-8

import PyQt4.QtGui as QtGui

LABEL_CAPTION = "Set Time"
EDIT_WIDTH = 100
BUTTON_LABEL = "Reflect"

class TimeSettingWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent=parent)
        self.setup_ui()

    def setup_ui(self):
        self.label = QtGui.QLabel(LABEL_CAPTION)

        self.line_edit = QtGui.QLineEdit()
        self.line_edit.setMaxLength(3)
        self.line_edit.setFixedWidth(EDIT_WIDTH)

        self.set_button = QtGui.QPushButton(BUTTON_LABEL, parent=self)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.set_button)
        self.setLayout(layout)

    def set_time(self):
        #TODO check
        self.edit_count = self.line_edit.text()

    def reset_edit(self):
        self.line_edit.clear()
