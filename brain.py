import configparser
import os
import threading

import requests

user = os.getlogin()
sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
sciezkaver = f"{sciezka}/bin"
config = configparser.ConfigParser()


def configfile(arg):
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    arg = arg.split("&")
    if arg[0] == "default":
        config["SETTINGS"]["allocatedram"] = "2048M"
        config["SETTINGS"]["specialarg"] = "False"
        config["SETTINGS"]["discordactivity"] = "True"
        data = requests.get("https://www.uuidtools.com/api/generate/v4/count/1").json()
        config["PROFILE"]["uuid"] = data[0]
        config["PROFILE"]["username"] = "Steve"
        with open(f"{sciezkaver}/config.ini", "w") as configfile:
            config.write(configfile)


def updateLines(self):
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    # * USERNAME
    Username = config.get("PROFILE", "username")
    self.ui.lab_user.setText(Username)
    self.ui.lab_home_username.setText(Username)
    self.ui.line_android_name.setText(Username)

    # * ALLOCATEDRAM
    Allocatedram = config.get("SETTINGS", "allocatedram")
    self.ui.line_android_adress.setText(Allocatedram)

    # * SPECIAL ARGUMENTS
    bufor = config.get("SETTINGS", "specialarg")
    if bufor == "True":
        SpecialArguments = True
    else:
        SpecialArguments = False
    self.ui.line_checkbox_arg.setChecked(SpecialArguments)
    if SpecialArguments == True:
        self.ui.line_checkbox_arg.setText("Checked")
    else:
        self.ui.line_checkbox_arg.setText("Unchecked")

    # * DiscordActivity
    bufor = config.get("SETTINGS", "discordactivity")
    if bufor == "True":
        DiscordActivity = True
    else:
        DiscordActivity = False
    self.ui.line_checkbox_rpc.setChecked(DiscordActivity)
    if DiscordActivity == True:
        self.ui.line_checkbox_rpc.setText("Checked")
    else:
        self.ui.line_checkbox_rpc.setText("Unchecked")


def checkinternet(self):
    url = "http://www.github.com"
    timeout = 5
    try:
        request = requests.get(url, timeout=timeout)
        self.ui.lab_tab2.setText("")
        self.ui.lab_tab2.setStyleSheet("background:rgb(51,51,51);")
        self.ui.lab_tab.setStyleSheet("background:rgb(51,51,51);")
        self.ui.frame_appname.setStyleSheet("")
        self.ui.frame_close.setStyleSheet("")
        self.ui.frame_min.setStyleSheet("")
        self.ui.frame_person.setStyleSheet("")
        self.ui.frame_user.setStyleSheet("")
    except (requests.ConnectionError, requests.Timeout) as exception:
        self.ui.lab_tab2.setText("Internet connection Error       ")
        self.ui.lab_tab2.setStyleSheet("background:#ff0033;")
        self.ui.lab_tab.setStyleSheet("background:#ff0033;")
        self.ui.frame_appname.setStyleSheet("background:#ff0033;")
        self.ui.frame_close.setStyleSheet("background:#ff0033;")
        self.ui.frame_min.setStyleSheet("background:#ff0033;")
        self.ui.frame_person.setStyleSheet("background:#ff0033;")
        self.ui.frame_user.setStyleSheet("background:#ff0033;")
    threading.Timer(10.0, lambda: checkinternet(self)).start()
