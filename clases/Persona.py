class Persona():
    def __init__(self):
        self.nombre = None
        self.apellido = None
        self.direccion = None
        self.telefono = None
        self.fecha_nacimiento = None

    def crear_persona(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        print("Se crea una persona")

    def leer_persona(self):
        print("Se lee el listado de personas")

    def actualizar_persona(self, nombre, apellido, direccion, telefono, fecha_nacimiento):
        print("Se actualiza una persona")

    def borra_persona(self):
        print("Se borra una persona")