#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow


class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()


    def init_ui(self):
        self.statusBar()
        self.setGeometry(500, 500, 500, 500)
        self.show()

