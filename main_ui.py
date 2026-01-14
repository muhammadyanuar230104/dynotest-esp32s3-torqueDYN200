# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStackedWidget, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.actionopen_file = QAction(MainWindow)
        self.actionopen_file.setObjectName(u"actionopen_file")
        self.actionopen_preview = QAction(MainWindow)
        self.actionopen_preview.setObjectName(u"actionopen_preview")
        self.actionopen_dashboard = QAction(MainWindow)
        self.actionopen_dashboard.setObjectName(u"actionopen_dashboard")
        self.actionclose = QAction(MainWindow)
        self.actionclose.setObjectName(u"actionclose")
        self.actionopen_2 = QAction(MainWindow)
        self.actionopen_2.setObjectName(u"actionopen_2")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionopen_calibration_torsi = QAction(MainWindow)
        self.actionopen_calibration_torsi.setObjectName(u"actionopen_calibration_torsi")
        self.actionSave_2 = QAction(MainWindow)
        self.actionSave_2.setObjectName(u"actionSave_2")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionClose_2 = QAction(MainWindow)
        self.actionClose_2.setObjectName(u"actionClose_2")
        self.actionClose_3 = QAction(MainWindow)
        self.actionClose_3.setObjectName(u"actionClose_3")
        self.actionopen_about = QAction(MainWindow)
        self.actionopen_about.setObjectName(u"actionopen_about")
        self.actionopen_calibration_rpm = QAction(MainWindow)
        self.actionopen_calibration_rpm.setObjectName(u"actionopen_calibration_rpm")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        sizePolicy.setHeightForWidth(self.main_header.sizePolicy().hasHeightForWidth())
        self.main_header.setSizePolicy(sizePolicy)
        self.main_header.setMaximumSize(QSize(16777215, 10))
        self.main_header.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.main_header.setFrameShape(QFrame.NoFrame)
        self.main_header.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setStyleSheet(u"background-color: rgb(0, 0, 255);")
        self.main_body.setFrameShape(QFrame.NoFrame)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_side_menu = QFrame(self.main_body)
        self.left_side_menu.setObjectName(u"left_side_menu")
        sizePolicy.setHeightForWidth(self.left_side_menu.sizePolicy().hasHeightForWidth())
        self.left_side_menu.setSizePolicy(sizePolicy)
        self.left_side_menu.setMaximumSize(QSize(10, 16777215))
        self.left_side_menu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.left_side_menu.setFrameShape(QFrame.NoFrame)
        self.left_side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.left_side_menu)

        self.center_main_item = QFrame(self.main_body)
        self.center_main_item.setObjectName(u"center_main_item")
        sizePolicy.setHeightForWidth(self.center_main_item.sizePolicy().hasHeightForWidth())
        self.center_main_item.setSizePolicy(sizePolicy)
        self.center_main_item.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.center_main_item.setFrameShape(QFrame.NoFrame)
        self.center_main_item.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_item)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_item)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        sizePolicy.setHeightForWidth(self.dashboard_page.sizePolicy().hasHeightForWidth())
        self.dashboard_page.setSizePolicy(sizePolicy)
        self.dashboard_page.setStyleSheet(u"background-color: rgb(255, 255, 127);")
        self.verticalLayout_3 = QVBoxLayout(self.dashboard_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.dashboard_page)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(170, 255, 255);")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_1 = QWidget(self.frame_6)
        self.widget_1.setObjectName(u"widget_1")
        sizePolicy.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy)
        self.widget_1.setStyleSheet(u"\n"
"\n"
"background-color: rgb(0, 255, 255);")

        self.verticalLayout_6.addWidget(self.widget_1)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.dashboard_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(0)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.frame_12)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy)
        self.frame_27.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_27)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_2 = QWidget(self.frame_27)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)

        self.verticalLayout_8.addWidget(self.widget_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_8)


        self.horizontalLayout_17.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_12)
        self.frame_28.setObjectName(u"frame_28")
        sizePolicy.setHeightForWidth(self.frame_28.sizePolicy().hasHeightForWidth())
        self.frame_28.setSizePolicy(sizePolicy)
        self.frame_28.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_28.setFrameShape(QFrame.NoFrame)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_28)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.widget_7 = QWidget(self.frame_28)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)

        self.verticalLayout_21.addWidget(self.widget_7)


        self.verticalLayout_22.addLayout(self.verticalLayout_21)


        self.horizontalLayout_17.addWidget(self.frame_28)

        self.frame_29 = QFrame(self.frame_12)
        self.frame_29.setObjectName(u"frame_29")
        sizePolicy.setHeightForWidth(self.frame_29.sizePolicy().hasHeightForWidth())
        self.frame_29.setSizePolicy(sizePolicy)
        self.frame_29.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_29.setFrameShape(QFrame.NoFrame)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_29)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_8 = QWidget(self.frame_29)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)

        self.verticalLayout_23.addWidget(self.widget_8)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.horizontalLayout_17.addWidget(self.frame_29)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setMaximumSize(QSize(500, 16777215))
        self.frame_13.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.box_port = QComboBox(self.frame_14)
        self.box_port.addItem("")
        self.box_port.setObjectName(u"box_port")
        sizePolicy.setHeightForWidth(self.box_port.sizePolicy().hasHeightForWidth())
        self.box_port.setSizePolicy(sizePolicy)
        font = QFont()
        self.box_port.setFont(font)
        self.box_port.setStyleSheet(u"QComboBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang */\n"
"    border: 2px solid white; /* Border putih */\n"
"    border-radius: 5px; /* Sudut membulat */\n"
"    padding: 5px; /* Padding internal */\n"
"    font-size: 16px; /* Ukuran font */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(0, 102, 255); /* Warna saat hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0); /* Warna teks dalam dropdown */\n"
"    background-color: rgb(255, 255, 255); /* Warna latar dropdown */\n"
"    selection-background-color: rgb(0, 102, 255); /* Warna pilihan yang disorot */\n"
"    selection-color: rgb(255, 255, 255); /* Warna teks pilihan yang disorot */\n"
"    border: 1px solid rgb(200, 200, 200); /* Border dropdown */\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.box_port)

        self.label_port = QLabel(self.frame_14)
        self.label_port.setObjectName(u"label_port")
        sizePolicy.setHeightForWidth(self.label_port.sizePolicy().hasHeightForWidth())
        self.label_port.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setBold(True)
        self.label_port.setFont(font1)
        self.label_port.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_port)

        self.label_baudrate = QLabel(self.frame_14)
        self.label_baudrate.setObjectName(u"label_baudrate")
        sizePolicy.setHeightForWidth(self.label_baudrate.sizePolicy().hasHeightForWidth())
        self.label_baudrate.setSizePolicy(sizePolicy)
        self.label_baudrate.setFont(font1)
        self.label_baudrate.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.label_baudrate)


        self.verticalLayout_10.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.button_connect = QPushButton(self.frame_15)
        self.button_connect.setObjectName(u"button_connect")
        sizePolicy.setHeightForWidth(self.button_connect.sizePolicy().hasHeightForWidth())
        self.button_connect.setSizePolicy(sizePolicy)
        self.button_connect.setFont(font1)
        self.button_connect.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_9.addWidget(self.button_connect)

        self.button_disconnect = QPushButton(self.frame_15)
        self.button_disconnect.setObjectName(u"button_disconnect")
        sizePolicy.setHeightForWidth(self.button_disconnect.sizePolicy().hasHeightForWidth())
        self.button_disconnect.setSizePolicy(sizePolicy)
        self.button_disconnect.setFont(font1)
        self.button_disconnect.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_disconnect)

        self.button_reset_database = QPushButton(self.frame_15)
        self.button_reset_database.setObjectName(u"button_reset_database")
        sizePolicy.setHeightForWidth(self.button_reset_database.sizePolicy().hasHeightForWidth())
        self.button_reset_database.setSizePolicy(sizePolicy)
        self.button_reset_database.setFont(font1)
        self.button_reset_database.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(255, 0, 0);\n"
"}")

        self.horizontalLayout_9.addWidget(self.button_reset_database)


        self.verticalLayout_10.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_cal_rpm = QLabel(self.frame_16)
        self.label_cal_rpm.setObjectName(u"label_cal_rpm")
        sizePolicy.setHeightForWidth(self.label_cal_rpm.sizePolicy().hasHeightForWidth())
        self.label_cal_rpm.setSizePolicy(sizePolicy)
        self.label_cal_rpm.setFont(font1)
        self.label_cal_rpm.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_cal_rpm)

        self.check_box_calibration = QCheckBox(self.frame_16)
        self.check_box_calibration.setObjectName(u"check_box_calibration")
        sizePolicy.setHeightForWidth(self.check_box_calibration.sizePolicy().hasHeightForWidth())
        self.check_box_calibration.setSizePolicy(sizePolicy)
        self.check_box_calibration.setFont(font1)
        self.check_box_calibration.setStyleSheet(u"QCheckBox {\n"
"	color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */    \n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px; /* setengah dari width/height untuk bulat sempurna */\n"
"    border: 2px solid #999;\n"
"    background-color: #ddd;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: red;\n"
"    border: 2px solid #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #55ff00;\n"
"}")

        self.horizontalLayout_6.addWidget(self.check_box_calibration)

        self.label_cal_torque = QLabel(self.frame_16)
        self.label_cal_torque.setObjectName(u"label_cal_torque")
        sizePolicy.setHeightForWidth(self.label_cal_torque.sizePolicy().hasHeightForWidth())
        self.label_cal_torque.setSizePolicy(sizePolicy)
        self.label_cal_torque.setFont(font1)
        self.label_cal_torque.setStyleSheet(u"QLabel {\n"
"    color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.label_cal_torque)


        self.verticalLayout_10.addWidget(self.frame_16)

        self.frame_18 = QFrame(self.frame_13)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_18.setFrameShape(QFrame.NoFrame)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.button_resume = QPushButton(self.frame_18)
        self.button_resume.setObjectName(u"button_resume")
        sizePolicy.setHeightForWidth(self.button_resume.sizePolicy().hasHeightForWidth())
        self.button_resume.setSizePolicy(sizePolicy)
        self.button_resume.setFont(font1)
        self.button_resume.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"			background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_12.addWidget(self.button_resume)

        self.button_stop = QPushButton(self.frame_18)
        self.button_stop.setObjectName(u"button_stop")
        sizePolicy.setHeightForWidth(self.button_stop.sizePolicy().hasHeightForWidth())
        self.button_stop.setSizePolicy(sizePolicy)
        self.button_stop.setFont(font1)
        self.button_stop.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"			background-color: rgb(255, 0, 0);\n"
"            }")

        self.horizontalLayout_12.addWidget(self.button_stop)

        self.check_box_cut_off = QCheckBox(self.frame_18)
        self.check_box_cut_off.setObjectName(u"check_box_cut_off")
        sizePolicy.setHeightForWidth(self.check_box_cut_off.sizePolicy().hasHeightForWidth())
        self.check_box_cut_off.setSizePolicy(sizePolicy)
        self.check_box_cut_off.setFont(font1)
        self.check_box_cut_off.setStyleSheet(u"QCheckBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks putih */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang biru */\n"
"    border: 2px solid rgb(255, 255, 255); /* Border putih */\n"
"    border-radius: 8px; /* Membulatkan sudut */\n"
"    padding: 10px; /* Memberi ruang di dalam elemen */\n"
"    font-size: 16px; /* Ukuran font */\n"
"    font-weight: bold; /* Teks tebal */\n"
"    text-align: center; /* Rata tengah teks */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px; /* Bulat sempurna */\n"
"    border: 2px solid #999;\n"
"    background-color: red; /* Default: merah (tidak aktif) */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: green; /* Hijau (aktif) */\n"
"    border: 2px solid #4CAF50;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: red; /* Merah (tidak aktif) */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    background-color: #ff5555; /* Lebih t"
                        "erang saat hover */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background-color: #55ff55; /* Lebih terang saat hover */\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.check_box_cut_off)


        self.verticalLayout_10.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy)
        self.frame_17.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_17.setFrameShape(QFrame.NoFrame)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pilih_speedometer = QComboBox(self.frame_17)
        self.pilih_speedometer.addItem("")
        self.pilih_speedometer.addItem("")
        self.pilih_speedometer.addItem("")
        self.pilih_speedometer.addItem("")
        self.pilih_speedometer.setObjectName(u"pilih_speedometer")
        sizePolicy.setHeightForWidth(self.pilih_speedometer.sizePolicy().hasHeightForWidth())
        self.pilih_speedometer.setSizePolicy(sizePolicy)
        self.pilih_speedometer.setFont(font)
        self.pilih_speedometer.setStyleSheet(u"QComboBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang */\n"
"    border: 2px solid white; /* Border putih */\n"
"    border-radius: 5px; /* Sudut membulat */\n"
"    padding: 5px; /* Padding internal */\n"
"    font-size: 16px; /* Ukuran font */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(0, 102, 255); /* Warna saat hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0); /* Warna teks dalam dropdown */\n"
"    background-color: rgb(255, 255, 255); /* Warna latar dropdown */\n"
"    selection-background-color: rgb(0, 102, 255); /* Warna pilihan yang disorot */\n"
"    selection-color: rgb(255, 255, 255); /* Warna teks pilihan yang disorot */\n"
"    border: 1px solid rgb(200, 200, 200); /* Border dropdown */\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pilih_speedometer)

        self.pilih_warna = QComboBox(self.frame_17)
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.addItem("")
        self.pilih_warna.setObjectName(u"pilih_warna")
        sizePolicy.setHeightForWidth(self.pilih_warna.sizePolicy().hasHeightForWidth())
        self.pilih_warna.setSizePolicy(sizePolicy)
        self.pilih_warna.setFont(font)
        self.pilih_warna.setStyleSheet(u"QComboBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang */\n"
"    border: 2px solid white; /* Border putih */\n"
"    border-radius: 5px; /* Sudut membulat */\n"
"    padding: 5px; /* Padding internal */\n"
"    font-size: 16px; /* Ukuran font */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(0, 102, 255); /* Warna saat hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0); /* Warna teks dalam dropdown */\n"
"    background-color: rgb(255, 255, 255); /* Warna latar dropdown */\n"
"    selection-background-color: rgb(0, 102, 255); /* Warna pilihan yang disorot */\n"
"    selection-color: rgb(255, 255, 255); /* Warna teks pilihan yang disorot */\n"
"    border: 1px solid rgb(200, 200, 200); /* Border dropdown */\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.pilih_warna)

        self.print_dynotest = QComboBox(self.frame_17)
        self.print_dynotest.addItem("")
        self.print_dynotest.addItem("")
        self.print_dynotest.addItem("")
        self.print_dynotest.addItem("")
        self.print_dynotest.addItem("")
        self.print_dynotest.setObjectName(u"print_dynotest")
        sizePolicy.setHeightForWidth(self.print_dynotest.sizePolicy().hasHeightForWidth())
        self.print_dynotest.setSizePolicy(sizePolicy)
        self.print_dynotest.setFont(font)
        self.print_dynotest.setLayoutDirection(Qt.LeftToRight)
        self.print_dynotest.setStyleSheet(u"QComboBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang */\n"
"    border: 2px solid white; /* Border putih */\n"
"    border-radius: 5px; /* Sudut membulat */\n"
"    padding: 5px; /* Padding internal */\n"
"    font-size: 16px; /* Ukuran font */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(0, 102, 255); /* Warna saat hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0); /* Warna teks dalam dropdown */\n"
"    background-color: rgb(255, 255, 255); /* Warna latar dropdown */\n"
"    selection-background-color: rgb(0, 102, 255); /* Warna pilihan yang disorot */\n"
"    selection-color: rgb(255, 255, 255); /* Warna teks pilihan yang disorot */\n"
"    border: 1px solid rgb(200, 200, 200); /* Border dropdown */\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.print_dynotest)


        self.verticalLayout_10.addWidget(self.frame_17)


        self.horizontalLayout_7.addWidget(self.frame_13)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.dashboard_page)
        self.preview_page = QWidget()
        self.preview_page.setObjectName(u"preview_page")
        sizePolicy.setHeightForWidth(self.preview_page.sizePolicy().hasHeightForWidth())
        self.preview_page.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.preview_page)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.preview_page)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.button_pdf_preview = QPushButton(self.frame_4)
        self.button_pdf_preview.setObjectName(u"button_pdf_preview")
        sizePolicy.setHeightForWidth(self.button_pdf_preview.sizePolicy().hasHeightForWidth())
        self.button_pdf_preview.setSizePolicy(sizePolicy)
        self.button_pdf_preview.setMaximumSize(QSize(16777215, 50))
        self.button_pdf_preview.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_5.addWidget(self.button_pdf_preview)

        self.button_power_preview = QPushButton(self.frame_4)
        self.button_power_preview.setObjectName(u"button_power_preview")
        sizePolicy.setHeightForWidth(self.button_power_preview.sizePolicy().hasHeightForWidth())
        self.button_power_preview.setSizePolicy(sizePolicy)
        self.button_power_preview.setMaximumSize(QSize(16777215, 50))
        self.button_power_preview.setFont(font1)
        self.button_power_preview.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_5.addWidget(self.button_power_preview)

        self.button_torsi_preview = QPushButton(self.frame_4)
        self.button_torsi_preview.setObjectName(u"button_torsi_preview")
        sizePolicy.setHeightForWidth(self.button_torsi_preview.sizePolicy().hasHeightForWidth())
        self.button_torsi_preview.setSizePolicy(sizePolicy)
        self.button_torsi_preview.setMaximumSize(QSize(16777215, 51))
        self.button_torsi_preview.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_5.addWidget(self.button_torsi_preview)

        self.button_hp_preview = QPushButton(self.frame_4)
        self.button_hp_preview.setObjectName(u"button_hp_preview")
        sizePolicy.setHeightForWidth(self.button_hp_preview.sizePolicy().hasHeightForWidth())
        self.button_hp_preview.setSizePolicy(sizePolicy)
        self.button_hp_preview.setMaximumSize(QSize(16777215, 50))
        self.button_hp_preview.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 18px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_5.addWidget(self.button_hp_preview)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.preview_page)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 85, 0);")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_8)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_4 = QWidget(self.frame_8)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)

        self.verticalLayout_18.addWidget(self.widget_4)


        self.verticalLayout_26.addLayout(self.verticalLayout_18)


        self.horizontalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 170, 255);")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_9)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.widget_6 = QWidget(self.frame_9)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)

        self.verticalLayout_19.addWidget(self.widget_6)


        self.verticalLayout_27.addLayout(self.verticalLayout_19)


        self.horizontalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.preview_page)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_10)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.widget_9 = QWidget(self.frame_10)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy)

        self.verticalLayout_20.addWidget(self.widget_9)


        self.verticalLayout_28.addLayout(self.verticalLayout_20)


        self.horizontalLayout_4.addWidget(self.frame_10)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.preview_page)
        self.file_page = QWidget()
        self.file_page.setObjectName(u"file_page")
        sizePolicy.setHeightForWidth(self.file_page.sizePolicy().hasHeightForWidth())
        self.file_page.setSizePolicy(sizePolicy)
        self.file_page.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.horizontalLayout_13 = QHBoxLayout(self.file_page)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.file_page)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setMaximumSize(QSize(600, 16777215))
        self.frame_20.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setLineWidth(0)
        self.verticalLayout_11 = QVBoxLayout(self.frame_20)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.tableView = QTableView(self.frame_20)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMaximumSize(QSize(16777215, 16777215))
        self.tableView.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.tableView)


        self.horizontalLayout_13.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.file_page)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setStyleSheet(u"background-color: rgb(0, 255, 127);")
        self.frame_19.setFrameShape(QFrame.NoFrame)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_19)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_19)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.frame_21.setLineWidth(0)
        self.verticalLayout_12 = QVBoxLayout(self.frame_21)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_21)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setMaximumSize(QSize(16777215, 40))
        self.frame_23.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_23.setFrameShape(QFrame.NoFrame)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.print_database = QComboBox(self.frame_23)
        self.print_database.addItem("")
        self.print_database.addItem("")
        self.print_database.addItem("")
        self.print_database.addItem("")
        self.print_database.setObjectName(u"print_database")
        sizePolicy.setHeightForWidth(self.print_database.sizePolicy().hasHeightForWidth())
        self.print_database.setSizePolicy(sizePolicy)
        self.print_database.setStyleSheet(u"QComboBox {\n"
"    color: rgb(255, 255, 255); /* Warna teks */\n"
"    background-color: rgb(0, 0, 255); /* Warna latar belakang */\n"
"    border: 2px solid white; /* Border putih */\n"
"    border-radius: 5px; /* Sudut membulat */\n"
"    padding: 5px; /* Padding internal */\n"
"    font-size: 16px; /* Ukuran font */\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgb(0, 102, 255); /* Warna saat hover */\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(0, 0, 0); /* Warna teks dalam dropdown */\n"
"    background-color: rgb(255, 255, 255); /* Warna latar dropdown */\n"
"    selection-background-color: rgb(0, 102, 255); /* Warna pilihan yang disorot */\n"
"    selection-color: rgb(255, 255, 255); /* Warna teks pilihan yang disorot */\n"
"    border: 1px solid rgb(200, 200, 200); /* Border dropdown */\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"")

        self.horizontalLayout_10.addWidget(self.print_database)

        self.button_kw = QPushButton(self.frame_23)
        self.button_kw.setObjectName(u"button_kw")
        sizePolicy.setHeightForWidth(self.button_kw.sizePolicy().hasHeightForWidth())
        self.button_kw.setSizePolicy(sizePolicy)
        self.button_kw.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_10.addWidget(self.button_kw)

        self.button_hp = QPushButton(self.frame_23)
        self.button_hp.setObjectName(u"button_hp")
        sizePolicy.setHeightForWidth(self.button_hp.sizePolicy().hasHeightForWidth())
        self.button_hp.setSizePolicy(sizePolicy)
        self.button_hp.setStyleSheet(u"QPushButton {\n"
"                color: rgb(255, 255, 255);\n"
"                background-color: rgb(0, 0, 255);\n"
"                border: 2px solid rgb(255, 255, 255);\n"
"                border-radius: 10px;\n"
"                padding: 8px 14px;\n"
"                font-size: 16px;\n"
"                font-weight: bold;\n"
"            }\n"
"            QPushButton:hover {\n"
"	background-color: rgb(0, 255, 0);\n"
"            }\n"
"")

        self.horizontalLayout_10.addWidget(self.button_hp)


        self.verticalLayout_12.addWidget(self.frame_23)

        self.frame_26 = QFrame(self.frame_21)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy)
        self.frame_26.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_26.setFrameShape(QFrame.NoFrame)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.frame_26.setLineWidth(0)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_3 = QWidget(self.frame_26)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 85, 127);")

        self.verticalLayout_13.addWidget(self.widget_3)


        self.horizontalLayout_16.addLayout(self.verticalLayout_13)


        self.verticalLayout_12.addWidget(self.frame_26)


        self.verticalLayout_17.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_22.setFrameShape(QFrame.NoFrame)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_22)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy)
        self.frame_25.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.frame_25.setFrameShape(QFrame.NoFrame)
        self.frame_25.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frame_25)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_5 = QWidget(self.frame_25)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.widget_5.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.verticalLayout_16.addWidget(self.widget_5)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addWidget(self.frame_25)


        self.verticalLayout_17.addWidget(self.frame_22)


        self.horizontalLayout_13.addWidget(self.frame_19)

        self.stackedWidget.addWidget(self.file_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_item)

        self.right_side_menu = QFrame(self.main_body)
        self.right_side_menu.setObjectName(u"right_side_menu")
        sizePolicy.setHeightForWidth(self.right_side_menu.sizePolicy().hasHeightForWidth())
        self.right_side_menu.setSizePolicy(sizePolicy)
        self.right_side_menu.setMaximumSize(QSize(10, 16777215))
        self.right_side_menu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.right_side_menu.setFrameShape(QFrame.NoFrame)
        self.right_side_menu.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.right_side_menu)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        sizePolicy.setHeightForWidth(self.main_footer.sizePolicy().hasHeightForWidth())
        self.main_footer.setSizePolicy(sizePolicy)
        self.main_footer.setMaximumSize(QSize(16777215, 10))
        self.main_footer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.main_footer.setFrameShape(QFrame.NoFrame)
        self.main_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_footer)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1080, 26))
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setMaximumSize(QSize(16777215, 16777215))
        self.menuDashboard = QMenu(self.menubar)
        self.menuDashboard.setObjectName(u"menuDashboard")
        sizePolicy.setHeightForWidth(self.menuDashboard.sizePolicy().hasHeightForWidth())
        self.menuDashboard.setSizePolicy(sizePolicy)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        sizePolicy.setHeightForWidth(self.menuFile.sizePolicy().hasHeightForWidth())
        self.menuFile.setSizePolicy(sizePolicy)
        self.menuPreview = QMenu(self.menubar)
        self.menuPreview.setObjectName(u"menuPreview")
        sizePolicy.setHeightForWidth(self.menuPreview.sizePolicy().hasHeightForWidth())
        self.menuPreview.setSizePolicy(sizePolicy)
        self.menuCalibration_Torsi = QMenu(self.menubar)
        self.menuCalibration_Torsi.setObjectName(u"menuCalibration_Torsi")
        sizePolicy.setHeightForWidth(self.menuCalibration_Torsi.sizePolicy().hasHeightForWidth())
        self.menuCalibration_Torsi.setSizePolicy(sizePolicy)
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        sizePolicy.setHeightForWidth(self.menuAbout.sizePolicy().hasHeightForWidth())
        self.menuAbout.setSizePolicy(sizePolicy)
        self.menuCalibration_RPM = QMenu(self.menubar)
        self.menuCalibration_RPM.setObjectName(u"menuCalibration_RPM")
        sizePolicy.setHeightForWidth(self.menuCalibration_RPM.sizePolicy().hasHeightForWidth())
        self.menuCalibration_RPM.setSizePolicy(sizePolicy)
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuDashboard.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPreview.menuAction())
        self.menubar.addAction(self.menuCalibration_Torsi.menuAction())
        self.menubar.addAction(self.menuCalibration_RPM.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuDashboard.addAction(self.actionopen_dashboard)
        self.menuFile.addAction(self.actionopen_file)
        self.menuPreview.addAction(self.actionopen_preview)
        self.menuCalibration_Torsi.addAction(self.actionopen_calibration_torsi)
        self.menuAbout.addAction(self.actionopen_about)
        self.menuCalibration_RPM.addAction(self.actionopen_calibration_rpm)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionopen_file.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionopen_preview.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionopen_dashboard.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionclose.setText(QCoreApplication.translate("MainWindow", u"close", None))
        self.actionopen_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionopen_calibration_torsi.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionClose_2.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionClose_3.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.actionopen_about.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionopen_calibration_rpm.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.box_port.setItemText(0, QCoreApplication.translate("MainWindow", u"Pilih Port", None))

        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port : 00", None))
        self.label_baudrate.setText(QCoreApplication.translate("MainWindow", u"Baudrate : 0000", None))
        self.button_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.button_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.button_reset_database.setText(QCoreApplication.translate("MainWindow", u"Reset Database", None))
        self.label_cal_rpm.setText(QCoreApplication.translate("MainWindow", u"Cal RPM : 0", None))
        self.check_box_calibration.setText(QCoreApplication.translate("MainWindow", u"Enable Cal", None))
        self.label_cal_torque.setText(QCoreApplication.translate("MainWindow", u"Cal Torque : 0", None))
        self.button_resume.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.button_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.check_box_cut_off.setText(QCoreApplication.translate("MainWindow", u"Disable Cut Off", None))
        self.pilih_speedometer.setItemText(0, QCoreApplication.translate("MainWindow", u"Pilih Speedometer", None))
        self.pilih_speedometer.setItemText(1, QCoreApplication.translate("MainWindow", u"RPM", None))
        self.pilih_speedometer.setItemText(2, QCoreApplication.translate("MainWindow", u"Power (W)", None))
        self.pilih_speedometer.setItemText(3, QCoreApplication.translate("MainWindow", u"Torsi (Nm)", None))

        self.pilih_warna.setItemText(0, QCoreApplication.translate("MainWindow", u"Pilih Warna", None))
        self.pilih_warna.setItemText(1, QCoreApplication.translate("MainWindow", u"Biru", None))
        self.pilih_warna.setItemText(2, QCoreApplication.translate("MainWindow", u"Merah", None))
        self.pilih_warna.setItemText(3, QCoreApplication.translate("MainWindow", u"Hijau", None))
        self.pilih_warna.setItemText(4, QCoreApplication.translate("MainWindow", u"Kuning", None))
        self.pilih_warna.setItemText(5, QCoreApplication.translate("MainWindow", u"Ungu", None))
        self.pilih_warna.setItemText(6, QCoreApplication.translate("MainWindow", u"Ocean", None))
        self.pilih_warna.setItemText(7, QCoreApplication.translate("MainWindow", u"Sunset", None))
        self.pilih_warna.setItemText(8, QCoreApplication.translate("MainWindow", u"Midnight", None))
        self.pilih_warna.setItemText(9, QCoreApplication.translate("MainWindow", u"Neon", None))
        self.pilih_warna.setItemText(10, QCoreApplication.translate("MainWindow", u"Sakura", None))
        self.pilih_warna.setItemText(11, QCoreApplication.translate("MainWindow", u"Shonen", None))
        self.pilih_warna.setItemText(12, QCoreApplication.translate("MainWindow", u"Akatsuki", None))
        self.pilih_warna.setItemText(13, QCoreApplication.translate("MainWindow", u"Idol", None))

        self.print_dynotest.setItemText(0, QCoreApplication.translate("MainWindow", u"Print Dynotest", None))
        self.print_dynotest.setItemText(1, QCoreApplication.translate("MainWindow", u"Export to XLSX", None))
        self.print_dynotest.setItemText(2, QCoreApplication.translate("MainWindow", u"Export to CSV", None))
        self.print_dynotest.setItemText(3, QCoreApplication.translate("MainWindow", u"Export to PNG", None))
        self.print_dynotest.setItemText(4, QCoreApplication.translate("MainWindow", u"Export to PDF", None))

        self.button_pdf_preview.setText(QCoreApplication.translate("MainWindow", u"Print PDF", None))
        self.button_power_preview.setText(QCoreApplication.translate("MainWindow", u"Print Graphic RPM ~ kW", None))
        self.button_torsi_preview.setText(QCoreApplication.translate("MainWindow", u"Print Graphic RPM ~ Torque", None))
        self.button_hp_preview.setText(QCoreApplication.translate("MainWindow", u"Print Graphic RPM ~ HP", None))
        self.print_database.setItemText(0, QCoreApplication.translate("MainWindow", u"Print Database", None))
        self.print_database.setItemText(1, QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.print_database.setItemText(2, QCoreApplication.translate("MainWindow", u"Export to XLSX", None))
        self.print_database.setItemText(3, QCoreApplication.translate("MainWindow", u"Export to CSV", None))

        self.button_kw.setText(QCoreApplication.translate("MainWindow", u"Print Graphic RPM ~ kW", None))
        self.button_hp.setText(QCoreApplication.translate("MainWindow", u"Print Graphic RPM ~ HP", None))
        self.menuDashboard.setTitle(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuPreview.setTitle(QCoreApplication.translate("MainWindow", u"Preview", None))
        self.menuCalibration_Torsi.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Torsi", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuCalibration_RPM.setTitle(QCoreApplication.translate("MainWindow", u"Calibration RPM", None))
    # retranslateUi

