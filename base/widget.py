#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QDesktopWidget, QTabWidget, QHBoxLayout, QVBoxLayout


class BaseWindow(QWidget):

    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent)
        self.tab = QTabWidget()
        self.init_ui()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create(self, width, height, title):
        self.resize(width, height)
        self.__center()
        self.show()

    def init_ui(self):
        pass


class BaseWidget(QWidget):
    name = ""

    def __init__(self, parent=None):
        super(BaseWidget, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        if self.name != "":
            self.setWindowTitle(self.name)
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
