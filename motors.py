from Socket import socketClient

#status = raw_input('Entre com o estado: ')
json = '[msg]:temp'# + status + '\r\n';
print json
socket = socketClient('192.168.0.68', 80)
socket.send(json)
msg = socket.receive()
print(msg.decode('utf-8'))
socket.close()
