class DummySensor(object):
    def __init__(self, place, _, __):
        self.place = place

    def start(self):
        return

    def data(self):
        return {
            'value': -1,
            'distance': -1
        }

    def stop(self):
        return
