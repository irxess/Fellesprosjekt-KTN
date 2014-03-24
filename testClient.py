import asyncore, socket, collections, json, threading, re
#import cursesUI

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
        json_msg = json.dumps(message)
        if len(message) > 1024:
            raise ValueError('message too long')
        self.send(json_msg)

    def handle_close(self):
        print 'client: connection closed'
        self.close()

    def handle_read(self):
        message = self.recv(1024)
        if not message:
            return
        # decode JSON here
        inn = json.loads(message)
        print inn.get("name") + ": " + inn.get("msg")

def read_and_send_input():
    while True:
        message = raw_input("> ")
        # send to server
        #inn = json.loads(message)
        ut = {"name" : username, "msg" : message}
        c.say( json.dumps(ut) )


username = raw_input("username: ")
while (re.match( '^[\w-]+$', username ) is None):
    print "Invalid username"
    username = raw_input("username: ")

c = Client(('mips.pvv.org', 1001), username)
thread = threading.Thread(target=asyncore.loop)
thread.daemon = True  # vil denne avsluttes?
thread.start()

#ui = cursesUI.clientInterface(username)
#ui.paintWindow()

read_and_send_input()
