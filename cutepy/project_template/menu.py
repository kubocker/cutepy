
from PyQt5.QtWidgets import (QMainWindow,
                             QWidget,
                             QDesktopWidget,
                             QTabWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QDialog,
                             QMessageBox,
                             QLabel,
                             QPushButton)
from .settings import CANVAS as ui


class BaseMainMenu(QMainWindow):

    width = ui['width']
    height = ui['height']
    pos_x = ui['x']
    pos_y = ui['y']

    def __init__(self, parent):
        super(BaseMainMenu, self).__init__(parent)
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
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()


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


def confirm_message(self, param, func=None):
    confirm = QMessageBox.question(self, 'Confirm', param, QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if confirm == QMessageBox.Yes:
        print("yes.....")
        if func is not None:
            func()
        self.close()
    else:
        print("no....")


class BaseDialog(QDialog):
    title = 'Form'

    def __init__(self, parent, date):
        super(BaseDialog, self).__init__(parent)
        self.create(500, 500, self.title)

        self.date = QLabel(date, self)
        self.add_btn = QPushButton('Add', self)
        self.cancel_btn = QPushButton('Cancel', self)

        self.init_ui()

    def __center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def create(self, width, height, title):
        self.resize(width, height)
        self.__center()
        self.setWindowTitle(title)
        return self

    def init_ui(self):
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()
        self.h_layout.addWidget(self.cancel_btn)
        self.h_layout.addWidget(self.add_btn)
        self.cancel_btn.clicked.connect(self.cancel)
        self.add_btn.clicked.connect(self.add)

    def add(self, post, call_func):
        confirm_message(self, post, call_func)

    def cancel(self, post, call_func):
        confirm_message(self, post, call_func)
