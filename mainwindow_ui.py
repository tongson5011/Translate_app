# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(883, 581)
        MainWindow.setStyleSheet(u"")
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionNew_2 = QAction(MainWindow)
        self.actionNew_2.setObjectName(u"actionNew_2")
        self.actionEdiw = QAction(MainWindow)
        self.actionEdiw.setObjectName(u"actionEdiw")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background-color: rgb(248, 248, 248);\n"
"	border: 10px solid #000;\n"
"	border-radius: 8px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.headers = QFrame(self.centralwidget)
        self.headers.setObjectName(u"headers")
        self.headers.setMinimumSize(QSize(0, 55))
        self.headers.setMaximumSize(QSize(16777215, 55))
        self.headers.setStyleSheet(u"#headers {\n"
"	background-color: #e1e1e1;\n"
"	color: #ababab;\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #d8d8d8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #e1e1e1;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QToolButton {\n"
"	background-color: #e8e8e8;\n"
"	border: 0px solid;\n"
"	border-radius: 5px;\n"
"}\n"
"QToolButton:hover {\n"
"	background-color: #d8d8d8;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.headers)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.headers_first_layouts = QHBoxLayout()
        self.headers_first_layouts.setSpacing(0)
        self.headers_first_layouts.setObjectName(u"headers_first_layouts")
        self.headers_first_layouts.setContentsMargins(6, -1, 0, -1)
        self.app_logo = QLabel(self.headers)
        self.app_logo.setObjectName(u"app_logo")
        self.app_logo.setMinimumSize(QSize(20, 20))
        self.app_logo.setMaximumSize(QSize(20, 20))
        self.app_logo.setStyleSheet(u"")
        self.app_logo.setPixmap(QPixmap(u"assects/icon/logo.png"))
        self.app_logo.setScaledContents(True)
        self.app_logo.setAlignment(Qt.AlignCenter)

        self.headers_first_layouts.addWidget(self.app_logo, 0, Qt.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.headers_first_layouts.addItem(self.horizontalSpacer_2)

        self.label = QLabel(self.headers)
        self.label.setObjectName(u"label")

        self.headers_first_layouts.addWidget(self.label, 0, Qt.AlignHCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.headers_first_layouts.addItem(self.horizontalSpacer)

        self.app_minimize = QPushButton(self.headers)
        self.app_minimize.setObjectName(u"app_minimize")
        self.app_minimize.setMinimumSize(QSize(40, 27))
        self.app_minimize.setMaximumSize(QSize(40, 27))
        font = QFont()
        font.setPointSize(19)
        self.app_minimize.setFont(font)

        self.headers_first_layouts.addWidget(self.app_minimize)

        self.app_maximize = QPushButton(self.headers)
        self.app_maximize.setObjectName(u"app_maximize")
        self.app_maximize.setMinimumSize(QSize(40, 27))
        self.app_maximize.setMaximumSize(QSize(40, 27))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.app_maximize.setFont(font1)
        icon = QIcon()
        icon.addFile(u"assects/icon/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.app_maximize.setIcon(icon)

        self.headers_first_layouts.addWidget(self.app_maximize)

        self.app_close = QPushButton(self.headers)
        self.app_close.setObjectName(u"app_close")
        self.app_close.setMinimumSize(QSize(40, 27))
        self.app_close.setMaximumSize(QSize(40, 27))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        font2.setBold(False)
        self.app_close.setFont(font2)
        self.app_close.setStyleSheet(u"\n"
"#app_close {\n"
"	border-top-right-radius: 8px;\n"
"}\n"
"#app_close:hover {\n"
"	background-color: #f12121;\n"
"}")

        self.headers_first_layouts.addWidget(self.app_close)


        self.verticalLayout_2.addLayout(self.headers_first_layouts)

        self.header_second_layouts = QFrame(self.headers)
        self.header_second_layouts.setObjectName(u"header_second_layouts")
        self.header_second_layouts.setMinimumSize(QSize(0, 25))
        self.header_second_layouts.setMaximumSize(QSize(16777215, 25))
        self.header_second_layouts.setStyleSheet(u"#headers #header_second_layouts {\n"
"	background-color: #e8e8e8;\n"
"}")
        self.headers_seconds_layouts = QHBoxLayout(self.header_second_layouts)
        self.headers_seconds_layouts.setSpacing(0)
        self.headers_seconds_layouts.setObjectName(u"headers_seconds_layouts")
        self.headers_seconds_layouts.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.header_second_layouts, 0, Qt.AlignBottom)

        self.verticalLayout_2.setStretch(0, 9)

        self.verticalLayout.addWidget(self.headers)

        self.contents = QFrame(self.centralwidget)
        self.contents.setObjectName(u"contents")
        self.contents.setMinimumSize(QSize(0, 0))
        self.pushButton = QPushButton(self.contents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(190, 200, 75, 24))
        self.radioButton = QRadioButton(self.contents)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(370, 260, 89, 20))

        self.verticalLayout.addWidget(self.contents)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionNew_2.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.actionEdiw.setText(QCoreApplication.translate("MainWindow", u"Ediw", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"open", None))
        self.app_logo.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Translate design by struyen247", None))
        self.app_minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.app_maximize.setText("")
        self.app_close.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
    # retranslateUi

