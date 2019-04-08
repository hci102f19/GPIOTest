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

        self.data = 0

    def run(self):
        while self.running:
            self.data = self.sensor.distance * 100

            sleep(0.25)

    def emit(self):
        return json.dumps({
            "place": self.place,
            "value": round(self.data, 2)
        })

    def stop(self):
        self.running = False
