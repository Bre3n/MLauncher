import configparser
import os
import webbrowser
import threading
import subprocess

import brain
from main import *  # IMPORTING THE MAIN.PY FILE

user = os.getlogin()
sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
sciezkaver = f"{sciezka}/bin"
config = configparser.ConfigParser()
config.read(f"{sciezkaver}/config.ini")
deleteBufor = False

GLOBAL_STATE = 0  # NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
GLOBAL_TITLE_BAR = (
    True  # NECESSERY FOR CHECKING WEATHER THE WINDWO IS FULL SCREEN OR NOT
)
init = False  # NECRESSERY FOR INITITTION OF THE WINDOW.

# tab_Buttons = ['bn_home', 'bn_bug', 'bn_android', 'bn_cloud'] #BUTTONS IN MAIN TAB
# android_buttons = ['bn_android_contact', 'bn_android_game', 'bn_android_clean', 'bn_android_world'] #BUTTONS IN ANDROID STACKPAGE

# THIS CLASS HOUSES ALL FUNCTION NECESSERY FOR OUR PROGRAMME TO RUN.a
class UIFunction(MainWindow):

    # ----> INITIAL FUNCTION TO LOAD THE FRONT STACK WIDGET AND TAB BUTTON I.E. HOME PAGE
    # INITIALISING THE WELCOME PAGE TO: HOME PAGE IN THE STACKEDWIDGET, SETTING THE BOTTOM LABEL AS THE PAGE NAME, SETTING THE BUTTON STYLE.
    def initStackTab(self):
        global init
        if init == False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True

    ################################################################################################

    # ------> SETING THE APPLICATION NAME IN OUR CUSTOME MADE TAB, WHERE LABEL NAMED: lab_appname()
    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)

    ################################################################################################zxc

    ################################################################################################

    # ----> RETURN STATUS MAX OR RESTROE
    # NECESSERY OFR THE MAXIMISE FUNCTION TRO WORK.
    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # -----> DEFAULT ACTION FUNCTIONa
    def constantFunction(self):
        # -----> DOUBLE CLICK RESULT IN MAXIMISE OF WINDOW
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                pass

        # ----> REMOVE NORMAL TITLE BAR
        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick

        # SINCE THERE IS NO WINDOWS TOPBAR, THE CLOSE MIN, MAX BUTTON ARE ABSENT AND SO THERE IS A NEED FOR THE ALTERNATIVE BUTTONS IN OUR
        # DIALOG BOX, WHICH IS CARRIED OUT BY THE BELOW CODE
        # -----> MINIMIZE BUTTON FUNCTION
        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        # -----> CLOSE APPLICATION FUNCTION BUTTON
        self.ui.bn_close.clicked.connect(lambda: self.closeprogram())

    ################################################################################################################

    # ----> BUTTON IN TAB PRESSED EXECUTES THE CORRESPONDING PAGE IN STACKEDWIDGET PAGES
    def buttonPressed(self, buttonName):
        # ------> THIS LINE CLEARS THE BG OF PREVIOUS TABS I.E. FROM THE LITER COLOR TO THE SAME BG COLOR I.E. TO CHANGE THE HIGHLIGHT.
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName == "bn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet(
                "background:rgb(91,90,90)"
            )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == "bn_bug":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
            self.ui.lab_tab.setText("Game")
            self.ui.frame_bug.setStyleSheet(
                "background:rgb(91,90,90)"
            )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST

        elif buttonName == "bn_android":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
            self.ui.lab_tab.setText("Settings")
            self.ui.frame_android.setStyleSheet(
                "background:rgb(91,90,90)"
            )  # SETS THE BACKGROUND OF THE CLICKED BUTTON TO LITER COLOR THAN THE REST
            UIFunction.androidStackPages(self, "page_contact")

        elif buttonName == "bn_github":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
            self.ui.lab_tab.setText("Github")
            UIFunction.androidStackPages(self, "page_world")

        elif buttonName == "bn_error":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
            self.ui.lab_tab.setText("Error Page")

        # ADD ANOTHER ELIF STATEMENT HERE FOR EXECTUITING A NEW MENU BUTTON STACK PAGE.

    ########################################################################################################################

    # ----> STACKWIDGET EACH PAGE FUNCTION PAGE FUNCTIONS
    # CODE TO PERFOMR THE TASK IN THE STACKED WIDGET PAGE
    # WHAT EVER WIDGET IS IN THE STACKED PAGES ITS ACTION IS EVALUATED HERE AND THEN THE REST FUNCTION IS PASSED.
    def stackPage(self):

        ######### PAGE_HOME ############# BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_HOME

        self.ui.bug_confirm.clicked.connect(lambda: APFunction.bug_confirm(self))

        ######### PAGE_BUG ############## BELOW DISPLAYS THE FUNCTION OF WIDGET, LABEL, PROGRESS BAR, E.T.C IN STACKEDWIDGET page_bug

        self.ui.bug_button.clicked.connect(lambda: APFunction.bug_button(self))
        self.ui.bug_button2.clicked.connect(lambda: APFunction.bug_button2(self))
        self.ui.bug_button3.clicked.connect(lambda: APFunction.bug_button3(self))

        #########PAGE ANDROID WIDGET AND ITS STACKANDROID WIDGET PAGES
        self.ui.bn_android_contact.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_contact")
        )
        self.ui.bn_android_game.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_game")
        )
        self.ui.bn_android_clean.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_clean")
        )
        self.ui.bn_android_world.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_world")
        )

        ######ANDROID > PAGE CONTACT >>>>>>>>>>>>>>>>>>>>
        self.ui.bn_android_contact_delete.clicked.connect(
            lambda: APFunction.deleteContact(self)
        )
        self.ui.line_checkbox_arg.clicked.connect(lambda: APFunction.checkBox_arg(self))
        self.ui.line_checkbox_rpc.clicked.connect(lambda: APFunction.checkBox_rpc(self))
        self.ui.line_checkbox_snapshots.clicked.connect(
            lambda: APFunction.checkBox_snapshots(self)
        )
        self.ui.bn_android_contact_edit.clicked.connect(
            lambda: APFunction.editable(self)
        )
        # asd
        self.ui.bn_android_contact_save.clicked.connect(
            lambda: APFunction.saveContact(self)
        )

        self.ui.bn_shortcut.clicked.connect(lambda: brain.createshortcut())

        #######ANDROID > PAGE GAMEPAD >>>>>>>>>>>>>>>>>>>
        self.ui.textEdit_gamepad.setVerticalScrollBar(
            self.ui.vsb_gamepad
        )  # SETTING THE TEXT FILED AREA A SCROLL BAR
        self.ui.textEdit_gamepad.setText("Type Here Something, or paste something here")

        ######ANDROID > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        # NOTHING HER
        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)

        ##########PAGE: INFORMATION #############

        self.ui.pushButton_github.clicked.connect(
            lambda: APFunction.pushButton_github(self)
        )

        self.ui.pushButton_magic.clicked.connect(
            lambda: APFunction.pushButton_magic(self)
        )

    ################################################################################################################################

    # -----> FUNCTION TO SHOW CORRESPONDING STACK PAGE WHEN THE ANDROID BUTTONS ARE PRESSED: CONTACT, GAME, CLOUD, WORLD
    # SINCE THE ANDROID PAGE AHS A SUB STACKED WIDGET WIT FOUR MORE BUTTONS, ALL THIS 4 PAGES CONTENT: BUTTONS, TEXT, LABEL E.T.C ARE INITIALIED OVER HERE.
    def androidStackPages(self, page):
        # ------> THIS LINE CLEARS THE BG COLOR OF PREVIOUS TABS
        for each in self.ui.frame_android_menu.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if page == "page_contact":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_contact)
            self.ui.lab_tab.setText("Settings > Profile")
            self.ui.frame_android_contact.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_game":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_game)
            self.ui.lab_tab.setText("Settings > GamePad")
            self.ui.frame_android_game.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
            self.ui.lab_tab.setText("Settings > Clean")
            self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_world":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_world)
            self.ui.lab_tab.setText("Settings > Information")
            self.ui.frame_android_world.setStyleSheet("background:rgb(91,90,90)")

        # ADD A ADDITIONAL ELIF STATEMNT WITH THE SIMILAR CODE UP ABOVE FOR YOUR NEW SUBMENU BUTTON IN THE ANDROID STACK PAGE.

    ##############################################################################################################


# ------> CLASS WHERE ALL THE ACTION OF TH SOFTWARE IS PERFORMED:
# THIS CLASS IS WHERE THE APPLICATION OF THE UI OR THE BRAINOF THE SOFTWARE GOES
# UNTILL NOW WE SEPCIFIED THE BUTTON CLICKS, SLIDERS, E.T.C WIDGET, WHOSE APPLICATION IS EXPLORED HERE. THOSE FUNCTION WHEN DONE IS
# REDIRECTED TO THIS AREA FOR THE PROCESSING AND THEN THE RESULT ARE EXPOTED.
# REMEMBER THE SOFTWARE UI HAS A FUNCTION WHOSE CODE SHOULD BE HERE
class APFunction:
    # -----> ADDING NUMBER TO ILLUSTRATE THE CAPABILITY OF THE PROGRESS BAR WHEN THE 'START' BUTTON IS PRESSED
    ###########################

    # -----> FUNCTION IN ACCOUNT OF CONTACT PAGE IN ANDROID MENU
    def editable(self):
        self.ui.line_android_name.setEnabled(True)
        self.ui.line_android_adress.setEnabled(True)
        self.ui.line_checkbox_arg.setEnabled(True)
        self.ui.line_checkbox_rpc.setEnabled(True)
        self.ui.line_checkbox_snapshots.setEnabled(True)

        self.ui.bn_android_contact_save.setEnabled(True)
        self.ui.bn_android_contact_edit.setEnabled(False)
        self.ui.bn_android_contact_delete.setEnabled(False)
        self.ui.bn_home.setEnabled(False)
        self.ui.bn_bug.setEnabled(False)
        self.ui.bn_android.setEnabled(False)
        self.ui.bn_android_contact.setEnabled(False)
        self.ui.bn_android_game.setEnabled(False)
        self.ui.bn_android_clean.setEnabled(False)
        self.ui.bn_android_world.setEnabled(False)

    def saveContact(self):
        self.ui.lab_user.setText(self.ui.line_android_name.text())
        self.ui.lab_home_username.setText(self.ui.line_android_name.text())
        self.ui.line_android_name.setEnabled(False)
        self.ui.line_android_adress.setEnabled(False)
        self.ui.line_checkbox_arg.setEnabled(False)
        self.ui.line_checkbox_rpc.setEnabled(False)
        self.ui.line_checkbox_snapshots.setEnabled(False)

        self.ui.bn_android_contact_save.setEnabled(False)
        self.ui.bn_android_contact_edit.setEnabled(True)
        self.ui.bn_android_contact_delete.setEnabled(True)
        self.ui.bn_home.setEnabled(True)
        self.ui.bn_bug.setEnabled(True)
        self.ui.bn_android.setEnabled(True)
        self.ui.bn_android_contact.setEnabled(True)
        self.ui.bn_android_game.setEnabled(True)
        self.ui.bn_android_clean.setEnabled(True)
        self.ui.bn_android_world.setEnabled(True)

        # * USERNAME
        username = self.ui.line_android_name.text()
        config["PROFILE"]["username"] = username
        brain.setCurrentDiscordRpc("Home Page", f"Playing as {username}")

        # * Alocated Ram

        self.ui.line_android_adress.setText(
            (self.ui.line_android_adress.text()).upper()
        )
        bufor = self.ui.line_android_adress.text()
        if bufor[-1] != "G" and bufor[-1] != "M":
            self.errorexec(
                "'Max Ram' must have a unit. One of this two: 'G', 'M'. Settings will not be applied and saved!!!",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            self.ui.line_android_adress.setText(config.get("SETTINGS", "allocatedram"))
        else:
            if bufor[-1] == "G":
                bufor = str(int(bufor.replace("G", "").replace("g", "")) * 1024) + "M"
                self.ui.line_android_adress.setText(bufor)
            var, buf, size = brain.check_ram(bufor)
            if var == True:
                config["SETTINGS"]["AllocatedRam"] = bufor
            else:
                self.ui.line_android_adress.setText(
                    config.get("SETTINGS", "allocatedram")
                )
                self.errorexec(
                    f"Cannot asing more ram than {buf}MB (80% of amount of available RAM ({size}) )",
                    "icons/1x/errorAsset 55.png",
                    "Ok",
                )

        # * Special Arguments
        if self.ui.line_checkbox_arg.isChecked() == True:
            config["SETTINGS"]["specialarg"] = "True"
        else:
            config["SETTINGS"]["specialarg"] = "False"

        # * DiscordActivity
        if self.ui.line_checkbox_rpc.isChecked() == True:
            config["SETTINGS"]["discordactivity"] = "True"
        else:
            config["SETTINGS"]["discordactivity"] = "False"

        # * Show snapshots
        if self.ui.line_checkbox_snapshots.isChecked() == True:
            config["SETTINGS"]["snapshots"] = "True"
        else:
            config["SETTINGS"]["snapshots"] = "False"

        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)
            
        threading.Thread(target=lambda: brain.GetReleases(self)).start()

    def deleteContact(self):
        global deleteBufor
        if deleteBufor == True:
            brain.configfile("default&a")
            brain.updateLines(self)
            deleteBufor = False
            self.errorexec(
                "Restored default settings.",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
        else:
            self.errorexec(
                "Saved settings will be deleted, If you want it, click one more time on delete button",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            deleteBufor = True

    def checkBox_arg(self):
        if self.ui.line_checkbox_arg.isChecked() == False:
            self.ui.line_checkbox_arg.setText("Unchecked")

        else:
            self.ui.line_checkbox_arg.setText("Checked")
            self.errorexec(
                "Recommended if you have alocated more than 2GB RAM",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )

    def checkBox_rpc(self):
        if self.ui.line_checkbox_rpc.isChecked() == False:
            self.ui.line_checkbox_rpc.setText("Unchecked")
        else:
            self.ui.line_checkbox_rpc.setText("Checked")

    def checkBox_snapshots(self):
        if self.ui.line_checkbox_snapshots.isChecked() == False:
            self.ui.line_checkbox_snapshots.setText("Unchecked")
        else:
            self.ui.line_checkbox_snapshots.setText("Checked")

    def pushButton_github(self):
        webbrowser.open("https://github.com/Bre3n/MLauncher")

    def pushButton_magic(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def bug_button(self):
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config["PROFILE"]["gameversion"] = "Vanilla"
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)
        self.ui.label_12.setText("Vanilla Versions")
        threading.Thread(target=lambda: brain.GetReleases(self)).start()

    def bug_button2(self):
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config["PROFILE"]["gameversion"] = "Forge"
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)
        self.ui.label_12.setText("Forge Versions")
        threading.Thread(target=lambda: brain.ForgeReleases(self)).start()

    def bug_button3(self):
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config["PROFILE"]["gameversion"] = "Server"
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)
        self.ui.label_12.setText("Server Versions")
        threading.Thread(target=lambda: brain.serverVersions(self)).start()

    def bug_confirm(self):
        bufor = self.ui.comboBox.currentText()
        self.ui.label_13.setText(f"Current Version: {bufor}")
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config["PROFILE"]["version"] = bufor
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)


###############################################################################################################################################################
