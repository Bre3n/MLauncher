import configparser
import ctypes
import os
import sys
import threading

import brain

ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

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


# DIALOGBOX CLASS WHICH MAKE THE DIALOGBOX WHEN CALLED.
# ------> DIALOG BOX CLASS : DIALOGBOX CONTAINING TWO BUTTONS, ONE MAEEAGE BAR, ONE ICON HOLDER, ONE HEADING DEFINING
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

        #############################################################################################                        -------(C1)
        # SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        # DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        # -----> MINIMIZE BUTTON OF DIALOGBOX
        self.d.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.d.bn_close.clicked.connect(lambda: self.close())

        # -----> THIS FUNCTION WILL CHECKT WEATHER THE BUTRTON ON THE DIALOGBOX IS CLICKED, AND IF SO DIRECTS TO THE FUNCTINON : diag_return()
        self.d.bn_east.clicked.connect(lambda: self.close())
        self.d.bn_west.clicked.connect(lambda: self.close())
        ##############################################################################################

        ##################################################################################################                        ------(C2)
        # SINCE THERE I S NO TOP BAR TO MOVE THE DIALOGBOX OVER THE SCREEN WE HAVE TO DEFINE THE MOUSE EVENT THAT IS RESPONSIBLE FOR THE
        # MOVEMENT. THIS IS CARRIED BY THIS FUNCTION
        # ---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER DIALOGBOX TOPBAR
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
    # THE DIALOG BOX IS DESIGNED TO BE CALLED FROM ANY WHERE IN THE UI WITH ABLE TO CHANGE THE STATRE OF THE TEXT SHOWN, BUTTON NAMES E.T.C
    # THIS IS MADE BY CALLING THIS FUNCTION WHICH TAKES: HEADING, MESSAGE, ICON, BUTTON NAME 1, BUTTON NAME 2 AS ARUMENT.
    # EMBED THE GIVEN PROPERT TO THE DIALOGBOX AND FINALLY DISPLAYS IT IN THE WINDOW.
    # -------> SETTING THE DIALOGBOX CONFIGRATION: TEXT IN BUTTON, LABEL, HEADING
    def dialogConstrict(self, heading, message, icon, btn1, btn2):
        self.d.lab_heading.setText(heading)
        self.d.lab_message.setText(message)
        self.d.bn_east.setText(btn2)
        self.d.bn_west.setText(btn1)
        pixmap = QtGui.QPixmap(icon)
        self.d.lab_icon.setPixmap(pixmap)

    ##################################################################################################


# ERRORBOX CREATES A SAMLL WINDOW TO DISPLAY THAT SOMETHING THAT THE USER PERFORMED HAS WENT WRONG.
# THIS CLASS ALSO HAS THE SAME PROPERTY AS THE DIALOGBOX CLASS WITH THE EXCEPTION THAT BOTH HAVE DIFFERENT UI INTERFACE ANS DIFFERENT APPLICATION.
# ------> ERROR BOX GIVING THE ERROR OCCURED IN THE PROCESS: TAKES THE HEADING, ICON AND BUTTON NAME
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


# OUR APPLICATION MAIN WINDOW :
# -----> MAIN APPLICATION CLASS
class MainWindow(QMainWindow):
    valueChanged = Signal(int)

    def __init__(self):
        applicationName = "MLauncher"
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.i = 0
        self.valueChanged.connect(self.changetheme)

        user = os.getlogin()
        sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
        sciezkaver = f"{sciezka}/bin"
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")

        brain.updateLines(self)
        threading.Thread(target=lambda: brain.checkinternet(self)).start()
        self.ui.lab_tab3.setVisible(False)
        with open(f"{sciezkaver}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        bufor = contentv[0]
        bufor = bufor.split("==")
        bufor = bufor[1]
        self.ui.label_version.setText(bufor)

        # ----> SET WINDOW TITLE AND ICON

        self.setWindowTitle(
            applicationName
        )  # SETS THE APPLICATION NAME IN THE WINDOW TOPBAR                        ---------(C4)
        # EVENTHOW IT IS AVSENT THIS IS NECESSERY AS THE OPERATING SYSTEM RECOGNISES THE SOFTWARE SUING THIS NAME
        # SO YOU WILL SEE THE NAME ENTERED HERE IN THE TASKBAR, TITLEBAR, E.T.C
        UIFunction.labelTitle(
            self, applicationName
        )  # PASSING THE CODE TO SET THE TITLE TO THE CUSTOME TOPBAR IN OUR UI
        # THIS UOFunction CLASS IS IN THE FILE: ui_function.py.
        ###############################

        # -----> INITIAL STACKED WIDGET PAGE WIDGET AND TAB
        # THIS MAKE THE INITIAL WINDOW OF OUR APPLICATION, I.E. THE FIRST PAGE OR THE WELCOME PAGE/SCREEN            ---------(C5)
        # IN OUR APPLICATION THIS IS THE MENU BAR, TOODLE SWITCH, MIN, MAX, CLOSE BUTTONS, AND THE HOME PAGE.
        # ALL THIS GET INITIALISED HERE.
        # SINCE ALL THE FUNCTION RELATED STUFF IS DONE IN THE ui_function.py FILE, IT GOES THERE
        # REMEMBER THIS FUNCTION CAN ALSO BE DONE HERE, BUT DUE TO CONVINENCE IT IS SHIFTD TO A NEW FILE.
        UIFunction.initStackTab(self)
        ############################################################

        # ----> CERTAIN TOOLS LIKE DRAG, MAXIMISE, MINIMISE, CLOSE AND HIDING OF THE WINDOWS TOPBAR
        # THIS WINDOW INITIALISES THE BUTTONS NECESSERY FOR THE MAINWINDOW LIKE: CLOSE, MIN, MAX E.T.C.                ---------(C6)
        UIFunction.constantFunction(self)
        #############################################################

        # ----> TOODLE THE MENU HERE
        # THIS CODE DETETS THE BUTTON IN THE RIGHT TOP IS PRESSED OR NOT AND IF PRESSED IT CONNECT  TO A FUNCTION IN THE ui_function.py                 ---------(C7)
        # FILE, WHICH EXPANDS THE MENU BAR TO DOUBLE ITS WIDTH MAKING ROOM FOR THE ABOUT PAGES.
        # THIS EFFECT CALLED AS TOODLE, CAN BE MADE USE IN MANY WAYS. CHECK THE FUNCTION: toodleMenu: IN THE ui_function.py
        # FILE FOR THE CLEAR WORKING
        #############################################################

        # ----> MENU BUTTON PRESSED EVENTS
        # NOW SINCE OUR DEMO APPLICATION HAS ONLY 4 MENU BUTTONS: Home, Bug, Android, Cloud, WHEN USER PRESSES IT THE FOLLOWING CODE             ---------(C8)
        # REDIRECTS IT TO THE ui_function.py FILE buttonPressed() FUNCTION TO MAKE THE NECESSERY RESPONSES TO THE BUTTON PRESSED.
        # IT TAKES SELF AND THE BUTTON NAME AS THE RGUMENT, THIS IS ONLY TO RECOGNISE WHICH BUTTON IS PRESSED BY THE buttonPressed() FUNCTION.
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
        #############################################################

        # -----> STACK PAGE FUNCTION
        # OUR APPLICATION CHANGES THE PAGES BY USING THE STACKED WIDGET, THIS CODE POINTS TO A FUNCTION IN ui_function.py FILE             ---------(C9)
        # WHICH GOES AND SETS THE DEFAULT IN THESE PAGES AND SEARCHES FOR THE RESPONSES MADE BY THE USER IN THE CORRSPONDING PAGES.
        UIFunction.stackPage(self)
        #############################################################

        # ----> EXECUTING THE ERROR AND DIALOG BOX MENU : THIS HELP TO CALL THEM WITH THE FUNCTIONS.
        # THIS CODE INITIALISED THE DIALOGBOX AND THE ERRORBOX, MAKES AN OBJECT OF THE CORRESPONDING CLASS, SO THAT WE CAN CALL THEM         ---------(C10)
        # WHENEVER NECESSERY.
        self.diag = dialogUi()
        self.error = errorUi()
        #############################################################

        #############################################################

        # UNCOMMENT THE RESPECTIVE LINES OF CODE AS REQUIRED:
        # WARNING: MAKE SURE THAT YOU COMMENT OUT CODES THAT IS ENTERED IN THIS FILE AND FILE ui_function.py FOR THE SMAE
        # WIDGET PERFORMING THE SAME FUNCTION.

        # --ADDING A NEW MENU BUTTON------------------:
        # REFER THE DOCUMENTATION: Documentation.pdf FILE

        # --CALLING A DIALOG BOX----------------------:
        # dialogexec("Heading", "Message", "icon", "Button1name", "button2name")

        # --CALLING A ERROR BOX-----------------------:
        # errorexec("Message", "icon", "buttonname")

        # --PAGE HOME---------------------------------:
        # --HEADING----------------------:
        # self.ui.lab_home_main_hed.setText("heading")
        # self.ui.lab_home_stat_hed.setText("Sata heading")

        # --LABEL------------------------:
        # self.ui.lab_home_main_disc.setText("-----------")
        # self.ui.lab_home_stat_disc.setText("--------------")

        # --PAGE BUG----------------------------------:
        # --CHANGING THE HEADING---------:
        # self.ui.lab_bug.setText("your heading")

        # --USING PROGRESS BAR VALUE-----:
        # self.ui.progressBar_bug.setValue(% in int)

        # --USING COMBO BOX--------------:
        # self.ui.comboBox_bug.addItem("item") #TO ADD ITEMS IN THE COMBOBOX LIST
        # self.ui.comboBox_bug.setItemText() #INDEX YOUR ADDED ITEM
        # self.ui.comboBox_bug.currentIndex() #GIVES THE CURRENT INDEX OF THE LIST

        # --USING START BUTTON-----------:
        # self.ui.bn_bug_start.clicked.connect(some function to execute) #THE FUNCTION GET ACTIVATED WHEN YOU CLICK THE BUTTON

        # --PAGE CLOUD--------------------------------:
        # --CHANGE HEADING---------------:
        # self.ui.lab_cloud_main.setText("heading")

        # --CHANGING LABELS--------------:
        # self.ui.label_2.setText("change: Clint ID")
        # self.ui.label_3.setText("change: Server Adress")
        # self.ui.label_4.setText("change: Proxy")

        # --USING LINE FILED-------------:
        # self.ui.line_cloud_id.setText("set the initial text")
        # text_get = self.ui.line_cloud_id.text() #GIVES THE TEXT ENTERED BY THE USER.
        # DO THE SAME CODE OFR THE RES OF THE LINE EDIT : line_cloud_adress and line_cloud_proxy

        # --USING THE PUSH BUTTONS-------:
        # self.ui.bn_cloud_clear.clicked.connect(function to execute)
        # self.ui.bn_cloud_connect.clikced.connect(function to execute)

        # --PAGE ANDROID:CONTACT----------------------:
        # --CHANGING THE HEADING---------:
        # self.ui.lab_android_contact.setText("Heading")

        # --CHANGING LABELS--------------:
        # self.ui.label.setText("-----")
        # perform the same for the label with obeject tname: 'label_5', 'label_6', 'label_7', 'label_8'

        # --USING TEXT FIELD-------------:
        # sefl.ui.line_android_name.setText("---")
        # self.ui.lineandroid_name.text() #TO GET WHAT THE USER HAS ENTERED.
        # PERFORM THE SAME CODE FOR THE: OBJECT NAME: 'line_android_adress', 'line_android_eamil', 'line_android_ph', 'line_android_org'

        # --USING PUSH BUTTONS-----------:
        # self.ui.bn_adroid_contact_edit.clicked.connect("function goes here")
        # self.ui.bn_adroid_contact_share.clicked.connect("function goes here")
        # self.ui.bn_adroid_contact_delete.clicked.connect("function goes here")
        # self.ui.bn_adroid_contact_save.clicked.connect("function goes here")

        # self.ui.bn_android_contact_save.setEnable(True) #TO ENABLE THE BUTTON
        # DO THE SAME FOR THE REST OF THE BUTTON WHEREEVER NECESSERY.

        # --PAGE ANDROID:GAME-------------------------:
        # --CHANGING THE HEADING---------:
        # self.ui.lab_gamepad.setText("-----")

        # --USING TEXT BROWSER-----------:
        # self.ui.textEdit_gamepad.setText("----")

        # FOR REST OF THE WIDGET GOTO THE Documentation.pdf AND CHECK THE LAYOUT FOR MORE DETAILS.

        # ---> MOVING THE WINDOW WHEN LEFT MOUSE PRESSED AND DRAGGED OVER APPNAME LABEL
        # SAME TO SAY AS IN COMMENT (C2)
        self.dragPos = self.pos()

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunction.returStatus() == 1:
                UIFunction.maximize_restore(self)

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

    # -----> FUNCTION WHICH OPENS THE DIALOG AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION dialogexec() WITH ALL THE PARAMETER
    # NOW WHENEVER YOU WANT A DIALOG BOX TO APPEAR IN THE APP LIKE IN PRESS OF CLODE BUTTON, THIS CAN BE DONE BY CALLING THIS FUNCTION.        ----------(C11)
    # IT TAKES DIALOG OBJECT(INITIALISED EARLIER), HEADER NAME OF DIALOG BOX, MESSAGE TO BE DISPLAYED, ICON, BUTTON NAMES.
    # THIS CODE EXECUTES THE DIALOGBOX AND SO WE CAN SEE THE DIALOG BOX IN THE SCREEN.
    # DURING THE APPEARENCE OF THIS WINDOW, YOU CANNOT USE THE MAINWINDOW, YOU SHPULD EITHER PRESS ANY ONE OFT HE PROVIDED BUTTONS
    # OR JUST CLODE THE DIALOG BOX.
    def dialogexec(self, heading, message, icon, btn1, btn2):
        dialogUi.dialogConstrict(self.diag, heading, message, icon, btn1, btn2)
        self.diag.exec_()

    #############################################################

    # -----> FUNCTION WHICH OPENS THE ERROR BOX AND DISPLAYS IT: SO TO CALL DIALOG BOX JUST CALL THE FUNCTION errorexec() WITH ALL THE PARAMETER
    # SAME AS COMMEND (C11), EXCEPT THIS IS FOR THE ERROR BOX.
    def errorexec(self, heading, icon, btnOk):
        errorUi.errorConstrict(self.error, heading, icon, btnOk)
        self.error.exec_()

    @Slot(int)
    def changetheme(self, var):
        if var == 2:
            self.ui.lab_tab2.setText("")
            self.ui.lab_tab3.setVisible(False)
            self.ui.lab_tab2.setStyleSheet("")
            self.ui.lab_tab.setStyleSheet("")
            self.ui.frame_appname.setStyleSheet("")
            self.ui.frame_close.setStyleSheet("")
            self.ui.frame_min.setStyleSheet("")
            self.ui.frame_person.setStyleSheet("")
            self.ui.frame_user.setStyleSheet("")
        else:
            self.ui.lab_tab2.setText(
                "Connection Error (click icon for more information ->)"
            )
            self.ui.lab_tab3.setVisible(True)
            self.ui.lab_tab2.setStyleSheet("background:#ff0033;")
            self.ui.lab_tab.setStyleSheet("background:#ff0033;")
            self.ui.frame_appname.setStyleSheet("background:#ff0033;")
            self.ui.frame_close.setStyleSheet("background:#ff0033;")
            self.ui.frame_min.setStyleSheet("background:#ff0033;")
            self.ui.frame_person.setStyleSheet("background:#ff0033;")
            self.ui.frame_user.setStyleSheet("background:#ff0033;")

    ##############################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

############################################################################################################################################################
