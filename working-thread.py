import threading
import time
import random


def excuteThread(i):
    print("Thread {} sleep at {} ".format(i, time.strftime("%H:%M:%S", time.gmtime())) )

    randSleepTime = random.randint(1, 5)

    time.sleep(randSleepTime)

    print("Thread {} stop sleeping at {}".format(i,time.strftime("%H:%M:%S", time.gmtime())))


for i in range(10):
    thread = threading.Thread(target=excuteThread, args=(i,))
    thread.start()

    print("Active Threads : ", threading.activeCount())
    print("Thread Objects :", threading.enumerate())



