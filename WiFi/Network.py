class Network(object):
    def __init__(self, accesspoint=None, essid=None):
        if accesspoint is None and essid is None:
            raise Exception("INFO MUST BE SET")

        self.access_points = []

        if accesspoint is not None:
            self.access_points.append(accesspoint)

        self.essid = essid if accesspoint is None else accesspoint.essid

    def add_access_point(self, access_point):
        self.access_points.append(access_point)

    def ssid(self):
        return self.essid

    def clear_networks(self):
        self.access_points.clear()

    def emit(self):
        return {
            'ssid': self.essid,
            'access_points': [ap.emit() for ap in self.access_points]
        }
