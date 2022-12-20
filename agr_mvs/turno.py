from datetime import datetime
from agr_mvs.ticket import Ticket
import math

# Constante que nos expresa la longitud del turno que es 5'5 horas.
HORAS_TURNO = 5
# Constante para el paso de horas a minutos dentro de las funciones
MINUTOS_HORA = 60

class Turno:
    horas_turno: list            # Mediante este array introducimos dos datetime que nos indican el inicio y el fin del turno
    tickets: list                # tickets dentro de un Turno.
    fecha:  datetime             # fecha del Turno           
    S:int                       # Número de servidores del Turno
    def __init__(self, horas_turno, S, fecha):
        self.horas_turno = horas_turno
        self.fecha = fecha
        self.tickets = []
        self.S = S

    
    def setS(self,servidores):
        self.S = servidores
        

    # Añadimos un Ticket a la lista de tickets del Turno
    def addTicket(self, ticket):
        if (self.fecha.date() == ticket.FechaTicket.date()):
                if (ticket.FechaTicket.timestamp() >= self.horas_turno[0].timestamp() and ticket.FechaTicket.timestamp() <= self.horas_turno[1].timestamp()):
                    self.tickets.append(ticket)
        else:
            # Excepción del tipo IndexError en caso de que no se pueda añadir el Ticket
            raise IndexError("El Ticket no pertenece al Turno")
<<<<<<< HEAD
<<<<<<< HEAD
        
=======

 
    

>>>>>>> e6b8f15 (Reestructuracion atributos #20)
=======
        
>>>>>>> 0fe79d0 (Corrección Comentarios)
    '''
    Para el cálculo del µ, se ha decidido que el valor de µ será el máximo de clientes que se han atendido en una hora.
    Vamos pasando por las distintas horas del turno y viendo la afluencia que ha habido en cada hora para quedarnos con la 
    mayor afluencia (max_afluencia) que sería la maxima por hora, por tanto la pasamos a minutos al devolverla.
    '''
    def __maximo_clientes_atendidos(self):
        max_afluencia = 0
        afluencia = 0
<<<<<<< HEAD
        hora_actual = self.horas_turno[0].hour
        hora_fin = self.horas_turno[1].hour
=======
        hora_actual = int(self.horas_turno[0].hour)
        hora_fin = int(self.horas_turno[1].hour)
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
        while (hora_actual <= hora_fin):
            for ticket in self.tickets:
                hora = ticket.FechaTicket.hour
                if (hora == hora_actual):
                    afluencia += 1
            if (afluencia > max_afluencia):
                max_afluencia = afluencia
            hora_actual += 1
            afluencia = 0
<<<<<<< HEAD
        return (max_afluencia/MINUTOS_HORA)
=======
        return (max_afluencia/60.0)
>>>>>>> e6b8f15 (Reestructuracion atributos #20)

    '''
    Para el calculo de λ debemos de tener en cuenta que lo hacemos por hora,
    con fin de simplificar el cálculo, vamos a realizar una división entre el numero de tickets 
    que tenemos en el turno y las horas del turno. (Representamos cada cliente por un ticket sin valorare el importe del ticket)
    El resultado lo vamos a dividir entre 60 para trabajar con minutos en los posteriores cálculos.
    '''
<<<<<<< HEAD
    def __clientes_unidad_tiempo(self):
        return ((len(self.tickets)/HORAS_TURNO)/MINUTOS_HORA)
    
  
  
=======
    def calculo_clientes_unidad_tiempo(self):
        return ((len(self.tickets)/HORAS_TURNO)/60.0)
    
    '''
    Calculo variables elementales para el calculo de las variables estadísticas, 0 contiene µ, 1 contiene λ y 2 contiene S. 
    '''
    def calculo_variables_elementales(self):
        variables_elementales = []
        variables_elementales.append(self.calculo_maximo_clientes_atendidos())
        variables_elementales.append(self.calculo_clientes_unidad_tiempo())
        variables_elementales.append(self.S)   
        return variables_elementales     
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
    
    '''
    Mediante esta funcion vamos a poder calcular la saturacion de la tienda.
    '''
<<<<<<< HEAD
    def saturacion(self):
        µ = self.__maximo_clientes_atendidos()
        λ = self.__clientes_unidad_tiempo()
        saturacion = λ/(µ*self.S)
=======
    def calculo_saturacion(self):
        variables = self.calculo_variables_elementales()
        saturacion = variables[1]/(variables[0]*variables[2])
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
        return saturacion
    
    
    '''
    Calculo del numero promedio de clientes en la cola: Lq = p / Ls (Siendo Ls el numero promedio de clientes que entran al sistema)
    Ls = λ / (µ - λ)
    '''
<<<<<<< HEAD
    def promedio_clientes_cola(self):
        µ = self.__maximo_clientes_atendidos()
        λ = self.__clientes_unidad_tiempo()
        saturacion = self.saturacion()
        promedio_clientes = saturacion * ( λ / (µ - λ))
=======
    def calculo_promedio_clientes_cola(self):
        saturacion = self.calculo_saturacion()
        variables = self.calculo_variables_elementales()
        promedio_clientes = saturacion * (variables[1] / (variables[0] - variables[1]))
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
        return promedio_clientes

    '''
    Calculo del tiempo promedio de espera de un cliente en la cola Wq = Lq/λ ( Vamos a expresar λ en minutos para que sea mas orientativo el resultado) 
    '''
    
<<<<<<< HEAD
    def tiempo_espera_cola(self):
        λ = self.__clientes_unidad_tiempo()
        promedio_clientes = self.promedio_clientes_cola()
        tiempo_espera_cola = (promedio_clientes / λ)
=======
    def calculo_tiempo_espera_cola(self):
        variables = self.calculo_variables_elementales()
        promedio_clientes = self.calculo_promedio_clientes_cola()
        tiempo_espera_cola = (promedio_clientes / variables[1])
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
        return tiempo_espera_cola

    '''
    Mediante este calculo vamos a poder obtener la probabilidad de que un cliente tenga que esperar en la cola mas de 30 minutos
    que es el tiempo a partir del cual se considera que podemos perder clientes. la formula es: p * e^(-µ*(1-p)*t). En este caso
    vamos a expresar el parámetro µ en minutos para que el resultado que arroje se base en minutos y no en horas. 
    '''
<<<<<<< HEAD
    def probabilidad_espera_cola(self,minutos):
        saturacion = self.saturacion()
        µ = self.__maximo_clientes_atendidos()
        exp = ((-µ) * (1 - saturacion) * minutos)
        probabilidad_cola = saturacion * math.exp(exp)
        return probabilidad_cola

=======
    def calculo_probabilidad_espera_cola(self,minutos):
        saturacion = self.calculo_saturacion()
        variables = self.calculo_variables_elementales()
        exp = ((-variables[0]) * (1 - saturacion) * minutos)
        probabilidad_cola = saturacion * math.exp(exp)
        return probabilidad_cola
    
    def calculo_variables_estadísticas(self):
        print("La saturacion de la tienda es: "+ str(self.calculo_saturacion()))
        print("El numero promedio de clientes en la cola es de : " + str(self.calculo_promedio_clientes_cola()))
        print("El tiempo promedio de espera de un cliente en la cola es de : "+ str(self.calculo_tiempo_espera_cola())+ " minutos")
        print("La probabilidad de que un cliente espere en la cola mas de 30 minutos es de: "+ str(self.calculo_probabilidad_espera_cola(30)))
        
>>>>>>> e6b8f15 (Reestructuracion atributos #20)
        

        
        
