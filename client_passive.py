import socket
import time
import threading

client = socket.socket()
address_to_server = ('localhost', 8686)

while True:
    try:
        client.connect(address_to_server)
        print ('connecthion Treu', client.recv(1024).decode('utf-8'))
        break
    except:
        pass
    time.sleep(0.5)


flag = True
def send_cl():
    global flag
    while flag:
        print(1)
        try:
            print('try1')
            vvod = input()
            client.send(vvod.encode('UTF-8'))
        except:
            print('ex')
            pass
        time.sleep(1)


vivod = threading.Thread(target=send_cl)
def read_cl():
    global flag
    while flag:
        try:
            print('try2')
            data = client.recv(1024).decode('utf-8')
            if data == 'server close':
                print('recive command - "', data, '"')
                flag = False
                break
            else:
                print(data)
        except:
            pass
        time.sleep(1)

vvod = threading.Thread(target=read_cl)


vivod.start()
vvod.start()
