# Libraries
import time

import RPi.GPIO as GPIO

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

# set GPIO Pins

sensors = [
    {
        "location": "LEFT",
        "trigger": 17,
        "echo": 27
    },
    {
        "location": "RIGHT",
        "trigger": 22,
        "echo": 23
    },
    {
        "location": "FRONT",
        "trigger": 24,
        "echo": 25
    },
]

# set GPIO direction (IN / OUT)

for s in sensors:
    GPIO.setup(s['trigger'], GPIO.OUT)
    GPIO.setup(s['echo'], GPIO.IN)


def distance():
    for s in sensors:
        # set Trigger to HIGH
        GPIO.output(s['trigger'], True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(s['trigger'], False)

        start_time = time.time()
        stop_time = time.time()

        # save StartTime
        while GPIO.input(s['echo']) == 0:
            start_time = time.time()

        # save time of arrival
        while GPIO.input(s['echo']) == 1:
            stop_time = time.time()

        # time difference between start and arrival
        time_elapsed = stop_time - start_time
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (time_elapsed * 34300) / 2

        print("{}:".format(s['location']))
        print("Measured Distance = {0:.2f} cm".format(distance))


if __name__ == '__main__':
    try:
        while True:
            distance()
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
