import socket
import threading
import time

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        host = '127.0.0.1'
        port =50111
        s = socket.socket()
        s.bind((host,port))
        s.listen(1)
        c, addr = s.accept()
        print("Connected from " + str(addr))
        while True:
            data = c.recv(1024)
            if not data:
                break
            print( "from connected host " + str(data))
            data = str(data).upper()
            print("Sending " + str(data))
            c.send(data.encode())
        c.close()

class Clinet(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self)

    def run(self):
        host = '127.0.0.1'
        port =50111
        s = socket.socket()
        s.connect((host,port))
        print("connecting  to " + str(host))
        while True:
            data = input("Enter....")
            if data=='q':
                break
            s.send(data.encode())
            print("Recived " + str(s.recv(1024)))
        s.close()

s = Server()
s.start()
c = Clinet()
time.sleep(2)
c.start()
c.join()
s.join()


