from asyncio import MultiLoopChildWatcher
from calendar import monthcalendar
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
import selenium

# import chromedriver_autoinstaller
import configparser
import ctypes
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

import datetime
from os import path
import os
import sys
import re
import threading

import requests

# from msedge.selenium_tools import Edge, EdgeOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import chromedriver_autoinstaller