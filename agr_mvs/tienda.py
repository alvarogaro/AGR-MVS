# Clase Tienda (entidad que representa cada Tienda de nuestra aplicación)
from agr_mvs.turno import Turno

class Tienda:
    # Nombre de la Tienda, Empresa para establecer el dato
    Nombre: str                     # Nombre de la tienda        
    Turnos: list                    # Turnos de la tienda

    # Getters (el resto se implementarán cuando sean necesarios) #
    def __init__(self, nombre):
        self.nombre = nombre
        self.turnos = []
        
    def add_Turno(self, turno):
        self.turnos.append(turno)
    
    # Método get para obtener el nombre de una tienda
    def getNombre (self):
        return self.nombre

    # Método get para obtener la empresa a la que pertenece la tienda
    def getEmpresa (self):
        return self.empresa

    # Método get para obtener los turnos asignados
    def getTurnos (self):
        return self.turnos