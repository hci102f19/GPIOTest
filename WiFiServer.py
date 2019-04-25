from server import Server
from wifi import WiFi


class WiFiServer(Server):
    def __init__(self, host, port, mdns_desc, mdns_addr):
        super().__init__(host, port, mdns_desc, mdns_addr)
        self.device = WiFi("wlan0", "AAU-1x")

    def start(self):
        self.device.start()
        self.server.message_loop.emits(self.device)
        super().start()

    def stop(self):
        self.device.stop()
        super().stop()
