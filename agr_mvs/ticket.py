from dataclasses import dataclass
from datetime import datetime

@dataclass
class Ticket:
    Id: int                 # Identificador del ticket
    Fecha_Ticket: datetime  # Fecha del ticket (Tipo datetime para sacar horas minutos y segundos).
    
    
    def __init__(self, id, fecha_ticket):
        self.id = id
        self.fecha_ticket = fecha_ticket
    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas
    