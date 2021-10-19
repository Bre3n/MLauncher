import configparser
import multiprocessing
import os
import time

import psutil
import requests
from pypresence import Presence

user = os.getlogin()
sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
sciezkaver = f"{sciezka}/bin"
config = configparser.ConfigParser()
currentDiscordRpc = ""
currentDiscordRpcDetails = ""
checkinternetbool = False
connectedRpc = False
rpc = 0


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
        setCurrentDiscordRpc("Home Page", "Playing as Steve")


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
    global checkinternetbool
    while True:
        try:
            request = requests.get(url, timeout=5)
            checkinternetbool = True
            if self.i == 2:
                self.i = 1
                self.valueChanged.emit(self.i)
        except (requests.ConnectionError, requests.Timeout) as exception:
            checkinternetbool = False
            if self.i == 1 or self.i == 0:
                self.i = 2
                self.valueChanged.emit(self.i)
        time.sleep(2)


def check_ram(allocated):
    byte = psutil.virtual_memory().total
    while True:
        if byte < 1024:
            size = f"{byte:.2f}"
            size = round(float(size)) * 1024
            break
        byte = byte / 1024
    bufor = int(size * 0.8)
    if int(allocated.replace("M", "")) > bufor:
        return False, bufor, size
    else:
        return True, 0, 0


def setCurrentDiscordRpc(bufor, bufor2):
    global currentDiscordRpc
    global currentDiscordRpcDetails
    currentDiscordRpcDetails = bufor
    currentDiscordRpc = bufor2


def connectRpc():
    global rpc
    global connectedRpc
    rpc = Presence(client_id="898206330517610558")
    rpc.connect()
    connectedRpc = True


def discordrpc(self):
    global connectedRpc
    global rpc
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    while True:
        bufor = "Discord.exe" in (i.name() for i in psutil.process_iter())
        if bufor == False:
            break
        if connectedRpc == False and checkinternetbool == True:
            self.i = 10
            self.valueChanged.emit(self.i)
            self.i = 1
        if connectedRpc == True and checkinternetbool == True:
            config.read(f"{sciezkaver}/config.ini")
            if (config.get("SETTINGS", "discordactivity")) == "True":
                if currentDiscordRpc == "":
                    rpc.update(details=currentDiscordRpcDetails, large_image="rpcimage")
                else:
                    rpc.update(
                        state=currentDiscordRpc,
                        details=currentDiscordRpcDetails,
                        large_image="rpcimage",
                    )
            else:
                rpc.clear()
        time.sleep(2)
