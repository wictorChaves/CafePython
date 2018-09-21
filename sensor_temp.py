import socket
import time

class socketClient(object):
    _socket = None
    _ip = '127.0.0.1'
    _port = 80

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port
        self.conection()


    def conection(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect(((self._ip, self._port)))
        self._socket.settimeout(10.0)

    def send(self, msg):
        try:
            self._socket.send(msg)
            return self._socket.recv(1024)
        except (socket.timeout, socket.error) as e:
            print "Error: {}!".format(e)
            print "Try again!"
            return self.send(msg)

    def close(self):
        self._socket = None

    def receive(self):
        return self._socket.recv(1024)


json = '[msg]:' + "temp" + '\r\n';
print json
#while True:
_socket = socketClient('192.168.0.53', 80)
confirm = _socket.send(json)
print(confirm.decode('utf-8'))
_socket.close()
