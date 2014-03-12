from socket import *
from threading import Thread


print'SERVER'

class listeningThread (Thread):
    def __init__(self, threadID, connectionSocket, addr):
        Thread.__init__(self)
        self.threadID = threadID
        self.connectionSocket = connectionSocket
        self.addr = addr
        self.newMessage = ""
        self.oldMessage = ""

    def run(self):
        while True: #should include a check if client wants to quit
            print 'venter pa melding'
            message, address = self.connectionSocket.recvfrom(1024)
            # might need a mutex here
            # docs.python.org/2/library/multiprocessing.html
            # 16.6.1.4
            print'package recieved from: ', address, "msg: ", message



serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 9008))
serverSocket.listen(5)

def acceptClient():
    threadsSpawned = 0
    listOfRunningThreads = []
    while True:
        vent=' '
        print 'venter pa klient'
        connectionSocket, addr = serverSocket.accept()
        print 'klient koblet til'
        print'starter ny thread'
        #t = Thread(target=recvMsg(connectionSocket,addr))
        #t.start()
        listOfRunningThreads.append(listeningThread(threadsSpawned, connectionSocket, addr))
        listOfRunningThreads[ threadsSpawned ].start()
        threadsSpawned += 1
        print'etter thread'


acceptClient()

