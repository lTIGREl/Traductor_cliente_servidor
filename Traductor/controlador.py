from servidor import Servidor
from interfaz import Pantalla
from threading import Thread
from cliente import cerrarServidor


class TraductorInteligente:
    pantalla = None
    idiomasEntrada = None
    idiomasSalida = None
    servidor = None
    hilo = None

    def cerrarServer(self):
        self.servidor.openClose = False
        cerrarServidor(self.servidor.address)
        self.pantalla.listMensajes.insert(0,'Servidor cerrado')

    def recargarPeticion(self, peticion=tuple):
        self.pantalla.listMensajes.insert(0, *peticion)

    def escucharPeticiones(self):
        self.servidor.run(self.recargarPeticion)

    def __init__(self):
        self.servidor = Servidor()
        self.pantalla = Pantalla(self.cerrarServer)
        self.hilo = Thread(target=self.escucharPeticiones)
        self.hilo.start()
        self.pantalla.mainlooop()
