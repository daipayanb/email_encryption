import sys
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from Email import encrypt_email
from Email import decrypt_email
from Email import newuser

qtCreatorFile = "rsegui.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        user, ok = QtWidgets.QInputDialog.getText(self, 'New User', 
    'Are you a new user?')
        user=str(user)
        if user in "YESYesyesYy":
            email, ok = QtWidgets.QInputDialog.getText(self, 'New User', 
    'Enter Your Email ID:')
            email1=str(email)
            self.sender.setText(email)
            newuser(email1)
            
        self.encrypt_and_send.clicked.connect(self.EncryptEmail)
        self.decrypt.clicked.connect(self.DecryptEmail)
        self.clear.clicked.connect(self.ClearEncrypt)
        self.clear_2.clicked.connect(self.ClearDecrypt)
        self.sender.setPlaceholderText("Your Email ID")
        self.receiver.setPlaceholderText("Receivers, Separate them by ';'")
        self.subject.setPlaceholderText("Enter Subject")
        self.message.setPlaceholderText("Enter Message")
        self.sender_2.setPlaceholderText("Your Email ID")
        self.message_2.setPlaceholderText("Encrypted Text")



    def EncryptEmail(self):
        sender = str(self.sender.text())
        receiver = str(self.receiver.text())
        receivers = receiver.split(';')
        subject = str(self.subject.text())
        message = str(self.message.text())
        password, ok = QtWidgets.QInputDialog.getText(self, 'Password', 
    'Enter your password:',QtWidgets.QLineEdit.Password)
        encrypt_email(sender,receivers,subject,message,password)

    def DecryptEmail(self):
        email = str(self.sender_2.text())
        message = str(self.message_2.text())
        self.decrypted.setText(decrypt_email(email,message))

    def ClearDecrypt(self):
        self.sender_2.clear()
        self.message_2.clear()

    def ClearEncrypt(self):
        self.sender.clear()
        self.message.clear()
        self.receiver.clear()
        self.subject.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
