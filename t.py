import sys
import time
import threading

from PySide2.QtCore import Qt, Signal, Slot
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QWidget


class MainWindow(QMainWindow):
    valueChanged = Signal(int)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(320, 100)
        self.setWindowTitle("aaaa")
        self.setStyleSheet(
            """
            QMainWindow
            {
                background-color:white;
                color:white;
                margin:0px
            }
            """
        )
        self.InitializeWindow()
        self.i = 0

        self.valueChanged.connect(self.bind)

    def InitializeWindow(self):
        self.statebar = QWidget(self)
        self.statebar.setGeometry(0, 40, 320, 54)
        print(sys._getframe().f_lineno)
        self.statebar.setStyleSheet("QWidget{background-color:#1EC5CD}")
        self.th_countdown = threading.Thread(target=self.countdown)
        self.th_countdown.setDaemon(True)
        self.th_countdown.start()

        self.message_main = QLabel(self.statebar)
        self.message_main.setGeometry(150, 7, 40, 37)
        self.message_main.setStyleSheet(
            "background:transparent;color:white;margin:0px;font-size:45px;font-weight:bold"
        )
        self.message_main.setWordWrap(True)
        self.message_main.hide()
        self.message_main.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.message_signature = QLabel(self.statebar)
        self.message_signature.setGeometry(50, 6, 42, 42)
        self.message_signature.setScaledContents(True)
        self.message_signature.setStyleSheet("background:transparent")

        self.message_result = QLabel(self.statebar)
        self.message_result.setGeometry(150, 6, 160, 25)
        self.message_result.setStyleSheet(
            "background:transparent;color:white;margin:0px;font-size:24px;font-weight:bold"
        )
        self.message_result.setWordWrap(True)
        self.message_result.hide()
        self.message_detail = QLabel(self.statebar)
        self.message_detail.setGeometry(150, 34, 160, 15)
        self.message_detail.setStyleSheet(
            "background:transparent;color:white;margin:0px;font-size:14px"
        )
        self.message_detail.setWordWrap(True)
        self.message_detail.hide()

    @Slot(int)
    def bind(self, ret):
        self.message_result.show()
        self.message_detail.show()
        self.message_main.hide()
        qss = "QWidget{background-color:%s}" % (
            "#1EC5CD" if ret % 2 == 0 else "#FA6400"
        )
        self.statebar.setStyleSheet(qss)
        self.message_result.setNum(ret)
        self.message_detail.setNum(ret)

    def countdown(self):
        while True:
            time.sleep(0.2)
            self.i += 1
            self.valueChanged.emit(self.i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())