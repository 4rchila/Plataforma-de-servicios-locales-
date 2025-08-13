#clase para manejar los datos de cada proveedor (ID), nombre, servicio, calificacion
class Proveedor:
    def __init__(self, id, nombre, servicio, calificacion):
        self.id = id
        self.nombre = nombre
        self.servicio = servicio
        self.calificacion = calificacion
    
    def agregar_proveedor(self, id, nombre, servicio, calificacion):
        self.id = id
        self.nombre = nombre
        self.servicio = servicio
        self.calificacion = calificacion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Servicio: {self.servicio}, Calificación: {self.calificacion}"

    def __lt__(self, other):
        return self.id < other.id
