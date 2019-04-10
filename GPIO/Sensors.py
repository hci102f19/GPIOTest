import json
import threading
from time import sleep

from .UltrasonicSensor import UltrasonicSensor


class Sensors(threading.Thread):
    def __init__(self):
        super().__init__()

        self.sensors = [
            UltrasonicSensor("Front", 0, 2),
            UltrasonicSensor("Right", 3, 4),
            UltrasonicSensor("Back", 5, 6),
            UltrasonicSensor("Left", 25, 27)
        ]
        for sensor in self.sensors:
            sensor.start()

        self.running = True

        self.values = {}

    def run(self):
        while self.running:
            self.values = {sensor.place: sensor.data() for sensor in self.sensors}
            sleep(0.1)

    def emit(self):
        return json.dumps(self.values)

    def stop(self):
        self.running = False
