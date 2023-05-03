#!/usr/bin/env python3

# pip install pyqt6 pyqt6_tools

import os
import sys
from PyQt6 import QtWidgets, uic

_scriptdir = os.path.dirname(os.path.realpath(__file__))
uifile = os.path.join(_scriptdir, 'main.ui')

class MainDialog(*uic.loadUiType(uifile)):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bindEvents()

    def bindEvents(self):
        self.btn_exit.clicked.connect(self.close)
        self.btn_res.clicked.connect(self.verdict)

    def verdict(self):
        try:
            a = int(self.textEdit_input.toPlainText())
        except ValueError:
            self.label_res.setText('ВВЕДИТЕ ЦЕЛОЕ ЧИСЛО!')
            return
        b = 0
        for i in range(2, int(a ** 0.5) + 1):
            if (a % i == 0):
                b = b + 1
        if (b <= 0):
            self.label_res.setText('Простое')
        else:
            self.label_res.setText('Не простое(')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainDialog()
    w.show()

    sys.exit(app.exec())
