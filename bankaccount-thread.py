import threading
import time
import random


class BankAccount(threading.Thread):
    acctBalance = 100

    def __init__(self, name , moneyRequest):
        threading.Thread.__init__(self)
        self.name = name
        self.moneyRequest = moneyRequest

    def run(self):
        threadLock.acquire()
        BankAccount.getMoney(self)
        threadLock.release()

    @staticmethod
    def getMoney(customer):
        print("{} tries to withdrawal ${} at {}".format(customer.name,
                                                        customer.moneyRequest,
                                                        time.strftime("%H:%M:%S", time.gmtime())))

        if BankAccount.acctBalance - customer.moneyRequest > 0:

            BankAccount.acctBalance -= customer.moneyRequest
            print("New account balance : ${}".format(BankAccount.acctBalance))

        else:
            print("Not Enough Money in Account")
            print("Current balance : ${}".format(BankAccount.acctBalance))

            time.sleep(3)

threadLock = threading.Lock()

Rob = BankAccount("Rob" , 1)
Paul = BankAccount("Paul" , 100)
Sally = BankAccount("Sally" , 50)

Rob.start()
Paul.start()
Sally.start()

Rob.join()
Paul.join()
Sally.join()

print("Execution ends")
