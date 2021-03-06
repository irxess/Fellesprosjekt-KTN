import asynchat
import asyncore
import socket
import threading
import re

class ChatClient(asynchat.async_chat):

    def __init__(self, host, port):
        asynchat.async_chat.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

        self.set_terminator('\n')
        self.buffer = []

    def collect_incoming_data(self, data):
        pass

    def found_terminator(self):
        pass

client = ChatClient('localhost', 5050)

thread = threading.Thread(target=asyncore.loop)
thread.daemon = True
thread.start()

username = raw_input("username: ")
while ( re.match('^[\w-]+$', username ) is None ):
    print "Invalid username"
    username = raw_input("username: ")

while True:
    message = raw_input('> ')
    client.push(message + '\n')
