from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import socket

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 209)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bt_server = QtWidgets.QPushButton(self.centralwidget)
        self.bt_server.setGeometry(QtCore.QRect(190, 20, 200, 31))
        self.bt_server.setObjectName("bt_server")
        self.bt_send = QtWidgets.QPushButton(self.centralwidget)
        self.bt_send.setGeometry(QtCore.QRect(60, 80, 111, 31))
        self.bt_send.setObjectName("bt_send")
        self.text_send = QtWidgets.QTextEdit(self.centralwidget)
        self.text_send.setGeometry(QtCore.QRect(220, 80, 241, 31))
        self.text_send.setObjectName("text_send")
        self.bt_give = QtWidgets.QPushButton(self.centralwidget)
        self.bt_give.setGeometry(QtCore.QRect(60, 130, 111, 31))
        self.bt_give.setObjectName("bt_give")
        self.text_give = QtWidgets.QLabel(self.centralwidget)
        self.text_give.setGeometry(QtCore.QRect(220, 130, 241, 31))
        self.text_give.setObjectName("text_give")
        MainWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.client = ''
        self.fun()



    def fun(self):
        self.bt_server.clicked.connect(lambda: self.server_vkl())
        self.bt_give.clicked.connect(lambda: self.give_text())
        self.bt_send.clicked.connect(lambda: self.send_text())


    def server_vkl(self):
        self.client = socket.socket()
        address_to_server = ('localhost', 8686)
        self.client.connect(address_to_server)
        #self.client.close()

    def send_text(self):
        self.client.send(self.text_send.toPlainText().encode('UTF-8'))


    def give_text(self):
        data = self.client.recv(1024)

        self.text_give.setText(data.decode('utf-8'))





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_server.setText(_translate("MainWindow", "подключиться к серверу"))
        self.bt_send.setText(_translate("MainWindow", "send"))
        self.bt_give.setText(_translate("MainWindow", "give"))
        self.text_give.setText(_translate("MainWindow", "0"))


def app():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()