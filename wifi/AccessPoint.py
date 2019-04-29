import math
import re


class AccessPoint(object):
    def __init__(self, data, tx_power=0):
        essid_regex = re.compile(r'ESSID:"(.*)"')
        signal_regex = re.compile(r'Signal level=(-\d+)')
        quality_regex = re.compile(r'Quality=(\d+)\/(\d+)')
        mac_regex = re.compile(r'Address: (([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))')
        frequency_regex = re.compile(r'Frequency:([0-9.]+) GHz')

        essid = essid_regex.search(data)
        signal = signal_regex.search(data)
        quality = quality_regex.search(data)
        mac = mac_regex.search(data)
        frequency = frequency_regex.search(data)

        self.tx_power = tx_power

        if essid is None or signal is None or mac is None:
            raise Exception("Not valid data")

        self.essid = essid.group(1)
        self.signal = int(signal.group(1))
        self.mac = mac.group(1)

        self.quality = round((int(quality.group(1)) / int(quality.group(2))) * 100, 2)

        self.frequency = float(frequency.group(1))

    def get_distance(self, rssi):
        print("RSSI: {}, Frequency: {}".format(rssi, self.frequency))
        exp = (27.55 - (20 * math.log10(self.frequency)) + abs(rssi)) / 20.0
        return math.pow(10.0, exp)

        # ratio = rssi * 1.0 / self.tx_power
        # if ratio < 1.0:
        #     return math.pow(ratio, 10)
        # return 0.89976 * math.pow(ratio, 7.7095) + 0.111

        # return round(pow(10, (self.tx_power - rssi) / (10 * 2)), 2)

    def emit(self):
        return {
            'essid': self.essid,
            'mac': self.mac,
            'signal': self.signal,
            'quality': self.quality,
            'distance': self.get_distance(int(self.signal))
        }
