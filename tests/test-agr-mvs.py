import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agr_mvs.enumturno import TipoTurno
from agr_mvs.tienda import Tienda
from agr_mvs.turno import Turno
from agr_mvs.ticket import Ticket
from hamcrest import *
import pytest
from datetime import datetime

tienda = Tienda("KFC")
turno1 = Turno(1, TipoTurno.ALMUERZO, 3.0, datetime(2020, 12, 12, 00, 00))
turno2 = Turno(2, TipoTurno.CENA, 3, datetime(2020, 12, 12, 00, 00))
ticket = []
ticket2 = []
minutos = [20, 25, 30, 35, 40, 45, 50, 55]

######################## TURNO DE LA MAÑANA ############################

hora = 13
for i in range(1, 6):
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[2])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[3])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[4])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[5])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora+1, minutos[2])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora+1, minutos[3])))
    ticket.append(Ticket(i, datetime(2020, 12, 12, hora+1, minutos[4])))
    hora += 1

for tickets in ticket:
    turno1.addTicket(tickets)


######################## TURNO DE LA TARDE ############################

hora = 19
for i in range(1, 6):
    print(hora)
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[0])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[1])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[2])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[3])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[4])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[5])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[6])))
    ticket2.append(Ticket(i, datetime(2020, 12, 12, hora, minutos[7])))
    hora += 1


for tickets in ticket2:
    turno2.addTicket(tickets)
'''
Test comprobación que se introducen los tickets correctamente en el turno de mañana
vamos intentando meter tickets fuera de hora y comparamos longitudes
'''


def test_turno_maniana_correcto():
    ticket_test = []
    len_inicial = len(turno1.Tickets)
    for i in range(19, 24):
        ticket_test.append(Ticket(i, datetime(2020, 12, 12, i, 30)))
    for tickets in ticket_test:
        turno1.addTicket(tickets)
    assert_that(len(turno1.Tickets), equal_to(len_inicial))


'''
Igual que el test anterior pero para el turno de tardes
'''


def test_turno_cena_correcto():
    len_inicial = len(turno2.Tickets)
    ticket_test = []
    for i in range(13, 19):
        ticket_test.append(Ticket(i, datetime(2020, 12, 12, i, 30)))
    for tickets in ticket_test:
        turno2.addTicket(tickets)
    assert_that(len(turno2.Tickets), equal_to(len_inicial))


'''
El cálculo de λ es dependiente del numero de tickets que tengamos, como el calculo se hace para luego trabajar en minutos, si por ejemplo tuvieramos un 
λ de 12 clientes/hora, esto sería 0,2 clientes/minuto, por tanto un valor razonable sería un λ entre 0 y 2.
'''


def test_calculo_λ():
    turno1.calculo_λ()
    turno2.calculo_λ()
    assert_that(turno1.getλ(), less_than_or_equal_to(2) and greater_than(0))
    assert_that(turno2.getλ(), less_than_or_equal_to(2) and greater_than(0))


'''
El cálculo de µ es dependiente de los tickets, como el calculo se hace para luego trabajar en minutos, si por ejemplo tuvieramos un 
µ de 15 clientes/hora, esto sería 0,25 clientes/minuto, por tanto un valor razonable sería un µ entre 0 y 2, al igual que hemos hecho con el test anterior.
'''


def test_calculo_µ():
    turno1.calculo_µ()
    turno2.calculo_µ()
    assert_that(turno1.getµ(), less_than_or_equal_to(2) and greater_than(0))
    assert_that(turno2.getµ(), less_than_or_equal_to(2) and greater_than(0))


'''
Todos los cálculos que vienen a continuación se van a realizar teniendo en cuenta que λ va a ser 0'2 clientes/minuto, µ va a ser 0'25 clientes/minuto
y que el numero de servidores que vamos a tener es 1. Tal y como se refleja en el enunciado del ejercicio que se ha especificado en el issue #22 

'''

'''
Test para comprobar la saturación
'''
def test_calculo_p():
    turno1.λ = 0.2
    turno1.µ = 0.25
    turno1.S = 1
    print(turno1)
    p = turno1.calculo_p()
    assert_that(p, close_to(0.8, 0.1))

'''
Calculo del numero promedio de clientes en la cola
'''
def test_calculo_Lq():
    Lq = turno1.calculo_L()
    assert_that(Lq, close_to(3.2, 0.1))

'''
Calculo del tiempo promedio de espera de un cliente en la cola
'''
def test_calculo_W():
    Wq = turno1.calculo_W()
    assert_that(Wq, close_to(16, 0.1))
    
'''
Calculo de la probabilidad de que un cliente espere en la cola mas de 25 minutos.
'''

def test_calculo_p_cola():
    Wq = turno1.calculo_P_Cola(25)
    assert_that(Wq, close_to(0.23, 0.1))


