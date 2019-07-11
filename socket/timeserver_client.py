import socket

PORT = 50000

socket_client= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# socket_client.bind(('127.0.0.1', PORT))

socket_client.sendto("Hello".encode(), ('10.153.146.40', PORT))

while True:
    t, server = socket_client.recvfrom(1024)
    print(t.decode())
    a = input("Input your command:")
    socket_client.sendto(a.encode(), server)

socket_client.close()