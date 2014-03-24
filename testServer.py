from __future__ import print_function
import asyncore, socket, collections, json

class ClientHandler(asyncore.dispatcher):
    def __init__(self, host, socket, address):
        asyncore.dispatcher.__init__(self, socket)
        self.host = host
        self.outbox = collections.deque()

    def sendMessage(self, message):
        self.outbox.append(message)

    def handle_read(self):
        client_message = self.recv(1024)
        if not client_message:
            print ('client disconnected')
            return
        print ('broadcasting message')
        ut = json.loads(client_message)
        self.host.broadcast(ut)

    def handle_write(self):
        if not self.outbox:
            return
        message = self.outbox.popleft()
        if len(message) > 1024:
            raise ValueError('message too long')
        self.send(message)

    def handle_close(self):
        print ("server: closed connection")
        self.close()

class Server(asyncore.dispatcher):
    def __init__(self, address=('mips.pvv.org', 1001)):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.listen(1)
        self.remote_clients = []
        print ("Waiting for connection")

    def handle_accept(self):
        socket, address = self.accept()
        print ("connection by", address)
        self.remote_clients.append(ClientHandler(self, socket, address))
        ut = {"name" : "server", "msg" : "Hello from server"}
        socket.send(json.dumps(ut))

    def handle_read(self):
        print ('received message: %s', self.read())

    def broadcast(self, message):
        print ('Broadcasting')
        for client in self.remote_clients:
            client.sendMessage(message)

s = Server(('0.0.0.0', 1001))
asyncore.loop()
