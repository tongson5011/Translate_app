from PyQt5.QtCore import QPropertyAnimation, QRect, QSize, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(200, 200))

        self.minimize_btn = QPushButton("-", self)
        self.minimize_btn.move(170, 0)
        self.minimize_btn.clicked.connect(self.minimize_animation)

    def minimize_animation(self):
        final_rect = QRect(170, 500, 0, 0)
        # Also animate the window's opacity using another QPropertyAnimation object
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)

        self.animation.setStartValue(QRect(self.geometry()))
        self.animation.setEndValue(self.geometry())
        self.animation.start()

        # self.opacity_animation = QPropertyAnimation(self, b"windowOpacity")
        # self.opacity_animation.setDuration(500)
        # self.opacity_animation.setStartValue(1.0)
        # self.opacity_animation.setEndValue(0.0)
        # self.opacity_animation.start()

    def paintEvent(self, event):
        # Override the paintEvent method to make the window transparent
        painter = QPainter(self)
        painter.setOpacity(0.5)
        painter.fillRect(self.rect(), Qt.transparent)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
