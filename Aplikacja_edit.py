import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import Qt
from PySide6.QtCore import Slot
from PySide6 import QtCore
import subprocess
import time
import losowanie1

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.haslo = []
        self.email = []
        self.poprawne_dane = ['login@2008.pl', '12345']
        loader = QUiLoader()
        self.window = loader.load("aplickacja.ui", self)
        self.window.password_show.pressed.connect(self.buttons)
        self.window.password_show.released.connect(self.buttons2)
        self.window.zaloguj.pressed.connect(self.dane)
        time.sleep(0.3)
        self.window.zaloguj.pressed.connect(self.dane2)
        self.window.exit_btn.pressed.connect(QApplication.instance().quit)

        self.window.zaloguj.pressed.connect(self.otworz)
        self.window.setWindowFlag(Qt.FramelessWindowHint)
        self.window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.window.show()

    @Slot()
    def buttons(self):
        self.window.haslo.setEchoMode(QLineEdit.EchoMode.Normal)

    def buttons2(self):
        self.window.haslo.setEchoMode(QLineEdit.EchoMode.Password)

    def dane(self):
        self.email.append((self.window.email.text()))
        seperator = ""
        seperator.join(self.email)

    def dane2(self):
        self.haslo.append(self.window.haslo.text())
        seperator = ""
        seperator.join(self.haslo)
        print("Odczytuje dane...")

    def otworz(self):
        lista = self.email + self.haslo
        if self.poprawne_dane == lista:
            time.sleep(0.3)
            QApplication.instance().quit()
            print("Poprawnie zalogowano!")
            cmd = "python losowanie1.py"
            p = subprocess.Popen(cmd, shell=True)
            p.communicate()
        else:
            time.sleep(0.3)
            print("Zły e-mail lub hasło!")
            self.email.clear()
            self.haslo.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec())