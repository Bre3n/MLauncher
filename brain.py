import configparser
import os
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
        config["SETTINGS"]["allocatedram"]="2048M"
        config["SETTINGS"]["specialarg"]="False"
        config["SETTINGS"]["discordactivity"]="True"
        data = requests.get("https://www.uuidtools.com/api/generate/v4/count/1").json()
        config["PROFILE"]["uuid"] = data[0]
        config["PROFILE"]["username"]="Steve"
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
