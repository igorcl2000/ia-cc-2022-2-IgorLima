import sys
from gui import Gui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication

if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    gui = Gui()
    gui.window.show()
    sys.exit(app.exec_())
