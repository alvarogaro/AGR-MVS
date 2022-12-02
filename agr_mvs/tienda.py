# Clase Tienda (entidad que representa cada Tienda de nuestra aplicación)
from agr_mvs.turno import Turno

class Tienda:
    # Nombre de la Tienda, Empresa para establecer el dato
    Nombre: str                     # Nombre de la tienda        
    Turnos: list                    # Turnos de la tienda

    # Getters (el resto se implementarán cuando sean necesarios) #
    def __init__(self, nombre):
        self.Nombre = nombre
        self.Turnos = []
        
    def add_Turno(self, turno):
        self.Turnos.append(turno)
    
    # Método get para obtener el Nombre de una tienda
    def getNombre (self):
        return self.Nombre

    # Método get para obtener los Turnos asignados
    def getTurnos (self):
        return self.Turnos
