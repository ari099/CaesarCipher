import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('caesar_cipher.ui', self)
      self.show()

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()