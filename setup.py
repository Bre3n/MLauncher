def downloader(url, path, var):
    with open(path, "wb") as f:
        response = requests.get(url, stream=True)
        total = response.headers.get("content-length")

        if total is None:
            f.write(response.content)
        else:
            if var == 1:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    downloaded += len(data)
                    f.write(data)
                    done = int(50 * downloaded / total)
                    sys.stdout.write(
                        "\r[{}{}]{}{}".format(
                            "█" * done,
                            "." * (50 - done),
                            f" {round(100*downloaded/total)}%",
                            f" {round(downloaded/1000)}KB/{round(total/1000)}KB  ",
                        )
                    )
                    sys.stdout.flush()
            else:
                downloaded = 0
                total = int(total)
                for data in response.iter_content(
                    chunk_size=max(int(total / 1000), 1024 * 1024)
                ):
                    f.write(data)


def pliki(pathh):
    i = 1
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
    import os
    import subprocess
    import sys
    import time
    from os import path
    import datetime
    import logging

    try:
        import requests
        import PySide2
        import zipfile
        import coloredlogs
    except ImportError:
        os.system(f"pip install doctext")
        os.system(f"pip install requests")
        os.system(f"pip install PySide2")
        os.system(f"pip install zipfile")
        os.system(f"pip install coloredlogs")
        os.execv(sys.executable, ["python"] + sys.argv)

    os.system("cls")

    now_date = str(datetime.date.today())
    user = os.getlogin()
    buffor = False
    sciezka = f"C:/Users/{user}/AppData/Roaming/.mlauncher"
    temp = f"C:/Users/{user}/AppData/Local/Temp"

    sciezkaver = f"{sciezka}/bin"
    txtFile = f"{sciezkaver}/vers.txt"
    if path.exists(sciezka) == False:
        os.mkdir(sciezka)
    if path.exists(f"{sciezka}/bin") == False:
        os.mkdir(f"{sciezka}/bin")

    pliki(f"{sciezkaver}/logs-setup")
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
    f = open(txtFile, "r")
    line_count = 0
    for line in f:
        if line != "\n":
            line_count += 1
    with open(txtFile) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
    if path.exists(f"{sciezkaver}/ver.txt") == True:
        os.remove(f"{sciezkaver}/ver.txt")
    f = open(f"{sciezkaver}/ver.txt", "a")
    for i in range(len(content)):
        f.write(f"{content[i]}\n")
    f.close()
    os.remove(f"{sciezkaver}/vers.txt")

    if path.exists(f"{sciezkaver}/version.txt") == False:
        f = open(f"{sciezkaver}/version.txt", "w")
        for i in range(int(len(content)/2)):
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
        if int(len(content)/2) != int(len(contentv)/2):
            logger.critical(f"CRITICAL: FILES DON'T HAVE SAME NUMER OF LINES!")
            logger.debug(f"DEBUG: Overwritting wrong file with 'None' lines")
            f = open(f"{sciezkaver}/version.txt", "w")
            for i in range(int(len(content)/2)):
                f.write("None\n")
        with open(f"{sciezkaver}/version.txt") as f:
            contentv = f.readlines()
            contentv = [x.strip() for x in contentv]
        for i in range(int(len(content) / 2)):
            if content[i] != contentv[i]:
                logger.warning(
                    f"WARNING: Lines didn't match   {content[i]}!={contentv[i]}"
                )
                bufor = content[i]
                bufor = bufor.split("&")
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
        for i in range(len(content)):
            f.write(f"{content[i]}\n")
        f.close()
        logger.debug(f"DEBUG: Overwritting old version file")
        os.remove(f"{sciezkaver}/ver.txt")
        logger.debug(f"DEBUG: Comparing files in directory")
        for i in range(int(len(content) / 2)):
            bufor = content[i]
            bufor = bufor.split("&")
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
