from PySide6.QtCore import QPropertyAnimation, QRect
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Minimize")
        self.setCentralWidget(self.button)
        self.setGeometry(QRect(100, 100, 200, 200))
        self.button.clicked.connect(self.minimize)

    def minimize(self):
        print('button clicked')
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(500)
        print(self.geometry())
        self.animation.setStartValue(QRect(self.geometry()))
        self.animation.setEndValue(self.geometry())
        print(self.geometry())

        self.animation.start()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
