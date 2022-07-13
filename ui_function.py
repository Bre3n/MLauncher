from configparser import ConfigParser
import os
import subprocess
import threading
import webbrowser

import brain
from main import *

roaming = os.getenv("APPDATA")
sciezka = f"{roaming}/.mlauncher"
sciezkaver = f"{sciezka}/bin"
config = ConfigParser()
config.read(f"{sciezkaver}/config.ini")
deleteBufor = False

GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True
init = False


class UIFunction(MainWindow):
    def initStackTab(self):
        global init
        if init == False:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")
            init = True

    def labelTitle(self, appName):
        self.ui.lab_appname.setText(appName)

    def returStatus():
        return GLOBAL_STATE

    def setStatus(status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    def constantFunction(self):
        def maxDoubleClick(stateMouse):
            if stateMouse.type() == QtCore.QEvent.MouseButtonDblClick:
                pass

        if True:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
            self.ui.frame_appname.mouseDoubleClickEvent = maxDoubleClick

        self.ui.bn_min.clicked.connect(lambda: self.showMinimized())

        self.ui.bn_close.clicked.connect(lambda: self.closeprogram())

    def buttonPressed(self, buttonName):
        for each in self.ui.frame_bottom_west.findChildren(QFrame):
            each.setStyleSheet("background:rgb(51,51,51)")

        if buttonName == "bn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.ui.lab_tab.setText("Home")
            self.ui.frame_home.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName == "bn_bug":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_bug)
            self.ui.lab_tab.setText("Game")
            self.ui.frame_bug.setStyleSheet("background:rgb(91,90,90)")

        elif buttonName == "bn_android":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
            self.ui.lab_tab.setText("Settings")
            self.ui.frame_android.setStyleSheet("background:rgb(91,90,90)")
            UIFunction.androidStackPages(self, "page_contact")

        elif buttonName == "bn_github":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
            self.ui.lab_tab.setText("Github")
            UIFunction.androidStackPages(self, "page_world")

        elif buttonName == "bn_error":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_error)
            self.ui.lab_tab.setText("Error Page")

        elif buttonName == "bn_instancesettings":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_about_bug)
            self.ui.lab_tab.setText("Instance Settings")
            brain.instancesettings(self)

        elif buttonName == "bn_mods":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_forge_mods)
            # self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_forge_mods_install)
            if self.ui.stackedWidget_3.currentIndex == 0:
                self.ui.lab_tab.setText("Forge Mods > Download")
            else:
                self.ui.lab_tab.setText("Forge Mods > Curseforge")
            self.ui.lab_tab.setText("Forge Mods")
            brain.forge_mods(self)

        elif buttonName == "bn_mods_nextPage":
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_forge_mods_web)
            self.ui.lab_tab.setText("Forge Mods > Curseforge")

        elif buttonName == "bn_mods_previousPage":
            self.ui.stackedWidget_3.setCurrentWidget(self.ui.page_forge_mods_download)
            self.ui.lab_tab.setText("Forge Mods > Download")

        elif buttonName == "bn_profile":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_android)
            UIFunction.androidStackPages(self, "page_contact")

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
        self.ui.bn_android_doc.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_doc")
        )
        self.ui.bn_faq.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_faq")
        )
        self.ui.bn_changelog.clicked.connect(
            lambda: UIFunction.androidStackPages(self, "page_changelog")
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

        ######ANDROID > PAGE CLEAN >>>>>>>>>>>>>>>>>>>>>>
        # NOTHING HER
        ##########PAGE: ABOUT HOME #############
        self.ui.text_about_home.setVerticalScrollBar(self.ui.vsb_about_home)

        ##########PAGE: INFORMATION #############

        self.ui.pushButton_github.clicked.connect(
            lambda: APFunction.pushButton_github(self)
        )

        self.ui.pushButton_issue.clicked.connect(
            lambda: APFunction.pushButton_issue(self)
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

        elif page == "page_doc":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_doc)
            self.ui.lab_tab.setText("Settings > Documentation")
            self.ui.frame_android_doc.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_faq":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_doc)
            self.ui.lab_tab.setText("Settings > Documentation")
            self.ui.webWidget.load(
                QtCore.QUrl("https://mlauncher.readthedocs.io/en/latest/faq/index.html")
            )
            self.ui.frame_android_doc.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_changelog":
            self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_doc)
            self.ui.lab_tab.setText("Settings > Documentation")
            self.ui.webWidget.load(
                QtCore.QUrl("https://mlauncher.readthedocs.io/en/latest/changelog.html")
            )
            self.ui.frame_android_doc.setStyleSheet("background:rgb(91,90,90)")

        elif page == "page_clean":
            pass

            """self.ui.stackedWidget_android.setCurrentWidget(self.ui.page_android_clean)
            self.ui.lab_tab.setText("Settings > Clean")
            self.ui.frame_android_clean.setStyleSheet("background:rgb(91,90,90)")"""

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
        self.ui.bn_android_doc.setEnabled(False)
        self.ui.bn_android_clean.setEnabled(False)
        self.ui.bn_android_world.setEnabled(False)

    def saveContact(self):
        username = self.ui.line_android_name.text()
        if any(not c.isalnum() for c in username) or username.isascii() == False:
            self.ui.line_android_name.setStyleSheet(
                "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
            )
            self.errorexec(
                "Only English chars! Special characters and spaces are not allowed!",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            return
        elif len(username) < 3:
            self.ui.line_android_name.setStyleSheet(
                "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
            )
            self.errorexec(
                "Your nickname is too short!\nMin 3 characters",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            return
        elif len(username) > 16:
            self.ui.line_android_name.setStyleSheet(
                "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
            )
            self.errorexec(
                "Your nickname is too long!\nMax 16 characters",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            return
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
        self.ui.bn_android_doc.setEnabled(True)
        self.ui.bn_android_clean.setEnabled(True)
        self.ui.bn_android_world.setEnabled(True)

        # * USERNAME

        self.ui.lab_user.setText(username)
        self.ui.lab_home_username.setText(username)
        config["PROFILE"]["username"] = username
        if username == "Krik" or username == "Kriktinus" or username == "Krek":
            applicationName = "PLauncher"
        else:
            applicationName = "MLauncher"
        self.ui.lab_appname.setText(applicationName)
        self.ui.line_android_name.setStyleSheet(
            "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid rgb(51,51,51);\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid rgb(112,112,112);\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
        )
        brain.setCurrentDiscordRpc("Home Page", f"Playing as {username}")

        # * Alocated Ram

        bufor = self.ui.line_android_adress.text().upper()
        bufor = bufor.replace("B", "")
        self.ui.line_android_adress.setText(bufor)
        if "G" in bufor and "M" in bufor:
            self.ui.line_android_adress.setStyleSheet(
                "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
            )
            self.ui.line_android_adress.setText(config.get("SETTINGS", "allocatedram"))
            self.errorexec(
                "Something weird occured with that amount of ram, check if it is entered correctly!",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
        elif bufor[-1] != "G" and bufor[-1] != "M":
            self.ui.line_android_adress.setStyleSheet(
                "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
            )
            self.ui.line_android_adress.setText(config.get("SETTINGS", "allocatedram"))
            self.errorexec(
                "'Max Ram' must have a unit. One of this two: 'G', 'M'. Settings will not be applied and saved!",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
        else:
            if bufor[-1] == "G":
                bufor = str(int(bufor.replace("G", "").replace("g", "")) * 1024) + "M"
                self.ui.line_android_adress.setText(bufor)
            var, buf, size = brain.check_ram(bufor)
            if var == True:
                config["SETTINGS"]["AllocatedRam"] = bufor
                self.ui.line_android_adress.setStyleSheet(
                    "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid rgb(51,51,51);\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid rgb(112,112,112);\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
                )
            else:
                self.ui.line_android_adress.setText(
                    config.get("SETTINGS", "allocatedram")
                )
                self.ui.line_android_adress.setStyleSheet(
                    "QLineEdit {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(51,51,51);\n}\n\nQLineEdit:disabled {\n	color:rgb(255,255,255);\n	border:2px solid red;\n	border-radius:4px;\n	background:rgb(112,112,112);\n}"
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

        threading.Thread(
            name="t-GetReleases", target=lambda: brain.GetReleases(self)
        ).start()

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
                "Recommended if you have alocated more than 2GB RAM\n(May cause starting problems)",
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

    def pushButton_issue(self):
        webbrowser.open("https://github.com/Bre3n/MLauncher/issues")

    def bug_button(self):
        self.ui.label_12.setText("Vanilla Versions")
        threading.Thread(
            name="t-GetReleases", target=lambda: brain.GetReleases(self)
        ).start()

    def bug_button2(self):
        self.ui.label_12.setText("Forge Versions")
        threading.Thread(
            name="t-ForgeReleases", target=lambda: brain.ForgeReleases(self, 1)
        ).start()

    def bug_button3(self):
        self.ui.label_12.setText("Modpacks")
        threading.Thread(
            name="t-ServerVersions", target=lambda: brain.serverVersions(self)
        ).start()

    def bug_confirm(self):
        bufor = self.ui.comboBox.currentText()
        self.ui.label_13.setText(f"Current Version: {bufor}")
        self.ui.label_2.setText(f"Current Version: {bufor}")
        if os.path.exists(f"{sciezka}/instances/{bufor}"):
            if (
                self.ui.label_12.text() == "Forge Versions"
                or self.ui.label_12.text() == "Modpacks"
            ):
                self.ui.bn_showMods.setVisible(True)
            else:
                self.ui.bn_showMods.setVisible(False)
        else:
            self.ui.bn_showMods.setVisible(False)
        config = ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config["PROFILE"]["gameversion"] = self.ui.label_12.text()
        config["PROFILE"]["version"] = bufor
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)
