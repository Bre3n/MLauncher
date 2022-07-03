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

from PySide2.QtWebEngineWidgets import QWebEngineView


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
        self.centralwidget.setStyleSheet(u"background:rgb(91,90,90);border-top-left-radius:10px;border-top-right-radius:10px;")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.centralwidget)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMaximumSize(QSize(16777215, 55))
        self.frame_top.setStyleSheet(u"border-top-left-radius:10px;border-top-right-radius:10px;")
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
        self.frame_appname.setStyleSheet(u"border-top-right-radius:0px;")
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
        self.frame_user.setStyleSheet(u"border-top-left-radius:0px;border-top-right-radius:0px;")
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

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)


        self.horizontalLayout_4.addWidget(self.frame_user)

        self.frame_person = QFrame(self.frame_top_east)
        self.frame_person.setObjectName(u"frame_person")
        self.frame_person.setMinimumSize(QSize(55, 55))
        self.frame_person.setMaximumSize(QSize(55, 55))
        self.frame_person.setStyleSheet(u"border-top-left-radius:0px;border-top-right-radius:0px;")
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
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,143,150);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
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
        self.frame_min.setStyleSheet(u"border-top-left-radius:0px;border-top-right-radius:0px;")
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
        self.frame_close.setStyleSheet(u"border-top-left-radius:0px;")
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
        self.frame_bottom.setStyleSheet(u"border-top-left-radius:0px;border-top-right-radius:0px;")
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
        self.frame_home.setFocusPolicy(Qt.WheelFocus)
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
        self.bn_mods = QPushButton(self.frame_android)
        self.bn_mods.setObjectName(u"bn_mods")
        self.bn_mods.setMinimumSize(QSize(80, 55))
        self.bn_mods.setMaximumSize(QSize(160, 55))
        self.bn_mods.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(35,160,170);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(55,190,203);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/1x/cloudAsset 48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_mods.setIcon(icon5)
        self.bn_mods.setIconSize(QSize(24, 24))
        self.bn_mods.setFlat(True)

        self.horizontalLayout_18.addWidget(self.bn_mods)


        self.horizontalLayout_17.addWidget(self.frame_android)


        self.verticalLayout_3.addWidget(self.frame_cloud)

        self.frame_mods = QFrame(self.frame_bottom_west)
        self.frame_mods.setObjectName(u"frame_mods")
        self.frame_mods.setMinimumSize(QSize(80, 55))
        self.frame_mods.setMaximumSize(QSize(160, 55))
        self.frame_mods.setFocusPolicy(Qt.WheelFocus)
        self.frame_mods.setFrameShape(QFrame.NoFrame)
        self.frame_mods.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_mods)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.bn_android = QPushButton(self.frame_mods)
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
        icon6 = QIcon()
        icon6.addFile(u"icons/1x/settAsset 50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android.setIcon(icon6)
        self.bn_android.setIconSize(QSize(24, 24))
        self.bn_android.setFlat(True)

        self.horizontalLayout_39.addWidget(self.bn_android)


        self.verticalLayout_3.addWidget(self.frame_mods)

        self.frame_4 = QFrame(self.frame_bottom_west)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_4)

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
        icon7 = QIcon()
        icon7.addFile(u"icons/1x/github.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_github.setIcon(icon7)
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
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_home_main = QFrame(self.page_home)
        self.frame_home_main.setObjectName(u"frame_home_main")
        self.frame_home_main.setStyleSheet(u"background:rgba(0,0,0,0.0);")
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
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(65)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setKerning(True)
        self.lab_home_main_hed.setFont(font3)
        self.lab_home_main_hed.setStyleSheet(u"QLabel {\n"
"	color:rgb(255,255,255);\n"
"	background:rgba(0,0,0,0);\n"
"}")
        self.lab_home_main_hed.setTextFormat(Qt.RichText)
        self.lab_home_main_hed.setScaledContents(False)
        self.lab_home_main_hed.setAlignment(Qt.AlignCenter)
        self.lab_home_main_hed.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_5.addWidget(self.lab_home_main_hed)

        self.lab_home_username = QLabel(self.frame_home_main)
        self.lab_home_username.setObjectName(u"lab_home_username")
        self.lab_home_username.setMaximumSize(QSize(16777215, 80))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(40)
        font4.setBold(True)
        font4.setWeight(75)
        self.lab_home_username.setFont(font4)
        self.lab_home_username.setStyleSheet(u"color:rgb(255,255,255);\n"
"background:rgba(0,0,0,0);")
        self.lab_home_username.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lab_home_username.setWordWrap(True)
        self.lab_home_username.setMargin(5)
        self.lab_home_username.setTextInteractionFlags(Qt.NoTextInteraction)

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
        font5.setBold(True)
        font5.setWeight(75)
        font5.setStyleStrategy(QFont.PreferAntialias)
        self.bn_play.setFont(font5)
        self.bn_play.setStyleSheet(u"QPushButton {\n"
"font-size:80px;\n"
"background-color: rgba(30,100,140,0.75);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"font-size:90px;\n"
"	background-color: rgba(70,140,190,0.75);\n"
"}\n"
"")

        self.verticalLayout_5.addWidget(self.bn_play)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_13)

        self.label_2 = QLabel(self.frame_home_main)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background:rgba(0,0,0,0.40);\n"
"border-radius: 5px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setMargin(3)

        self.horizontalLayout_31.addWidget(self.label_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 2, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_31)


        self.horizontalLayout_19.addWidget(self.frame_home_main)

        self.vert_divide = QFrame(self.page_home)
        self.vert_divide.setObjectName(u"vert_divide")
        self.vert_divide.setStyleSheet(u"background:rgba(0,0,0,0)")
        self.vert_divide.setFrameShape(QFrame.VLine)
        self.vert_divide.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_19.addWidget(self.vert_divide)

        self.frame_home_stat = QFrame(self.page_home)
        self.frame_home_stat.setObjectName(u"frame_home_stat")
        sizePolicy.setHeightForWidth(self.frame_home_stat.sizePolicy().hasHeightForWidth())
        self.frame_home_stat.setSizePolicy(sizePolicy)
        self.frame_home_stat.setMinimumSize(QSize(220, 0))
        self.frame_home_stat.setMaximumSize(QSize(250, 16777215))
        self.frame_home_stat.setStyleSheet(u"background:rgba(80,80,80,0.7);")
        self.frame_home_stat.setFrameShape(QFrame.NoFrame)
        self.frame_home_stat.setFrameShadow(QFrame.Plain)
        self.verticalLayout_6 = QVBoxLayout(self.frame_home_stat)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer)

        self.news_latest = QLabel(self.frame_home_stat)
        self.news_latest.setObjectName(u"news_latest")
        self.news_latest.setFont(font)
        self.news_latest.setAutoFillBackground(False)
        self.news_latest.setStyleSheet(u"background:rgba(80,80,80,0);")

        self.horizontalLayout_34.addWidget(self.news_latest)

        self.news_index = QLabel(self.frame_home_stat)
        self.news_index.setObjectName(u"news_index")
        self.news_index.setFont(font)
        self.news_index.setStyleSheet(u"background:rgba(80,80,80,0);")

        self.horizontalLayout_34.addWidget(self.news_index)


        self.verticalLayout_6.addLayout(self.horizontalLayout_34)

        self.stackedWidget_2 = QStackedWidget(self.frame_home_stat)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setStyleSheet(u"background:rgba(80,80,80,0.3);\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;")
        self.page_news_1 = QWidget()
        self.page_news_1.setObjectName(u"page_news_1")
        self.verticalLayout_23 = QVBoxLayout(self.page_news_1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_6)

        self.news_1 = QLabel(self.page_news_1)
        self.news_1.setObjectName(u"news_1")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.news_1.setFont(font6)
        self.news_1.setStyleSheet(u"")
        self.news_1.setAlignment(Qt.AlignCenter)
        self.news_1.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.news_1)

        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.verticalLayout_23.addLayout(self.verticalLayout_28)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_10)

        self.news_1_2 = QLabel(self.page_news_1)
        self.news_1_2.setObjectName(u"news_1_2")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(14)
        self.news_1_2.setFont(font7)
        self.news_1_2.setAlignment(Qt.AlignCenter)
        self.news_1_2.setWordWrap(True)

        self.verticalLayout_23.addWidget(self.news_1_2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_23.addItem(self.verticalSpacer_9)

        self.stackedWidget_2.addWidget(self.page_news_1)
        self.page_news_2 = QWidget()
        self.page_news_2.setObjectName(u"page_news_2")
        self.verticalLayout_24 = QVBoxLayout(self.page_news_2)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalSpacer_13 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_13)

        self.news_2 = QLabel(self.page_news_2)
        self.news_2.setObjectName(u"news_2")
        self.news_2.setFont(font6)
        self.news_2.setAlignment(Qt.AlignCenter)
        self.news_2.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.news_2)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")

        self.verticalLayout_24.addLayout(self.verticalLayout_29)

        self.verticalSpacer_12 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_12)

        self.news_2_2 = QLabel(self.page_news_2)
        self.news_2_2.setObjectName(u"news_2_2")
        self.news_2_2.setFont(font7)
        self.news_2_2.setAlignment(Qt.AlignCenter)
        self.news_2_2.setWordWrap(True)

        self.verticalLayout_24.addWidget(self.news_2_2)

        self.verticalSpacer_11 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_11)

        self.stackedWidget_2.addWidget(self.page_news_2)
        self.page_news_3 = QWidget()
        self.page_news_3.setObjectName(u"page_news_3")
        self.verticalLayout_25 = QVBoxLayout(self.page_news_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_16 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_16)

        self.news_3 = QLabel(self.page_news_3)
        self.news_3.setObjectName(u"news_3")
        self.news_3.setFont(font6)
        self.news_3.setAlignment(Qt.AlignCenter)
        self.news_3.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.news_3)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")

        self.verticalLayout_25.addLayout(self.verticalLayout_30)

        self.verticalSpacer_15 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_15)

        self.news_3_2 = QLabel(self.page_news_3)
        self.news_3_2.setObjectName(u"news_3_2")
        self.news_3_2.setFont(font7)
        self.news_3_2.setAlignment(Qt.AlignCenter)
        self.news_3_2.setWordWrap(True)

        self.verticalLayout_25.addWidget(self.news_3_2)

        self.verticalSpacer_14 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_14)

        self.stackedWidget_2.addWidget(self.page_news_3)
        self.page_news_4 = QWidget()
        self.page_news_4.setObjectName(u"page_news_4")
        self.verticalLayout_26 = QVBoxLayout(self.page_news_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_19 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_19)

        self.news_4 = QLabel(self.page_news_4)
        self.news_4.setObjectName(u"news_4")
        self.news_4.setFont(font6)
        self.news_4.setAlignment(Qt.AlignCenter)
        self.news_4.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.news_4)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")

        self.verticalLayout_26.addLayout(self.verticalLayout_31)

        self.verticalSpacer_18 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_18)

        self.news_4_2 = QLabel(self.page_news_4)
        self.news_4_2.setObjectName(u"news_4_2")
        self.news_4_2.setFont(font7)
        self.news_4_2.setAlignment(Qt.AlignCenter)
        self.news_4_2.setWordWrap(True)

        self.verticalLayout_26.addWidget(self.news_4_2)

        self.verticalSpacer_17 = QSpacerItem(20, 113, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_17)

        self.stackedWidget_2.addWidget(self.page_news_4)
        self.page_news_5 = QWidget()
        self.page_news_5.setObjectName(u"page_news_5")
        self.verticalLayout_27 = QVBoxLayout(self.page_news_5)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalSpacer_22 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_22)

        self.news_5 = QLabel(self.page_news_5)
        self.news_5.setObjectName(u"news_5")
        self.news_5.setFont(font6)
        self.news_5.setAlignment(Qt.AlignCenter)
        self.news_5.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.news_5)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")

        self.verticalLayout_27.addLayout(self.verticalLayout_32)

        self.verticalSpacer_21 = QSpacerItem(20, 96, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_21)

        self.news_5_2 = QLabel(self.page_news_5)
        self.news_5_2.setObjectName(u"news_5_2")
        self.news_5_2.setFont(font7)
        self.news_5_2.setAlignment(Qt.AlignCenter)
        self.news_5_2.setWordWrap(True)

        self.verticalLayout_27.addWidget(self.news_5_2)

        self.verticalSpacer_20 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_20)

        self.stackedWidget_2.addWidget(self.page_news_5)

        self.verticalLayout_6.addWidget(self.stackedWidget_2)

        self.bn_news_open = QPushButton(self.frame_home_stat)
        self.bn_news_open.setObjectName(u"bn_news_open")
        self.bn_news_open.setFont(font7)
        self.bn_news_open.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(170,120,35,0.75);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(191,150,80,0.75);\n"
"}\n"
"")

        self.verticalLayout_6.addWidget(self.bn_news_open)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.bn_news_previous = QPushButton(self.frame_home_stat)
        self.bn_news_previous.setObjectName(u"bn_news_previous")
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(22)
        self.bn_news_previous.setFont(font8)
        self.bn_news_previous.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(50,150,50,0.75);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(100,180,100,0.75);\n"
"}\n"
"")

        self.horizontalLayout_33.addWidget(self.bn_news_previous)

        self.bn_news_next = QPushButton(self.frame_home_stat)
        self.bn_news_next.setObjectName(u"bn_news_next")
        self.bn_news_next.setFont(font8)
        self.bn_news_next.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(50,150,50,0.75);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(100,180,100,0.75);\n"
"}\n"
"")

        self.horizontalLayout_33.addWidget(self.bn_news_next)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)


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
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(20)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_7.setFont(font9)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.error_lab = QLabel(self.frame_2)
        self.error_lab.setObjectName(u"error_lab")
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(16)
        self.error_lab.setFont(font10)
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
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(10)
        self.text_about_home.setFont(font11)
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
        self.page_forge_mods = QWidget()
        self.page_forge_mods.setObjectName(u"page_forge_mods")
        self.page_forge_mods.setStyleSheet(u"background:rgb(91,90,90);")
        self.horizontalLayout_29 = QHBoxLayout(self.page_forge_mods)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.stackedWidget_3 = QStackedWidget(self.page_forge_mods)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_forge_mods_download = QWidget()
        self.page_forge_mods_download.setObjectName(u"page_forge_mods_download")
        self.verticalLayout_4 = QVBoxLayout(self.page_forge_mods_download)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_2 = QWidget(self.page_forge_mods_download)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_26 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_3 = QSpacerItem(45, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_3)

        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy2)
        font12 = QFont()
        font12.setFamily(u"Courier New")
        font12.setPointSize(24)
        font12.setBold(False)
        font12.setWeight(50)
        self.label_23.setFont(font12)
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_23)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_10)

        self.bn_mods_nextPage = QPushButton(self.widget_2)
        self.bn_mods_nextPage.setObjectName(u"bn_mods_nextPage")
        sizePolicy2.setHeightForWidth(self.bn_mods_nextPage.sizePolicy().hasHeightForWidth())
        self.bn_mods_nextPage.setSizePolicy(sizePolicy2)
        self.bn_mods_nextPage.setFont(font10)
        self.bn_mods_nextPage.setStyleSheet(u"background:rgb(80,80,80);border-radius:22%;")
        icon8 = QIcon()
        icon8.addFile(u"icons/1x/next-page-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_mods_nextPage.setIcon(icon8)
        self.bn_mods_nextPage.setIconSize(QSize(45, 45))
        self.bn_mods_nextPage.setFlat(True)

        self.horizontalLayout_26.addWidget(self.bn_mods_nextPage)


        self.verticalLayout_4.addWidget(self.widget_2)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget = QWidget(self.page_forge_mods_download)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout_43 = QHBoxLayout(self.widget)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_18 = QLabel(self.widget)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        font13 = QFont()
        font13.setFamily(u"Courier New")
        font13.setPointSize(14)
        self.label_18.setFont(font13)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_18)

        self.label_20 = QLabel(self.widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font13)

        self.horizontalLayout_42.addWidget(self.label_20)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_42)


        self.verticalLayout_33.addWidget(self.widget)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.comboBox_2 = QComboBox(self.page_forge_mods_download)
        self.comboBox_2.setObjectName(u"comboBox_2")
        font14 = QFont()
        font14.setFamily(u"Courier New")
        font14.setPointSize(20)
        self.comboBox_2.setFont(font14)
        self.comboBox_2.setStyleSheet(u"QComboBox {\n"
"padding:2px;\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-rig"
                        "ht-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.comboBox_2)

        self.bn_mod_set = QPushButton(self.page_forge_mods_download)
        self.bn_mod_set.setObjectName(u"bn_mod_set")
        sizePolicy2.setHeightForWidth(self.bn_mod_set.sizePolicy().hasHeightForWidth())
        self.bn_mod_set.setSizePolicy(sizePolicy2)
        self.bn_mod_set.setFont(font14)
        self.bn_mod_set.setStyleSheet(u"QPushButton {\n"
"border-radius:5px;\n"
"padding:5px;\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.horizontalLayout_35.addWidget(self.bn_mod_set)


        self.verticalLayout_33.addLayout(self.horizontalLayout_35)

        self.label_21 = QLabel(self.page_forge_mods_download)
        self.label_21.setObjectName(u"label_21")
        sizePolicy1.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy1)
        font15 = QFont()
        font15.setFamily(u"Courier New")
        font15.setPointSize(12)
        self.label_21.setFont(font15)

        self.verticalLayout_33.addWidget(self.label_21)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.line_mod_name = QLineEdit(self.page_forge_mods_download)
        self.line_mod_name.setObjectName(u"line_mod_name")
        font16 = QFont()
        font16.setFamily(u"Courier New")
        font16.setPointSize(16)
        self.line_mod_name.setFont(font16)
        self.line_mod_name.setStyleSheet(u"QLineEdit {\n"
"padding:2px;\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:5px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_37.addWidget(self.line_mod_name)

        self.line_mod_version = QLineEdit(self.page_forge_mods_download)
        self.line_mod_version.setObjectName(u"line_mod_version")
        self.line_mod_version.setFont(font16)
        self.line_mod_version.setStyleSheet(u"QLineEdit {\n"
"padding:2px;\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(51,51,51);\n"
"	border-radius:4px;\n"
"	background:rgb(51,51,51);\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"	color:rgb(255,255,255);\n"
"	border:2px solid rgb(112,112,112);\n"
"	border-radius:5px;\n"
"	background:rgb(112,112,112);\n"
"}")

        self.horizontalLayout_37.addWidget(self.line_mod_version)

        self.bn_mod_setmod = QPushButton(self.page_forge_mods_download)
        self.bn_mod_setmod.setObjectName(u"bn_mod_setmod")
        sizePolicy2.setHeightForWidth(self.bn_mod_setmod.sizePolicy().hasHeightForWidth())
        self.bn_mod_setmod.setSizePolicy(sizePolicy2)
        self.bn_mod_setmod.setFont(font14)
        self.bn_mod_setmod.setStyleSheet(u"QPushButton {\n"
"border-radius:5px;\n"
"	padding:5px;\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")

        self.horizontalLayout_37.addWidget(self.bn_mod_setmod)


        self.verticalLayout_33.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_36.addItem(self.verticalSpacer_23)


        self.verticalLayout_33.addLayout(self.horizontalLayout_36)

        self.scrollArea = QScrollArea(self.page_forge_mods_download)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 100, 410))
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout_34 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_22 = QLabel(self.scrollAreaWidgetContents)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        font17 = QFont()
        font17.setFamily(u"Courier New")
        self.label_22.setFont(font17)
        self.label_22.setWordWrap(True)

        self.verticalLayout_34.addWidget(self.label_22)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_33.addWidget(self.scrollArea)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.comboBox_3 = QComboBox(self.page_forge_mods_download)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font14)
        self.comboBox_3.setStyleSheet(u"QComboBox {\n"
"padding:2px;\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-rig"
                        "ht-radius: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"")

        self.horizontalLayout_38.addWidget(self.comboBox_3)

        self.bn_mod_del = QPushButton(self.page_forge_mods_download)
        self.bn_mod_del.setObjectName(u"bn_mod_del")
        sizePolicy2.setHeightForWidth(self.bn_mod_del.sizePolicy().hasHeightForWidth())
        self.bn_mod_del.setSizePolicy(sizePolicy2)
        self.bn_mod_del.setFont(font14)
        self.bn_mod_del.setStyleSheet(u"QPushButton {\n"
"padding:5px;\n"
"border-radius:5px;\n"
"	border: none;\n"
"	background-color: rgb(255,50,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214,45,45);\n"
"}\n"
"")

        self.horizontalLayout_38.addWidget(self.bn_mod_del)


        self.verticalLayout_33.addLayout(self.horizontalLayout_38)


        self.verticalLayout_4.addLayout(self.verticalLayout_33)

        self.bn_mod_openFolder = QPushButton(self.page_forge_mods_download)
        self.bn_mod_openFolder.setObjectName(u"bn_mod_openFolder")
        font18 = QFont()
        font18.setFamily(u"Courier New")
        font18.setPointSize(18)
        self.bn_mod_openFolder.setFont(font18)
        self.bn_mod_openFolder.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(170,120,35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(191,150,80);\n"
"}\n"
"")

        self.verticalLayout_4.addWidget(self.bn_mod_openFolder)

        self.stackedWidget_3.addWidget(self.page_forge_mods_download)
        self.page_forge_mods_web = QWidget()
        self.page_forge_mods_web.setObjectName(u"page_forge_mods_web")
        self.verticalLayout_36 = QVBoxLayout(self.page_forge_mods_web)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_3 = QWidget(self.page_forge_mods_web)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.horizontalLayout_40 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.bn_mods_previousPage = QPushButton(self.widget_3)
        self.bn_mods_previousPage.setObjectName(u"bn_mods_previousPage")
        sizePolicy2.setHeightForWidth(self.bn_mods_previousPage.sizePolicy().hasHeightForWidth())
        self.bn_mods_previousPage.setSizePolicy(sizePolicy2)
        self.bn_mods_previousPage.setFont(font10)
        self.bn_mods_previousPage.setStyleSheet(u"background:rgb(80,80,80);border-radius:22%;")
        icon9 = QIcon()
        icon9.addFile(u"icons/1x/previous-page-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_mods_previousPage.setIcon(icon9)
        self.bn_mods_previousPage.setIconSize(QSize(45, 45))
        self.bn_mods_previousPage.setFlat(True)

        self.horizontalLayout_40.addWidget(self.bn_mods_previousPage)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy4)
        self.widget_4.setStyleSheet(u"border:1.5px solid black;border-radius:20%")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.bn_mods_web_previous = QPushButton(self.widget_4)
        self.bn_mods_web_previous.setObjectName(u"bn_mods_web_previous")
        sizePolicy2.setHeightForWidth(self.bn_mods_web_previous.sizePolicy().hasHeightForWidth())
        self.bn_mods_web_previous.setSizePolicy(sizePolicy2)
        self.bn_mods_web_previous.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius:15%;\n"
"	background-color: rgb(80,80,80);\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/1x/whiteBack.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_mods_web_previous.setIcon(icon10)
        self.bn_mods_web_previous.setIconSize(QSize(30, 30))

        self.horizontalLayout_41.addWidget(self.bn_mods_web_previous)

        self.bn_mods_web_forward = QPushButton(self.widget_4)
        self.bn_mods_web_forward.setObjectName(u"bn_mods_web_forward")
        self.bn_mods_web_forward.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius:15%;\n"
"	background-color: rgb(80,80,80);\n"
"}\n"
"")
        icon11 = QIcon()
        icon11.addFile(u"icons/1x/whiteForward.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_mods_web_forward.setIcon(icon11)
        self.bn_mods_web_forward.setIconSize(QSize(30, 30))

        self.horizontalLayout_41.addWidget(self.bn_mods_web_forward)

        self.bn_mods_web_home = QPushButton(self.widget_4)
        self.bn_mods_web_home.setObjectName(u"bn_mods_web_home")
        sizePolicy2.setHeightForWidth(self.bn_mods_web_home.sizePolicy().hasHeightForWidth())
        self.bn_mods_web_home.setSizePolicy(sizePolicy2)
        self.bn_mods_web_home.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius:15%;\n"
"	background-color: rgb(80,80,80);\n"
"}\n"
"")
        self.bn_mods_web_home.setIcon(icon3)
        self.bn_mods_web_home.setIconSize(QSize(30, 30))

        self.horizontalLayout_41.addWidget(self.bn_mods_web_home)


        self.horizontalLayout_40.addWidget(self.widget_4)

        self.horizontalSpacer_11 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_11)

        self.label_24 = QLabel(self.widget_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy2.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy2)
        font19 = QFont()
        font19.setFamily(u"Courier New")
        font19.setPointSize(24)
        font19.setBold(True)
        font19.setWeight(75)
        self.label_24.setFont(font19)
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_24)

        self.horizontalSpacer_7 = QSpacerItem(45, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addWidget(self.widget_3)

        self.webWidget_mods = QWebEngineView(self.page_forge_mods_web)
        self.webWidget_mods.setObjectName(u"webWidget_mods")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.webWidget_mods.sizePolicy().hasHeightForWidth())
        self.webWidget_mods.setSizePolicy(sizePolicy5)

        self.verticalLayout_12.addWidget(self.webWidget_mods)


        self.verticalLayout_36.addLayout(self.verticalLayout_12)

        self.stackedWidget_3.addWidget(self.page_forge_mods_web)

        self.horizontalLayout_29.addWidget(self.stackedWidget_3)

        self.stackedWidget.addWidget(self.page_forge_mods)
        self.page_about_android = QWidget()
        self.page_about_android.setObjectName(u"page_about_android")
        self.page_about_android.setStyleSheet(u"background:rgb(91,90,90);")
        self.stackedWidget.addWidget(self.page_about_android)
        self.page_about_bug = QWidget()
        self.page_about_bug.setObjectName(u"page_about_bug")
        self.page_about_bug.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayoutWidget = QWidget(self.page_about_bug)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 711, 471))
        self.verticalLayout_20 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 50))
        font20 = QFont()
        font20.setFamily(u"Segoe UI")
        font20.setPointSize(26)
        self.label_15.setFont(font20)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_15)

        self.label_16 = QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        font21 = QFont()
        font21.setFamily(u"Segoe UI")
        font21.setPointSize(18)
        self.label_16.setFont(font21)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_16)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_19 = QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName(u"label_19")
        font22 = QFont()
        font22.setFamily(u"Segoe UI")
        font22.setPointSize(20)
        self.label_19.setFont(font22)
        self.label_19.setStyleSheet(u"background:rgb(75,75,75);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_19)

        self.label_17 = QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font22)
        self.label_17.setStyleSheet(u"background:rgb(75,75,75);")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_17)

        self.lb_bug_open = QLabel(self.verticalLayoutWidget)
        self.lb_bug_open.setObjectName(u"lb_bug_open")
        self.lb_bug_open.setFont(font22)
        self.lb_bug_open.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.lb_bug_open)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_7)


        self.horizontalLayout_6.addLayout(self.verticalLayout_22)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.bug_sharedsaves = QPushButton(self.verticalLayoutWidget)
        self.bug_sharedsaves.setObjectName(u"bug_sharedsaves")
        self.bug_sharedsaves.setFont(font22)
        self.bug_sharedsaves.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        self.bug_sharedsaves.setFlat(True)

        self.verticalLayout_21.addWidget(self.bug_sharedsaves)

        self.bug_optifine = QPushButton(self.verticalLayoutWidget)
        self.bug_optifine.setObjectName(u"bug_optifine")
        self.bug_optifine.setFont(font22)
        self.bug_optifine.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        self.bug_optifine.setFlat(True)

        self.verticalLayout_21.addWidget(self.bug_optifine)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_8)


        self.horizontalLayout_6.addLayout(self.verticalLayout_21)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.bug_repair = QPushButton(self.verticalLayoutWidget)
        self.bug_repair.setObjectName(u"bug_repair")
        font23 = QFont()
        font23.setFamily(u"Segoe UI")
        font23.setPointSize(15)
        self.bug_repair.setFont(font23)
        self.bug_repair.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        self.bug_repair.setFlat(True)

        self.verticalLayout_20.addWidget(self.bug_repair)

        self.bug_openfolder = QPushButton(self.verticalLayoutWidget)
        self.bug_openfolder.setObjectName(u"bug_openfolder")
        self.bug_openfolder.setFont(font23)
        self.bug_openfolder.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(50,150,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(100,180,100);\n"
"}\n"
"")
        self.bug_openfolder.setFlat(True)

        self.verticalLayout_20.addWidget(self.bug_openfolder)

        self.bug_bn_delete = QPushButton(self.verticalLayoutWidget)
        self.bug_bn_delete.setObjectName(u"bug_bn_delete")
        self.bug_bn_delete.setFont(font23)
        self.bug_bn_delete.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(255,50,50);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(214,45,45);\n"
"}\n"
"")

        self.verticalLayout_20.addWidget(self.bug_bn_delete)

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
        font24 = QFont()
        font24.setFamily(u"Segoe UI")
        font24.setPointSize(36)
        font24.setBold(True)
        font24.setWeight(75)
        self.label_14.setFont(font24)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_13 = QLabel(self.page_bug)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_13)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_2)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.bug_button = QPushButton(self.page_bug)
        self.bug_button.setObjectName(u"bug_button")
        self.bug_button.setMinimumSize(QSize(230, 40))
        self.bug_button.setFont(font8)
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

        self.horizontalLayout_32.addWidget(self.bug_button)

        self.bug_button2 = QPushButton(self.page_bug)
        self.bug_button2.setObjectName(u"bug_button2")
        self.bug_button2.setMinimumSize(QSize(230, 40))
        font25 = QFont()
        font25.setFamily(u"Courier New")
        font25.setPointSize(24)
        self.bug_button2.setFont(font25)
        self.bug_button2.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgb(100,170,0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(120,200,0);\n"
"}\n"
"")
        self.bug_button2.setFlat(True)

        self.horizontalLayout_32.addWidget(self.bug_button2)

        self.bug_button3 = QPushButton(self.page_bug)
        self.bug_button3.setObjectName(u"bug_button3")
        self.bug_button3.setMinimumSize(QSize(230, 40))
        font26 = QFont()
        font26.setFamily(u"SimSun")
        font26.setPointSize(22)
        self.bug_button3.setFont(font26)
        self.bug_button3.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgb(100,170,0)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(120,200,0);\n"
"}\n"
"")

        self.horizontalLayout_32.addWidget(self.bug_button3)


        self.verticalLayout_19.addLayout(self.horizontalLayout_32)

        self.label_12 = QLabel(self.page_bug)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font20)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_12)

        self.comboBox = QComboBox(self.page_bug)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.comboBox.setFont(font22)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"	border: 2px solid rgb(51,51,51);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	border: 2px solid rgb(0,143,170);\n"
"	border-radius: 5px;	\n"
"	color:rgb(255,255,255);\n"
"	background-color: rgb(0,143,170);\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"	background: rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: darkgray;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 5px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 5px;\n"
""
                        "}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(icons/1x/arrow.png);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    background:rgb(51,51,51);\n"
"}\n"
"")

        self.verticalLayout_19.addWidget(self.comboBox)

        self.bug_confirm = QPushButton(self.page_bug)
        self.bug_confirm.setObjectName(u"bug_confirm")
        self.bug_confirm.setFont(font22)
        self.bug_confirm.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color:rgb(170,0,70)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(200,0,90);\n"
"}\n"
"")
        self.bug_confirm.setFlat(True)

        self.verticalLayout_19.addWidget(self.bug_confirm)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)

        self.bn_instancesettings = QPushButton(self.page_bug)
        self.bn_instancesettings.setObjectName(u"bn_instancesettings")
        self.bn_instancesettings.setFont(font22)
        self.bn_instancesettings.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(0,160,170);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(0,180,200);\n"
"}\n"
"")
        self.bn_instancesettings.setFlat(True)

        self.verticalLayout_19.addWidget(self.bn_instancesettings)


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
        self.bn_android_contact.setIcon(icon6)
        self.bn_android_contact.setIconSize(QSize(13, 16))
        self.bn_android_contact.setFlat(True)

        self.horizontalLayout_21.addWidget(self.bn_android_contact)


        self.horizontalLayout_20.addWidget(self.frame_android_contact)

        self.frame_android_faq = QFrame(self.frame_android_menu)
        self.frame_android_faq.setObjectName(u"frame_android_faq")
        self.frame_android_faq.setMinimumSize(QSize(80, 30))
        self.frame_android_faq.setMaximumSize(QSize(80, 30))
        self.frame_android_faq.setFrameShape(QFrame.NoFrame)
        self.frame_android_faq.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_android_faq)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.bn_android_faq = QPushButton(self.frame_android_faq)
        self.bn_android_faq.setObjectName(u"bn_android_faq")
        self.bn_android_faq.setMinimumSize(QSize(80, 30))
        self.bn_android_faq.setMaximumSize(QSize(80, 30))
        self.bn_android_faq.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(91,90,90);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgba(0,0,0,0);\n"
"}")
        self.bn_android_faq.setIcon(icon4)
        self.bn_android_faq.setIconSize(QSize(20, 13))
        self.bn_android_faq.setFlat(True)

        self.horizontalLayout_22.addWidget(self.bn_android_faq)


        self.horizontalLayout_20.addWidget(self.frame_android_faq)

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
        icon12 = QIcon()
        icon12.addFile(u"icons/1x/cleanAsset 59.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_clean.setIcon(icon12)
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
        icon13 = QIcon()
        icon13.addFile(u"icons/1x/smile2Asset 1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_android_world.setIcon(icon13)
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
        self.frame_android_field = QFrame(self.frame_android_bottom)
        self.frame_android_field.setObjectName(u"frame_android_field")
        self.frame_android_field.setFrameShape(QFrame.NoFrame)
        self.frame_android_field.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame_android_field)
        self.gridLayout_4.setSpacing(5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.label_5 = QLabel(self.frame_android_field)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)
        self.label_5.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_5, 3, 0, 1, 3)

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

        self.label_4 = QLabel(self.frame_android_field)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font7)

        self.gridLayout_4.addWidget(self.label_4, 6, 0, 1, 1)

        self.label_6 = QLabel(self.frame_android_field)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)
        self.label_6.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label_6, 4, 0, 1, 1)

        self.line_checkbox_rpc = QCheckBox(self.frame_android_field)
        self.line_checkbox_rpc.setObjectName(u"line_checkbox_rpc")
        self.line_checkbox_rpc.setEnabled(False)
        self.line_checkbox_rpc.setFont(font)
        self.line_checkbox_rpc.setStyleSheet(u"QCheckBox {\n"
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
"")

        self.gridLayout_4.addWidget(self.line_checkbox_rpc, 5, 3, 1, 1)

        self.line_checkbox_arg = QCheckBox(self.frame_android_field)
        self.line_checkbox_arg.setObjectName(u"line_checkbox_arg")
        self.line_checkbox_arg.setEnabled(False)
        self.line_checkbox_arg.setFont(font)
        self.line_checkbox_arg.setStyleSheet(u"QCheckBox {\n"
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
"")
        self.line_checkbox_arg.setTristate(False)

        self.gridLayout_4.addWidget(self.line_checkbox_arg, 4, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 7, 8, 1, 1)

        self.label_8 = QLabel(self.frame_android_field)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font7)

        self.gridLayout_4.addWidget(self.label_8, 5, 0, 1, 1)

        self.label = QLabel(self.frame_android_field)
        self.label.setObjectName(u"label")
        self.label.setFont(font7)
        self.label.setStyleSheet(u"color:rgb(255,255,255);")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 3)

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

        self.line_checkbox_snapshots = QCheckBox(self.frame_android_field)
        self.line_checkbox_snapshots.setObjectName(u"line_checkbox_snapshots")
        self.line_checkbox_snapshots.setEnabled(False)
        self.line_checkbox_snapshots.setFont(font)
        self.line_checkbox_snapshots.setStyleSheet(u"QCheckBox {\n"
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
"")

        self.gridLayout_4.addWidget(self.line_checkbox_snapshots, 6, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 8, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 4, 8, 1, 1)

        self.bn_shortcut = QPushButton(self.frame_android_field)
        self.bn_shortcut.setObjectName(u"bn_shortcut")
        self.bn_shortcut.setFont(font)
        self.bn_shortcut.setStyleSheet(u"QPushButton {\n"
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
        self.bn_shortcut.setFlat(True)

        self.gridLayout_4.addWidget(self.bn_shortcut, 9, 3, 1, 1)


        self.gridLayout_3.addWidget(self.frame_android_field, 0, 2, 2, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.lab_person_icon = QLabel(self.frame_android_bottom)
        self.lab_person_icon.setObjectName(u"lab_person_icon")
        self.lab_person_icon.setMinimumSize(QSize(200, 160))
        self.lab_person_icon.setMaximumSize(QSize(200, 160))
        self.lab_person_icon.setPixmap(QPixmap(u"icons/1x/peopleAsset 62.png"))

        self.gridLayout_3.addWidget(self.lab_person_icon, 0, 1, 1, 1)


        self.verticalLayout_10.addWidget(self.frame_android_bottom)

        self.stackedWidget_android.addWidget(self.page_android_contact)
        self.page_android_faq = QWidget()
        self.page_android_faq.setObjectName(u"page_android_faq")
        self.page_android_faq.setStyleSheet(u"background:rgb(91,90,90);")
        self.verticalLayout_11 = QVBoxLayout(self.page_android_faq)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.webWidget = QWebEngineView(self.page_android_faq)
        self.webWidget.setObjectName(u"webWidget")

        self.verticalLayout_11.addWidget(self.webWidget)

        self.stackedWidget_android.addWidget(self.page_android_faq)
        self.page_android_clean = QWidget()
        self.page_android_clean.setObjectName(u"page_android_clean")
        self.page_android_clean.setStyleSheet(u"background:rgb(91,90,90);")
        self.gridLayout_5 = QGridLayout(self.page_android_clean)
        self.gridLayout_5.setSpacing(5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
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
        font27 = QFont()
        font27.setFamily(u"Segoe UI")
        font27.setPointSize(28)
        self.label_11.setFont(font27)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_11)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_3 = QLabel(self.page_android_world)
        self.label_3.setObjectName(u"label_3")
        font28 = QFont()
        font28.setFamily(u"Segoe UI")
        font28.setPointSize(36)
        self.label_3.setFont(font28)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_3)


        self.horizontalLayout_30.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_version = QLabel(self.page_android_world)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setFont(font28)
        self.label_version.setMargin(50)

        self.verticalLayout_16.addWidget(self.label_version)


        self.horizontalLayout_30.addLayout(self.verticalLayout_16)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.pushButton_faq = QPushButton(self.page_android_world)
        self.pushButton_faq.setObjectName(u"pushButton_faq")
        self.pushButton_faq.setFont(font10)
        self.pushButton_faq.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(125,125,125);\n"
"}\n"
"\n"
"")

        self.verticalLayout_35.addWidget(self.pushButton_faq)

        self.pushButton_issue = QPushButton(self.page_android_world)
        self.pushButton_issue.setObjectName(u"pushButton_issue")
        self.pushButton_issue.setFont(font10)
        self.pushButton_issue.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(125,125,125);\n"
"}\n"
"\n"
"")

        self.verticalLayout_35.addWidget(self.pushButton_issue)

        self.pushButton_github = QPushButton(self.page_android_world)
        self.pushButton_github.setObjectName(u"pushButton_github")
        self.pushButton_github.setFont(font10)
        self.pushButton_github.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(110,110,110)\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(125,125,125);\n"
"}\n"
"\n"
"")

        self.verticalLayout_35.addWidget(self.pushButton_github)


        self.verticalLayout_14.addLayout(self.verticalLayout_35)


        self.horizontalLayout_27.addLayout(self.verticalLayout_14)

        self.stackedWidget_android.addWidget(self.page_android_world)

        self.verticalLayout_9.addWidget(self.stackedWidget_android)

        self.stackedWidget.addWidget(self.page_android)

        self.horizontalLayout_14.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_low = QFrame(self.frame_bottom_east)
        self.frame_low.setObjectName(u"frame_low")
        self.frame_low.setMinimumSize(QSize(0, 22))
        self.frame_low.setMaximumSize(QSize(16777215, 22))
        self.frame_low.setStyleSheet(u"")
        self.frame_low.setFrameShape(QFrame.NoFrame)
        self.frame_low.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_low)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_tab = QFrame(self.frame_low)
        self.frame_tab.setObjectName(u"frame_tab")
        font29 = QFont()
        font29.setFamily(u"Segoe UI")
        self.frame_tab.setFont(font29)
        self.frame_tab.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_tab.setFrameShape(QFrame.NoFrame)
        self.frame_tab.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_tab)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_2)

        self.lab_tab = QLabel(self.frame_tab)
        self.lab_tab.setObjectName(u"lab_tab")
        self.lab_tab.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.lab_tab.sizePolicy().hasHeightForWidth())
        self.lab_tab.setSizePolicy(sizePolicy1)
        font30 = QFont()
        font30.setFamily(u"Segoe UI Light")
        font30.setPointSize(12)
        self.lab_tab.setFont(font30)
        self.lab_tab.setStyleSheet(u"color:rgb(255,255,255);")

        self.horizontalLayout_12.addWidget(self.lab_tab)


        self.horizontalLayout_11.addWidget(self.frame_tab)

        self.frame_drag = QFrame(self.frame_low)
        self.frame_drag.setObjectName(u"frame_drag")
        self.frame_drag.setMinimumSize(QSize(350, 22))
        self.frame_drag.setMaximumSize(QSize(350, 33))
        self.frame_drag.setStyleSheet(u"background:rgb(51,51,51);")
        self.frame_drag.setFrameShape(QFrame.NoFrame)
        self.frame_drag.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_drag)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lab_tab2 = QLabel(self.frame_drag)
        self.lab_tab2.setObjectName(u"lab_tab2")
        sizePolicy1.setHeightForWidth(self.lab_tab2.sizePolicy().hasHeightForWidth())
        self.lab_tab2.setSizePolicy(sizePolicy1)
        self.lab_tab2.setFont(font11)

        self.horizontalLayout_13.addWidget(self.lab_tab2)

        self.bn_error = QPushButton(self.frame_drag)
        self.bn_error.setObjectName(u"bn_error")
        self.bn_error.setEnabled(False)
        self.bn_error.setMaximumSize(QSize(25, 20))
        icon14 = QIcon()
        icon14.addFile(u"icons/1x/errorAsset 55.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bn_error.setIcon(icon14)
        self.bn_error.setIconSize(QSize(25, 20))
        self.bn_error.setFlat(True)

        self.horizontalLayout_13.addWidget(self.bn_error)


        self.horizontalLayout_11.addWidget(self.frame_drag)


        self.verticalLayout_2.addWidget(self.frame_low)


        self.horizontalLayout_2.addWidget(self.frame_bottom_east)


        self.verticalLayout.addWidget(self.frame_bottom)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.bn_min, self.bn_news_open)
        QWidget.setTabOrder(self.bn_news_open, self.bn_close)
        QWidget.setTabOrder(self.bn_close, self.frame_home)
        QWidget.setTabOrder(self.frame_home, self.bn_home)
        QWidget.setTabOrder(self.bn_home, self.bn_bug)
        QWidget.setTabOrder(self.bn_bug, self.bn_mods)
        QWidget.setTabOrder(self.bn_mods, self.frame_mods)
        QWidget.setTabOrder(self.frame_mods, self.bn_android)
        QWidget.setTabOrder(self.bn_android, self.bn_github)
        QWidget.setTabOrder(self.bn_github, self.bn_play)
        QWidget.setTabOrder(self.bn_play, self.bn_profile)
        QWidget.setTabOrder(self.bn_profile, self.bn_news_previous)
        QWidget.setTabOrder(self.bn_news_previous, self.bn_news_next)
        QWidget.setTabOrder(self.bn_news_next, self.text_about_home)
        QWidget.setTabOrder(self.text_about_home, self.bn_mods_nextPage)
        QWidget.setTabOrder(self.bn_mods_nextPage, self.comboBox_2)
        QWidget.setTabOrder(self.comboBox_2, self.bn_mod_set)
        QWidget.setTabOrder(self.bn_mod_set, self.line_mod_name)
        QWidget.setTabOrder(self.line_mod_name, self.line_mod_version)
        QWidget.setTabOrder(self.line_mod_version, self.bn_mod_setmod)
        QWidget.setTabOrder(self.bn_mod_setmod, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.comboBox_3)
        QWidget.setTabOrder(self.comboBox_3, self.bn_mod_del)
        QWidget.setTabOrder(self.bn_mod_del, self.bn_mod_openFolder)
        QWidget.setTabOrder(self.bn_mod_openFolder, self.bn_mods_previousPage)
        QWidget.setTabOrder(self.bn_mods_previousPage, self.bn_mods_web_previous)
        QWidget.setTabOrder(self.bn_mods_web_previous, self.bn_mods_web_forward)
        QWidget.setTabOrder(self.bn_mods_web_forward, self.bn_mods_web_home)
        QWidget.setTabOrder(self.bn_mods_web_home, self.bug_sharedsaves)
        QWidget.setTabOrder(self.bug_sharedsaves, self.bug_optifine)
        QWidget.setTabOrder(self.bug_optifine, self.bug_repair)
        QWidget.setTabOrder(self.bug_repair, self.bug_openfolder)
        QWidget.setTabOrder(self.bug_openfolder, self.bug_bn_delete)
        QWidget.setTabOrder(self.bug_bn_delete, self.bug_button)
        QWidget.setTabOrder(self.bug_button, self.bug_button2)
        QWidget.setTabOrder(self.bug_button2, self.bug_button3)
        QWidget.setTabOrder(self.bug_button3, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.bug_confirm)
        QWidget.setTabOrder(self.bug_confirm, self.bn_instancesettings)
        QWidget.setTabOrder(self.bn_instancesettings, self.bn_android_contact)
        QWidget.setTabOrder(self.bn_android_contact, self.bn_android_faq)
        QWidget.setTabOrder(self.bn_android_faq, self.bn_android_clean)
        QWidget.setTabOrder(self.bn_android_clean, self.bn_android_world)
        QWidget.setTabOrder(self.bn_android_world, self.line_android_adress)
        QWidget.setTabOrder(self.line_android_adress, self.line_checkbox_rpc)
        QWidget.setTabOrder(self.line_checkbox_rpc, self.line_checkbox_arg)
        QWidget.setTabOrder(self.line_checkbox_arg, self.line_android_name)
        QWidget.setTabOrder(self.line_android_name, self.bn_android_contact_edit)
        QWidget.setTabOrder(self.bn_android_contact_edit, self.bn_android_contact_delete)
        QWidget.setTabOrder(self.bn_android_contact_delete, self.bn_android_contact_save)
        QWidget.setTabOrder(self.bn_android_contact_save, self.line_checkbox_snapshots)
        QWidget.setTabOrder(self.line_checkbox_snapshots, self.bn_shortcut)
        QWidget.setTabOrder(self.bn_shortcut, self.pushButton_faq)
        QWidget.setTabOrder(self.pushButton_faq, self.pushButton_issue)
        QWidget.setTabOrder(self.pushButton_issue, self.pushButton_github)
        QWidget.setTabOrder(self.pushButton_github, self.bn_error)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_android.setCurrentIndex(1)


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
        self.bn_mods.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_mods.setText("")
        self.bn_android.setText("")
        self.lab_home_main_hed.setText(QCoreApplication.translate("MainWindow", u"Welcome", None))
        self.lab_home_username.setText(QCoreApplication.translate("MainWindow", u"Steve", None))
#if QT_CONFIG(tooltip)
        self.bn_play.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.news_latest.setText(QCoreApplication.translate("MainWindow", u"Latest", None))
        self.news_index.setText(QCoreApplication.translate("MainWindow", u"1/5", None))
        self.news_1.setText(QCoreApplication.translate("MainWindow", u"NEWS TITLE", None))
        self.news_1_2.setText(QCoreApplication.translate("MainWindow", u"NEWS DESCRIPTION", None))
        self.news_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_2_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_3_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_4_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.news_5_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bn_news_open.setText(QCoreApplication.translate("MainWindow", u"Open article", None))
        self.bn_news_previous.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.bn_news_next.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Error Page", None))
        self.error_lab.setText(QCoreApplication.translate("MainWindow", u"Error text", None))
        self.lab_about_home.setText(QCoreApplication.translate("MainWindow", u"About: Home", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"FORGE MODS", None))
        self.bn_mods_nextPage.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Forge version: ", None))
        self.label_20.setText("")
        self.bn_mod_set.setText(QCoreApplication.translate("MainWindow", u"Set Version", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"       [MOD NAME]        [MOD VERSION [OPTIONAL]]", None))
        self.line_mod_name.setPlaceholderText("")
        self.line_mod_version.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Without .jar", None))
        self.bn_mod_setmod.setText(QCoreApplication.translate("MainWindow", u"Download Mod", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Downloading mods are in alpha and may totally change. For now there is no official API from CurseForge so all have to be manual. There is many bugs that are resource-intensive and hard to fix. As soon as he shows up an official API, will be implemented to installer.</p></body></html>", None))
        self.bn_mod_del.setText(QCoreApplication.translate("MainWindow", u"Delete Mod", None))
        self.bn_mod_openFolder.setText(QCoreApplication.translate("MainWindow", u"Open mods folder", None))
        self.bn_mods_previousPage.setText("")
        self.bn_mods_web_previous.setText("")
        self.bn_mods_web_forward.setText("")
        self.bn_mods_web_home.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"FORGE MODS", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Instance settings", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"[Instance name]", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"[is shared?]", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"[optifine installed?]", None))
        self.lb_bug_open.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.bug_sharedsaves.setText(QCoreApplication.translate("MainWindow", u"Shared saves", None))
        self.bug_optifine.setText(QCoreApplication.translate("MainWindow", u"Optifine", None))
        self.bug_repair.setText(QCoreApplication.translate("MainWindow", u"Repair instance", None))
        self.bug_openfolder.setText(QCoreApplication.translate("MainWindow", u"Open folder", None))
        self.bug_bn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete Instance", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Game Versions", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Current Version:", None))
        self.bug_button.setText(QCoreApplication.translate("MainWindow", u"Vanilla", None))
        self.bug_button2.setText(QCoreApplication.translate("MainWindow", u"Forge", None))
        self.bug_button3.setText(QCoreApplication.translate("MainWindow", u"Server", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Vanilla Versions", None))
        self.bug_confirm.setText(QCoreApplication.translate("MainWindow", u"Set version", None))
        self.bn_instancesettings.setText(QCoreApplication.translate("MainWindow", u"Instance settings", None))
#if QT_CONFIG(tooltip)
        self.bn_android_contact.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_contact.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_faq.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_faq.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_clean.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_clean.setText("")
#if QT_CONFIG(tooltip)
        self.bn_android_world.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.bn_android_world.setText("")
        self.lab_android_contact.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Max RAM: ", None))
        self.line_android_adress.setText(QCoreApplication.translate("MainWindow", u"2048M", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Show Snapshots", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Special arguments", None))
        self.line_checkbox_rpc.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.line_checkbox_arg.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Discord Activity", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Nickname", None))
        self.line_android_name.setText(QCoreApplication.translate("MainWindow", u"Steve", None))
        self.bn_android_contact_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.bn_android_contact_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.bn_android_contact_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.line_checkbox_snapshots.setText(QCoreApplication.translate("MainWindow", u"Unchecked", None))
        self.bn_shortcut.setText(QCoreApplication.translate("MainWindow", u"Create shortcut on desktop", None))
        self.lab_person_icon.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Information:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Version:", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton_faq.setText(QCoreApplication.translate("MainWindow", u"FAQ", None))
        self.pushButton_issue.setText(QCoreApplication.translate("MainWindow", u"Report an issue", None))
        self.pushButton_github.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.lab_tab.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.frame_drag.setToolTip(QCoreApplication.translate("MainWindow", u"Drag", None))
#endif // QT_CONFIG(tooltip)
        self.lab_tab2.setText("")
#if QT_CONFIG(statustip)
        self.bn_error.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.bn_error.setText("")
    # retranslateUi

