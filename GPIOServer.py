from gpio.Sensors import Sensors
from server import Server


class GPIOServer(Server):
    def __init__(self, host, port, mdns_desc, mdns_addr):
        super().__init__(host, port, mdns_desc, mdns_addr)
        self.us = Sensors()

    def start(self):
        self.us.start()
        self.server.message_loop.emits(self.us)
        super().start()

    def stop(self):
        self.us.stop()
        super().stop()
