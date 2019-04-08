from time import sleep

from GPIO.UltrasonicSensor import UltrasonicSensor

us = UltrasonicSensor("TEST", 17, 4)
us.start()

try:
    while True:
        print(us.emit())
        sleep(0.25)
except KeyboardInterrupt:
    us.stop()
