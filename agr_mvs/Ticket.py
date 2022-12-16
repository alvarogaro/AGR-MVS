from dataclasses import dataclass
from datetime import datetime

@dataclass
#  Como dato alternativo sabemos que cada persona gasta una media de 6 euros por pedido
#  Esto nos servirá para poder calcular el promedio de clientes que atendemos. 
#  No va a ser necesario tener el importe del ticket ya que va a ser considerado como un cliente.
class Ticket:
    id: int                 # Identificador del ticket
    fecha_ticket: datetime  # Fecha del ticket (Tipo datetime para sacar horas minutos y segundos).
    
    
    # Getters (el resto se implementarán cuando sean necesarios) #
    def __init__(self, id, fecha_ticket):
        self.id = id
        self.fecha_ticket = fecha_ticket
    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas
    