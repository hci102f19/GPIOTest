import json
import threading
from time import sleep

from gpiozero import DistanceSensor


class UltrasonicSensor(threading.Thread):
    def __init__(self, place, trigger, echo):
        super().__init__()

        self.place = place
        self.trigger = trigger
        self.echo = echo
        self.sensor = DistanceSensor(self.echo, self.trigger, max_distance=5)

        self.running = True

        self.history = []
        self.history_size = 10

    def run(self):
        while self.running:
            self.history = self.history[-(self.history_size - 1):] + [self.sensor.distance * 100]

            sleep(0.1)

    def data(self):
        if not self.history:
            return 0
        return round(sum(self.history) / len(self.history), 2)

    def emit(self):
        return json.dumps({
            "place": self.place,
            "value": self.data()
        })

    def stop(self):
        self.running = False
