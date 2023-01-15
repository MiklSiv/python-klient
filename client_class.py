import socket
import time
import threading

class Client():
    def __init__(self, adress_server = 'localhost', port_server = 8686):
        self.adress = adress_server
        self.port = port_server
        self.client = None
        self.flag = True

    def connection(self):
        self.client = socket.socket()
        while True:
            try:
                self.client.connect((self.adress, self.port))
                print('connecthion Treu', self.client.recv(1024).decode('utf-8'))
                break
            except:
                pass
            time.sleep(0.5)


    def send_cl(self):
        while self.flag:
            try:
                vvod = input()
                self.client.send(vvod.encode('UTF-8'))
                if vvod == 'close':
                    self.flag = False
                    break

            except:
                print('ex_send')
                pass
            time.sleep(1)

    def read_cl(self):
        while self.flag:
            try:
                data = self.client.recv(1024).decode('utf-8')
                if data == 'connecthione close':
                    print('recive command - "', data, '"')
                    self.flag = False
                    break
                else:
                    print(data)
            except:
                pass
            time.sleep(1)

    def new_connecthion(self):
        self.connection()
        vod = threading.Thread(target=self.read_cl)
        vivod = threading.Thread(target=self.send_cl)
        vivod.start()
        vod.start()
        vod.join()
        vivod.join()


klient = Client( adress_server = '127.0.0.1', port_server = 8686)
klient.new_connecthion()