# Clase Empresa (objeto valor que guarda los datos de cada empresa)

from dataclasses import dataclass

@dataclass
class Empresa:
    nombre: str             # Nombre de la empresa
    listaTiendas: list      # Lista de Tiendas que pertenecen a esta empresa
    
    # Getters (el resto se implementarán cuando sean necesarios) #
    
    ## Constructor para la Clase Empresa, en su inicio no tenemos ninguna tienda sino que las tenemos que añadir
    def __init__(self, nombre):
        self.nombre = nombre
    
    # Añadimos una Tienda a la lista de tiendas de la empresa
    def addTienda (self, tienda):
        self.listaTiendas.append(tienda)

    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas
    
    