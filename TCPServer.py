from socket import *
from threading import Thread


print'SERVER'


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 9007))
serverSocket.listen(5)

def acceptClient():
    
    while True:
        vent=' '
        print 'venter pa klient'
        connectionSocket, addr = serverSocket.accept()
        print 'klient koblet til'
        print'starter ny thread'
        t = Thread(target=recvMsg(connectionSocket,addr))
        t.start()
        print'etter thread'


def recvMsg(connectionSocket,addr):
    while True:
        print 'venter pa melding'
        message, address = connectionSocket.recvfrom(1024)
        print'package recieved from: ', address, "msg: ", message


Thread(target=acceptClient()).start()

