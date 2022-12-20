import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agr_mvs.tienda import Tienda
from agr_mvs.turno import Turno
from agr_mvs.ticket import Ticket
from hamcrest import *
import pytest
from datetime import datetime
horario1 = []
horario1.append(datetime(2020, 12, 12, 13, 00))
horario1.append(datetime(2020, 12, 12, 18, 00))
tienda = Tienda("KFC")
turno1 = Turno(horario1, 1.0, datetime(2020, 12, 12, 00, 00))
ticket = []
minutos = [0,5,10,13,15,20,23,25,30,33,35,40,45,50,55]

######################## TURNO DE LA MAÑANA ############################

hora = 13
id = 1;
for i in range(1,5):
    for j in minutos:
        ticket.append(Ticket(id, datetime(2020, 12, 12, hora,j)))
        id += 1
    hora += 1

for tickets in ticket:
    turno1.addTicket(tickets)

'''
Calculo del numero promedio de clientes en la cola
'''
def test_promedio_clientes_cola():
    promedio_clientes = turno1.promedio_clientes_cola()
    assert_that(promedio_clientes, close_to(3.2, 0.1))

'''
Calculo del tiempo promedio de espera de un cliente en la cola
'''
def test_tiempo_espera_cola():
    tiempo_espera_cola = turno1.tiempo_espera_cola()
    assert_that(tiempo_espera_cola, close_to(16, 0.1))
    
'''
Calculo de la probabilidad de que un cliente espere en la cola mas de 25 minutos.
'''

def test_probabilidad_espera_cola():
    probabilidad_cola = turno1.probabilidad_espera_cola(25)
    assert_that(probabilidad_cola, close_to(0.23, 0.1))






