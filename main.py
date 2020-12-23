from PyQt5.QtWidgets import *
from fen1 import Fen
import sys

app = QApplication(sys.argv)

fen = Fen()
fen.show()

app.exec_()