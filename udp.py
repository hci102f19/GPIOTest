import json
import uuid

from Server import Server


class Sonar(object):
    def __init__(self):
        self.sensors = [
            uuid.uuid4().hex,
            uuid.uuid4().hex,
            uuid.uuid4().hex,
            uuid.uuid4().hex
        ]

    def emit(self):
        return json.dumps(self.sensors)


sonar = Sonar()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(sonar)

server.start()
