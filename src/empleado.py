# Clase Empleado (objeto valor que representa un empleado de una tienda)

from dataclasses import dataclass

@dataclass(frozen=True)
class Empleado:
    ID: str             # ID única para cada empleado
    nombre: str         # Nombre completo del empleado

    # Getters (el resto se implementarán cuando sean necesarios) #

    # Método get para obtener el nombre completo de un empleado
    def getNombre (self):
        return self.nombre