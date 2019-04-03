import json

from .UltrasonicSensor import UltrasonicSensor


class Sensors(object):
    def __init__(self):
        self.sensors = [
            UltrasonicSensor("Front", 0, 2),
            UltrasonicSensor("Right", 3, 4),
            UltrasonicSensor("Back", 5, 6),
            UltrasonicSensor("Left", 25, 27)
        ]
        for sensor in self.sensors:
            sensor.start()

    def emit(self):
        return json.dumps([s.emit() for s in self.sensors])
