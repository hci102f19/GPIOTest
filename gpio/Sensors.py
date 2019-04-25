import json
import threading
from time import sleep

from gpio.DummySensor import DummySensor
from .UltrasonicSensor import UltrasonicSensor


class Sensors(threading.Thread):
    def __init__(self):
        super().__init__()

        self.sensors = [
            UltrasonicSensor("Front", 24, 25),
            UltrasonicSensor("Right", 22, 23),
            DummySensor("Back", 17, 4),
            UltrasonicSensor("Left", 17, 27)
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
        for s in self.sensors:
            s.stop()
        self.running = False
