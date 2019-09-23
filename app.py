import sys, string
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
   def __init__(self):
      super(Ui, self).__init__()
      uic.loadUi('caesar_cipher.ui', self)

      # Find the slider with the name "CipherDial"
      self.slider = self.findChild(QtWidgets.QSlider, 'CipherDial')
      self.slider.valueChanged.connect(self.sliderMoved)

      # Find the textbox labeled with "UserInput"
      self.textbox = self.findChild(QtWidgets.QTextEdit, 'UserText')
      self.textbox.textChanged.connect(self.userInputChanged)
      self.alphabet = list(string.ascii_lowercase)

      # Find the label labeled (hehe) with "CipherTextOutput"
      self.cipherTextOutput = self.findChild(QtWidgets.QLabel, 'CipherTextOutput')

      # Find the label labeled (hehe) with "SliderNumber"
      self.sliderNumber = self.findChild(QtWidgets.QLabel, 'SliderNumber')

      self.show()
   
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

   def encryptString(self, text, key):
      """
      Encrypt a string the Caesar cipher
      :param text:
      :param key:
      """
      alphabet = list(string.ascii_lowercase)
      cipher_alphabet = self.rotateLeft(list(string.ascii_lowercase), key)
      for i in range(0, len(text)):
         isUpperCase = False
         # Find the letter character in the cipher alphabet and get it's index
         if text[i].lower() in alphabet:
            # Is the character at index "i" uppercase or lowercase?
            if text[i].isupper(): isUpperCase = True
            index = alphabet.index(text[i].lower()) # Get the index used for it in the alphabet list
            text_list = list(text) # Turn the text into a list to manipulate it
            
            # Determine if the original character was uppercase or lowercase from the variable "isUpperCase"
            # Replace the letter with the cipher alphabet equivalent
            text_list[i] = cipher_alphabet[index] if isUpperCase == False else cipher_alphabet[index].upper()
            text = "".join(text_list) # Turn the text back into a string
      
      return text # Return the cipher text
   
   # ############################# UI CONTROL METHODS #############################
   def sliderMoved(self):
      # This is executed when the slider is moved
      # self.textbox.setText(str(self.slider.value()))
      key = self.slider.value()
      user_text = self.textbox.toPlainText()
      self.sliderNumber.setText("Key: " + str(key))
      if len(user_text) > 0:
         self.cipherTextOutput.setText(self.encryptString(user_text, key))
   
   def userInputChanged(self):
      key = self.slider.value()
      user_text = self.textbox.toPlainText()
      if len(user_text) == 0:
          self.cipherTextOutput.setText("Cipher text should appear here....")
      else: self.cipherTextOutput.setText(self.encryptString(user_text, key))

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()