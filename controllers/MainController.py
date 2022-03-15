from PyQt5.QtMultimedia import QMediaPlayer
from PyQt5.QtWidgets import QPushButton

from model.model import Model
from views.ButtonMines import ButtonMines
from views.MainWindow import MainWindow
from views.UserLabels import UserLabels

import  random


class MainController:
    def __init__(self):
        # model

        self.model = Model()

        # views

        self.mainWindow = MainWindow(self)
        self.userLabels = UserLabels(self)
        self.buttonMines = ButtonMines(self)

        self.media = QMediaPlayer()

    def main(self):
        # initialize main window
        self.mainWindow.main()

        # initialize user labels
        self.userLabels.main()

        # initialize mine buttons
        self.buttonMines.main()

    # listeners

    def check_bomb(self, btn: QPushButton):
        chance = random.randint(1, 100)

        if chance < self.model.difficulty:
            btn.setIcon(self.model.icon)
            # todo : end the game here

        else:
            btn.setIcon(self.model.secure_icon)
            btn.setDisabled(True)
