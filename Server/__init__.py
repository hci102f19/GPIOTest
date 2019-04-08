import socket
import threading

from .MessageLoop import MessageLoop


class Server(threading.Thread):
    def __init__(self, host, port):
        super().__init__()
        self.host = host
        self.port = port
        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((host, port))

        self.buffer_size = 1024

        self.clients = []

        self.running = True

        self.message_loop = MessageLoop(self.socket, self.clients)

    def run(self):
        print("Starting server on {}:{}".format(self.host, self.port))
        self.message_loop.start()
        while self.running:
            try:
                message, address = self.socket.recvfrom(self.buffer_size)
            except ConnectionResetError:
                continue

            if message.decode('utf-8') == 'HELO':
                if address not in self.clients:
                    ip, port = address
                    print("Client connected from: {}:{}".format(ip, port))
                    self.clients.append(address)
            else:
                self.socket.sendto('InvalidHELOMessage'.encode('utf-8'), address)
