import socket
import time

PORT = 50000

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(('', PORT))
print("Connection start!")

while True:
    info, channel = socket_server.recvfrom(1024)
    print("connection from", channel)
    react = ""
    info = info.decode()
    if info == "Hello":
        react = "Please input your requirement.(time, host)"
    elif info == "time":
        react = "The time is {}.".format(time.time())
    elif info == "host":
        react = "The host is {}.".format(socket_server.getsockname())
    elif info == "Bye.":
        react = "Bye"
        break
    else:
        react = "Please input time or host!"
    socket_server.sendto(react.encode(), channel)

socket_server.close()