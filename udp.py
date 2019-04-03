from GPIO.Sensors import Sensors
from Server import Server

sensors = Sensors()

server = Server("0.0.0.0", 20001)
server.message_loop.emits(sensors)

server.start()
