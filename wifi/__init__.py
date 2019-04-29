import json
import re
import subprocess
import threading
from time import sleep

from wifi.AccessPoint import AccessPoint
from wifi.Network import Network


class WiFi(threading.Thread):
    def __init__(self, device, ssid=None):
        super().__init__()

        self.ssid = ssid

        self.device = device
        self.cmd = "sudo iwlist {} scanning | egrep 'Cell |Frequency|Quality|ESSID'".format(device)

        self.is_running = True

        self.networks = []

        self.network = None if ssid is None else Network(essid=ssid)

        self.tx_power = self.get_tx_power()

    def run(self):
        while self.is_running:
            output = subprocess.getoutput(self.cmd)

            self.networks.clear()
            if self.network is not None:
                self.network.clear_networks()

            self.parse_output(output)

            sleep(1)

    def stop(self):
        self.is_running = False

    def parse_output(self, output):
        cur_package = ""
        for line in output.split('\n'):
            line = line.strip()
            if line[0:4] == 'Cell':
                if cur_package:
                    self.parse_network(cur_package)
                    cur_package = ""
            cur_package += "{}\n".format(line)

        if cur_package:
            self.parse_network(cur_package)

    def parse_network(self, cur_package):
        access_point = AccessPoint(cur_package, tx_power=self.tx_power)

        if self.ssid is None:
            for network in self.networks:
                if network.ssid() == access_point.essid:
                    network.add_access_point(access_point)
                    return

            self.networks.append(Network(accesspoint=access_point))
            return

        elif self.ssid == access_point.essid:
            self.network.add_access_point(access_point)

    def emit(self):
        if self.ssid is None:
            return json.dumps([n.emit() for n in self.networks])
        return json.dumps(self.network.emit())

    def get_tx_power(self):
        cmd = "iwconfig {} | egrep 'Tx-Power='".format(self.device)
        output = subprocess.getoutput(cmd)

        re_tx_power = re.compile(r'Tx-Power=(\d+) dBm')

        tx_power = re_tx_power.search(output).group(1)

        return -int(tx_power)
