
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
    # Los Turnos se dividen en dos tipos, almuerzos(1), Cenas(2)
    Tipo_turno: TipoTurno
    Tickets: list                   # Tickets dentro de un Turno.
    Fecha:  datetime
    # Clientes atendidos por unidad de Tiempo (Calculado con importe de los tickets)
    µ: float
    λ: float                       # Clientes que llegan por unidad de Tiempo
    # Numero de Máquinas TPV en funcionamiento en el Turno. (Similar a Número de Servidores)
    S: float

    # Inicializamos Todos los Datos del Turno (Numero de máquinas disponibles, Tipo_Turno y id del Turno ), excepto los calculados y los Tickets
    def __init__(self, id, Tipo_turno, S, λ, Tickets=None, µ=None):
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
    def getNombre(self):
        return self.nombre

    # Método get para obtener la empresa a la que pertenece la tienda
    def getEmpresa(self):
        return self.empresa

    # Método get para obtener los turnos asignados
    def getTurnos(self):
        return self.turnos

    # Método para obtener el µ
    def getµ(self):
        return self.µ
    # Método para obtener el λ

    def getλ(self):
        return self.λ
    # Método para obtener el numero de Servidores (S)

    def getS(self):
        return self.S

      # Método para calcular el µ
    '''
   Para el cálculo de µ simplificaremos el problema y lo calcularemos teniendo en cuenta la hora del turno con mayor afluencia, y ese va a ser el valor.
    '''

    def calculo_µ(self):
        max_afluencia = 0
        afluencia = 0
        if (self.Tipo_turno == TipoTurno.ALMUERZO):
            hora_actual = 13
            hora_fin = 18
            while (hora_actual <= hora_fin):
                for ticket in self.Tickets:
                    if (ticket.fecha_ticket.hour == hora_actual):
                        afluencia += 1
                if (afluencia > max_afluencia):
                    max_afluencia = afluencia
                hora_actual += 1
            self.µ = max_afluencia
        else:
            hora_actual = 18
            hora_fin = 23
            while (hora_actual <= hora_fin):
                for ticket in self.Tickets:
                    if (ticket.fecha_ticket.hour == hora_actual):
                        afluencia += 1
                if (afluencia > max_afluencia):
                    max_afluencia = afluencia
                hora_actual += 1
            self.µ = max_afluencia

    '''
    Cuando calculamos λ vamos a hacer una simplificación del problema por tanto se va a realizar una media entre las horas que tiene un 
    turno y el numero de ventas que hemos tenido.
    '''

    def calculo_λ(self):
        self.λ = len(self.Tickets)/5.5
