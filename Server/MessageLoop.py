import threading
from time import sleep


class MessageLoop(threading.Thread):
    def __init__(self, socket, clients):

        super().__init__()
        self.socket = socket
        self.clients = clients

        self.emit = None

        self.running = True

    def run(self):
        while self.running:
            if self.emit is not None:
                data = self.pack(self.emit.emit())
                if data is not None:
                    for c in self.clients:
                        self.socket.sendto(data, c)

            sleep(1)

    def pack(self, data):
        if isinstance(data, str):
            return data.encode('utf-8')
        elif isinstance(data, bytes):
            return data
        return None

    def emits(self, obj: object):
        self.emit = obj
