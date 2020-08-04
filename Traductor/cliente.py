import socket
def cerrarServidor(direction):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (direction, 6787)
    sock.connect(server_address)
    sock.close()
