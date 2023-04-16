from PySide6.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu, QSizeGrip
from translate_ui_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QPoint, QSize
from PySide6.QtGui import QIcon, QAction, QResizeEvent, QCursor, QMouseEvent

import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        QSizeGrip(self.top_left_line)
        QSizeGrip(self.top_right_line)
        QSizeGrip(self.buttom_left_line)
        QSizeGrip(self.buttom_right_line)
    #     self.top_line.enterEvent = self.handleEnterEvent
    #     self.top_line.leaveEvent = self.handleLeaveEvent

    # def handleEnterEvent(self, event):
    #     print('EnterEvent')

    # def handleLeaveEvent(self, event):
    #     print('LeaveEvent')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowFlags(Qt.FramelessWindowHint)
    # window.setWindowOpacity(0)
    # window.left_line.setWindowOpacity
    # window.main_widget.setStyleSheet('background-color: #555;')
    # window.main_widget.setWindowOpacity(1)
    window.setAttribute(Qt.WA_TranslucentBackground)

    # hidden mouse resize line
    window.left_line.setStyleSheet("background-color: rgba(0,0,0,0.01)")
    window.top_line.setStyleSheet("background-color: rgba(0,0,0,0.01)")
    window.buttom_line.setStyleSheet("background-color: rgba(0,0,0,0.01)")
    window.right_line.setStyleSheet("background-color: rgba(0,0,0,0.01)")

    window.show()
    sys.exit(app.exec())
