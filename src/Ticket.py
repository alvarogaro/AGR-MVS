from dataclasses import dataclass
from datetime import datetime

@dataclass
#  Como dato alternativo sabemos que cada persona gasta una media de 6 euros por pedido
#  Esto nos servirá para poder calcular el promedio de clientes que atendemos. 
class Ticket:
    id: int                 # Identificador del ticket
    fecha_ticket: datetime  # Fecha del ticket (Tipo datetime para sacar horas minutos y segundos).
    importe: float          # Importe del ticket (Calculamos así el numero de clientes por pedido)
    
    
    # Getters (el resto se implementarán cuando sean necesarios) #

    # Método get para obtener las tiendas que pertenecen a la empresa
    def getListaTiendas (self):
        return self.listaTiendas
    