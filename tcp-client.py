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

def read_cl():
    global flag

    count = 0
    while flag:
        count += 1
        data = "massege " + str(count)
        client.send(data.encode('UTF-8'))
        time.sleep(1)



def close():
    global flag
    print('recive command - "', client.recv(1024).decode('utf-8'), '"')
    flag = False




vivod = threading.Thread(target=read_cl)
end = threading.Thread(target=close)

end.start()
vivod.start()



