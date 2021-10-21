import configparser
import multiprocessing
import os
import time
import json
import psutil
import math
import ctypes
import enlighten
import threading
import requests
from pypresence import Presence
import minecraft_launcher_lib
from minecraft_launcher_lib.forge import (
    install_forge_version,
    run_forge_installer,
    supports_automatic_install,
)
from minecraft_launcher_lib.fabric import (
    install_fabric,
    get_all_minecraft_versions,
    get_stable_minecraft_versions,
    get_latest_loader_version,
)
from os import path
import zipfile
import subprocess

user = os.getlogin()
sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
sciezkaver = f"{sciezka}/bin"
sciezkains = f"{sciezka}/instances"
sciezkajvms = f"{sciezka}/jvms"
config = configparser.ConfigParser()
currentDiscordRpc = ""
currentDiscordRpcDetails = ""
checkinternetbool = False
connectedRpc = False
rpc = 0
Lista = ""
iterablebool = 5
canPlay = True


def download(url, pathh, self):
    MANAGER = enlighten.get_manager()
    i = 0
    r = requests.get(url, stream=True)
    assert r.status_code == 200, r.status_code
    dlen = int(r.headers.get("Content-Length", "0")) or None
    with MANAGER.counter(
        color="green", total=dlen and math.ceil(dlen / 2 ** 20), unit="MiB", leave=False
    ) as ctr, open(pathh, "wb", buffering=2 ** 24) as f:
        for chunk in r.iter_content(chunk_size=2 ** 20):
            i += 1
            self.ui.lab_tab2.setText(f"Downloading {i}/{math.ceil(dlen/2**20)}")
            print(chunk[-16:].hex().upper())
            f.write(chunk)


def createFiles():
    # * FOLDERS
    if path.exists(f"{sciezka}/instances") == False:
        os.mkdir(f"{sciezka}/instances")
    if path.exists(f"{sciezka}/instances/.Minecraft_Instances") == False:
        open(f"{sciezka}/instances/.Minecraft_Instances.txt", "w").close()
    if path.exists(f"{sciezka}/cache") == False:
        os.mkdir(f"{sciezka}/cache")
    if path.exists(f"{sciezka}/jvms") == False:
        os.mkdir(f"{sciezka}/jvms")

    # * CONFIG
    config.read(f"{sciezkaver}/config.ini")
    if config.has_section("JVMS") == False:
        config.add_section("JVMS")
    if config.has_section("SETTINGS") == False:
        config.add_section("SETTINGS")
    if config.has_section("PROFILE") == False:
        config.add_section("PROFILE")
    if config.has_option("SETTINGS", "java-1.8") == False:
        config["SETTINGS"]["java-1.8"] = f"{sciezkajvms}/jre1.8.0_281/bin/javaw.exe"
    if config.has_option("SETTINGS", "java-16") == False:
        config["SETTINGS"]["java-16"] = f"{sciezkajvms}/jdk-16.0.2/bin/javaw.exe"
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
        config["PROFILE"]["version"] = "1.17.1"
    ALLOCATEDRAM = config.get("SETTINGS", "AllocatedRam")
    if ALLOCATEDRAM[-1] == "G":
        ALLOCATEDRAM = str(int(ALLOCATEDRAM.replace("G", "")) * 1024) + "M"
        config["SETTINGS"]["AllocatedRam"] = ALLOCATEDRAM
    with open(f"{sciezkaver}/config.ini", "w") as configfile:
        config.write(configfile)


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
        config["PROFILE"]["version"] = "1.17.1"

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

    # * Current Version
    bufor = config.get("PROFILE", "version")
    self.ui.label_13.setText(f"Current Version: {bufor}")


def iterablebooldef(var):
    global iterablebool
    iterablebool = var


def checkinternet(self):
    global iterablebool
    url = "http://www.github.com"
    global checkinternetbool
    while iterablebool > 0:
        iterablebool = iterablebool
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
    global iterablebool
    global connectedRpc
    global rpc
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    while iterablebool > 0:
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
        time.sleep(2)


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
    buforlist = []
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
        buforlist.append(bufor[i])
    if var == False:
        for key in VersionsA:
            if key["type"] == "release":
                bufor = key["id"]
                if bufor in buforlist:
                    Releases.append(f"release {bufor} <-- local installed")
                else:
                    Releases.append(f"release {bufor}")
    else:
        for key in VersionsA:
            if key["type"] == "release":
                bufor = key["id"]
                if bufor in buforlist:
                    Releases.append(f"release {bufor} <-- local installed")
                else:
                    Releases.append(f"release {bufor}")
            if key["type"] == "snapshot":
                bufor = key["id"]
                if bufor in buforlist:
                    Releases.append(f"snapchot {bufor} <-- local installed")
                else:
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


def playthread(self):
    threading.Thread(target=lambda: play(self)).start()


def play(self):
    global canPlay
    if canPlay == False:
        self.errorexec(
            "All the necessary stuff you need have not been downloaded yet! Please wait",
            "icons/1x/smile2Asset 1.png",
            "Ok",
        )
        return 0
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    username = config.get("PROFILE", "username")
    token = config.get("PROFILE", "uuid")
    uuid = token.replace("-", "")
    allocatedram = config.get("SETTINGS", "allocatedram")
    specialarg = config.get("SETTINGS", "specialarg")
    jvmArguments = f"-Xmx{allocatedram}"

    callback = {
        "setStatus": lambda text: print(text),
    }
    content = config.get("PROFILE", "version")
    type = self.ui.label_12.text()
    local = False
    """if "local" in content:
        local = True"""
    if type == "Vanilla Versions":
        content = (
            content.replace("release", "")
            .replace("snapshot", "")
            .replace("<-- local installed", "")
            .replace("local", "")
            .replace(" ", "")
        )
    versionPath = content.replace(" ", "-")
    if local == True:
        content = content.split("-")
        version = content[1]
    else:
        version = content
    versionPathh = f"{sciezkains}/{versionPath}/.minecraft"
    bufor = version.split(".")
    if int(bufor[1]) >= 16:
        executablePath = config.get("SETTINGS", "java-16")
    else:
        executablePath = config.get("SETTINGS", "java-1.8")
    options = {
        "username": username,
        "uuid": uuid,
        "token": token,
        "jvmArguments": [jvmArguments],
        "executablePath": executablePath,
    }

    if path.exists(f"{sciezkains}/{versionPath}") == False:
        os.mkdir(f"{sciezkains}/{versionPath}")
        """with zipfile.ZipFile(f"{sciezkains}/.minecraft.zip", "r") as zipObj:
            zipObj.extractall(f"{sciezkains}/{versionPath}/.minecraft")"""
        minecraft_launcher_lib.install.install_minecraft_version(
            version, versionPathh, callback=callback
        )
        play(self)
    else:
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, versionPathh, options
        )
        subprocess.call(minecraft_command)


def downloadstuff(self):
    global canPlay
    canPlay = False
    if path.exists(f"{sciezkains}/.minecraft.zip") == False:
        download(
            "https://www.dropbox.com/s/pu8qla6yoogstnf/.minecraft.zip?dl=1",
            f"{sciezkains}/.minecraft.zip",
            self,
        )
    if (
        path.exists(f"{sciezkajvms}/jre1.8.0_281") == False
        or path.exists(f"{sciezkajvms}/jdk-16.0.2") == False
    ):
        download(
            "https://www.dropbox.com/s/spdx9qinhsr66n4/jvms.zip?dl=1",
            f"{sciezkajvms}/jvms.zip",
            self,
        )
        with zipfile.ZipFile(f"{sciezkajvms}/jvms.zip", "r") as zipObj:
            zipObj.extractall(f"{sciezkajvms}/")
    self.errorexec(
        "Now you can safetly close program. Or just play. idk",
        "icons/1x/smile2Asset 1.png",
        "Ok",
    )
    canPlay = True
