import socket
from TextAPI import ApiTranslator


class Servidor:
    apitranslator = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    openClose = True
    connection = socket
    mensaje = None
    address = '127.0.0.1'

    def run(self, addPeticiones):
        self.apitranslator = ApiTranslator()
        self.sock.bind((self.address, 6787))
        self.sock.listen(1)
        while self.openClose:
            try:
                self.connection, client_address = self.sock.accept()
                data = self.connection.recv(4098)
                if (data and self.openClose):
                    self.mensaje = str(data.decode('utf-8'))
                    array = self.mensaje.split(':')
                    traduccion = self.apitranslator.traducirTexto(
                        array[2], array[1])
                    tupla = (array[0]+': '+array[2], array[1] +
                             ': '+traduccion, 'From: '+str(client_address))
                    data = traduccion.encode('utf-8')
                    addPeticiones(tupla)
                    self.connection.sendall(data)

            finally:
                self.connection.close()
