#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QMainWindow, QWidget
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
        self.status_bar = self.statusBar()
        self.menu_bar = self.menuBar()
        self.setGeometry(self.pos_x, self.pos_y, self.width, self.height)
        self.show()

    def create(self, widget):
        self.setCentralWidget(widget)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
        self.setWindowTitle(self._title)

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
        self.status_bar.showMessage(self._message)
