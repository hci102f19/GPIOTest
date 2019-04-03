import threading
from time import sleep

from gpiozero import DistanceSensor


class UltrasonicSensor(threading.Thread):
    def __init__(self, place, trigger, echo):
        super().__init__()

        self.place = place
        self.trigger = trigger
        self.echo = echo
        self.sensor = DistanceSensor(self.echo, self.trigger)

        self.data = 0

    def run(self):
        while True:
            self.data = self.sensor.distance * 100
            sleep(1)

    def emit(self):
        return self.data
