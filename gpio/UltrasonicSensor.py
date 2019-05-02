import threading
from time import sleep

from gpiozero import DistanceSensor


class UltrasonicSensor(threading.Thread):
    def __init__(self, place, trigger, echo):
        super().__init__()

        self.place = place
        self.trigger = trigger
        self.echo = echo

        self.sensor = DistanceSensor(self.echo, self.trigger, max_distance=2)

        self.running = True

        self.history = []
        self.history_size = 10

    def run(self):
        while self.running:
            distance = self.sensor.distance

            if distance < 1000:
                self.history = self.history[-(self.history_size - 1):] + [distance]

            sleep(0.1)

    def data(self):
        if not self.history:
            return {
                'value': 0,
                'distance': 0
            }
        val = round(sum(self.history) / len(self.history), 2)
        return {
            'value': val,
            'distance': val * 100
        }

    def emit(self):
        return {
            "place": self.place,
            "value": self.data()
        }

    def stop(self):
        self.running = False
