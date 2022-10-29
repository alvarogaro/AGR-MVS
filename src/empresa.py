# Clase Empresa (objeto valor que guarda los datos de cada empresa)

from dataclasses import dataclass

@dataclass
class Empresa:
    nombre: str             # Nombre de la empresa
    listaTiendas: list      # Lista de Tiendas que pertenecen a esta empresa
    
    # Getters (el resto se implementarán cuando sean necesarios) #

    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas