import socket

import netifaces as ni
from zeroconf import ServiceInfo, Zeroconf


class mDNS(object):
    def __init__(self, port, mdns_desc, mdns_addr):
        try:
            ni.ifaddresses('wlan0')
            self.ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        except ValueError:
            self.ip = socket.gethostbyname(socket.gethostname())

        self.port = port
        desc = {
            'version': '0.1',
            'base_url': "http://{}:{}/".format(self.ip, str(self.port)),
            'path': '/'
        }

        self.info = ServiceInfo(
            "_http._tcp.local.",
            "{}._http._tcp.local.".format(mdns_desc),
            socket.inet_aton(self.ip), self.port, 0, 0,
            desc, "{}.".format(mdns_addr)
        )

        self.zeroconf = Zeroconf()

    def register(self):
        self.zeroconf.register_service(self.info)

    def unregister(self):
        self.zeroconf.unregister_service(self.info)
