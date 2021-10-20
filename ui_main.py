# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 550)
        MainWindow.setMinimumSize(QSize(800, 550))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"color:rgb(255,255,255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_top)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top_east = QFrame(self.frame_top)
        self.frame_top_east.setObjectName(u"frame_top_east")
        self.frame_top_east.setMaximumSize(QSize(16777215, 55))
        self.frame_top_east.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_top_east.setFrameShape(QFrame.NoFrame)
        self.frame_top_east.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_east)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_appname = QFrame(self.frame_top_east)
        self.frame_appname.setObjectName(u"frame_appname")
        self.frame_appname.setFrameShape(QFrame.NoFrame)
        self.frame_appname.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_appname)
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.label_9 = QLabel(self.frame_appname)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(25, 25))
        self.label_9.setMaximumSize(QSize(25, 25))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(24)
        self.label_9.setFont(font1)
        self.label_9.setPixmap(QPixmap(u"icons/1x/dragAsset 52.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_9)

        self.lab_appname = QLabel(self.frame_appname)
        self.lab_appname.setObjectName(u"lab_appname")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(24)
        self.lab_appname.setFont(font2)
        self.lab_appname.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_10.addWidget(self.lab_appname)


        self.horizontalLayout_4.addWidget(self.frame_appname)

        self.frame_user = QFrame(self.frame_top_east)
        self.frame_user.setObjectName(u"frame_user")
        self.frame_user.setFrameShape(QFrame.NoFrame)
        self.frame_user.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_user)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_8)

        self.lab_user = QLabel(self.frame_user)
        self.lab_user.setObjectName(u"lab_user")
        self.lab_user.setFont(font2)
        self.lab_user.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_user.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.lab_user)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setFrameShape(QFrame.NoFrame)
        self.frame_person.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_person)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.bn_profile = QPushButton(self.frame_person)
        self.bn_profile.setObjectName(u"bn_profile")
        self.bn_profile.setMinimumSize(QSize(55, 55))
        self.bn_profile.setMaximumSize(QSize(55, 55))
        self.bn_profile.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"icons/1x/peple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_profile.setIcon(icon)
        self.bn_profile.setIconSize(QSize(55, 55))

        self.horizontalLayout_8.addWidget(self.bn_profile)


        self.horizontalLayout_4.addWidget(self.frame_person)

        self.frame_min = QFrame(self.frame_top_east)
        self.frame_min.setObjectName(u"frame_min")
        self.frame_min.setMinimumSize(QSize(55, 55))
        self.frame_min.setMaximumSize(QSize(55, 55))
        self.frame_min.setFrameShape(QFrame.NoFrame)
        self.frame_min.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_min)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.bn_min = QPushButton(self.frame_min)
        self.bn_min.setObjectName(u"bn_min")
        self.bn_min.setMaximumSize(QSize(55, 55))
        self.bn_min.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/1x/hideAsset 53.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_min.setIcon(icon1)
        self.bn_min.setIconSize(QSize(22, 22))
        self.bn_min.setFlat(True)

        self.horizontalLayout_7.addWidget(self.bn_min)


        self.horizontalLayout_4.addWidget(self.frame_min)

        self.frame_close = QFrame(self.frame_top_east)
        self.frame_close.setObjectName(u"frame_close")
        self.frame_close.setMinimumSize(QSize(55, 55))
        self.frame_close.setMaximumSize(QSize(55, 55))
        self.frame_close.setFrameShape(QFrame.NoFrame)
        self.frame_close.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_close)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.bn_close = QPushButton(self.frame_close)
        self.bn_close.setObjectName(u"bn_close")
        self.bn_close.setMaximumSize(QSize(55, 55))
        self.bn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/1x/closeAsset 43.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_close.setIcon(icon2)
        self.bn_close.setIconSize(QSize(22, 22))
        self.bn_close.setFlat(True)

        self.horizontalLayout_5.addWidget(self.bn_close)


        self.horizontalLayout_4.addWidget(self.frame_close)


        self.horizontalLayout.addWidget(self.frame_top_east)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_bottom = QFrame(self.centralwidget)
        self.frame_bottom.setObjectName(u"frame_bottom")
        self.frame_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_bottom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_bottom_west = QFrame(self.frame_bottom)
        self.frame_bottom_west.setObjectName(u"frame_bottom_west")
        self.frame_bottom_west.setMinimumSize(QSize(80, 0))
        self.frame_bottom_west.setMaximumSize(QSize(80, 16777215))
        self.frame_bottom_west.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_bottom_west.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_west.setFrameShadow(QFrame.Plain)
        self.verticalLayout_3 = QVBoxLayout(self.frame_bottom_west)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_home = QFrame(self.frame_bottom_west)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(80, 55))
        self.frame_home.setMaximumSize(QSize(160, 55))
        self.frame_home.setFrameShape(QFrame.NoFrame)
        self.frame_home.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_home)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.bn_home = QPushButton(self.frame_home)
        self.bn_home.setObjectName(u"bn_home")
        self.bn_home.setMinimumSize(QSize(80, 55))
        self.bn_home.setMaximumSize(QSize(160, 55))
        self.bn_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(130,40,200);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(130,90,200);\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u"icons/1x/homeAsset 46.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_home.setIcon(icon3)
        self.bn_home.setIconSize(QSize(22, 22))
        self.bn_home.setFlat(True)

        self.horizontalLayout_15.addWidget(self.bn_home)


        self.verticalLayout_3.addWidget(self.frame_home)

        self.frame_bug = QFrame(self.frame_bottom_west)
        self.frame_bug.setObjectName(u"frame_bug")
        self.frame_bug.setMinimumSize(QSize(80, 55))
        self.frame_bug.setMaximumSize(QSize(160, 55))
        self.frame_bug.setFrameShape(QFrame.NoFrame)
        self.frame_bug.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_bug)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.bn_bug = QPushButton(self.frame_bug)
        self.bn_bug.setObjectName(u"bn_bug")
        self.bn_bug.setMinimumSize(QSize(80, 55))
        self.bn_bug.setMaximumSize(QSize(160, 55))
        self.bn_bug.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"icons/1x/gameAsset 61.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_bug.setIcon(icon4)
        self.bn_bug.setIconSize(QSize(22, 22))
        self.bn_bug.setFlat(True)

        self.horizontalLayout_16.addWidget(self.bn_bug)


        self.verticalLayout_3.addWidget(self.frame_bug)

        self.frame_cloud = QFrame(self.frame_bottom_west)
        self.frame_cloud.setObjectName(u"frame_cloud")
        self.frame_cloud.setMinimumSize(QSize(80, 55))
        self.frame_cloud.setMaximumSize(QSize(160, 55))
        self.frame_cloud.setFrameShape(QFrame.NoFrame)
        self.frame_cloud.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cloud)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_android = QFrame(self.frame_cloud)
        self.frame_android.setObjectName(u"frame_android")
        self.frame_android.setMinimumSize(QSize(80, 55))
        self.frame_android.setMaximumSize(QSize(160, 55))
        self.frame_android.setFrameShape(QFrame.NoFrame)
        self.frame_android.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_android)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_android)
        self.bn_android.setObjectName(u"bn_android")
        self.bn_android.setMinimumSize(QSize(80, 55))
        self.bn_android.setMaximumSize(QSize(160, 55))
        self.bn_android.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(170,120,35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(191,150,80);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/settAsset 50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android.setIcon(icon5)
        self.bn_android.setIconSize(QSize(22, 22))
        self.bn_android.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_android)


        self.horizontalLayout_17.addWidget(self.frame_android)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_8 = QFrame(self.frame_bottom_west)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.frame_8)

        self.bn_github = QPushButton(self.frame_bottom_west)
        self.bn_github.setObjectName(u"bn_github")
        self.bn_github.setMinimumSize(QSize(80, 55))
        self.bn_github.setMaximumSize(QSize(80, 55))
        self.bn_github.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(100,110,120);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(140,140,140);\n"
"}\n"
"")
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_github.setIcon(icon6)
        self.bn_github.setIconSize(QSize(45, 45))

        self.verticalLayout_3.addWidget(self.bn_github)


        self.horizontalLayout_2.addWidget(self.frame_bottom_west)

        self.frame_bottom_east = QFrame(self.frame_bottom)
        self.frame_bottom_east.setObjectName(u"frame_bottom_east")
        self.frame_bottom_east.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_east.setFrameShadow(QFrame.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame_bottom_east)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_bottom_east)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 55))
        self.stackedWidget.setStyleSheet(u"")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.page_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_19 = QHBoxLayout(self.page_home)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 5, 0, 5)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setFrameShape(QFrame.NoFrame)
        self.frame_home_main.setFrameShadow(QFrame.Plain)
        self.verticalLayout_5 = QVBoxLayout(self.frame_home_main)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.lab_home_main_hed = QLabel(self.frame_home_main)
        self.lab_home_main_hed.setObjectName(u"lab_home_main_hed")
        self.lab_home_main_hed.setMinimumSize(QSize(0, 55))
        self.lab_home_main_hed.setMaximumSize(QSize(16777215, 100))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semilight")
        font3.setPointSize(60)
        self.lab_home_main_hed.setFont(font3)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)
        self.lab_home_main_hed.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_username = QLabel(self.frame_home_main)
        self.lab_home_username.setObjectName(u"lab_home_username")
        self.lab_home_username.setMaximumSize(QSize(16777215, 80))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(36)
        self.lab_home_username.setFont(font4)
        self.lab_home_username.setStyleSheet(u"color:rgb(255,255,255);")
        self.lab_home_username.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lab_home_username.setWordWrap(True)
        self.lab_home_username.setMargin(5)

        self.verticalLayout_5.addWidget(self.lab_home_username)

        self.bn_play = QPushButton(self.frame_home_main)
        self.bn_play.setObjectName(u"bn_play")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bn_play.sizePolicy().hasHeightForWidth())
        self.bn_play.setSizePolicy(sizePolicy)
        self.bn_play.setMaximumSize(QSize(16777215, 200))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(72)
        self.bn_play.setFont(font5)
        self.bn_play.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(30,100,140);\n"
"border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(70,140,190);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.bn_play)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(220, 16777215))
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame_home_stat)
        self.label_2.setObjectName(u"label_2")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(22)
        self.label_2.setFont(font6)
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label_2)


        self.horizontalLayout_19.addWidget(self.frame_home_stat)

        self.stackedWidget.addWidget(self.page_home)
        self.page_error = QWidget()
        self.page_error.setObjectName(u"page_error")
        self.page_error.setMinimumSize(QSize(220, 0))
        self.page_error.setMaximumSize(QSize(720, 475))
        self.verticalLayout_18 = QVBoxLayout(self.page_error)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_2 = QFrame(self.page_error)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_17 = QVBoxLayout(self.frame_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 60))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(20)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.error_lab = QLabel(self.frame_2)
        self.error_lab.setObjectName(u"error_lab")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(16)
        self.error_lab.setFont(font8)
        self.error_lab.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.error_lab.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.error_lab)


        self.verticalLayout_18.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_error)
        self.page_about_home = QWidget()
        self.page_about_home.setObjectName(u"page_about_home")
        self.page_about_home.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_13 = QVBoxLayout(self.page_about_home)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(5, 5, 5, 5)
        self.lab_about_home = QLabel(self.page_about_home)
        self.lab_about_home.setObjectName(u"lab_about_home")
        self.lab_about_home.setMinimumSize(QSize(0, 55))
        self.lab_about_home.setMaximumSize(QSize(16777215, 55))
        self.lab_about_home.setFont(font1)
        self.lab_about_home.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_13.addWidget(self.lab_about_home)

        self.frame_about_home = QFrame(self.page_about_home)
        self.frame_about_home.setObjectName(u"frame_about_home")
        self.frame_about_home.setFrameShape(QFrame.StyledPanel)
        self.frame_about_home.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_about_home)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(5, 5, 0, 5)
        self.text_about_home = QTextEdit(self.frame_about_home)
        self.text_about_home.setObjectName(u"text_about_home")
        self.text_about_home.setEnabled(True)
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(10)
        self.text_about_home.setFont(font9)
        self.text_about_home.setStyleSheet(u"color:rgb(255,255,255);")
        self.text_about_home.setFrameShape(QFrame.NoFrame)
        self.text_about_home.setFrameShadow(QFrame.Plain)
        self.text_about_home.setReadOnly(True)
        self.text_about_home.setTextInteractionFlags(Qt.TextBrowserInteraction)

        self.horizontalLayout_28.addWidget(self.text_about_home)

        self.vsb_about_home = QScrollBar(self.frame_about_home)
        self.vsb_about_home.setObjectName(u"vsb_about_home")
        self.vsb_about_home.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_about_home.setOrientation(Qt.Vertical)

        self.horizontalLayout_28.addWidget(self.vsb_about_home)


        self.verticalLayout_13.addWidget(self.frame_about_home)

        self.stackedWidget.addWidget(self.page_about_home)
        self.page_about_cloud = QWidget()
        self.page_about_cloud.setObjectName(u"page_about_cloud")
        self.page_about_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_about_cloud)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_10 = QLabel(self.page_about_cloud)
        self.label_10.setObjectName(u"label_10")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(30)
        self.label_10.setFont(font10)
        self.label_10.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_10)

        self.stackedWidget.addWidget(self.page_about_cloud)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_bug)
        self.page_bug = QWidget()
        self.page_bug.setObjectName(u"page_bug")
        self.page_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_7 = QVBoxLayout(self.page_bug)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_14 = QLabel(self.page_bug)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font4)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.label_12 = QLabel(self.page_bug)
        self.label_12.setObjectName(u"label_12")
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(26)
        self.label_12.setFont(font11)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_12)

        self.comboBox = QComboBox(self.page_bug)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(20)
        self.comboBox.setFont(font12)

        self.verticalLayout_19.addWidget(self.comboBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_6)

        self.bug_button = QPushButton(self.page_bug)
        self.bug_button.setObjectName(u"bug_button")
        self.bug_button.setFont(font6)
        self.bug_button.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgb(100,170,0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(120,200,0);\n"
"}\n"
"")
        self.bug_button.setFlat(True)

        self.verticalLayout_19.addWidget(self.bug_button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)

        self.bug_open_folder = QPushButton(self.page_bug)
        self.bug_open_folder.setObjectName(u"bug_open_folder")
        self.bug_open_folder.setFont(font)
        self.bug_open_folder.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(170,120,35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(191,150,80);\n"
"}\n"
"")
        self.bug_open_folder.setFlat(True)

        self.verticalLayout_19.addWidget(self.bug_open_folder)


        self.horizontalLayout_3.addLayout(self.verticalLayout_19)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_bug)
        self.page_cloud = QWidget()
        self.page_cloud.setObjectName(u"page_cloud")
        self.page_cloud.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_8 = QVBoxLayout(self.page_cloud)
        self.verticalLayout_8.setSpacing(5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget.addWidget(self.page_cloud)
        self.page_android = QWidget()
        self.page_android.setObjectName(u"page_android")
        self.page_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_9 = QVBoxLayout(self.page_android)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_android_menu = QFrame(self.page_android)
        self.frame_android_menu.setObjectName(u"frame_android_menu")
        self.frame_android_menu.setMinimumSize(QSize(0, 30))
        self.frame_android_menu.setMaximumSize(QSize(16777215, 30))
        self.frame_android_menu.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_android_menu.setFrameShape(QFrame.NoFrame)
        self.frame_android_menu.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_android_menu)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_android_contact = QFrame(self.frame_android_menu)
        self.frame_android_contact.setObjectName(u"frame_android_contact")
        self.frame_android_contact.setMinimumSize(QSize(80, 30))
        self.frame_android_contact.setMaximumSize(QSize(80, 30))
        self.frame_android_contact.setFrameShape(QFrame.NoFrame)
        self.frame_android_contact.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_android_contact)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.bn_android_contact = QPushButton(self.frame_android_contact)
        self.bn_android_contact.setObjectName(u"bn_android_contact")
        self.bn_android_contact.setMinimumSize(QSize(80, 30))
        self.bn_android_contact.setMaximumSize(QSize(80, 30))
        self.bn_android_contact.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_contact.setIcon(icon5)
        self.bn_android_contact.setIconSize(QSize(13, 16))
        self.bn_android_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_android_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_game = QFrame(self.frame_android_menu)
        self.frame_android_game.setObjectName(u"frame_android_game")
        self.frame_android_game.setMinimumSize(QSize(80, 30))
        self.frame_android_game.setMaximumSize(QSize(80, 30))
        self.frame_android_game.setFrameShape(QFrame.NoFrame)
        self.frame_android_game.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_game)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_android_game = QPushButton(self.frame_android_game)
        self.bn_android_game.setObjectName(u"bn_android_game")
        self.bn_android_game.setMinimumSize(QSize(80, 30))
        self.bn_android_game.setMaximumSize(QSize(80, 30))
        self.bn_android_game.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_game.setIcon(icon4)
        self.bn_android_game.setIconSize(QSize(20, 13))
        self.bn_android_game.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_android_game)


        self.horizontalLayout_20.addWidget(self.frame_android_game)

        self.frame_android_clean = QFrame(self.frame_android_menu)
        self.frame_android_clean.setObjectName(u"frame_android_clean")
        self.frame_android_clean.setMinimumSize(QSize(80, 30))
        self.frame_android_clean.setMaximumSize(QSize(80, 30))
        self.frame_android_clean.setFrameShape(QFrame.NoFrame)
        self.frame_android_clean.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_android_clean)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.bn_android_clean = QPushButton(self.frame_android_clean)
        self.bn_android_clean.setObjectName(u"bn_android_clean")
        self.bn_android_clean.setMinimumSize(QSize(80, 30))
        self.bn_android_clean.setMaximumSize(QSize(80, 30))
        self.bn_android_clean.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/cleanAsset 59.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_clean.setIcon(icon7)
        self.bn_android_clean.setFlat(True)

        self.horizontalLayout_23.addWidget(self.bn_android_clean)


        self.horizontalLayout_20.addWidget(self.frame_android_clean)

        self.frame_android_world = QFrame(self.frame_android_menu)
        self.frame_android_world.setObjectName(u"frame_android_world")
        self.frame_android_world.setMinimumSize(QSize(80, 30))
        self.frame_android_world.setMaximumSize(QSize(80, 30))
        self.frame_android_world.setFrameShape(QFrame.NoFrame)
        self.frame_android_world.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_android_world)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.bn_android_world = QPushButton(self.frame_android_world)
        self.bn_android_world.setObjectName(u"bn_android_world")
        self.bn_android_world.setMinimumSize(QSize(80, 30))
        self.bn_android_world.setMaximumSize(QSize(80, 30))
        self.bn_android_world.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/smile2Asset 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_world.setIcon(icon8)
        self.bn_android_world.setFlat(True)

        self.horizontalLayout_24.addWidget(self.bn_android_world)


        self.horizontalLayout_20.addWidget(self.frame_android_world)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.frame_android_menu)

        self.stackedWidget_android = QStackedWidget(self.page_android)
        self.stackedWidget_android.setObjectName(u"stackedWidget_android")
        self.stackedWidget_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.page_android_contact = QWidget()
        self.page_android_contact.setObjectName(u"page_android_contact")
        self.page_android_contact.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_10 = QVBoxLayout(self.page_android_contact)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.lab_android_contact = QLabel(self.page_android_contact)
        self.lab_android_contact.setObjectName(u"lab_android_contact")
        self.lab_android_contact.setMinimumSize(QSize(0, 55))
        self.lab_android_contact.setMaximumSize(QSize(16777215, 55))
        self.lab_android_contact.setFont(font1)
        self.lab_android_contact.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_10.addWidget(self.lab_android_contact)

        self.frame_android_bottom = QFrame(self.page_android_contact)
        self.frame_android_bottom.setObjectName(u"frame_android_bottom")
        self.frame_android_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_android_bottom.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_android_bottom)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/peopleAsset 62.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 7, 8, 1, 1)

        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(14)
        self.label_5.setFont(font13)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

        self.line_checkbox_rpc = QCheckBox(self.frame_android_field)
        self.line_checkbox_rpc.setObjectName(u"line_checkbox_rpc")
        self.line_checkbox_rpc.setEnabled(False)
        self.line_checkbox_rpc.setFont(font)

        self.gridLayout_4.addWidget(self.line_checkbox_rpc, 5, 3, 1, 1)

        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font13)

        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 1)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font13)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

        self.line_checkbox_arg = QCheckBox(self.frame_android_field)
        self.line_checkbox_arg.setObjectName(u"line_checkbox_arg")
        self.line_checkbox_arg.setEnabled(False)
        self.line_checkbox_arg.setFont(font)
        self.line_checkbox_arg.setStyleSheet(u"color:rgb(255,255,255);")
        self.line_checkbox_arg.setTristate(False)

        self.gridLayout_4.addWidget(self.line_checkbox_arg, 4, 3, 1, 1)

        self.frame_3 = QFrame(self.frame_android_field)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(100, 0, 0, 0)
        self.bn_android_contact_edit = QPushButton(self.frame_3)
        self.bn_android_contact_edit.setObjectName(u"bn_android_contact_edit")
        self.bn_android_contact_edit.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_edit.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_edit.setFont(font)
        self.bn_android_contact_edit.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_edit)

        self.bn_android_contact_delete = QPushButton(self.frame_3)
        self.bn_android_contact_delete.setObjectName(u"bn_android_contact_delete")
        self.bn_android_contact_delete.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_delete.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_delete.setFont(font)
        self.bn_android_contact_delete.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(112,0,0);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(112,0,0);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_delete)

        self.bn_android_contact_save = QPushButton(self.frame_3)
        self.bn_android_contact_save.setObjectName(u"bn_android_contact_save")
        self.bn_android_contact_save.setEnabled(False)
        self.bn_android_contact_save.setMinimumSize(QSize(69, 25))
        self.bn_android_contact_save.setMaximumSize(QSize(69, 25))
        self.bn_android_contact_save.setFont(font)
        self.bn_android_contact_save.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(200,20,20);\n"
"}\n"
"QPushButton:hover {\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border: 2px solid rgb(0,143,150);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QPushButton:disabled {	\n"
"	border-radius: 5px;	\n"
"	border: 2px solid rgb(112,112,112);\n"
"	background-color: rgb(112,112,112);\n"
"}")

        self.horizontalLayout_25.addWidget(self.bn_android_contact_save)


        self.gridLayout_4.addWidget(self.frame_3, 7, 0, 1, 7)

        self.line_android_name = QLineEdit(self.frame_android_field)
        self.line_android_name.setObjectName(u"line_android_name")
        self.line_android_name.setEnabled(False)
        self.line_android_name.setMinimumSize(QSize(300, 25))
        self.line_android_name.setMaximumSize(QSize(400, 25))
        self.line_android_name.setFont(font)
        self.line_android_name.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_name, 1, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 8, 3, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font13)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.line_android_adress = QLineEdit(self.frame_android_field)
        self.line_android_adress.setObjectName(u"line_android_adress")
        self.line_android_adress.setEnabled(False)
        self.line_android_adress.setMinimumSize(QSize(300, 25))
        self.line_android_adress.setMaximumSize(QSize(400, 25))
        self.line_android_adress.setFont(font)
        self.line_android_adress.setStyleSheet(u"QLineEdit {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:4px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.gridLayout_4.addWidget(self.line_android_adress, 3, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 8, 1, 1)

        self.label_4 = QLabel(self.frame_android_field)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font13)

        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 1)

        self.line_checkbox_snapshots = QCheckBox(self.frame_android_field)
        self.line_checkbox_snapshots.setObjectName(u"line_checkbox_snapshots")
        self.line_checkbox_snapshots.setEnabled(False)
        self.line_checkbox_snapshots.setFont(font)

        self.gridLayout_4.addWidget(self.line_checkbox_snapshots, 6, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 1, 2, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_game = QWidget()
        self.page_android_game.setObjectName(u"page_android_game")
        self.page_android_game.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_game)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.lab_gamepad = QLabel(self.page_android_game)
        self.lab_gamepad.setObjectName(u"lab_gamepad")
        self.lab_gamepad.setMinimumSize(QSize(0, 55))
        self.lab_gamepad.setMaximumSize(QSize(16777215, 55))
        self.lab_gamepad.setFont(font1)
        self.lab_gamepad.setStyleSheet(u"color:rgb(255,255,255);")

        self.verticalLayout_11.addWidget(self.lab_gamepad)

        self.frame_textbar = QFrame(self.page_android_game)
        self.frame_textbar.setObjectName(u"frame_textbar")
        self.frame_textbar.setStyleSheet(u"background:rgb(91,90,90);")
        self.frame_textbar.setFrameShape(QFrame.StyledPanel)
        self.frame_textbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_textbar)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(5, 0, 0, 0)
        self.textEdit_gamepad = QTextEdit(self.frame_textbar)
        self.textEdit_gamepad.setObjectName(u"textEdit_gamepad")
        self.textEdit_gamepad.setFont(font)
        self.textEdit_gamepad.setStyleSheet(u"color:rgb(255,255,255);")
        self.textEdit_gamepad.setFrameShape(QFrame.NoFrame)
        self.textEdit_gamepad.setFrameShadow(QFrame.Plain)
        self.textEdit_gamepad.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.textEdit_gamepad.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_26.addWidget(self.textEdit_gamepad)

        self.vsb_gamepad = QScrollBar(self.frame_textbar)
        self.vsb_gamepad.setObjectName(u"vsb_gamepad")
        self.vsb_gamepad.setStyleSheet(u"QScrollBar:vertical {\n"
"	background:rgb(51,51,51);\n"
"    width:20px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background:rgb(0,143,170);\n"
"}\n"
"QScrollBar::add-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}\n"
"QScrollBar::sub-page:vertical {\n"
" 	background:rgb(51,51,51);\n"
"}")
        self.vsb_gamepad.setOrientation(Qt.Vertical)
        self.vsb_gamepad.setInvertedControls(True)

        self.horizontalLayout_26.addWidget(self.vsb_gamepad)


        self.verticalLayout_11.addWidget(self.frame_textbar)

        self.stackedWidget_android.addWidget(self.page_android_game)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName(u"page_android_clean")
        self.page_android_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 0, 5, 1, 1)

        self.groupBox_clean = QGroupBox(self.page_android_clean)
        self.groupBox_clean.setObjectName(u"groupBox_clean")
        self.groupBox_clean.setMinimumSize(QSize(250, 300))
        self.groupBox_clean.setMaximumSize(QSize(250, 300))
        self.groupBox_clean.setSizeIncrement(QSize(0, 0))
        self.groupBox_clean.setFont(font9)
        self.groupBox_clean.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.groupBox_clean.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_clean.setFlat(False)
        self.groupBox_clean.setCheckable(False)
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_clean)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.radioButton = QRadioButton(self.groupBox_clean)
        self.radioButton.setObjectName(u"radioButton")
        font14 = QFont()
        font14.setFamily(u"Segoe UI")
        font14.setPointSize(9)
        self.radioButton.setFont(font14)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton.setAutoRepeat(False)
        self.radioButton.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox_clean)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font14)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_2.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.groupBox_clean)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setFont(font14)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_3.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_clean)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setFont(font14)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
"	background:rgb(91,90,90);\n"
"    color:white;\n"
"}\n"
"QRadioButton::indicator {\n"
"    width:10px;\n"
"    height:10px;\n"
"    border-radius: 7px;\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:rgb(91,90,90);\n"
"    border:2px solid rgb(51,51,51);\n"
"}")
        self.radioButton_4.setAutoExclusive(True)

        self.verticalLayout_12.addWidget(self.radioButton_4)

        self.checkBox = QCheckBox(self.groupBox_clean)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font14)
        self.checkBox.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox)

        self.checkBox_4 = QCheckBox(self.groupBox_clean)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setFont(font14)
        self.checkBox_4.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")
        self.checkBox_4.setTristate(False)

        self.verticalLayout_12.addWidget(self.checkBox_4)

        self.checkBox_2 = QCheckBox(self.groupBox_clean)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font14)
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.groupBox_clean)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setFont(font14)
        self.checkBox_3.setStyleSheet(u"QCheckBox {\n"
"    color:rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked:pressed {\n"
"	border:2px solid rgb(51,51,51);\n"
"   	background:rgb(0,143,170);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color:rgb(0,143,170);\n"
"    border: 2px solid rgb(51,51,51);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:pressed {\n"
"    border:2px solid rgb(51,51,51);\n"
"	background:rgb(91,90,90);\n"
"}\n"
"\n"
"")

        self.verticalLayout_12.addWidget(self.checkBox_3)


        self.gridLayout_5.addWidget(self.groupBox_clean, 0, 0, 1, 1)

        self.lab_clean = QLabel(self.page_android_clean)
        self.lab_clean.setObjectName(u"lab_clean")
        self.lab_clean.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.lab_clean, 0, 1, 2, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 2, 1)

        self.groupBox = QGroupBox(self.page_android_clean)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(250, 300))
        self.groupBox.setMaximumSize(QSize(250, 300))
        self.groupBox.setFont(font14)
        self.groupBox.setStyleSheet(u"QGroupBox{\n"
"	border:1px solid rgb(51,51,51);	\n"
"	border-radius:4px;\n"
"	color:white;\n"
"	background:rgb(91,90,90);\n"
"}\n"
"")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSlider_2 = QSlider(self.groupBox)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    height:5px;\n"
"    background: rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background:rgb(0,143,170);\n"
"    width: 10px;\n"
"margin:-8px 0\n"
"}\n"
"\n"
"QSlider::add-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:horizondal {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.gridLayout_6.addWidget(self.horizontalSlider_2, 0, 0, 1, 1)

        self.verticalSlider = QSlider(self.groupBox)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"QSlider::groove:vertical {\n"
"    background: red;\n"
"    width:5px\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 10px;\n"
"    background:rgb(0,143,170);\n"
"	margin:0 -8px\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background:rgb(51,51,51);\n"
"}")
        self.verticalSlider.setTracking(True)
        self.verticalSlider.setOrientation(Qt.Vertical)
        self.verticalSlider.setInvertedAppearance(False)
        self.verticalSlider.setInvertedControls(False)
        self.verticalSlider.setTickPosition(QSlider.NoTicks)

        self.gridLayout_6.addWidget(self.verticalSlider, 0, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox, 0, 3, 1, 1)

        self.stackedWidget_android.addWidget(self.page_android_clean)
        self.page_android_world = QWidget()
        self.page_android_world.setObjectName(u"page_android_world")
        self.page_android_world.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_27 = QHBoxLayout(self.page_android_world)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.page_android_world)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 50))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(28)
        self.label_11.setFont(font15)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_11)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_3 = QLabel(self.page_android_world)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_3)


        self.horizontalLayout_30.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_version = QLabel(self.page_android_world)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setFont(font4)
        self.label_version.setMargin(50)

        self.verticalLayout_16.addWidget(self.label_version)


        self.horizontalLayout_30.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)

        self.pushButton_magic = QPushButton(self.page_android_world)
        self.pushButton_magic.setObjectName(u"pushButton_magic")
        self.pushButton_magic.setFont(font)
        self.pushButton_magic.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(125,125,125);\n"
"}\n"
"\n"
"")

        self.verticalLayout_14.addWidget(self.pushButton_magic)

        self.pushButton_github = QPushButton(self.page_android_world)
        self.pushButton_github.setObjectName(u"pushButton_github")
        self.pushButton_github.setFont(font)
        self.pushButton_github.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(125,125,125);\n"
"}\n"
"\n"
"")

        self.verticalLayout_14.addWidget(self.pushButton_github)


        self.horizontalLayout_27.addLayout(self.verticalLayout_14)

        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_android)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 20))
        self.frame_low.setMaximumSize(QSize(16777215, 20))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font16)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        self.lab_tab.setEnabled(True)
        font17 = QFont()
        font17.setFamily(u"Segoe UI Light")
        font17.setPointSize(12)
        self.lab_tab.setFont(font17)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(350, 20))
        self.frame_drag.setMaximumSize(QSize(350, 20))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lab_tab2 = QLabel(self.frame_drag)
        self.lab_tab2.setObjectName(u"lab_tab2")
        self.lab_tab2.setFont(font9)

        self.horizontalLayout_13.addWidget(self.lab_tab2)

        self.bn_error = QPushButton(self.frame_drag)
        self.bn_error.setObjectName(u"bn_error")
        self.bn_error.setEnabled(False)
        self.bn_error.setMaximumSize(QSize(25, 20))
        icon9 = QIcon()
        icon9.addFile(u"icons/1x/errorAsset 55.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_error.setIcon(icon9)
        self.bn_error.setIconSize(QSize(25, 20))
        self.bn_error.setFlat(True)

        self.horizontalLayout_13.addWidget(self.bn_error)


        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_android.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_9.setText("")
        self.lab_appname.setText(QCoreApplication.translate("MainWindow", u"MLauncher", None))
        self.lab_user.setText(QCoreApplication.translate("MainWindow", u"Username", None))
#if QT_CONFIG(tooltip)
        self.bn_min.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_min.setText("")
#if QT_CONFIG(tooltip)
        self.bn_close.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_close.setText("")
#if QT_CONFIG(tooltip)
        self.bn_home.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_home.setText("")
#if QT_CONFIG(tooltip)
        self.bn_bug.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_bug.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.lab_home_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
#if QT_CONFIG(tooltip)
        self.bn_play.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"adsdasdasdastfgfdgfgdhkjhjk", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Error Page", None))
        self.error_lab.setText(QCoreApplication.translate("MainWindow", u"Error text", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Home", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Empty", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Game Versions", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Vanilla Versions", None))
        self.bug_button.setText(QCoreApplication.translate("MainWindow", u" Change type", None))
        self.bug_open_folder.setText(QCoreApplication.translate("MainWindow", u"Open Minecraft Versions folder", None))
#if QT_CONFIG(tooltip)
        self.bn_android_contact.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_contact.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_game.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_game.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_clean.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_clean.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_world.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_world.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.lab_person_icon.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Max RAM: ", None))
        self.line_checkbox_rpc.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Discord Activity", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.line_checkbox_arg.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.bn_android_contact_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_android_contact_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.line_android_name.setText(QCoreApplication.translate("MainWindow", u"Steve", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Special arguments", None))
        self.line_android_adress.setText(QCoreApplication.translate("MainWindow", u"2048M", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Show Snapshots", None))
        self.line_checkbox_snapshots.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.lab_gamepad.setText(QCoreApplication.translate("MainWindow", u"GamePad", None))
        self.groupBox_clean.setTitle(QCoreApplication.translate("MainWindow", u"Review", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Clean History", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Clean Password", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Clean Chache", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Clean Bookmarks", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Did you liked the UI", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Did you like the Color Scheme", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Did you like Custome Buttons", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Did you like the Stacked Window", None))
        self.lab_clean.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Sliders", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Information:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_magic.setText(QCoreApplication.translate("MainWindow", u"Magic!", None))
        self.pushButton_github.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
        self.lab_tab2.setText("")
        self.bn_error.setText("")
    # retranslateUi

