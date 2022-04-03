import datetime
from os import path
import os
import sys
import re
import brain
import threading

import requests
#from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()


roaming = os.getenv("APPDATA")
sciezka = f"{roaming}/.mlauncher"
sciezkaver = f"{sciezka}/bin"
sciezkains = f"{sciezka}/instances"


DOMAIN = "https://www.curseforge.com"
URL = "https://www.curseforge.com/minecraft/mc-mods"
URL2 = ""
VERSION = ""
MOD_NAME = ""
FORGEVERSION = ""
game_version = [
    "1.13.2",  #! 1.13
    "1.14.2",  #! 1.14
    "1.14.3",
    "1.14.4",
    "1.15",  #! 1.15
    "1.15.1",
    "1.15.2",
    "1.16.1",  #! 1.16
    "1.16.2",
    "1.16.3",
    "1.16.4",
    "1.16.5",
    "1.17.1",  #! 1.17
    "1.18",  #! 1.18
    "1.18.1",
]
game_version2 = [
    "2020709689%3A7132",  #! 1.13
    "2020709689%3A7361",  #! 1.14
    "2020709689%3A7413",
    "2020709689%3A7469",
    "2020709689%3A7664",  #! 1.15
    "2020709689%3A7675",
    "2020709689%3A7722",
    "2020709689%3A7892",  #! 1.16
    "2020709689%3A8010",
    "2020709689%3A8056",
    "2020709689%3A8134",
    "2020709689%3A8203",
    "2020709689%3A8516",  #! 1.17
    "2020709689%3A8830",  #! 1.18
    "2020709689%3A8857",
]


def down_mod(self):
    bufor = self.ui.label_20.text()
    if not bufor:
        return
    threading.Thread(target=download_mod(self)).start()


def download_mod(self):
    options = webdriver.ChromeOptions()
    options.use_chromium = True
    options.add_argument("window-size=1,1")
    options.add_argument("disable-gpu")
    options.add_argument("--safebrowsing-disable-download-protection")
    options.add_argument("log-level=3")
    options.add_experimental_option("prefs", {"safebrowsing.enabled": "false"})
    browser = webdriver.Chrome(options=options)
    browser.set_window_position(-10000, 0)

    URL = self.ui.line_mod_name.text()
    FORGEVERSION = self.ui.label_20.text()
    MC_PATH = f"{sciezkains}/f-{FORGEVERSION}/.minecraft/mods"
    VERSION = self.ui.line_mod_version.text()
    FORGEVERSION = FORGEVERSION.split("-")
    FORGEVERSION = FORGEVERSION[0]
    print(FORGEVERSION)
    if FORGEVERSION in game_version:
        bufor = game_version.index(FORGEVERSION)
        FORGEVERSION = game_version2[bufor]
    else:
        return 0
    if "curseforge" in URL:
        MOD_NAME = URL.split("/")
        MOD_NAME = MOD_NAME[5]
        MOD_NAME = MOD_NAME.lower()
        URL2 = f"https://www.curseforge.com/minecraft/mc-mods/{MOD_NAME}/files/all?filter-game-version={FORGEVERSION}"
    else:
        '''bufor = re.sub(r"[^a-zA-Z0-9]+", " ", URL)
        print(bufor)
        a = browser.get(
            f"https://www.curseforge.com/minecraft/mc-mods/search?search={bufor}"
        )
        try:
            search = browser.find_element(By.PARTIAL_LINK_TEXT, URL).get_attribute(
                "href"
            )
        except NoSuchElementException:
            print("Nie znaleziono moda")
        MOD_NAME = search.split("/")
        MOD_NAME = MOD_NAME[5]
        MOD_NAME = MOD_NAME.lower()
        URL2 = f"{search}/files/all?filter-game-version={FORGEVERSION}"'''
        MOD_NAME = URL.lower()
        URL2 = f"https://www.curseforge.com/minecraft/mc-mods/{MOD_NAME}/files/all?filter-game-version={FORGEVERSION}"
    print(URL2)
    a = browser.get(URL2)
    if VERSION != "":
        search = browser.find_element(By.PARTIAL_LINK_TEXT, VERSION).get_attribute(
            "href"
        )
    else:
        search = browser.find_element(By.TAG_NAME, "tr")
        # search[0]
    mod_id = (
        (str(search).replace("https://", ""))
        .replace("www.curseforge.com", "")
        .replace("minecraft", "")
        .replace("/", "")
        .replace("mc-mods", "")
        .replace("download", "")
        .replace(MOD_NAME, "")
        .replace("files", "")
    )
    print(mod_id)
    browser.get(
        f"https://www.curseforge.com/minecraft/mc-mods/{MOD_NAME}/files/{mod_id}"
    )
    mod_id2 = browser.find_element(By.XPATH, "//span[@class='text-sm']").text
    print(mod_id2)
    mod_id = list(mod_id)
    r = requests.get(
        f"https://media.forgecdn.net/files/{mod_id[0]}{mod_id[1]}{mod_id[2]}{mod_id[3]}/{mod_id[4]}{mod_id[5]}{mod_id[6]}/{mod_id2}"
    )
    open(f"{MC_PATH}/{VERSION}.jar", "wb").write(r.content)
    brain.forge_mods.reload_mods(self)


"""https://media.forgecdn.net/files/3419/412/create-mc1.16.5_v0.3.2d.jar
https://www.curseforge.com/minecraft/mc-mods/create/download/3419412"""


#             Create 1.16.5 v0.3.2d
#             appleskin-forge-mc1.16.x-2.1.0.jar

# time.sleep(50)
