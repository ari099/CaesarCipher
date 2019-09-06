import sys, string
from PyQt5 import QtWidgets, uic

def rotateLeft(array, k):
   """
   Rotate a list to the left
   :param k:
   """
   return array[abs(k):] + array[:abs(k)]
   
def rotateRight(array, k):
   """
   Rotate a list to the right
   :param k:
   """
   return array[-abs(k):] + array[:-abs(k)]

def encryptString(text, key):
   """
   Encrypt a string the Caesar cipher
   :param text:
   :param key:
   """
   alphabet = list(string.ascii_lowercase)
   cipher_alphabet = rotateLeft(list(string.ascii_lowercase), key)
   for i in range(0, len(text)):
      isUpperCase = False
      # Find the letter character in the cipher alphabet and get it's index
      if text[i].lower() in alphabet:
         if text[i].isupper(): isUpperCase = True
         index = alphabet.index(text[i].lower()) # Get the index used for it in the alphabet list
         text_list = list(text) # Turn the text into a list to manipulate it
         text_list[i] = cipher_alphabet[index] if isUpperCase == False else cipher_alphabet[index].upper() # Replace the letter with the cipher alphabet equivalent
         text = "".join(text_list) # Turn the text back into a string
   
   return text # Return the cipher text



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
      self.slider.valueChanged.connect(self.sliderMoved)

      # Find the textbox labeled with "UserInput"
      self.textbox = self.findChild(QtWidgets.QTextEdit, 'UserText')
      self.alphabet = list(string.ascii_lowercase)

      # Find the label labeled (hehe) with "CipherTextOutput"
      self.cipherTextOutput = self.findChild(QtWidgets.QLabel, 'CipherTextOutput')

      self.show()
   
   def sliderMoved(self):
      # This is executed when the slider is moved
      # self.textbox.setText(str(self.slider.value()))
      key = self.slider.value()
      user_text = self.textbox.toPlainText()
      if len(user_text) > 0:
         self.cipherTextOutput.setText(encryptString(user_text, key))

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()