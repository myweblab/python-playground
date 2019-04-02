import threading
import time

tLock = threading.Lock()

class AsyncWrite(threading.Thread):
    def __init__(self, text, out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out
    
    def run(self):
        tLock.acquire()

        print("in lock")
        f = open(self.out, "a")
        f.write(self.text + "\n|")
        f.close()
        time.sleep(2)
        tLock.release()
        print("finished & released")

i=10
while i > 0:
    message = input("enter")
    background = AsyncWrite(message,"out.txt")
    background.start()
    print(100+400)
    i -=1
    background.join()
    