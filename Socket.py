import socket

class socketClient(object):
    socket = None

    def __init__(self, ip, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(((ip, port)))

    def send(self, msg):
        self.socket.send(msg)

    def close(self):
        self.socket.close()

    def receive(self):
        return self.socket.recv(10240)