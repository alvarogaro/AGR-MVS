# Clase Tienda (entidad que representa cada Tienda de nuestra aplicación)

from src.empresa import Empresa
from src.Turno import Turno

class Tienda:
    # Nombre de la Tienda, Empresa para establecer el dato
    id: int                         # Identificador de la tienda
    nombre: str                     # Nombre de la tienda
    empresa: Empresa                # Empresa a la que pertenece la tienda
    turno: Turno                    # Turn

    # Getters (el resto se implementarán cuando sean necesarios) #

    # Método get para obtener el nombre de una tienda
    def getNombre (self):
        return self.nombre

    # Método get para obtener la empresa a la que pertenece la tienda
    def getEmpresa (self):
        return self.empresa

    # Método get para obtener los turnos asignados
    def getTurnos (self):
        return self.turnos