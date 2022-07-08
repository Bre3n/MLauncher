filelink = "https://raw.githubusercontent.com/Bre3n/MLauncher/master/files/links.txt"


def downloader(url, path, var):
    r = requests.get(url, stream=True)
    if var == 1:
        with open(path, "wb") as f:
            total_length = int(r.headers.get("content-length"))
            for chunk in progress.bar(
                r.iter_content(chunk_size=1024), expected_size=(total_length / 1024) + 1
            ):
                if chunk:
                    f.write(chunk)
                    f.flush()
    else:
        with open(path, "wb") as f:
            total = r.headers.get("content-length")

            if total is None:
                f.write(r.content)
            else:
                total = int(total)
                for data in r.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    f.write(data)


def pliki(sciezka):
    i = 0
    pathh = f"{sciezka}/logs-setup"

    # * LOGS
    if path.exists(pathh) == False:
        os.mkdir(pathh)
    if path.exists(f"{pathh}/.SORT_BY_MODIFICATION_TIME.txt") == False:
        open(f"{pathh}/.SORT_BY_MODIFICATION_TIME.txt", "w").close()
    if path.exists(f"{pathh}/{now_date}-9.log") == True:
        os.remove(f"{pathh}/{now_date}-9.log")
    if path.exists(f"{pathh}/{now_date}.log") == True:
        while path.exists(f"{pathh}/{now_date}-{i}.log") == True:
            i = i + 1
        os.rename(f"{pathh}/{now_date}.log", f"{pathh}/{now_date}-{i}.log")
    else:
        if path.exists(f"{pathh}/latest.log") == True:
            os.rename(
                f"{pathh}/latest.log",
                f"{pathh}/{now_date}.log",
            )


if __name__ == "__main__":
    import datetime
    import logging
    import os
    import subprocess
    import sys
    import time
    import math
    from os import path

    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.withdraw()

    try:
        from configparser import ConfigParser
        from zipfile import ZipFile
        import psutil
        import coloredlogs
        import PySide2
        import requests
        from clint.textui import progress
        import pypresence
        import winshell
        import pythoncom
        import win32com.client
        #import selenium
        #import chromedriver_autoinstaller
    except ImportError:
        os.system(f"pip install doctext -U")
        os.system(f"pip install requests -U")
        os.system(f"pip install PySide2 -U")
        os.system(f"pip install zipfile -U")
        os.system(f"pip install coloredlogs -U")
        os.system(f"pip install configparser -U")
        os.system(f"pip install clint -U")
        os.system(f"pip install psutil -U")
        os.system(f"pip install pypresence -U")
        os.system(f"pip install winshell -U")
        os.system(f"pip install pywin32 -U")
        os.system(f"pip install selenium -U")
        # os.system(f"pip install edgedriver-autoinstaller -U")
        os.system(f"pip install chromedriver_autoinstaller -U")
        os.execv(sys.executable, ["python"] + sys.argv)

    os.system(f"pip install minecraft-launcher-lib -U")

    config = ConfigParser()

    os.system("cls")

    now_date = str(datetime.date.today())
    buffor = False
    user = os.getlogin()
    roaming = os.getenv("APPDATA")
    sciezka = f"{roaming}/.mlauncher"

    sciezkaver = f"{sciezka}/bin"
    txtFile = f"{sciezkaver}/ver.txt"
    if path.exists(sciezka) == False:
        os.mkdir(sciezka)
    if path.exists(f"{sciezka}/bin") == False:
        os.mkdir(f"{sciezka}/bin")

    pliki(sciezkaver)
    logging.Formatter(fmt="%(asctime)s.%(msecs)03d", datefmt="%Y-%m-%d,%H:%M:%S")
    logging.basicConfig(
        filename=f"{sciezkaver}/logs-setup/latest.log",
        format="%(asctime)s %(message)s",
        filemode="w",
    )
    logger = logging.getLogger(__name__)
    coloredlogs.install(level="DEBUG", logger=logger)

    logger.debug(f"DEBUG: Starting")
    try:
        downloader(
            filelink,
            txtFile,
            0,
        )

        logger.debug(f"DEBUG: Downloaded version file")
        with open(txtFile) as f:
            content = f.readlines()
            content = [x.strip() for x in content]
        os.remove(f"{sciezkaver}/ver.txt")

        if path.exists(f"{sciezkaver}/version.txt") == False:
            f = open(f"{sciezkaver}/version.txt", "w")
            for i in range(int(len(content) / 2)):
                f.write(f"{content[i]}\n")
            f.close()
            logger.info(f"INFO: Version file didn't exist")
            logger.warning(f"WARNING: Restarting!")
            os.execv(sys.executable, ["python"] + sys.argv)
        else:
            logger.debug(f"DEBUG: Starting version comparing")
            with open(f"{sciezkaver}/version.txt") as f:
                contentv = f.readlines()
                contentv = [x.strip() for x in contentv]
            if int(len(content) / 2) != int(len(contentv)):
                logger.critical(f"CRITICAL: FILES DON'T HAVE SAME NUMER OF LINES!")
                logger.debug(f"DEBUG: Overwritting wrong file with 'None' lines")
                f = open(f"{sciezkaver}/version.txt", "w")
                for i in range(int(len(content) / 2)):
                    f.write("None\n")
            with open(f"{sciezkaver}/version.txt") as f:
                contentv = f.readlines()
                contentv = [x.strip() for x in contentv]
            for i in range(int(len(content) / 2)):
                if content[i] != contentv[i]:
                    logger.warning(
                        f"WARNING: Lines didn't match   {content[i]}!={contentv[i]}"
                    )
                    bufor = content[i].replace(" ", "")
                    bufor = bufor.split("==")
                    checkzip = bufor[0].split(".")
                    logger.debug(f"DEBUG: Downloading   {bufor[0]}")
                    downloader(
                        content[i + (int(len(content) / 2))],
                        f"{sciezkaver}/{bufor[0]}",
                        1,
                    )
                    print(" ")
                    logger.debug(f"DEBUG: Download complete")
                    if checkzip[1] == "zip":
                        logger.info(f"INFO: Detected zip file. Extractings")
                        with ZipFile(f"{sciezkaver}/{bufor[0]}", "r") as zipObj:
                            zipObj.extractall(f"{sciezkaver}/{checkzip[0]}")
                        os.remove(f"{sciezkaver}/{bufor[0]}")
            f = open(f"{sciezkaver}/version.txt", "w")
            for i in range(int(len(content) / 2)):
                f.write(f"{content[i]}\n")
            f.close()
            logger.debug(f"DEBUG: Overwritting old version file")
            logger.debug(f"DEBUG: Comparing files in directory")
            for i in range(int(len(content) / 2)):
                bufor = content[i].replace(" ", "")
                bufor = bufor.split("==")
                checkzip = bufor[0].split(".")
                buforr = bufor[0]
                if checkzip[1] == "zip":
                    bufor[0] = checkzip[0]
                if path.exists(f"{sciezkaver}/{bufor[0]}") == False:
                    logger.warning(
                        f"WARNING: There is no file named   {bufor[0]}   in directory"
                    )
                    logger.debug(f"DEBUG: Downloading   {bufor[0]}")
                    downloader(
                        content[i + (int(len(content) / 2))],
                        f"{sciezkaver}/{buforr}",
                        1,
                    )
                    print(" ")
                    logger.debug(f"DEBUG: Download complete")
                    if checkzip[1] == "zip":
                        logger.info(f"INFO: Detected zip file. Extracting")
                        with ZipFile(f"{sciezkaver}/{buforr}", "r") as zipObj:
                            zipObj.extractall(f"{sciezkaver}/{checkzip[0]}")
                        os.remove(f"{sciezkaver}/{buforr}")
            logger.debug(f"DEBUG: Program process complete")

            logging.shutdown()
            desktop = winshell.desktop()
            cwd = os.getcwd()
            if path.exists(f"{sciezka}/cache/setup.txt"):
                f = open(f"{sciezka}/cache/setup.txt", "r")
                bufor = f.read()
                bufor = bufor.replace("\\", "/")
                try:
                    os.remove(bufor)
                except Exception:
                    pass
                f.close()
                try:
                    os.remove(f"{sciezka}/cache/setup.txt")
                except Exception:
                    pass
            if (
                cwd != f"{roaming}\\.mlauncher\\bin"
                and cwd != f"C:\\Users\\{user}\\Desktop\\Projekty\\LauncherUi\\setup"
            ):
                if path.exists(f"{sciezka}/cache") == False:
                    os.mkdir(f"{sciezka}/cache")
                f = open(f"{sciezka}/cache/setup.txt", "w")
                f.write(f"{cwd}\setup.py")
                f.close()
            if path.exists(f"{desktop}/MLauncher.lnk") == False:
                if path.exists(f"{sciezka}/cache/shortcut.txt") == False:
                    path = os.path.join(desktop, "MLauncher.lnk")
                    target = f"{sciezkaver}\\setup.py"
                    icon = f"{sciezkaver}/icons/1x/icon.ico"
                    shell = win32com.client.Dispatch("WScript.Shell")
                    shortcut = shell.CreateShortCut(path)
                    shortcut.Targetpath = target
                    shortcut.IconLocation = icon
                    shortcut.save()
                    f = open(f"{sciezka}/cache/shortcut.txt", "w")
                    f.write("Shortcut created")
                    f.close()
            os.chdir(f"{sciezkaver}/")
    except ConnectionError:
        os.system("cls")
        logger.error(f"ERROR: Connection Error, can't check for updates")
        if path.exists(f"{sciezkaver}/main.py"):
            logger.debug(f"DEBUG: Starting offline mode in 3s")
            time.sleep(3)
            subprocess.call(["python", f'"{sciezkaver}/main.py"'])
        else:
            logger.critical(
                f"CRITICAL: Can't download required files, check your internet connection and try again"
            )
    if path.exists(f"{sciezkaver}/main.lnk"):
        os.system(f"{sciezkaver}/main.lnk")
    else:
        logger.critical(f"CRITICAL: Something weird occured, try again")
