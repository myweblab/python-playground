from threading import Thread
import time
def timer(name,delay,repeat):
    print("timer : " + name + " Started")
    while repeat > 0:
        time.sleep(delay)
        print(name+ " : " + str(time.ctime()))
        repeat=-1
    print("Timer {0} Completed".format(name))

t1 = Thread(target=timer, args=("Timer1",10,100))
t2 = Thread(target=timer, args=("Timer2",20,150))
t3 = Thread(target=timer, args=("Timer3",10,200))
t4= Thread(target=timer, args=("Timer4",20,250))

t1.start()
t2.start()
t3.start()
t4.start()
