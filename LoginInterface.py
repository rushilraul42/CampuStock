import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def _init_(self):
        super(Login, self)._init_()
        loadUi("login.ui", self)
        self.verify.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        PID = self.PID.text()
        password = self.password.text()
        print("Successfully logged in PID:", PID, "and password:", password)

    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class CreateAcc(QDialog):
    def _init_(self):
        super(CreateAcc,self)._init_()
        loadUi("register.ui", self)
        self.signup.clicked.connect(self.createaccfunction)
        self.password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password2.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        PID = self.PID.text()
        email = self.email.text()
        phone = self.phone.text()
        branch = self.branch.text()
        if self.password1.text() == self.password2.text():  # Fixed
            password = self.password.text()
            print("Successful")
            login = Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex() + 1)

if __name__ == "_main_":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    mainwindow = Login()
    mainwindow.setWindowTitle("Login")
    mainwindow.setFixedSize(480, 630)
    widget.addWidget(mainwindow)
    widget.show()
    sys.exit(app.exec_())