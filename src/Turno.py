
from datetime import datetime
from src.enums.enum_turno import TipoTurno
from src.Ticket import Ticket
# DUDAS: 
# Como expresar la longitud del turno que es 5'5 horas siempre
# Como hacer los test
# Cambios en la Estructura de pablo

class Turno:
    # Nombre de la Turno, Empresa para establecer el dato
    # La longitud de un Turno es: 5'5 horas
    # λ: Tasa media de llegada de clientes: Lo vamos a calcular mediante el numero de clientes que llegan y las horas que tenemos en el turno (5'5)
    # Se obtiene mediante registros de las cámaras y se hace una media.
    id: str                         # Identificador del Turno
    Tipo_turno: TipoTurno           # Los Turnos se dividen en dos tipos, almuerzos(1), Cenas(2)
    Tickets: list                   # Tickets dentro de un Turno.
    Fecha:  datetime
    µ : float                       # Clientes atendidos por unidad de Tiempo (Calculado con importe de los tickets)
    λ : float                       # Clientes que llegan por unidad de Tiempo 
    S : float                       # Numero de Máquinas TPV en funcionamiento en el Turno. (Similar a Número de Servidores)
    
    
    # Inicializamos Todos los Datos del Turno (Numero de máquinas disponibles, Tipo_Turno y id del Turno ), excepto los calculados y los Tickets
    def __init__(self,id,Tipo_turno,S,λ,Tickets=None,µ=None):
        self.id = id
        self.Tipo_turno = Tipo_turno
        self.Tickets = Tickets
        self.µ = µ
        self.S = S
        self.λ = λ
    
    # Añadimos un Ticket a la lista de Tickets del Turno
    def addTicket(self, ticket):
        self.Tickets.append(ticket)
    
    # Método get para obtener el nombre de una tienda
    def getNombre (self):
        return self.nombre

    # Método get para obtener la empresa a la que pertenece la tienda
    def getEmpresa (self):
        return self.empresa

    # Método get para obtener los turnos asignados
    def getTurnos (self):
        return self.turnos
    
    # Método para obtener el µ
    def getµ (self):
        return self.µ
    # Método para obtener el λ
    def getλ (self):
        return self.λ
    # Método para obtener el numero de Servidores (S)
    def getS (self):
        return self.S
    
  
        
        
    
    
    
    
    