#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow
from .settings import CANVAS as ui


class MainMenu(QMainWindow):

    width = ui['width']
    height = ui['height']
    pos_x = ui['x']
    pos_y = ui['y']

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.statusBar()
        self.setGeometry(self.pos_x, self.pos_y, self.width, self.height)
        self.show()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.setWindowTitle(self._title)
