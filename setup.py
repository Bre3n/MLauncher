def downloader(url, path, var):
    if var == 1:
        resp = requests.get(url, stream=True)
        total = int(resp.headers.get("content-length", 0))
        with open(path, "wb") as file, tqdm(
            desc=path,
            total=total,
            unit="iB",
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
    else:
        with open(path, "wb") as f:
            response = requests.get(url, stream=True)
            total = response.headers.get("content-length")

            if total is None:
                f.write(response.content)
            else:
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    f.write(data)


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
        print(
            f"Cannot asing more ram than {bufor}MB (80% of amount of available RAM ({size}) )"
        )
        exit()


def pliki(sciezka):
    i = 1
    pathh = f"{sciezka}/logs-setup"

    # * CONFIG
    config.read(f"{sciezka}/config.ini")
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
    if config.has_option("PROFILE", "uuid") == False:
        data = requests.get("https://www.uuidtools.com/api/generate/v4/count/1").json()
        config["PROFILE"]["uuid"] = data[0]
    if config.has_option("PROFILE", "username") == False:
        config["PROFILE"]["username"] = "Steve"
    ALLOCATEDRAM = config.get("SETTINGS", "AllocatedRam")
    if ALLOCATEDRAM[-1] == "G":
        ALLOCATEDRAM = str(int(ALLOCATEDRAM.replace("G", "")) * 1024) + "M"
        config["SETTINGS"]["AllocatedRam"] = ALLOCATEDRAM
    with open(f"{sciezka}/config.ini", "w") as configfile:
        config.write(configfile)

    # * LOGS

    if path.exists(pathh) == False:
        os.mkdir(pathh)
    if path.exists(f"{pathh}/SORT_BY_MODIFICATION_TIME.txt") == False:
        f = open(f"{pathh}/SORT_BY_MODIFICATION_TIME.txt", "w")
        f.write("")
        f.close()
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
    from os import path

    try:
        import configparser
        import zipfile
        import psutil
        import coloredlogs
        import PySide2
        import requests
        from tqdm import tqdm
    except ImportError:
        os.system(f"pip install doctext")
        os.system(f"pip install requests")
        os.system(f"pip install PySide2")
        os.system(f"pip install zipfile")
        os.system(f"pip install coloredlogs")
        os.system(f"pip install configparser")
        os.system(f"pip install tqdm")
        os.system(f"pip install psutil")
        os.execv(sys.executable, ["python"] + sys.argv)

    config = configparser.ConfigParser()

    os.system("cls")

    now_date = str(datetime.date.today())
    user = os.getlogin()
    buffor = False
    sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
    temp = f"C:/Users/{user}/AppData/Local/Temp"

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

    downloader(
        "https://raw.githubusercontent.com/Bre3n/MLauncher/master/files/links.txt",
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
            print(int(len(content) / 2))
            print(int(len(contentv)))
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
                    with zipfile.ZipFile(f"{sciezkaver}/{bufor[0]}", "r") as zipObj:
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
                    with zipfile.ZipFile(f"{sciezkaver}/{buforr}", "r") as zipObj:
                        zipObj.extractall(f"{sciezkaver}/{checkzip[0]}")
                    os.remove(f"{sciezkaver}/{buforr}")
        logger.debug(f"DEBUG: Program process complete")
        os.chdir(f"{sciezkaver}/")
        subprocess.call(["python", f"{sciezkaver}/main.py"])
