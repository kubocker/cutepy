#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QDesktopWidget


class BaseWindow(QWidget):

    def __init__(self, parent=None):
        super(BaseWindow, self).__init__(parent)

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create(self, width, height, title):
        self.resize(width, height)
        self.__center()
