import asynchat
import asyncore
import socket

chat_room = {}

class ChatHandler(asynchat.async_chat):
    def __init__(self, sock):
        asynchat.async_chat.__init__(self, sock=sock, map=chat_room)

        self.set_terminator('\n')
        self.buffer = []

    def collect_incoming_data(self, data):
        self.buffer.append(data)

    def found_terminator(self):
        msg = ''.join(self.buffer)
        print 'Received:', msg
        for handler in chat_room.itervalues():
            if hasattr(handler, 'push'):
                handler.push(msg + '\n')
        self.buffer = []

class ChatServer(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self, map=chat_room)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            sock, addr = pair
            print 'Incoming connection from %s' % repr(addr)
            handler = ChatHandler(sock)

server = ChatServer('localhost', 5050)

print 'Serving on localhost:5050'
asyncore.loop(map=chat_room)
