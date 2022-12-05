from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication, QLabel, \
    QPushButton, QAction


def on_hello_pushbutton_clicked():
    hello_label.setVisible(True)


def on_action_reset_triggered():
    hello_label.setVisible(False)


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])

    window = uic.loadUi("QtHelloWorld.ui")

    hello_label = window.findChild(QLabel, 'hellolabel')
    hello_label.setVisible(False)

    hello_btn = window.findChild(QPushButton, 'hellopushbutton')
    hello_btn.clicked.connect(on_hello_pushbutton_clicked)

    action_reset = window.findChild(QAction, 'actionReset')
    action_reset.triggered.connect(on_action_reset_triggered)

    window.show()

    app.exec_()