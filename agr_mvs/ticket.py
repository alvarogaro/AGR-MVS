from dataclasses import dataclass
from datetime import datetime

@dataclass
class Ticket:
    id: int                 # Identificador del ticket
    FechaTicket: datetime  # Fecha del ticket (Tipo datetime para sacar horas minutos y segundos).
    
    
    def __init__(self, id, fecha_ticket):
        self.id = id
        self.FechaTicket = fecha_ticket