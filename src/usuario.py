# Clase Usuario (objeto valor que representa a un usuario de la aplicación)

from dataclasses import dataclass

@dataclass
class Usuario:
    ID: str                 # ID única para cada usuario
    ubicacion: str          # Ubicación del usuario

    # Getters (el resto se implementarán cuando sean necesarios) #

    # Método get para obtener la ubicación de un usuario
    def getUbicacion (self):
        return self.ubicacion