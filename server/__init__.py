from server.UDPServer import UDPServer
from server.mDNS import mDNS


class Server(object):
    def __init__(self, host, port, mdns_desc, mdns_addr):
        self.mdns_desc = mdns_desc

        self.server = UDPServer(host, port)
        self.mdns = mDNS(port, mdns_desc, mdns_addr)

    def start(self):
        print("Starting: {}".format(self.mdns_desc))
        self.server.start()
        self.mdns.register()

    def stop(self):
        print("Stopping: {}".format(self.mdns_desc))
        self.server.stop()
        self.mdns.unregister()

    def list_clients(self):
        for idx, c in enumerate(self.server.clients):
            print("{}: {}".format(idx + 1, c))
