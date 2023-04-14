from PySide6.QtWidgets import QMainWindow, QApplication, QMenuBar, QMenu
import PySide6QtAds as pqt
from mainwindow_ui import Ui_MainWindow
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QPoint, QSize
from PySide6.QtGui import QIcon, QAction, QResizeEvent, QCursor, QMouseEvent


class Main_menu_bar(QMainWindow):
    def __init__(self):
        super().__init__()
        menubar = self.menuBar()
        self.isAppEntered = False
        file_menu = QMenu("File", self)
        file_edit = QMenu("Edit", self)
        file_window = QMenu("Window", self)
        file_view = QMenu("View", self)
        file_help = QMenu("Help", self)
        self.setStyleSheet('''
        background-color:  #e8e8e8; font-size: 10pt; ''')
        menubar.addMenu(file_menu)
        menubar.addMenu(file_edit)
        menubar.addMenu(file_window)
        menubar.addMenu(file_view)
        menubar.addMenu(file_help)
        style = "QMenuBar::item:selected { background: #c8c8c8; border-radius: 2px;} QMenuBar::item:pressed {  background: #c8c8c8; }"
        menubar.setStyleSheet(style)
        file_menu.setStyleSheet(
            "QMenu::item:selected { background-color: #c8c8c8; }")
        # =======================
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        file_menu.addActions([new_action, open_action])


class Main_ui(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_ui, self).__init__()
        self.setupUi(self)
        # =======================end headers===========================#
        # remove default window title
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.WindowShadeButtonHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.app_close.clicked.connect(lambda: self.close())
        # self.app_minimize.clicked.connect(lambda: self.showMinimized())
        self.app_maximize.clicked.connect(self.resize_app)
        self.app_minimize.clicked.connect(self.minimized_animation)
        self.headers.mousePressEvent = self.pressWindow
        # =======================end headers===========================#
        file_menu = QMenu('&File')
        self.app_menu_bar = QMenuBar()
        self.app_menu_bar.addMenu(file_menu)
        self.headers_seconds_layouts.addWidget(Main_menu_bar())

    # ===========================Resize function ===========================#
    def enterEvent(self, event):
        self.isAppEntered = True
        # if pointer_x >= 0 and pointer_x <= 4 and pointer_y >= 0 and pointer_y <= 580:
        #     print(f'{pointer_x}, {pointer_y}')
        #     self.setCursor(Qt.SizeHorCursor)
        # else:
        #     self.setCursor(QCursor(Qt.ArrowCursor))
        return super().enterEvent(event)

    def leaveEvent(self, event):
        self.isAppEntered = False
        return super().leaveEvent(event)

    # ===========================End resize function=======================#
    def on_focus_changed(old, new):
        pos = QCursor.pos()
        print(f"Cursor position: {pos.x()}, {pos.y()}")

    # ======================= headers functions ===========================#

    def pressWindow(self, event):
        if not self.isMaximized():
            if event.button() == Qt.MouseButton.LeftButton:
                self._move()
                return super().mousePressEvent(event)

    def _move(self):
        window = self.window().windowHandle()
        window.startSystemMove()

    def resize_app(self):
        print(self.isMaximized())
        if self.isMaximized():
            self.showNormal()
            self.app_maximize.setIcon(QIcon(u":/icons/maximize.png"))
        else:
            self.showMaximized()
            self.app_maximize.setIcon(QIcon(u":/icons/compress.png"))

    def maximised_app(self):
        pass

    def minimized_animation(self):
        self.showMinimized()
        pass
    # ======================= end headers functions ===========================#


if __name__ == '__main__':
    app = QApplication([])
    window = Main_ui()
    window.show()
    app.exec()
