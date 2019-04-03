import socket

msgFromClient = "HELO"

bytesToSend = str.encode(msgFromClient)

# serverAddressPort = ("192.168.1.100", 20001)
serverAddressPort = ("127.0.0.1", 20001)

bufferSize = 1024

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)

while True:
    message, _ = UDPClientSocket.recvfrom(bufferSize)

    print(message)
