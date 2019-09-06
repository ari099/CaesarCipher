import sys, string
from PyQt5 import QtWidgets, uic

class Queue(object):
   """
   Simple queue data structure
   """
   def __init__(self, arr):
      self.values = arr
   
   def __repr__(self):
      return str(self.values)
   
   def __len__(self):
      return len(self.values)
   
   def enqueue(self, value):
      self.values.insert(0, value)
   
   def dequeue(self):
      return self.values.pop()
   
   def peek(self):
      return self.values[-1:][0]

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('caesar_cipher.ui', self)

      # Find the slider with the name "CipherDial"
      self.slider = self.findChild(QtWidgets.QSlider, 'CipherDial')
      self.slider.valueChanged.connect(self.encryptString)

      # Find the textbox labeled with "UserInput"
      self.textbox = self.findChild(QtWidgets.QTextEdit, 'UserText')
      self.alphabet = list(string.ascii_lowercase)

      self.show()
   
   def encryptString(self):
      # This is executed when the slider is moved
      # self.textbox.setText(str(self.slider.value()))
      key = self.slider.value()
      user_text = self.textbox.toPlainText()
      print(str(self.rotateLeft(self.alphabet, key)))
      # if len(user_text) > 0:
      #    new_list = self.rotateLeft(self.alphabet, key)
      #    for character in user_text
   
   def rotateLeft(self, array, k):
      """
      Rotate a list to the left
      :param k:
      """
      return array[abs(k):] + array[:abs(k)]
   
   def rotateRight(self, array, k):
      """
      Rotate a list to the right
      :param k:
      """
      return array[-abs(k):] + array[:-abs(k)]

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()