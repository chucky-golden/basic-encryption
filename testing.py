import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QGridLayout, QMessageBox
from PyQt5.QtCore import pyqtSlot
from cryptography.fernet import Fernet
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "ENCRYPTION APP"
        self.left = 550
        self.top = 150
        self.width = 350
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowIcon(QIcon("imgg.JPG"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        layout = QGridLayout()
        self.setStyleSheet("background-color: #660000; color: white;")

        button1 = QPushButton('check for generated key', self)
        button1.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 8px;}')
        button1.move(100, 50)
        button1.clicked.connect(self.check_key)
        layout.addWidget(button1)

        button3 = QPushButton('generate key', self)
        button3.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 8px;}')
        button3.move(100, 50)
        button3.clicked.connect(self.write_key)
        layout.addWidget(button3)

        button = QPushButton('select file to encrypt', self)
        button.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 8px;}')
        button.move(100, 50)
        button.clicked.connect(self.encrypt)
        layout.addWidget(button)

        button2 = QPushButton('select file to decrypt', self)
        button2.setStyleSheet('QPushButton {background-color: #cc0000; color: white; padding: 8px;}')
        button2.move(100, 50)
        button2.clicked.connect(self.decrypt)
        layout.addWidget(button2)

        self.setLayout(layout)
        self.show()

    @pyqtSlot()
    def check_key(self):
        msg = QMessageBox()
        with open("key.key", "rb") as key_file:
            content = key_file.read()

        if content == '':
            textboxvalue = 'Key not fount'
            msg.question(self, 'Message', "" + textboxvalue, QMessageBox.Ok, QMessageBox.Ok)
        else:
            textboxvalue = 'Key exists'
            msg.question(self, 'Message', "" + textboxvalue, QMessageBox.Ok, QMessageBox.Ok)

    def write_key(self):
        msg = QMessageBox()
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        textboxvalue = 'Key generated'
        msg.question(self, 'Message', "" + textboxvalue, QMessageBox.Ok, QMessageBox.Ok)


    def encrypt(self):
        msg = QMessageBox()
        key = open("key.key", "rb").read()
        file_name = QFileDialog.getOpenFileName \
            (self, 'Open File', 'c:\\', 'Text Files (*.pdf *.docx *.xls)')
        image_path = file_name[0]
        f = Fernet(key)
        with open(image_path, "rb") as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(image_path, 'wb') as j:
            j.write(encrypted_data)
        textboxvalue = 'Encryption successful'
        msg.question(self, 'Message', "" + textboxvalue, QMessageBox.Ok, QMessageBox.Ok)

    def decrypt(self):
        msg = QMessageBox()
        key = open("key.key", "rb").read()
        file_name = QFileDialog.getOpenFileName \
            (self, 'Open File', 'c:\\', 'Text Files (*.pdf *.docx *.xls)')
        image_path = file_name[0]
        f = Fernet(key)
        with open(image_path, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = f.decrypt(encrypted_data)

        with open(image_path, "wb") as file:
            file.write(decrypted_data)
        textboxvalue = 'Decryption successful'
        msg.question(self, 'Message', "" + textboxvalue, QMessageBox.Ok, QMessageBox.Ok)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())