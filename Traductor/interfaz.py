from tkinter import *
from tkinter import ttk, PhotoImage
from threading import Thread


class Pantalla:
    raiz = None
    listLangSupp = None
    encenderApagar = None
    listMensajes = None
    labelImagen = None
    framePrincipal = None

    def __init__(self, cerrarServer):
        self.raiz = Tk()
        self.raiz.title('Traductor Ucuenca')
        self.raiz.resizable(0, 0)
        panelOpciones = ttk.Notebook(self.raiz, width='700', height='400')
        self.framePrincipal = Frame(panelOpciones)
        self.framePrincipal.pack()
        labelTexto = Label(
            self.framePrincipal, text='Servidor de traducción de texto\nUniversidad de Cuenca', font=('Verdana', 20))
        labelTexto.place(relx=0.5, y=50, anchor=CENTER)

        Label(self.framePrincipal, text='Elaborado por:',
              font=('Verdana', 16)).place(x=100, y=100)
        Label(self.framePrincipal, text='Fernando Tigre',
              font=('Verdana', 16)).place(x=250, y=150)
        Label(self.framePrincipal, text='Santiago Araujo',
              font=('Verdana', 16)).place(x=250, y=200)
        Label(self.framePrincipal, text='Andrés Sumba',
              font=('Verdana', 16)).place(x=250, y=250)

        frameHistorial = Frame(panelOpciones)
        frameHistorial.pack()
        Label(frameHistorial, text='Historial de peticiones:',
              font=('Verdana', 12)).place(x=50, y=15)
        self.listMensajes = Listbox(frameHistorial, width='40', height='15')
        self.listMensajes.place(x=30, y=60)
        self.listLangSupp = Listbox(frameHistorial, width='40', height='10')
        self.listLangSupp.place(x=360, y=60)
        idiomasEntrada = (
            'es-MX, Español latinoamerica',
            'en-US, American English',
            'pl-Pl, Polaco',
            'el-Gr, Griego',
            'de-Al, Aleman',
            'fr-Fr, Francés',
            'it-It, Italiano'
        )
        self.listLangSupp.insert(0, *idiomasEntrada)
        Label(frameHistorial, text='Idiomas soportados:',
              font=('Verdana', 12)).place(x=390, y=15)
        panelOpciones.add(frameHistorial, text='Historial')
        panelOpciones.add(self.framePrincipal, text='Acerca de')
        panelOpciones.pack()
        self.encenderApagar = ttk.Button(
            frameHistorial, text='Apagar')
        self.encenderApagar.place(x=550, y=300)
        self.encenderApagar.config(command=cerrarServer)

    def mainlooop(self):
        escudo = PhotoImage(file='escudo.png')
        self.labelImagen = Label(self.framePrincipal, image=escudo)
        self.labelImagen.place(x=580, y=0)
        self.raiz.mainloop()

        # self.encenderApagar.config(command=action)
