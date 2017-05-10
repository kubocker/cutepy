from PyQt5.QtWidgets import (QMainWindow,
                             QDesktopWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QDialog,
                             QMessageBox,
                             QLabel,
                             QPushButton)


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
