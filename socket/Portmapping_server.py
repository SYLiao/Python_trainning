import socket
import threading
import time
import sys

class portmappingServer(object):
    def __init__(self, IP, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((IP, PORT))
        self.reply = "Please input command."

    def Listen(self, ClientIP):
        self.socket.listen(200)
        while True:
            try:
                conn, info = self.socket.accept()
                if info[0] != ClientIP:
                    conn.send("You are not allowed to connect.".encode())
                    conn.close()
                    continue
                else:
                    conn.send("Connection success at {}.".format(time.time()).encode())
                    t = threading.Thread(target=self.Reply(), args=(conn, ))
                    t.start()
            except:
                print("There are some errors.")
        self.socket.close()

    def Reply(self, conn):
        while True:
            data = conn.recv(1024)
            data = data.decode()
            if data == "Hello":
                conn.send("The time is {}".format(time.timezone))
            elif data == "bye":
                conn.close()
                break
            else:
                conn.send('Please input "Hello"!')


if __name__ == "__main__":
    port = sys.argv[0]
    IP = sys.argv[1]
    Client = sys.argv[2]
    Server = portmappingServer(IP, port)
    Server.Listen(Client)


