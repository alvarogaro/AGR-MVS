# Clase Tienda (entidad que representa cada Tienda de nuestra aplicación)

from src.empresa import Empresa
from src.empleado import Empleado
from src.enums.enum_turno import Turno

class Tienda:
    nombre: str                     # Nombre de la tienda
    empresa: Empresa                # Empresa a la que pertenece la tienda
    ubicacion: str                  # Ubicación de la tienda
    turnos: dict(Empleado,Turno)    # Diccionario que guarda pares de personas y turnos asignados.
    pedidosTurno: dict(Turno,int)   # Diccionario que guarda turnos y pedidos que se han hecho en ese turno.

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