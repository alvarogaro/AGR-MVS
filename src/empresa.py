# Clase Empresa (objeto valor que guarda los datos de cada empresa)

from dataclasses import dataclass

@dataclass
class Empresa:
    nombre: str             # Nombre de la empresa (string)
    listaTiendas: list      # Lista de Tiendas que pertenecen a esta empresa (lista de datos de tipo Tienda)
    
    # Getters #

    # Método get para obtener el nombre de una empresa
    def getNombre (self):
        return self.nombre

    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas