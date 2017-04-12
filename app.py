#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from base.menu import MainMenu


def main():
    app = QApplication(sys.argv)
    menu = MainMenu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
