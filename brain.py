import configparser
import multiprocessing
import os
import time
import json
import psutil
import requests
from pypresence import Presence
import minecraft_launcher_lib as MCLib
from os import path

user = os.getlogin()
sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
sciezkaver = f"{sciezka}/bin"
config = configparser.ConfigParser()
currentDiscordRpc = ""
currentDiscordRpcDetails = ""
checkinternetbool = False
connectedRpc = False
rpc = 0
Lista = ""


def createFiles():
    # * CONFIG
    config.read(f"{sciezkaver}/config.ini")
    if config.has_section("SETTINGS") == False:
        config.add_section("SETTINGS")
    if config.has_section("PROFILE") == False:
        config.add_section("PROFILE")
    if config.has_option("SETTINGS", "allocatedram") == False:
        config["SETTINGS"]["allocatedram"] = "2048M"
    if config.has_option("SETTINGS", "specialarg") == False:
        config["SETTINGS"]["specialarg"] = "False"
    if config.has_option("SETTINGS", "discordactivity") == False:
        config["SETTINGS"]["discordactivity"] = "True"
    if config.has_option("SETTINGS", "snapshots") == False:
        config["SETTINGS"]["snapshots"] = "False"
    if config.has_option("PROFILE", "uuid") == False:
        data = requests.get("https://www.uuidtools.com/api/generate/v4/count/1").json()
        config["PROFILE"]["uuid"] = data[0]
    if config.has_option("PROFILE", "username") == False:
        config["PROFILE"]["username"] = "Steve"
    if config.has_option("PROFILE", "version") == False:
        config["PROFILE"]["version"] = "1.8"
    ALLOCATEDRAM = config.get("SETTINGS", "AllocatedRam")
    if ALLOCATEDRAM[-1] == "G":
        ALLOCATEDRAM = str(int(ALLOCATEDRAM.replace("G", "")) * 1024) + "M"
        config["SETTINGS"]["AllocatedRam"] = ALLOCATEDRAM
    with open(f"{sciezkaver}/config.ini", "w") as configfile:
        config.write(configfile)

    # * FOLDERS
    if path.exists(f"{sciezka}/instances") == False:
        os.mkdir(f"{sciezka}/instances")


def configfile(arg):
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    arg = arg.split("&")
    if arg[0] == "default":
        config["SETTINGS"]["allocatedram"] = "2048M"
        config["SETTINGS"]["specialarg"] = "False"
        config["SETTINGS"]["discordactivity"] = "True"
        config["SETTINGS"]["snapshots"] = "False"
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
        self.ui.line_checkbox_arg.setText("Checked")
    else:
        SpecialArguments = False
        self.ui.line_checkbox_arg.setText("Unchecked")
    self.ui.line_checkbox_arg.setChecked(SpecialArguments)

    # * DiscordActivity
    bufor = config.get("SETTINGS", "discordactivity")
    if bufor == "True":
        DiscordActivity = True
        self.ui.line_checkbox_rpc.setText("Checked")
    else:
        DiscordActivity = False
        self.ui.line_checkbox_rpc.setText("Unchecked")
    self.ui.line_checkbox_rpc.setChecked(DiscordActivity)

    # * Show Snapshots
    bufor = config.get("SETTINGS", "snapshots")
    if bufor == "True":
        ShowSnapshots = True
        self.ui.line_checkbox_snapshots.setText("Checked")
    else:
        ShowSnapshots = False
        self.ui.line_checkbox_snapshots.setText("Unchecked")
    self.ui.line_checkbox_snapshots.setChecked(ShowSnapshots)


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
        time.sleep(10)


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
            if (config.get("SETTINGS", "discordactivity")) == "True":
                if currentDiscordRpc == "":
                    rpc.update(details=currentDiscordRpcDetails, large_image="rpcimage")
                elif currentDiscordRpc == "quit()":
                    rpc.clear()
                else:
                    rpc.update(
                        state=currentDiscordRpc,
                        details=currentDiscordRpcDetails,
                        large_image="rpcimage",
                    )
            else:
                rpc.clear()
        time.sleep(20)


def GetReleases(self):
    self.ui.comboBox.clear()
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    if config.get("SETTINGS", "snapshots") == "True":
        var = True
    else:
        var = False
    global Lista
    Releases = []
    McVers = []
    if Lista == "":
        Lista = requests.get(
            "https://launchermeta.mojang.com/mc/game/version_manifest.json"
        ).json()
    VersionsA = Lista["versions"]
    bufor = [
        name
        for name in os.listdir(f"{sciezka}/instances")
        if os.path.isdir(os.path.join(f"{sciezka}/instances", name))
    ]
    for i in range(int(len(bufor))):
        McVers.append(f"local {bufor[i]}")
    if var == False:
        for key in VersionsA:
            if key["type"] == "release":
                bufor = key["id"]
                Releases.append(f"release {bufor}")
    else:
        for key in VersionsA:
            if key["type"] == "release":
                bufor = key["id"]
                Releases.append(f"release {bufor}")
            if key["type"] == "snapshot":
                bufor = key["id"]
                Releases.append(f"snapshot {bufor}")
    for i in range(int(len(Releases))):
        McVers.append(Releases[i])
    self.ui.comboBox.addItems(McVers)


def serverVersions(self):
    self.ui.comboBox.clear()
    versions = configparser.ConfigParser()
    versions.read(f"{sciezkaver}/versions.ini")
    bufor = versions.sections()
    self.ui.comboBox.addItems(bufor)


def play(self):
    content = self.ui.comboBox.currentText()
    print(content)
    pass
