import re


class AccessPoint(object):
    def __init__(self, data):
        essid_regex = re.compile(r'ESSID:"(.*)"')
        signal_regex = re.compile(r'Signal level=(-\d+)')
        quality_regex = re.compile(r'Quality=(\d+)\/(\d+)')
        mac_regex = re.compile(r'Address: (([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}))')

        essid = essid_regex.search(data)
        signal = signal_regex.search(data)
        quality = quality_regex.search(data)
        mac = mac_regex.search(data)

        if essid is None or signal is None or mac is None:
            print(data)
            raise Exception("Not valid data")

        self.essid = essid.group(1)
        self.signal = int(signal.group(1))
        self.mac = mac.group(1)

        self.quality = round((int(quality.group(1)) / int(quality.group(2))) * 100, 2)

    def emit(self):
        return {
            'essid': self.essid,
            'mac': self.mac,
            'signal': self.signal,
            'quality': self.quality
        }
