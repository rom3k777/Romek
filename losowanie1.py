# Importowanie bibliotek

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLineEdit, QLabel, QTextEdit, QMainWindow
from PySide6.QtGui import QCloseEvent, QPixmap, Qt, QIcon
from PySide6 import QtCore
import time
import random
class LoginWindow(QWidget):

    def __init__(self):
        self.liczba_osob = None
        self.osoby = []
        super().__init__()
        self.setup()

    def setup(self):

        # zdjecia (napisy)
        tlo = QLabel(self)
        tlo_jpg = QPixmap('Losowanie4').scaled(400, 600)
        tlo.setPixmap(tlo_jpg)
        tlo.move(0, 0)

        osoba = QLabel(self)
        osoba_jpg = QPixmap('losowanie2.png').scaled(350, 60)
        osoba.setPixmap(osoba_jpg)
        osoba.move(15, 180)

        witaj = QLabel(self)
        witaj_jpg = QPixmap('losowanie3.png').scaled(350, 100)
        witaj.setPixmap(witaj_jpg)
        witaj.move(30, 50)

        autor = QLabel(self)
        autor_jpg = QPixmap("autor.png").scaled(350, 95)
        autor.setPixmap(autor_jpg)
        autor.move(30, 475)

        # Odczytywanie imion
        self.liczba_osob = (QLineEdit(self))
        self.liczba_osob.setPlaceholderText("  Podaj Tutaj")
        self.liczba_osob.setStyleSheet("""
                    border: 2px solid rgb(34, 40, 49);
                    border-radius: 20px;
                    background-color: "#00ADB5";
                    color: "#222831";
                    font-family: "Pixel Emulator";
                    width: 200;
                    height: 40;
            """)
        self.liczba_osob.setFixedWidth(150)
        self.liczba_osob.move(15, 270)

        # przyciski
        clear_btn = QPushButton(self)
        clear_btn.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        clear_btn.setIcon(QIcon("clear.png"))
        clear_btn.setStyleSheet("""
                background-color: "transparent";
                width: 20;
                height: 20;
        """)
        clear_btn.pressed.connect(QApplication.instance().quit)
        clear_btn.move(363, 10)

        submit_btn = QPushButton("Losuj", self)
        submit_btn.setStyleSheet("""
        QPushButton {
                background-color: "#00ADB5";
                font-family: "Pixel Emulator";
                color: "#222831";
                border: 2px solid rgb(34, 40, 49);
                border-radius: 20px;
                width: 145;
                height: 40;
        }
        QPushButton:hover{
                background-color: "#222831";
                font-family: "Pixel Emulator";
                color: "#00ADB5";
                border: 2px solid rgb(0, 173, 181);
                border-radius: 20px;
                width: 145;
                height: 40;
        }
            """)
        submit_btn.move(115, 330)
        submit_btn.clicked.connect(self.informativeText)

        kolejny_btn = QPushButton("Dodaj kolejna osobe", self)
        kolejny_btn.setStyleSheet("""
        QPushButton {
                background-color: "#00ADB5";
                font-family: "Pixel Emulator";
                color: "#222831";
                border: 2px solid rgb(34, 40, 49);
                border-radius: 20px;
                width: 180;
                height: 40;
        }
        QPushButton:hover{
                background-color: "#222831";
                font-family: "Pixel Emulator";
                color: "#00ADB5";
                border: 2px solid rgb(0, 173, 181);
                border-radius: 20px;
                width: 180;
                height: 40;
        }
            """)
        kolejny_btn.move(190, 270)
        kolejny_btn.clicked.connect(self.losowanie)

        quit_btn = QPushButton("Wyczysc liste osob", self)
        quit_btn.setStyleSheet("""
        QPushButton {
                background-color: "#00ADB5";
                font-family: "Pixel Emulator";
                color: "#222831";
                border: 2px solid rgb(34, 40, 49);
                border-radius: 20px;
                width: 160;
                height: 40;
        }
        QPushButton:hover {
                background-color: "#222831";
                font-family: "Pixel Emulator";
                color: "#00ADB5";
                border: 2px solid rgb(0, 173, 181);
                border-radius: 20px;
                width: 160;
                height: 40;
        }
            """)
        quit_btn.move(110, 390)
        quit_btn.clicked.connect(self.osoby.clear)

        # ustawienia głównego okna
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(400, 600)
        self.setWindowTitle("Losowator")
        self.setWindowIcon(QPixmap("losowanie.gif"))
        self.show()

    def losowanie(self):
        self.osoby.append(self.liczba_osob.text())
        self.liczba_osob.clear()

    def informativeText(self):
        try:
            d = random.choice(self.osoby)
            separator = ", "
            e = separator.join(self.osoby)
            time.sleep(0.5)
            msg = QMessageBox()
            msg.setWindowFlag(Qt.FramelessWindowHint)
            msg.setStyleSheet("""
            QPushButton {
                    background-color: "#00ADB5";
                    font-family: "Pixel Emulator";
                    color: "#222831";
                    border: 2px solid rgb(34, 40, 49);
                    border-radius: 20px;
                    width: 75;
                    height: 40;
            }
            QMessageBox {
                    color: "#00ADB5";
                    background: "#393E46";
                    border: 2px solid rgb(34, 40, 49);
                    border-radius: 20px;
            }
            color: "#393E46";
            color: "#00ADB5";
            background-color: "#393E46";
            font-family: "Pixel Emulator";
            """)
            msg.setText(f"Osoby które braly udzial w losowaniu:\n{e}")
            msg.setInformativeText(f"         Wylosowana osoba to:\n             {d}")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.move(780, 600)
            msg.exec()
        except IndexError:
            print("Wpierw Podaj osoby!")


if __name__ == '__main__':
    app = QApplication([])

    login_window = LoginWindow()

    app.exec()