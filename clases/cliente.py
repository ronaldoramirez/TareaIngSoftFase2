import Persona
class cliente(Persona):
    def _init_(self):
        super()
        self.nit

    def crear_cliente(self):
        print("Se crea una cliente")

    def leer_cliente(self):
        print("Se lee el listado de cliente")

    def actualizar_cliente(self):
        print("Se actualiza una cliente")

    def borra_cliente(self):
        print("Se borra un cliente")