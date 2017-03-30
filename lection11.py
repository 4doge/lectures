from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QLineEdit, QDateEdit
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont

import sys


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_interface()

    def init_interface(self):
        font = QFont("SansSerif", 14)

        QToolTip.setFont(font)

        btn_no_action = QPushButton("Button: No action", self)
        btn_no_action.setToolTip("Button tooltip on hover.")
        btn_no_action.resize(150, 50)  # width height
        btn_no_action.move(0, 0)  # left right

        btn_quit = QPushButton("Button: Quit app", self)
        btn_quit.resize(150, 50)
        btn_quit.move(0, 55)
        btn_quit.clicked.connect(QCoreApplication.instance().quit)

        btn_call_func = QPushButton("Button: Call func", self)
        btn_call_func.resize(150, 50)
        btn_call_func.move(0, 55 * 2)
        btn_call_func.clicked.connect(self.say_hello)

        textbox = QLineEdit(self)
        textbox.setObjectName("textbox_obj")
        textbox.move(160, 5)
        textbox.resize(150, 50)

        btn_read_text = QPushButton("Button: Read text", self)
        btn_read_text.resize(150, 50)
        btn_read_text.move(0, 55 * 3)
        btn_read_text.clicked.connect(self.read_text)

        date = QDateEdit(self)
        date.move(0, 55 * 4)


        self.setToolTip("Window tooltip on hover.")
        self.setGeometry(0, 0, 350, 350)  # left top width height
        self.setWindowTitle("Window title here.")
        self.show()

    def say_hello(self):
        sender = self.sender()
        sender.move(10, 10)
        print("Hello from `{}`".format(sender))

    def read_text(self):
        text = self.findChild(QLineEdit, "textbox_obj").text()
        sender = self.sender().text()
        print("`{}` read value `{}`".format(sender, text))


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # w = QWidget()
    w = MainWindow()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.setWindowTitle('Simple')
    # w.show()

    sys.exit(app.exec_())
