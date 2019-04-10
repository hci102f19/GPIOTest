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

        self.HELOMessage = 'HELO'

        self.message_loop = MessageLoop(self.socket, self.clients)

    def run(self):
        print("Starting server on {}:{}".format(self.host, self.port))
        self.message_loop.start()

        self.socket.settimeout(1.0)

        while self.running:
            try:
                message, address = self.socket.recvfrom(self.buffer_size)
            except ConnectionResetError:
                continue
            except socket.timeout:
                continue

            if message.decode('utf-8') == self.HELOMessage:
                if address not in self.clients:
                    ip, port = address
                    print("Client connected from: {}:{}".format(ip, port))
                    self.message_loop.send(self.HELOMessage, address)
                    self.clients.append(address)
            else:
                self.message_loop.send('InvalidHELOMessage', address)

    def stop(self):
        self.message_loop.stop()
        self.running = False
