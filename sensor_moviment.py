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

json = '[msg]:' + "{\"method\":\"out\", \"sensor\":\"mov\"}" + '\r\n';
print json
socket = socketClient('192.168.0.43', 80)
socket.send(json)
msg = socket.receive()
print(msg.decode('utf-8'))
socket.close()
