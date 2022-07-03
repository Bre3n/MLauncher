from configparser import ConfigParser
import ctypes
import os
import sys
import threading
from os import close, path
from random import randrange

from pypresence import Presence

import brain

# import forge_mods

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
from PySide2.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QEvent,
    QMetaObject,
    QObject,
    QPoint,
    QPropertyAnimation,
    QRect,
    QSize,
    Qt,
    QTime,
    QUrl,
    Signal,
    Slot,
)
from PySide2.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QIcon,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
)
from PySide2.QtWidgets import *

from ui_dialog import Ui_Dialog
from ui_error import Ui_Error
from ui_function import *
from ui_main import Ui_MainWindow


class dialogUi(QDialog):
    def __init__(self, parent=None):

        super(dialogUi, self).__init__(parent)
        self.d = Ui_Dialog()
        self.d.setupUi(self)
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint
        )  # REMOVING WINDOWS TOP BAR AND MAKING IT FRAMELESS (AS WE HAVE AMDE A CUSTOME FRAME IN THE WINDOW ITSELF)
        self.setAttribute(
            QtCore.Qt.WA_TranslucentBackground
        )  # MAKING THE WINDOW TRANSPARENT SO THAT TO GET A TRUE FLAT UI

        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        self.d.bn_close.clicked.connect(lambda: self.closeprogram(self))

        self.dragPos = self.pos()  # INITIAL POSOTION OF THE DIALOGBOX

        def movedialogWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.d.frame_top.mouseMoveEvent = movedialogWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE DIALOGBOX DURING MOUSE DRAG
        ################

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #################################################################################################

    #################################################################################################                        ------(C3)
    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)

    ##################################################################################################


class errorUi(QDialog):
    def __init__(self, parent=None):

        super(errorUi, self).__init__(parent)
        self.e = Ui_Error()
        self.e.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # -----> CLOSE APPLICATION FUNCTION BUTTON: CORRESPONDING TO THE bn_ok OF THE ERRORBOX
        self.e.bn_ok.clicked.connect(lambda: self.close())

        # SAME AD DESCRIBED IN COMMEND (C2)
        # ---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER ERRORBOX TOPBAR
        self.dragPos = self.pos()  # INITIAL POSOTION OF THE ERRORBOX

        def moveWindow(event):
            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.e.frame_top.mouseMoveEvent = moveWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE ERRORBOX DURING MOUSE DRAG
        ################

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #############################################

    # SAME AS DESCRIBED IN COMMEND (C3)
    # -------> SETTING THE ERRORBOX CONFIGRATION: TEXT IN BUTTON, LABEL, HEADING
    def errorConstrict(self, heading, icon, btnOk):
        self.e.lab_heading.setText(heading)
        self.e.bn_ok.setText(btnOk)
        pixmap2 = QtGui.QPixmap(icon)
        self.e.lab_icon.setPixmap(pixmap2)


class MainWindow(QMainWindow):
    valueChanged = Signal(int)
    closebool = True

    def __init__(self):
        self.diag = dialogUi()
        self.error = errorUi()
        applicationName = "MLauncher"
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        brain.createFiles()

        random = randrange(3)
        if random == 0:
            self.ui.page_home.setStyleSheet("background: url(icons/main_page_1.jpg);")
        elif random == 1:
            self.ui.page_home.setStyleSheet("background: url(icons/main_page_2.jpg);")
        else:
            self.ui.page_home.setStyleSheet("background: url(icons/main_page_3.jpg);")
        
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_forge_mods_download)
        self.ui.bn_mod_set.clicked.connect(lambda: brain.forge_mods.set_mod(self))
        self.ui.bn_mod_del.clicked.connect(lambda: brain.forge_mods.delete_mod(self))

        # self.ui.bn_mod_setmod.clicked.connect(lambda: forge_mods.down_mod(self))

        self.ui.bn_mod_openFolder.clicked.connect(
            lambda: brain.forge_mods.openFolder(self)
        )

        self.ui.webWidget.load(
            QtCore.QUrl("https://mlauncher.readthedocs.io/en/latest/faq/index.html")
        )
        self.ui.webWidget_mods.load(
            QtCore.QUrl("https://www.curseforge.com/minecraft/mc-mods")
        )

        roaming = os.getenv("APPDATA")
        sciezka = f"{roaming}/.mlauncher"
        sciezkaver = f"{sciezka}/bin"
        sciezkains = f"{sciezka}/instances"
        sciezkajvms = f"{sciezka}/jvms"
        config = ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        username = config.get("PROFILE", "username")
        if (
            path.exists(f"{sciezkajvms}/jre1.8.0_281") == False
            or path.exists(f"{sciezkajvms}/jdk-17.0.2") == False
            or os.path.getsize(f"{sciezkajvms}/jvm1_8.zip") < 78355000
            or os.path.getsize(f"{sciezkajvms}/jvm17.zip") < 170000000
            or path.exists(f"{sciezkains}/shared/.minecraft") == False
        ):
            threading.Thread(target=lambda: brain.downloadstuff(self)).start()

        self.i = 0
        self.valueChanged.connect(self.changetheme)
        brain.news(self)
        threading.Thread(target=lambda: brain.GetReleases(self)).start()
        threading.Thread(target=lambda: brain.ForgeReleases(self, 0)).start()

        brain.updateLines(self)
        threading.Thread(target=lambda: brain.checkinternet(self)).start()
        brain.setCurrentDiscordRpc("Home Page", f"Playing as {username}")
        threading.Thread(target=lambda: brain.discordrpc(self)).start()
        self.ui.bn_error.setVisible(False)
        with open(f"{sciezkaver}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        bufor = contentv[0]
        bufor = bufor.split("==")
        bufor = bufor[1]
        self.ui.label_version.setText(bufor)

        # ----> SET WINDOW TITLE AND ICON

        self.setWindowTitle(applicationName)

        UIFunction.labelTitle(self, applicationName)
        ###############################

        UIFunction.initStackTab(self)
        ############################################################

        UIFunction.constantFunction(self)
        #############################################################

        self.ui.bn_home.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_home")
        )
        self.ui.bn_bug.clicked.connect(lambda: UIFunction.buttonPressed(self, "bn_bug"))
        self.ui.bn_android.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_android")
        )
        self.ui.bn_github.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_github")
        )
        self.ui.bn_error.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_error")
        )
        self.ui.bn_play.clicked.connect(lambda: brain.playthread(self))
        self.ui.bn_news_previous.clicked.connect(lambda: brain.newsScroll(self, 0))
        self.ui.bn_news_next.clicked.connect(lambda: brain.newsScroll(self, 1))
        self.ui.bn_news_open.clicked.connect(lambda: brain.newsOpen(self))
        self.ui.bn_instancesettings.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_instancesettings")
        )
        self.ui.bn_mods.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_mods")
        )
        self.ui.bn_mods_nextPage.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_mods_nextPage")
        )
        self.ui.bn_mods_previousPage.clicked.connect(
            lambda: UIFunction.buttonPressed(self, "bn_mods_previousPage")
        )
        self.ui.bn_mods_web_previous.clicked.connect(
            lambda: self.ui.webWidget_mods.page().triggerAction(QWebEnginePage.Back)
        )
        self.ui.bn_mods_web_forward.clicked.connect(
            lambda: self.ui.webWidget_mods.page().triggerAction(QWebEnginePage.Forward)
        )
        self.ui.bn_mods_web_home.clicked.connect(
            lambda: self.ui.webWidget_mods.load(
                QtCore.QUrl("https://www.curseforge.com/minecraft/mc-mods")
            )
        )

        #############################################################

        UIFunction.stackPage(self)
        #############################################################

        self.dragPos = self.pos()

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE: WE CHOOSE THE TOPMOST FRAME WHERE THE APPLICATION NAME IS PRESENT AS THE AREA TO MOVE THE WINDOW.
        self.ui.frame_appname.mouseMoveEvent = moveWindow  # CALLING THE FUNCTION TO CJANGE THE POSITION OF THE WINDOW DURING MOUSE DRAG

    # ----> FUNCTION TO CAPTURE THE INITIAL POSITION OF THE MOUSE: NECESSERY FOR THE moveWindow FUNCTION
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    #############################################################

    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()

    #############################################################

    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()

    @Slot(int)
    def changetheme(self, var):
        if var == 1:
            self.ui.lab_tab2.setText("")
            self.ui.bn_error.setVisible(False)
            self.ui.bn_error.setEnabled(False)
            self.ui.lab_tab2.setStyleSheet("")
            self.ui.lab_tab.setStyleSheet("")
            self.ui.frame_appname.setStyleSheet("")
            self.ui.frame_close.setStyleSheet("")
            self.ui.frame_min.setStyleSheet("")
            self.ui.frame_person.setStyleSheet("")
            self.ui.frame_user.setStyleSheet("")
        elif var == 2:
            self.ui.lab_tab2.setText(
                "Connection Error (click icon for more information ->)"
            )
            self.ui.bn_error.setVisible(True)
            self.ui.bn_error.setEnabled(True)
            self.ui.lab_tab2.setStyleSheet("background:#ff0033;")
            self.ui.lab_tab.setStyleSheet("background:#ff0033;")
            self.ui.frame_appname.setStyleSheet("background:#ff0033;")
            self.ui.frame_close.setStyleSheet("background:#ff0033;")
            self.ui.frame_min.setStyleSheet("background:#ff0033;")
            self.ui.frame_person.setStyleSheet("background:#ff0033;")
            self.ui.frame_user.setStyleSheet("background:#ff0033;")
            self.ui.error_lab.setText(
                "Connection Error\n{google connection timeout 5s}\n\nFirst check your internet connection, if all is alright thats may be problem with google"
            )
        elif var == 10:
            brain.connectRpc()

    def closeprogram(self):
        if self.closebool == True:
            bufor = -5
            threading.Thread(target=lambda: brain.iterablebooldef(bufor)).start()
            self.close()
        else:
            threading.Thread(
                target=lambda: self.errorexec(
                    "Can't close program, please wait up to few minutes. We are still downloading necessary stuff.",
                    "icons/1x/errorAsset 55.png",
                    "Ok",
                )
            ).start()


##############################################################


if __name__ == "__main__":
    os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--enable-logging --log-level=3"
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################################################################################################
