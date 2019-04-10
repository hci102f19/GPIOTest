from GPIO.UltrasonicSensor import UltrasonicSensor
from Server import Server

us = UltrasonicSensor("TEST", 17, 4)
us.start()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(us)

server.start()

while True:
    text = input()
    print(text)