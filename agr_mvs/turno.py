from datetime import datetime
from agr_mvs.ticket import Ticket
import math

# Constante que nos expresa la longitud del turno que es 5'5 horas.
HORAS_TURNO = 5.5

class Turno:
    Id: int                      # Identificador del Turno
    Horas_Turno: list            # Mediante este array introducimos dos datetime que nos indican el inicio y el fin del turno
    Tickets: list                # Tickets dentro de un Turno.
    Fecha:  datetime             # Fecha del Turno
    µ: float                     # Clientes que son atendidos por unidad de tiempo (hora)
    λ: float                     # Clientes que llegan por unidad de tiempo (hora)
    S: float                     # Numero de TPV que tenemos disponibles (Nos los aporta la tienda como dato)           
            

    
    def __init__(self, id, horas_turno, S, Fecha, µ=None, λ=None, p=None):
        self.Id = id
        self.Horas_Turno = horas_turno
        self.Fecha = Fecha
        self.Tickets = []
        self.µ = µ
        self.S = S
        self.λ = λ

    def __str__(self):
        cadena = "-----------Objeto tipo Turno-----------\n"
        print(cadena)
        print("id =", self.Id)
        print("Tipo_turno =", self.Horas_Turno)
        print("Fecha =", self.Fecha)
        print("µ =", self.µ)
        print("λ =", self.λ)
        print("S =", self.S)
        print("Tickets =", self.Tickets)
        print("\n")
        return cadena
    # Añadimos un Ticket a la lista de Tickets del Turno
    def addTicket(self, ticket):
        if (self.Fecha.date() == ticket.FechaTicket.date()):
                if (ticket.FechaTicket.timestamp() >= self.Horas_Turno[0].timestamp() and ticket.FechaTicket.timestamp() <= self.Horas_Turno[1].timestamp()):
                    self.Tickets.append(ticket)
        else:
            # Excepción del tipo IndexError en caso de que no se pueda añadir el Ticket
            raise IndexError("El Ticket no pertenece al Turno")
            
    # Método get para obtener el nombre de una tienda
    def getNombre(self):
        return self.Nombre
    
    def getµ(self):
        return self.µ

    def getλ(self):
        return self.λ

    def getS(self):
        return self.S

    '''
    Para el cálculo del µ, se ha decidido que el valor de µ será el máximo de clientes que se han atendido en una hora.
    Se va a dividir entre 60 para trabajar con minutos en los posteriores cálculos.
    '''
    def calculo_µ(self):
        max_afluencia = 0
        afluencia = 0
        hora_actual = int(self.Horas_Turno[0].hour)
        hora_fin = int(self.Horas_Turno[1].hour)
        print(hora_actual)
        print(hora_fin)
        while (hora_actual <= hora_fin):
            for ticket in self.Tickets:
                hora = ticket.FechaTicket.hour
                if (hora == hora_actual):
                    afluencia += 1
            if (afluencia > max_afluencia):
                max_afluencia = afluencia
            hora_actual += 1
            afluencia = 0
        self.µ = (max_afluencia/60.0)

    '''
    Para el calculo de λ debemos de tener en cuenta que lo hacemos por hora,
    con fin de simplificar el cálculo, vamos a realizar una división entre el numero de tickets 
    que tenemos en el turno y las horas del turno. (Representamos cada cliente por un ticket sin valorare el importe del ticket)
    El resultado lo vamos a dividir entre 60 para trabajar con minutos en los posteriores cálculos.
    '''
    def calculo_λ(self):
        self.λ = (len(self.Tickets)/HORAS_TURNO)/60.0
    
    '''
    Calculo variables elementales para el calculo de las variables estadísticas
    '''
    def calculo_variables_elementales(self):
        if (self.µ == None or self.λ == None):
            self.calculo_µ()
            self.calculo_λ()
    
    '''
    Mediante esta funcion vamos a poder calcular la saturacion de la tienda.
    '''
    def calculo_saturacion(self):
        self.calculo_variables_elementales()
        saturacion = self.λ/(self.µ*self.S)
        return saturacion
    
    
    '''
    Calculo del numero promedio de clientes en la cola: Lq = p / Ls (Siendo Ls el numero promedio de clientes que entran al sistema)
    Ls = λ / (µ - λ)
    '''
    def calculo_promedio_clientes_cola(self):
        saturacion = self.calculo_saturacion()
        promedio_clientes = saturacion * (self.λ / (self.µ - self.λ))
        return promedio_clientes

    '''
    Calculo del tiempo promedio de espera de un cliente en la cola Wq = Lq/λ ( Vamos a expresar λ en minutos para que sea mas orientativo el resultado) 
    '''
    
    def calculo_tiempo_espera_cola(self):
        self.calculo_variables_elementales()
        promedio_clientes = self.calculo_promedio_clientes_cola()
        tiempo_espera_cola = promedio_clientes / self.λ
        return tiempo_espera_cola

    '''
    Mediante este calculo vamos a poder obtener la probabilidad de que un cliente tenga que esperar en la cola mas de 30 minutos
    que es el tiempo a partir del cual se considera que podemos perder clientes. la formula es: p * e^(-µ*(1-p)*t). En este caso
    vamos a expresar el parámetro µ en minutos para que el resultado que arroje se base en minutos y no en horas. 
    '''
    def calculo_probabilidad_espera_cola(self,minutos):
        saturacion = self.calculo_saturacion()
        exp = (-self.µ * (1 - saturacion) * minutos)
        probabilidad_cola = saturacion * math.exp(exp)
        return probabilidad_cola
    
    def calculo_variables_estadísticas():
        print("La saturacion de la tienda es: "+ str(Turno.calculo_saturacion()))
        print("El numero promedio de clientes en la cola es de : " + str(Turno.calculo_promedio_clientes_cola()))
        print("El tiempo promedio de espera de un cliente en la cola es de : "+ str(Turno.calculo_tiempo_espera_cola())+ " minutos")
        print("La probabilidad de que un cliente espere en la cola mas de 30 minutos es de: "+ str(Turno.calculo_probabilidad_espera_cola(30)))
        
        

        
        
