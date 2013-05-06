#coding: utf-8

import sys
import PyQt4.QtGui as QtGui
import ButtonBoxWidget
import CountDownWidget
import TimeSettingWidget

PANEL_HEIGHT = 450
PANEL_WIDTH = 350
WINDOW_TITLE = "Ramen Timer"

def main():
    app = QtGui.QApplication(sys.argv)
    panel = QtGui.QWidget()

    #time_widget = TimeSettingWidget.TimeSettingWidget(parent=panel)
    countdown_widget = CountDownWidget.CountDownWidget(parent=panel)
    button_box_widget = ButtonBoxWidget.ButtonBoxWidget(parent=panel)

    panel_layout = QtGui.QVBoxLayout()

   #panel_layout.addWidget(time_widget)
    panel_layout.addWidget(countdown_widget)
    panel_layout.addWidget(button_box_widget)
    panel.setLayout(panel_layout)
    panel.setFixedSize(PANEL_HEIGHT, PANEL_WIDTH)

    main_window = QtGui.QMainWindow()
    main_window.setWindowTitle(WINDOW_TITLE)
    main_window.setCentralWidget(panel)
    main_window.show()

    #time_widget.set_button.clicked.connect(time_widget.set_time)
    #time_widget.set_button.clicked.connect(countdown_widget.set_time)
    countdown_widget.set_button.clicked.connect(countdown_widget.set_time)
    button_box_widget.start_button.clicked.connect(countdown_widget.start_countdown)
    button_box_widget.stop_button.clicked.connect(countdown_widget.stop_countdown)
    button_box_widget.reset_button.clicked.connect(countdown_widget.reset_count)
    #button_box_widget.reset_button.clicked.connect(time_widget.reset_edit)
    button_box_widget.quit_button.clicked.connect(app.quit)

    app.exec_()

if __name__ == '__main__':
    main()
