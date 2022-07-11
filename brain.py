import configparser
import ctypes
from email.headerregistry import ContentTransferEncodingHeader
import json
import math
import os
import shutil
import subprocess
import threading
import time
import webbrowser
import zipfile
from os import listdir, path
from os.path import isfile, join

from clint.textui import progress
import minecraft_launcher_lib
import psutil
import pythoncom
import requests
import win32com.client
import winshell
from minecraft_launcher_lib.forge import (
    install_forge_version,
    run_forge_installer,
    supports_automatic_install,
)
from pypresence import Presence
from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QAction, QApplication, QFileDialog, QLabel, QMainWindow

roaming = os.getenv("APPDATA")
sciezka = f"{roaming}/.mlauncher"
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
ForgeVersions = ""
ForgeVersionss = ""
ServerVersions = ""
deleteInstance = False
ProgressBarMc_value = 1
ProgressBarMc_total = 2
articleURL = [1, 2, 3, 4, 5]


def download(url, pathh, self, value):
    r = requests.get(url, stream=True)
    i = 5
    percentagebufor = 0
    with open(pathh, "wb") as f:
        total_length = int(r.headers.get("content-length")) or None
        for chunk in progress.bar(
            r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1
        ):
            if chunk:
                i = i + 1
                if total_length != None:
                    lenght = int(round((total_length / 1024) + 1))
                    percentage = int(round(i / ((total_length / 1024) + 1) * 100))
                    visual_percentage = ("█" * (percentage // 10)) + (
                        "  " * (10 - (percentage // 10))
                    )
                    percentageModulus = percentage % 1
                    if percentageModulus == 0 and percentagebufor != percentage:
                        self.ui.lab_tab2.setText(
                            f"Downloading {percentage}% |{visual_percentage}| {i}/{lenght}"
                        )
                        percentagebufor = percentage
                f.write(chunk)
                f.flush()


def createshortcut():
    desktop = winshell.desktop()
    if os.path.exists(f"{desktop}/MLauncher.lnk") == False:
        path = os.path.join(desktop, "MLauncher.lnk")
        target = f"{sciezkaver}\\setup.py"
        icon = f"{sciezkaver}/icons/1x/icon.ico"
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.IconLocation = icon
        shortcut.save()


def createFiles():
    # * FOLDERS
    if path.exists(f"{sciezka}/instances") == False:
        os.mkdir(f"{sciezka}/instances")
    if path.exists(f"{sciezka}/instances/.Minecraft_Instances") == False:
        open(f"{sciezka}/instances/.Minecraft_Instances.txt", "w").close()
    if path.exists(f"{sciezka}/cache") == False:
        os.mkdir(f"{sciezka}/cache")
    if path.exists(f"{sciezka}/cache/img") == False:
        os.mkdir(f"{sciezka}/cache/img")
    if path.exists(f"{sciezka}/jvms") == False:
        os.mkdir(f"{sciezka}/jvms")
    if path.exists(f"{sciezka}/minecraft-folders") == False:
        os.mkdir(f"{sciezka}/minecraft-folders")
    if path.exists(f"{sciezka}/minecraft-folders/saves") == False:
        os.mkdir(f"{sciezka}/minecraft-folders/saves")

    # * CONFIG
    config.read(f"{sciezkaver}/config.ini")

    # * JVMS
    if config.has_section("JVMS") == False:
        config.add_section("JVMS")
    if config.has_option("JVMS", "java-1.8") == False:
        config["JVMS"]["java-1.8"] = f"{sciezkajvms}/jre1.8.0_281/bin/javaw.exe"
    if config.has_option("JVMS", "java-17") == False:
        config["JVMS"]["java-17"] = f"{sciezkajvms}/jdk-17.0.2/bin/javaw.exe"
    if config.has_option("JVMS", "specialarg-1.8") == False:
        config["JVMS"][
            "specialarg-1.8"
        ] = "Dsun.rmi.dgc.server.gcInterval=2147483646 -XX:+UnlockExperimentalVMOptions -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M"
    if config.has_option("JVMS", "specialarg-17") == False:
        config["JVMS"]["specialarg-17"] = "False"

    # * SETTINGS
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

    # * PROFILE
    if config.has_option("PROFILE", "uuid") == False:
        data = requests.get("https://www.uuidtools.com/api/generate/v4/count/1").json()
        config["PROFILE"]["uuid"] = data[0]
    if config.has_option("PROFILE", "username") == False:
        config["PROFILE"]["username"] = "Steve"
    if config.has_option("PROFILE", "version") == False:
        config["PROFILE"]["version"] = "1.17.1"
    if config.has_option("PROFILE", "gameVersion") == False:
        config["PROFILE"]["gameVersion"] = "Vanilla Versions"

    # * CHECK RAM UNIT
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
    self.ui.label_2.setText(f"Current Version: {bufor}")


def iterablebooldef(var):
    global iterablebool
    iterablebool = var


def checkinternet(self):
    global iterablebool
    global checkinternetbool
    while iterablebool > 0:
        self.ui.bn_play.text()
        iterablebool = iterablebool
        try:
            request = requests.get("http://www.google.com", timeout=5)
            checkinternetbool = True
            if self.i == 2:
                self.i = 1
                self.valueChanged.emit(self.i)
        except (requests.ConnectionError, requests.Timeout) as exception:
            checkinternetbool = False
            if self.i == 1 or self.i == 0:
                self.i = 2
                self.valueChanged.emit(self.i)
        time.sleep(20)


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
        self.ui.bn_play.text()
        bufor = "Discord.exe" in (i.name() for i in psutil.process_iter())
        if bufor != False:
            if connectedRpc == False and checkinternetbool == True:
                self.i = 10
                self.valueChanged.emit(self.i)
                self.i = 1
            if connectedRpc == True and checkinternetbool == True:
                config.read(f"{sciezkaver}/config.ini")
                if (config.get("SETTINGS", "discordactivity")) == "True":
                    if currentDiscordRpc == "":
                        rpc.update(
                            details=currentDiscordRpcDetails, large_image="rpcimage"
                        )
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
    try:
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
        customlist = []
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
            if path.exists(f"{sciezka}/instances/{bufor[i]}/.minecraft") == True:
                buforlist.append(bufor[i])
        if var == False:
            for key in VersionsA:
                if key["type"] == "release":
                    bufor = key["id"]
                    if bufor in buforlist:
                        Releases.append(f"release {bufor} <-- local installed")
                        buforlist.remove(bufor)
                    else:
                        Releases.append(f"release {bufor}")
        else:
            for key in VersionsA:
                if key["type"] == "release":
                    bufor = key["id"]
                    if bufor in buforlist:
                        Releases.append(f"release {bufor} <-- local installed")
                        buforlist.remove(bufor)
                    else:
                        Releases.append(f"release {bufor}")
                if key["type"] == "snapshot":
                    bufor = key["id"]
                    if bufor in buforlist:
                        Releases.append(f"snapshot {bufor} <-- local installed")
                        buforlist.remove(bufor)
                    else:
                        Releases.append(f"snapshot {bufor}")
        for i in range(int(len(Releases))):
            McVers.append(Releases[i])
        global ServerVersions
        if ServerVersions == "":
            versions = configparser.ConfigParser()
            versions.read(f"{sciezkaver}/servers.ini")
            ServerVersions = versions.sections()
            """for i in range(len(ServerVersions)):
                ServerVersions[i] = ServerVersions[i].replace("s_","")"""
        self.ui.comboBox.addItems(McVers)
    except Exception:
        pass


def clearList(self):
    global Lista
    global ServerVersions
    global ForgeVersions
    Lista = ""
    ServerVersions = ""
    ForgeVersions = ""
    GetReleases(self)


def serverVersions(self):
    global ServerVersions
    self.ui.comboBox.clear()
    if ServerVersions == "":
        versions = configparser.ConfigParser()
        versions.read(f"{sciezkaver}/versions.ini")
        ServerVersions = versions.sections()
        """for i in range(len(ServerVersions)):
            ServerVersions[i] = ServerVersions[i].replace("s_","")"""
    self.ui.comboBox.addItems(ServerVersions)


def ForgeReleases(self, var):
    global ForgeVersions
    global ForgeVersionss
    global buforlist
    try:
        customlist = []
        buforlist = []
        bufor = [
            name
            for name in os.listdir(f"{sciezka}/instances")
            if os.path.isdir(os.path.join(f"{sciezka}/instances", name))
        ]
        for i in range(int(len(bufor))):
            if path.exists(f"{sciezka}/instances/{bufor[i]}/.minecraft") == True:
                buforr = bufor[i].replace("f-", "")
                buforlist.append(buforr)
        if ForgeVersions == "":
            ForgeVersions = []
            if ForgeVersionss == "":
                ForgeVersionss = minecraft_launcher_lib.forge.list_forge_versions()
            for i in range(len(ForgeVersionss)):
                niewytrzymam = ForgeVersionss[i].split("-")
                niewytrzymam = niewytrzymam[0].split(".")
                if int(niewytrzymam[1]) >= 13:
                    if ForgeVersionss[i] in buforlist:
                        ForgeVersions.append(f"{ForgeVersionss[i]} <-- local installed")
                    else:
                        ForgeVersions.append(f"{ForgeVersionss[i]}")
        if var == 1:
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(ForgeVersions)
    except Exception:
        pass


def playthread(self):
    if self.closebool == False:
        self.errorexec(
            "All the necessary stuff you need have not been downloaded yet! Please wait",
            "icons/1x/smile2Asset 1.png",
            "Ok",
        )
        return
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")
    bufor = config["PROFILE"]["gameversion"]
    if bufor == "Vanilla Versions":
        threading.Thread(
            name="t-PlayVanilla", target=lambda: playVanilla(self, 1)
        ).start()
    # TODO: ADD FORGE AND SERVER
    if bufor == "Forge Versions":
        threading.Thread(name="t-PlayForge", target=lambda: playForge(self, 1)).start()
    if bufor == "Modpacks":
        threading.Thread(name="t-PlayServers", target=lambda: playServers(self)).start()


def downloadingCount(self):
    i = 0
    while True:
        time.sleep(0.5)
        if self.ui.bn_play.text() == "Downloading":
            global ProgressBarMc_value
            global ProgressBarMc_total
            percentage_one = ProgressBarMc_total / 100
            percentage = int(round(ProgressBarMc_value // percentage_one))
            visual_percentage = ("█" * (percentage // 10)) + (
                "  " * (10 - (percentage // 10))
            )
            if ProgressBarMc_value == ProgressBarMc_total:
                self.ui.lab_tab2.setText(f" ")
            else:
                self.ui.lab_tab2.setText(
                    f"Downloading {percentage}% |{visual_percentage}| {ProgressBarMc_value}/{ProgressBarMc_total}"
                )
        else:
            break
    self.ui.lab_tab2.setText("Downloaded")
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")
    time.sleep(0.5)
    self.ui.lab_tab2.setText("Downloaded")
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")
    time.sleep(0.5)
    self.ui.lab_tab2.setText("Downloaded")
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")


def playForge(self, var):
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")

    username = config.get("PROFILE", "username")
    token = config.get("PROFILE", "uuid")
    uuid = token.replace("-", "")
    allocatedram = config.get("SETTINGS", "allocatedram")
    specialarg = config.get("SETTINGS", "specialarg")
    jvmArguments = []
    jvmArguments.append(f"-Xmx{allocatedram}")

    max_value = [0]

    callback = {
        "setStatus": lambda text: print(text),
        "setProgress": lambda value: ProgressBarMc(value, max_value[0], self),
        "setMax": lambda value: ProgressBarMcMaximum(max_value, value),
    }

    content = config.get("PROFILE", "version")
    if var != 2:
        versionPath = (
            content.replace("release", "")
            .replace("snapshot", "")
            .replace("<-- local installed", "")
            .replace("local", "")
            .replace(" ", "")
        )
        version = versionPath
        versionPath = "f-" + version
        versionPathh = f"{sciezkains}/{versionPath}/.minecraft"
    else:
        config_servers = configparser.ConfigParser()
        config_servers.read(f"{sciezkaver}/servers.ini")
        version = config_servers.get(f"{content}", "forgeVersion")
        versionPath = content
        versionPathh = f"{sciezkains}/{content}/.minecraft"

    bufor = version.split("-")
    bufor = bufor[0].split(".")
    try:
        if int(bufor[1]) >= 16:
            executablePath = config.get("JVMS", "java-17")
        else:
            executablePath = config.get("JVMS", "java-1.8")
    except Exception:
        executablePath = config.get("JVMS", "java-17")

    if specialarg == "True":
        if bufor[1] != int:
            if int(bufor[1]) >= 16:
                buf = config.get("JVMS", "specialarg-17")
                buf = buf.split(" ")
                for i in range(len(buf)):
                    jvmArguments.append(buf[i])
            else:
                buf = config.get("JVMS", "specialarg-1.8")
                buf = buf.split(" ")
                for i in range(len(buf)):
                    jvmArguments.append(buf[i])
        else:
            buf = config.get("JVMS", "specialarg-17")
            buf = buf.split(" ")
            for i in range(len(buf)):
                jvmArguments.append(buf[i])
    options = {
        "username": username,
        "uuid": uuid,
        "token": token,
        "jvmArguments": jvmArguments,
        "executablePath": executablePath,
    }
    settings_ins = configparser.ConfigParser()
    settings_ins.read(f"{sciezkains}/{versionPath}/settings_ins.ini")

    if path.exists(f"{sciezkains}/{versionPath}") == False or var == 0 or var == 2:
        self.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:55px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:65px;background-color: rgba(70,140,190,0.7);}"
        )
        self.ui.bn_play.setText(f"Downloading")
        threading.Thread(
            name="t-DownloadingCount", target=lambda: downloadingCount(self)
        ).start()
        os.mkdir(f"{sciezkains}/{versionPath}/")
        os.mkdir(f"{sciezkains}/{versionPath}/.minecraft")
        shutil.copy(
            f"{sciezkaver}/launcher_profiles.json",
            f"{sciezkains}/{versionPath}/.minecraft/launcher_profiles.json",
        )
        subprocess.check_call(
            'mklink /J "%s" "%s"'
            % (
                f"{sciezkains}/{versionPath}/.minecraft/assets",
                f"{sciezkains}/shared/.minecraft/assets",
            ),
            shell=True,
        )
        subprocess.check_call(
            'mklink /J "%s" "%s"'
            % (
                f"{sciezkains}/{versionPath}/.minecraft/runtime",
                f"{sciezkains}/shared/.minecraft/runtime",
            ),
            shell=True,
        )
        subprocess.check_call(
            'mklink /J "%s" "%s"'
            % (
                f"{sciezkains}/{versionPath}/.minecraft/libraries",
                f"{sciezkains}/shared/.minecraft/libraries",
            ),
            shell=True,
        )

        # * run installation
        try:
            """if (
                path.exists(
                    f"{sciezkains}/shared/.minecraft/libraries/net/minecraftforge/ForgeAutoRenamingTool/0.1.17/ForgeAutoRenamingTool-0.1.17-all.jar"
                )
                and path.exists(
                    f"{sciezkains}/shared/.minecraft/libraries/net/minecraftforge/ForgeAutoRenamingTool/0.1.17/ForgeAutoRenamingTool-0.1.17.jar"
                )
                == False
            ):
                shutil.move(
                    f"{sciezkains}/shared/.minecraft/libraries/net/minecraftforge/ForgeAutoRenamingTool/0.1.17/ForgeAutoRenamingTool-0.1.17-all.jar",
                    f"{sciezkains}/shared/.minecraft/libraries/net/minecraftforge/ForgeAutoRenamingTool/0.1.17/ForgeAutoRenamingTool-0.1.17.jar",
                )"""
            self.closebool = False
            if supports_automatic_install(version):
                versionPathh = versionPathh.replace("/", "\\")
                install_forge_version(version, versionPathh, callback=callback)
            else:
                xxx = config.get("JVMS", "java-1.17")
                playVanilla(self, 0)
                print(xxx)
                run_forge_installer(version, xxx)
        except Exception as e:
            # shutil.rmtree(f"{sciezkains}/{versionPath}/")
            self.errorexec(
                f"Something weird occured with forge instalation. Try again or wait for fix :( {e}",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
            self.ui.bn_play.setStyleSheet(
                "QPushButton {font-size:80px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:90px;background-color: rgba(70,140,190,0.7);}"
            )
            self.ui.bn_play.setText(f"Play")
            return
        self.closebool = True

        # * create instance settings_ins
        if (
            path.exists(f"{sciezkains}/{versionPath}/settings_ins.ini") == False
            or settings_ins.has_section(f"{version}") == False
            or settings_ins.has_option(f"{version}", "gametype") == False
            or settings_ins.has_option(f"{version}", "isshared") == False
            or settings_ins.has_option(f"{version}", "isseparate") == False
            or settings_ins.has_option(f"{version}", "isoptifine") == False
        ):
            if settings_ins.has_section(f"{version}") == False:
                settings_ins.add_section(f"{version}")
            if settings_ins.has_option(f"{version}", "gametype") == False:
                settings_ins[f"{version}"]["gametype"] = "Forge"
            if settings_ins.has_option(f"{version}", "isshared") == False:
                settings_ins[f"{version}"]["isshared"] = "no"
            if settings_ins.has_option(f"{version}", "isseparate") == False:
                settings_ins[f"{version}"]["isseparate"] = "yes"
            if settings_ins.has_option(f"{version}", "isoptifine") == False:
                settings_ins[f"{version}"]["isoptifine"] = "no"
            with open(
                f"{sciezkains}/{versionPath}/settings_ins.ini", "w"
            ) as configfile:
                settings_ins.write(configfile)

        # * play minecraft
        if var == 1:
            playForge(self, 1)
    else:
        self.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:70px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:80px;background-color: rgba(70,140,190,0.7);}"
        )
        self.ui.bn_play.setText(f"Launched")
        setCurrentDiscordRpc(f"Minecraft {version}", f"Playing as {username}")
        threading.Thread(
            name="t-PlayingCheck", target=lambda: playingcheck(self)
        ).start()
        version = minecraft_launcher_lib.utils.get_installed_versions(f"{versionPathh}")
        try:
            version = version[1]["id"]
        except Exception:
            version = version[0]["id"]
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, versionPathh, options
        )
        clearList(self)
        try:
            subprocess.call(minecraft_command)
        except Exception:
            self.errorexec(
                "Something weird occured with this instance. Please use repair button in instance settings",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )


def ProgressBarMc(value, total, self):
    global ProgressBarMc_value
    global ProgressBarMc_total
    ProgressBarMc_value = value
    ProgressBarMc_total = total


def ProgressBarMcMaximum(max_value, value):
    max_value[0] = value


def playVanilla(self, var):
    config = configparser.ConfigParser()
    config.read(f"{sciezkaver}/config.ini")

    username = config.get("PROFILE", "username")
    token = config.get("PROFILE", "uuid")
    uuid = token.replace("-", "")
    allocatedram = config.get("SETTINGS", "allocatedram")
    specialarg = config.get("SETTINGS", "specialarg")
    jvmArguments = []
    jvmArguments.append(f"-Xmx{allocatedram}")

    max_value = [0]

    callback = {
        "setStatus": lambda text: print(text),
        "setProgress": lambda value: ProgressBarMc(value, max_value[0], self),
        "setMax": lambda value: ProgressBarMcMaximum(max_value, value),
    }

    content = config.get("PROFILE", "version")
    """if var == 0:
        content = content.split('-')
        content = content[0]"""
    versionPath = (
        content.replace("release", "")
        .replace("snapshot", "")
        .replace("<-- local installed", "")
        .replace("local", "")
        .replace(" ", "")
    )
    version = versionPath
    #! adssadsdaasd

    if var == 0:
        versionPath = versionPath.split("-")
        versionPath = f"{versionPath[0]}" + "-forge-" + f"{versionPath[1]}"
    versionPathh = f"{sciezkains}/{versionPath}/.minecraft"

    bufor = version.split(".")
    if var == 0:
        version = version.split("-")
        version = version[0]
    try:
        if int(bufor[1]) >= 16:
            executablePath = config.get("JVMS", "java-17")
        else:
            executablePath = config.get("JVMS", "java-1.8")
    except Exception:
        executablePath = config.get("JVMS", "java-17")

    if specialarg == "True":
        if bufor[1] != int:
            if int(bufor[1]) >= 16:
                buf = config.get("JVMS", "specialarg-17")
                buf = buf.split(" ")
                for i in range(len(buf)):
                    jvmArguments.append(buf[i])
            else:
                buf = config.get("JVMS", "specialarg-1.8")
                buf = buf.split(" ")
                for i in range(len(buf)):
                    jvmArguments.append(buf[i])
        else:
            buf = config.get("JVMS", "specialarg-17")
            buf = buf.split(" ")
            for i in range(len(buf)):
                jvmArguments.append(buf[i])
    options = {
        "username": username,
        "uuid": uuid,
        "token": token,
        "jvmArguments": jvmArguments,
        "executablePath": executablePath,
    }

    settings_ins = configparser.ConfigParser()
    settings_ins.read(f"{sciezkains}/{versionPath}/settings_ins.ini")

    if path.exists(f"{sciezkains}/{versionPath}") == False or var == 0 or var == 2:
        self.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:55px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:65px;background-color: rgba(70,140,190,0.7);}"
        )
        self.ui.bn_play.setText(f"Downloading")
        threading.Thread(
            name="t-DownloadingCount", target=lambda: downloadingCount(self)
        ).start()
        if path.exists(f"{sciezkains}/{versionPath}/") == False:
            os.mkdir(f"{sciezkains}/{versionPath}/")
            os.mkdir(f"{sciezkains}/{versionPath}/.minecraft")
            shutil.copy(
                f"{sciezkaver}/launcher_profiles.json",
                f"{sciezkains}/{versionPath}/.minecraft/launcher_profiles.json",
            )
            subprocess.check_call(
                'mklink /J "%s" "%s"'
                % (
                    f"{sciezkains}/{versionPath}/.minecraft/saves",
                    f"{sciezka}/minecraft-folders/saves",
                ),
                shell=True,
            )
            subprocess.check_call(
                'mklink /J "%s" "%s"'
                % (
                    f"{sciezkains}/{versionPath}/.minecraft/assets",
                    f"{sciezkains}/shared/.minecraft/assets",
                ),
                shell=True,
            )
            subprocess.check_call(
                'mklink /J "%s" "%s"'
                % (
                    f"{sciezkains}/{versionPath}/.minecraft/runtime",
                    f"{sciezkains}/shared/.minecraft/runtime",
                ),
                shell=True,
            )
            subprocess.check_call(
                'mklink /J "%s" "%s"'
                % (
                    f"{sciezkains}/{versionPath}/.minecraft/libraries",
                    f"{sciezkains}/shared/.minecraft/libraries",
                ),
                shell=True,
            )

        # * run installation
        self.closebool = False
        minecraft_launcher_lib.install.install_minecraft_version(
            version, versionPathh, callback=callback
        )
        self.closebool = True
        # * create instance settings_ins
        if (
            path.exists(f"{sciezkains}/{versionPath}/settings_ins.ini") == False
            or settings_ins.has_section(f"{version}") == False
            or settings_ins.has_option(f"{version}", "gametype") == False
            or settings_ins.has_option(f"{version}", "isshared") == False
            or settings_ins.has_option(f"{version}", "isseparate") == False
            or settings_ins.has_option(f"{version}", "isoptifine") == False
        ):
            if settings_ins.has_section(f"{version}") == False:
                settings_ins.add_section(f"{version}")
            if settings_ins.has_option(f"{version}", "gametype") == False:
                settings_ins[f"{version}"]["gametype"] = "Vanilla"
            if settings_ins.has_option(f"{version}", "isshared") == False:
                settings_ins[f"{version}"]["isshared"] = "yes"
            if settings_ins.has_option(f"{version}", "isseparate") == False:
                settings_ins[f"{version}"]["isseparate"] = "yes"
            if settings_ins.has_option(f"{version}", "isoptifine") == False:
                settings_ins[f"{version}"]["isoptifine"] = "no"
            with open(
                f"{sciezkains}/{versionPath}/settings_ins.ini", "w"
            ) as configfile:
                settings_ins.write(configfile)

        # * play minecraft
        if var == 1:
            playVanilla(self, 1)
    else:
        self.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:70px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:80px;background-color: rgba(70,140,190,0.7);}"
        )
        self.ui.bn_play.setText(f"Launched")
        setCurrentDiscordRpc(f"Minecraft {version}", f"Playing as {username}")
        threading.Thread(
            name="t-PlayingCheck", target=lambda: playingcheck(self)
        ).start()
        version = minecraft_launcher_lib.utils.get_installed_versions(f"{versionPathh}")
        try:
            version = version[1]["id"]
        except Exception:
            version = version[0]["id"]
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, versionPathh, options
        )
        clearList(self)
        try:
            subprocess.call(minecraft_command)
        except Exception:
            self.errorexec(
                "Something weird occured with this instance. Please use repair button in instance settings",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )


class playServers:
    def __init__(self, selfui):
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        config_servers = configparser.ConfigParser()
        config_servers.read(f"{sciezkaver}/servers.ini")
        bufor = config["PROFILE"]["version"]
        forgeVersion = config_servers.get(f"{bufor}", "forgeVersion")
        if (
            path.exists(
                f"C:\\Users\\mwgoi\\AppData\\Roaming\\.mlauncher\\instances\\{bufor}"
            )
            == False
        ):
            playForge(selfui, 2)

        # CHECKING MODS
        self.checkmods(config, config_servers)
        selfui.ui.bn_play.setText("Launched")
        versionPath = f"C:\\Users\\mwgoi\\AppData\\Roaming\\.mlauncher\\instances\\{bufor}\\.minecraft"
        version = minecraft_launcher_lib.utils.get_installed_versions(f"{versionPath}")
        username = config.get("PROFILE", "username")
        token = config.get("PROFILE", "uuid")
        uuid = token.replace("-", "")
        allocatedram = config.get("SETTINGS", "allocatedram")
        specialarg = config.get("SETTINGS", "specialarg")
        jvmArguments = []
        jvmArguments.append(f"-Xmx{allocatedram}")
        options = {
            "username": username,
            "uuid": uuid,
            "token": token,
            "jvmArguments": jvmArguments,
            "executablePath": "C:\\Users\\mwgoi\\AppData\\Roaming/.mlauncher/jvms/jdk-17.0.2/bin/javaw.exe",
        }
        try:
            version = version[1]["id"]
        except Exception:
            version = version[0]["id"]
        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(
            version, versionPath, options
        )
        subprocess.call(minecraft_command)

    def checkmods(self, config, config_servers):
        version = config.get("PROFILE", "version")
        forgeVersion = config_servers.get(f"{version}", "forgeVersion")
        mods = config_servers.options(version)
        bufor = mods.index("mods")
        mods = mods[bufor + 1 :]
        versionPath = f"C:\\Users\\mwgoi\\AppData\\Roaming\\.mlauncher\\instances\\{version}\\.minecraft\\mods"
        if path.exists(versionPath) == False:
            os.mkdir(versionPath)
        localMods = [f for f in listdir(versionPath) if isfile(join(versionPath, f))]
        for i in localMods:
            if i not in mods:
                print("deleted ", i)
                os.remove(f"{versionPath}/{i}")
        for i in mods:
            if i not in localMods:
                url = config_servers.get(version, i)
                r = requests.get(url, stream=True)
                percentagebufor = 0
                with open(f"{versionPath}/{i}", "wb") as f:
                    total_length = int(r.headers.get("content-length")) or None
                    for chunk in progress.bar(
                        r.iter_content(chunk_size=1024),
                        expected_size=(total_length / 1024) + 1,
                    ):
                        if chunk:
                            f.write(chunk)
                            f.flush()


def playingcheck(self):
    global iterablebool
    time.sleep(20)
    while iterablebool > 0:
        buforplay = "javaw.exe" in (i.name() for i in psutil.process_iter())
        if buforplay == False:
            if self.ui.bn_play.text() != "Downloading":
                self.ui.bn_play.setText("Play")
            config = configparser.ConfigParser()
            config.read(f"{sciezkaver}/config.ini")
            username = config.get("PROFILE", "username")
            setCurrentDiscordRpc("Home Page", f"Playing as {username}")
            return
        time.sleep(10)


def downloadstuff(self):
    self.closebool = False
    progress = "DOWNLOADED"
    if path.exists(f"{sciezkains}/shared") == False:
        os.mkdir(f"{sciezkains}/shared")

    # * .MINECRAFT
    if (
        path.exists(f"{sciezkains}/shared/.minecraft.zip") == False
        or os.path.getsize(f"{sciezkains}/shared/.minecraft.zip") < 497370000
        or path.exists(f"{sciezkains}/shared/.minecraft") == False
    ):
        if path.exists(f"{sciezkains}/shared/.minecraft") == False:
            # * AHVE TO DOWNLOAD
            download(
                "https://www.dropbox.com/s/1f8ipykii17o2u4/.minecraft.zip?dl=1",
                f"{sciezkains}/shared/.minecraft.zip",
                self,
                30000,
            )
        if path.exists(f"{sciezkains}/shared/.minecraft.zip") == True:
            self.ui.lab_tab2.setText(f"UNZIPPING")
            with zipfile.ZipFile(f"{sciezkains}/shared/.minecraft.zip", "r") as zipObj:
                zipObj.extractall(f"{sciezkains}/shared/.minecraft")

    # * JAVA 1.8
    if path.exists(f"{sciezkajvms}/jre1.8.0_281") == False:
        if (
            path.exists(f"{sciezkajvms}/jvm1_8.zip") == False
            or os.path.getsize(f"{sciezkajvms}/jvm1_8.zip") < 78355000
        ):
            download(
                "https://www.dropbox.com/s/xji1r8xbvnsw9tq/jre1.8.0_281.zip?dl=1",
                f"{sciezkajvms}/jvm1_8.zip",
                self,
                0,
            )
        self.ui.lab_tab2.setText(f"UNZIPPING")
        with zipfile.ZipFile(f"{sciezkajvms}/jvm1_8.zip", "r") as zipObj:
            zipObj.extractall(f"{sciezkajvms}/")
        progress = "DOWNLOADED"

    # * JAVA 17
    if path.exists(f"{sciezkajvms}/jdk-17.0.2") == False:
        if (
            path.exists(f"{sciezkajvms}/jvm17.zip") == False
            or os.path.getsize(f"{sciezkajvms}/jvm17.zip") < 184262000
        ):
            download(
                "https://www.dropbox.com/s/8nviopyiwtj7mtb/jdk-17.0.2_windows-x64_bin.zip?dl=1",
                f"{sciezkajvms}/jvm17.zip",
                self,
                0,
            )
        self.ui.lab_tab2.setText(f"UNZIPPING")
        with zipfile.ZipFile(f"{sciezkajvms}/jvm17.zip", "r") as zipObj:
            zipObj.extractall(f"{sciezkajvms}/")
        progress = "DOWNLOADED"

    self.closebool = True
    self.ui.lab_tab2.setText(progress)
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")
    time.sleep(0.5)
    self.ui.lab_tab2.setText(progress)
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")
    time.sleep(0.5)
    self.ui.lab_tab2.setText(progress)
    time.sleep(1)
    self.ui.lab_tab2.setText(f"")


def newsScroll(self, var):
    index = self.ui.stackedWidget_2.currentIndex()
    if var == 1:
        if index == 4:
            self.ui.stackedWidget_2.setCurrentIndex(0)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(index + 1)
    else:
        if index == 0:
            self.ui.stackedWidget_2.setCurrentIndex(4)
        else:
            self.ui.stackedWidget_2.setCurrentIndex(index - 1)
    index = self.ui.stackedWidget_2.currentIndex()
    self.ui.news_index.setText(f"{index+1}/5")
    if index == 0:
        self.ui.news_latest.setText("Latest")
    else:
        self.ui.news_latest.setText("")


def newsOpen(self):
    global articleURL
    index = self.ui.stackedWidget_2.currentIndex()
    webbrowser.open(f"https://www.minecraft.net{articleURL[index]}")


def news(self):
    global articleURL
    try:
        bufor = minecraft_launcher_lib.utils.get_minecraft_news(5)
        bufor = bufor["article_grid"]
        title = [1, 2, 3, 4, 5]
        sub_title = [1, 2, 3, 4, 5]
        imageURL = [1, 2, 3, 4, 5]
        articleURL = [1, 2, 3, 4, 5]
        header = {"user-agent": f"launcher"}

        for i in range(5):
            number = bufor[i]
            default_tile = number["default_tile"]
            title[i] = default_tile["title"]
            sub_title[i] = default_tile["sub_header"]
            image_buf = default_tile["image"]
            imageURL[i] = image_buf["imageURL"]
            articleURL[i] = number["article_url"]

            img_data = requests.get(
                f"https://www.minecraft.net{imageURL[i]}", headers=header
            ).content
            with open(f"{sciezka}/cache/img/{i}.png", "wb") as handler:
                handler.write(img_data)

        self.ui.news_1.setText(title[0])
        self.ui.news_2.setText(title[1])
        self.ui.news_3.setText(title[2])
        self.ui.news_4.setText(title[3])
        self.ui.news_5.setText(title[4])
        self.ui.news_1_2.setText(sub_title[0])
        self.ui.news_2_2.setText(sub_title[1])
        self.ui.news_3_2.setText(sub_title[2])
        self.ui.news_4_2.setText(sub_title[3])
        self.ui.news_5_2.setText(sub_title[4])

        img = QtGui.QPixmap(f"{sciezka}/cache/img/0.png")
        img = img.scaled(225, 225)
        lbl = QLabel(self)
        lbl.setPixmap(img)
        lbl.mousePressEvent = lambda x: newsOpen(self)
        self.ui.verticalLayout_28.addWidget(lbl)
        #############
        img = QtGui.QPixmap(f"{sciezka}/cache/img/1.png")
        img = img.scaled(225, 225)
        lbl = QLabel(self)
        lbl.setPixmap(img)
        lbl.mousePressEvent = lambda x: newsOpen(self)
        self.ui.verticalLayout_29.addWidget(lbl)
        #############
        img = QtGui.QPixmap(f"{sciezka}/cache/img/2.png")
        img = img.scaled(225, 225)
        lbl = QLabel(self)
        lbl.setPixmap(img)
        lbl.mousePressEvent = lambda x: newsOpen(self)
        self.ui.verticalLayout_30.addWidget(lbl)
        #############
        img = QtGui.QPixmap(f"{sciezka}/cache/img/3.png")
        img = img.scaled(225, 225)
        lbl = QLabel(self)
        lbl.setPixmap(img)
        lbl.mousePressEvent = lambda x: newsOpen(self)
        self.ui.verticalLayout_31.addWidget(lbl)
        #############
        img = QtGui.QPixmap(f"{sciezka}/cache/img/4.png")
        img = img.scaled(225, 225)
        lbl = QLabel(self)
        lbl.setPixmap(img)
        lbl.mousePressEvent = lambda x: newsOpen(self)
        self.ui.verticalLayout_32.addWidget(lbl)
    except Exception:
        self.ui.news_1.setText("No information from server")
        self.ui.news_2.setText("No information from server")
        self.ui.news_3.setText("No information from server")
        self.ui.news_4.setText("No information from server")
        self.ui.news_5.setText("No information from server")
        self.ui.news_1_2.setText("")
        self.ui.news_2_2.setText("")
        self.ui.news_3_2.setText("")
        self.ui.news_4_2.setText("")
        self.ui.news_5_2.setText("")


# * INSTANCE SETTINGS
class instancesettings:
    def __init__(self, selfui):
        config = configparser.ConfigParser()
        config.read(f"{sciezkaver}/config.ini")
        global deleteInstance
        deleteInstance = False
        bufor = (
            selfui.ui.label_13.text()
            .replace("release", "")
            .replace("snapshot", "")
            .replace("<-- local installed", "")
            .replace("local", "")
            .replace("Current Version:", "")
            .replace(" ", "")
        )
        if config.get("PROFILE", "gameversion") == "Forge Versions":
            bufor = "f-" + bufor

        selfui.ui.label_16.setText(bufor)

        # * Change lineedit visibility
        """not_resize = selfui.ui.bug_line_customname.sizePolicy()
        not_resize.setRetainSizeWhenHidden(True)
        selfui.ui.bug_line_customname.setSizePolicy(not_resize)"""

        # * BUTTONS

        pathExist = path.exists(f"{sciezkains}/{bufor}")
        # * bug_openfolder
        if pathExist == False:
            selfui.ui.bug_openfolder.setText(
                "Can't open instance folder, because instance is not installed"
            )
            selfui.ui.bug_openfolder.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
            )
        else:
            try:
                selfui.ui.bug_openfolder.clicked.disconnect()
            except Exception:
                pass
            selfui.ui.bug_openfolder.clicked.connect(
                lambda: self.openFolder(bufor, selfui)
            )
            selfui.ui.bug_openfolder.setText("Open folder")
            selfui.ui.bug_openfolder.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(100,180,100);}"
            )

        # * bug_repair
        if pathExist == False:
            selfui.ui.bug_repair.setText(
                "Can't repair this instance, because instance is not installed"
            )
            selfui.ui.bug_repair.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
            )
        else:
            try:
                selfui.ui.bug_repair.clicked.disconnect()
            except Exception:
                pass
            selfui.ui.bug_repair.clicked.connect(
                lambda: threading.Thread(
                    name="t-RepairInstance",
                    target=lambda: self.repairInstance(bufor, selfui),
                ).start()
            )
            selfui.ui.bug_repair.setText("Repair Instance")
            selfui.ui.bug_repair.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(100,180,100);}"
            )

        # * bug_bn_delete
        if pathExist == True:
            selfui.ui.bug_bn_delete.setEnabled(True)
            try:
                selfui.ui.bug_bn_delete.clicked.disconnect()
            except Exception:
                pass
            selfui.ui.bug_bn_delete.clicked.connect(
                lambda: self.bnDelete(bufor, selfui)
            )
            selfui.ui.bug_bn_delete.setText("Delete Instance")
        else:
            selfui.ui.bug_bn_delete.setEnabled(False)
            selfui.ui.bug_bn_delete.setText(
                "Can't delete bacause instance is not found"
            )
        try:
            selfui.ui.bug_optifine.clicked.disconnect()
        except Exception:
            pass
        if pathExist == True:
            settings_ins = configparser.ConfigParser()
            settings_ins.read(f"{sciezkains}/{bufor}/settings_ins.ini")
            if (
                path.exists(f"{sciezkains}/{bufor}/settings_ins.ini") == False
                or settings_ins.has_section(f"{bufor}") == False
                or settings_ins.has_option(f"{bufor}", "isshared") == False
                or settings_ins.has_option(f"{bufor}", "isseparate") == False
                or settings_ins.has_option(f"{bufor}", "isoptifine") == False
            ):
                if settings_ins.has_section(f"{bufor}") == False:
                    settings_ins.add_section(f"{bufor}")
                if settings_ins.has_option(f"{bufor}", "isshared") == False:
                    settings_ins[f"{bufor}"]["isshared"] = "no"
                if settings_ins.has_option(f"{bufor}", "isseparate") == False:
                    settings_ins[f"{bufor}"]["isseparate"] = "yes"
                if settings_ins.has_option(f"{bufor}", "isoptifine") == False:
                    settings_ins[f"{bufor}"]["isoptifine"] = "no"
                with open(f"{sciezkains}/{bufor}/settings_ins.ini", "w") as configfile:
                    settings_ins.write(configfile)
            isshared = settings_ins.get(f"{bufor}", "isshared")
            isseparate = settings_ins.get(f"{bufor}", "isseparate")
            isoptifine = settings_ins.get(f"{bufor}", "isoptifine")

            # * SAVES
            try:
                selfui.ui.bug_sharedsaves.clicked.disconnect()
            except Exception:
                pass
            selfui.ui.bug_sharedsaves.clicked.connect(
                lambda: self.sharedSaves(bufor, selfui)
            )

            if isshared == "yes":
                selfui.ui.label_19.setText("Save Shared")
                selfui.ui.bug_sharedsaves.setText("Split saves")
                selfui.ui.bug_sharedsaves.setStyleSheet(
                    "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
                )
            else:
                selfui.ui.label_19.setText("Save Not Shared")
                selfui.ui.bug_sharedsaves.setText("Connect saves")

            # * Optifine

            versionOptifine = minecraft_launcher_lib.utils.get_installed_versions(
                f"{sciezkains}/{bufor}/.minecraft"
            )
            for i in range(len(versionOptifine)):
                if (versionOptifine[i]["id"]).lower().find("optifine") != -1:
                    selfui.ui.label_17.setText("Optifine Installed")
                    selfui.ui.bug_optifine.setText("Uninstall Optifine")
                    selfui.ui.bug_optifine.setStyleSheet(
                        "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
                    )
                    selfui.ui.bug_optifine.clicked.connect(
                        lambda: self.bnOptifine(selfui, bufor)
                    )
                else:
                    selfui.ui.label_17.setText("Optifine Not Installed")
                    selfui.ui.bug_optifine.setText("Install Optifine")
                    if bufor.startswith("f"):
                        selfui.ui.webWidget_optifine.hide()
                        buforr = bufor.replace("f-", "").split("-")
                        selfui.ui.label_26.setText(
                            f"Download {buforr[0]} version and paste optifine file (.jar) into that path"
                        )
                        selfui.ui.label_25.setText(
                            f"{sciezkains}/{bufor}/.minecraft/mods".replace("/", "\\")
                        )
                    else:
                        selfui.ui.webWidget_optifine.show()
                        selfui.ui.label_26.setText(
                            "Copy and paste that path in optifine"
                        )
                        selfui.ui.label_25.setText(
                            f"{sciezkains}/{bufor}/.minecraft".replace("/", "\\")
                        )
                    selfui.ui.bug_optifine.clicked.connect(
                        lambda: selfui.ui.stackedWidget.setCurrentWidget(
                            selfui.ui.page_optifine
                        )
                    )

            """
            if isoptifine == "yes":
                selfui.ui.label_17.setText("Optifine Installed")
                selfui.ui.bug_optifine.setText("Uninstall Optifine")
                selfui.ui.bug_optifine.setStyleSheet(
                    "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
                )
            else:
                selfui.ui.label_17.setText("Optifine Not Installed")
                selfui.ui.bug_optifine.setText("Install Optifine")"""

    def sharedSaves(self, version, selfui):
        buforinstance = f"{sciezkains}/{version}/.minecraft"
        settings_ins = configparser.ConfigParser()
        settings_ins.read(f"{sciezkains}/{version}/settings_ins.ini")
        isshared = settings_ins.get(f"{version}", "isshared")
        if isshared == "yes":
            try:
                os.remove(f"{buforinstance}/saves")
            except Exception:
                shutil.rmtree(f"{buforinstance}/saves")
            os.mkdir(f"{buforinstance}/saves")
            selfui.ui.label_19.setText("Save Not Shared")
            selfui.ui.bug_sharedsaves.setText("Connect saves")
            settings_ins[f"{version}"]["isshared"] = "no"
        else:
            onlyfiles = [
                f
                for f in listdir(f"{buforinstance}/saves")
                if isfile(join(f"{buforinstance}/saves", f))
            ]
            for i in onlyfiles:
                print(i)
                shutil.move(
                    f"{sciezkains}/{version}/.minecraft/saves/{i}",
                    f"{sciezka}/minecraft-folders/saves/{i}",
                )
            try:
                os.remove(f"{buforinstance}/saves")
            except Exception:
                shutil.rmtree(f"{buforinstance}/saves")
            print("asdd")
            subprocess.check_call(
                'mklink /J "%s" "%s"'
                % (
                    f"{sciezkains}/{version}/.minecraft/saves",
                    f"{sciezka}/minecraft-folders/saves",
                ),
                shell=True,
            )
            selfui.ui.label_19.setText("Save Shared")
            selfui.ui.bug_sharedsaves.setText("Split saves")
            selfui.ui.bug_sharedsaves.setStyleSheet(
                "QPushButton {\nborder: none;background-color: rgb(50,150,50);}QPushButton:hover {background-color: rgb(255,50,50);}"
            )
            settings_ins[f"{version}"]["isshared"] = "yes"

        with open(f"{sciezkains}/{version}/settings_ins.ini", "w") as configfile:
            settings_ins.write(configfile)

    def openFolder(self, version, selfui):
        buforinstance = f"{sciezkains}/{version}/.minecraft"
        buforinstance = r'explorer /select,"{}"'.format(buforinstance).replace(
            "/", "\\"
        )
        subprocess.Popen(buforinstance)

    def bnDelete(self, version, selfui):
        global deleteInstance
        if deleteInstance == False:
            deleteInstance = True
            selfui.errorexec(
                "Saved instance will be deleted, If you want it, click one more time on delete button",
                "icons/1x/errorAsset 55.png",
                "Ok",
            )
        else:
            deleteInstance = False
            shutil.rmtree(f"{sciezkains}/{version}")
            instancesettings(selfui)

    def repairInstance(self, version, selfui):
        selfui.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:55px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:65px;background-color: rgba(70,140,190,0.7);}"
        )
        selfui.ui.bn_play.setText(f"Downloading")
        buforinstance = f"{sciezkains}/{version}/.minecraft"
        max_value = [0]

        callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: ProgressBarMc(value, max_value[0], selfui),
            "setMax": lambda value: ProgressBarMcMaximum(max_value, value),
        }
        threading.Thread(
            name="t-DownloadingCount", target=lambda: downloadingCount(selfui)
        ).start()
        if version.startswith("f-"):
            version = version.replace("f-", "")
            # versionPathh = buforinstance.replace("/", "\\")
            install_forge_version(version, buforinstance, callback=callback)
        elif version.startswith("s_"):
            config_servers = configparser.ConfigParser()
            config_servers.read(f"{sciezkaver}/servers.ini")
            buforinstance = f"{sciezkains}/{version}/.minecraft"
            version = config_servers.get(f"{version}", "forgeVersion")
            install_forge_version(version, buforinstance, callback=callback)
        else:
            minecraft_launcher_lib.install.install_minecraft_version(
                version, buforinstance, callback=callback
            )
        selfui.ui.bn_play.setStyleSheet(
            "QPushButton {font-size:80px;background-color: rgba(30,100,140,0.7);border-radius: 10px;}QPushButton:hover {font-size:90px;background-color: rgba(70,140,190,0.7);}"
        )
        selfui.ui.bn_play.setText(f"Play")

    def bnOptifine(self, selfui, version):
        versionOptifine = minecraft_launcher_lib.utils.get_installed_versions(
            f"{sciezkains}/{version}/.minecraft"
        )
        for i in range(len(versionOptifine)):
            if (versionOptifine[i]["id"]).lower().find("optifine") != -1:
                bufor = versionOptifine[i]["id"]
                shutil.rmtree(f"{sciezkains}/{version}/.minecraft/versions/{bufor}")
                selfui.ui.label_17.setText("Optifine Not Installed")
                selfui.ui.bug_optifine.setText("Install Optifine")


class forge_mods:
    def __init__(self, selfui):
        forge_installed = []
        for i in range(len(ForgeVersionss)):
            if ForgeVersionss[i] in buforlist:
                forge_installed.append(ForgeVersionss[i])
        selfui.ui.comboBox_2.clear()
        if not forge_installed:
            selfui.ui.comboBox_2.addItem("No forge version installed")
        else:
            selfui.ui.comboBox_2.addItems(forge_installed)
        bufor = [
            name
            for name in os.listdir(f"{sciezka}/instances")
            if os.path.isdir(os.path.join(f"{sciezka}/instances", name))
        ]
        for i in range(int(len(bufor))):
            if path.exists(f"{sciezka}/instances/{bufor[i]}/.minecraft") == True:
                buforr = bufor[i].replace("f-", "")
                buforlist.append(buforr)

    def set_mod(self):
        bufor = self.ui.comboBox_2.currentText()
        if bufor == "No forge version installed":
            return
        self.ui.label_20.setText(self.ui.comboBox_2.currentText())
        forge_mods.reload_mods(self)

    def reload_mods(self):
        bufor = self.ui.label_20.text()
        onlyfiles = [
            f
            for f in listdir(f"{sciezka}/instances/{'f-'+bufor}/.minecraft/mods")
            if isfile(join(f"{sciezka}/instances/{'f-'+bufor}/.minecraft/mods", f))
        ]
        self.ui.comboBox_3.clear()
        if onlyfiles:
            self.ui.comboBox_3.addItems(onlyfiles)
        else:
            self.ui.comboBox_3.addItem("No mods")

    def delete_mod(self):
        bufor = self.ui.label_20.text()
        if not bufor:
            return
        bufor_mod = self.ui.comboBox_3.currentText()
        if bufor_mod != "No mods":
            os.remove(f"{sciezka}/instances/{'f-'+bufor}/.minecraft/mods/{bufor_mod}")
            index = self.ui.comboBox_3.findText(bufor_mod)
            self.ui.comboBox_3.removeItem(index)

    def openFolder(selfui):
        bufor = selfui.ui.label_20.text()
        if bufor != "":
            buforinstance = f"{sciezka}/instances/{'f-'+bufor}/.minecraft/mods"
            buforinstance = r'explorer /select,"{}"'.format(buforinstance).replace(
                "/", "\\"
            )
            subprocess.Popen(buforinstance)
            selfui.ui.bn_mod_openFolder.setText("Open mods folder")
        else:
            selfui.ui.bn_mod_openFolder.setText("Open mods folder (SELECT VERSION)")
