# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translate_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 589)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.buttom_line = QFrame(self.centralwidget)
        self.buttom_line.setObjectName(u"buttom_line")
        self.buttom_line.setMinimumSize(QSize(0, 5))
        self.buttom_line.setMaximumSize(QSize(16777215, 5))
        self.buttom_line.setCursor(QCursor(Qt.SizeVerCursor))
        self.buttom_line.setStyleSheet(u"")
        self.buttom_line.setFrameShape(QFrame.StyledPanel)
        self.buttom_line.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.buttom_line, 4, 1, 1, 1)

        self.right_line = QFrame(self.centralwidget)
        self.right_line.setObjectName(u"right_line")
        self.right_line.setMinimumSize(QSize(5, 0))
        self.right_line.setMaximumSize(QSize(5, 16777215))
        self.right_line.setCursor(QCursor(Qt.SizeHorCursor))
        self.right_line.setStyleSheet(u"")
        self.right_line.setFrameShape(QFrame.StyledPanel)
        self.right_line.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.right_line)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_right_line = QFrame(self.right_line)
        self.top_right_line.setObjectName(u"top_right_line")
        self.top_right_line.setMinimumSize(QSize(10, 10))
        self.top_right_line.setMaximumSize(QSize(10, 10))
        self.top_right_line.setStyleSheet(u"background-color: transparent;")
        self.top_right_line.setFrameShape(QFrame.StyledPanel)
        self.top_right_line.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.top_right_line)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.buttom_right_line = QFrame(self.right_line)
        self.buttom_right_line.setObjectName(u"buttom_right_line")
        self.buttom_right_line.setMinimumSize(QSize(10, 10))
        self.buttom_right_line.setMaximumSize(QSize(10, 10))
        self.buttom_right_line.setStyleSheet(u"background-color: transparent;")
        self.buttom_right_line.setFrameShape(QFrame.StyledPanel)
        self.buttom_right_line.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.buttom_right_line)


        self.gridLayout.addWidget(self.right_line, 1, 2, 4, 1)

        self.top_line = QFrame(self.centralwidget)
        self.top_line.setObjectName(u"top_line")
        self.top_line.setMinimumSize(QSize(0, 5))
        self.top_line.setMaximumSize(QSize(16777215, 5))
        self.top_line.setCursor(QCursor(Qt.SizeVerCursor))
        self.top_line.setStyleSheet(u"")
        self.top_line.setFrameShape(QFrame.StyledPanel)
        self.top_line.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.top_line, 1, 1, 1, 1)

        self.left_line = QFrame(self.centralwidget)
        self.left_line.setObjectName(u"left_line")
        self.left_line.setMinimumSize(QSize(5, 0))
        self.left_line.setMaximumSize(QSize(5, 16777215))
        self.left_line.setCursor(QCursor(Qt.SizeHorCursor))
        self.left_line.setStyleSheet(u"")
        self.left_line.setFrameShape(QFrame.StyledPanel)
        self.left_line.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_line)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.top_left_line = QFrame(self.left_line)
        self.top_left_line.setObjectName(u"top_left_line")
        self.top_left_line.setMinimumSize(QSize(10, 10))
        self.top_left_line.setMaximumSize(QSize(10, 10))
        self.top_left_line.setStyleSheet(u"background-color: transparent;")
        self.top_left_line.setFrameShape(QFrame.StyledPanel)
        self.top_left_line.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.top_left_line)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.buttom_left_line = QFrame(self.left_line)
        self.buttom_left_line.setObjectName(u"buttom_left_line")
        self.buttom_left_line.setMinimumSize(QSize(10, 10))
        self.buttom_left_line.setMaximumSize(QSize(10, 10))
        self.buttom_left_line.setStyleSheet(u"background-color: transparent;")
        self.buttom_left_line.setFrameShape(QFrame.StyledPanel)
        self.buttom_left_line.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.buttom_left_line)


        self.gridLayout.addWidget(self.left_line, 1, 0, 4, 1)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setStyleSheet(u"#main_widget {\n"
"\n"
"border: 1px solid #e8e8e8;\n"
"border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.main_widget, 2, 1, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

