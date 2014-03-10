import asyncore, socket, collections

class Client(asyncore.dispatcher):
    def __init__(self, host_address, name):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.name = name
        self.connect(host_address)
        self.outbox = collections.deque()
        print 'client started'

    def say(self, message):
        self.outbox.append(message)
        print 'enqueued message'

    def handle_write(self):
        if not self.outbox:
            return
        message = self.outbox.popleft()
        if len(message) > 1024:
            raise ValueError('message too long')
        self.send(message)

    def handle_close(self):
        print 'client: connection closed'
        self.close()

    def handle_read(self):
        message = self.recv(1024)
        if not message:
            return
        print 'received ', message
        #self.send('Hello from client')

name = raw_input('write your nickname: ')
c = Client(('127.0.0.1', 5007), name)
# spawn other thread reading input here
asyncore.loop()
