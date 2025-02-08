import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from convert import ConverterLogic

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.logic = ConverterLogic()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Конвертор валют')
        self.relize(300, 200)

        currencies =
