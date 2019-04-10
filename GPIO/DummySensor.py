class DummySensor(object):
    def __init__(self, place, _, __):
        self.place = place

    def start(self):
        return

    def data(self):
        return {
            'value': 0,
            'distance': 0
        }

    def stop(self):
        return
