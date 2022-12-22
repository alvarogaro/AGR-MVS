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
ticket =[]
servidores = 1
horario1.append(datetime(2020, 12, 12, 13, 00))
horario1.append(datetime(2020, 12, 12, 18, 00))
tienda = Tienda("KFC")
turno1 = Turno(horario1, servidores, datetime(2020, 12, 12, 00, 00))
minutos = [0,5,10,13,15,20,23,25,30,33,35,40,45,50,55]

######################## TURNO DE LA MAÑANA ############################

hora = 13
id = 1;
for i in range(1,5):
    for j in minutos:
        ticket.append(Ticket(id, datetime(2020, 12, 12, hora,j)))
        id += 1
    hora += 1

<<<<<<< HEAD

def array_Tickets(turno, ticket):
    for tickets in ticket:
        turno.addTicket(tickets)
        


array_Tickets(turno1,ticket)

'''
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 227ea8f (Documentacion Test  #26 #27)
En los siguientes test se va a calcular la saturacion, promedio clientes en la cola, espera en la cola y probabilidad en funcion del numero de servidores
y comprobamos que efectivamente cuando aumentamos el numero de servidores vamos a tener valores menores, por tanto aumentaría la productividad de la tienda
como hemos reflejado en el issue #26 vemos que la productividad es inversa a la saturacion, y la reforma de los locales va en relación al aumento de servidores
'''
<<<<<<< HEAD
=======

def array_Tickets(turno, ticket):
    for tickets in ticket:
        turno.addTicket(tickets)
        


array_Tickets(turno1,ticket)

>>>>>>> a00fb7a (productividad y reformas #26 #27)
=======
>>>>>>> 227ea8f (Documentacion Test  #26 #27)
def test_saturacion():
    saturacion1 = turno1.saturacion()
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    saturacion2 = test_turno.saturacion()
    assert_that(saturacion2, less_than(saturacion1))
<<<<<<< HEAD
=======
Calculo del numero promedio de clientes en la cola
'''
=======
    
    
>>>>>>> a00fb7a (productividad y reformas #26 #27)
def test_promedio_clientes_cola():
    promedio_clientes_1 = turno1.promedio_clientes_cola()
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    promedio_clientes_2 = test_turno.promedio_clientes_cola()
    assert_that(promedio_clientes_2, less_than(promedio_clientes_1))


def test_tiempo_espera_cola():
<<<<<<< HEAD
    tiempo_espera_cola = turno1.tiempo_espera_cola()
    assert_that(tiempo_espera_cola, close_to(16, 0.1))
>>>>>>> a042c13 (cambio planteamiento test #20)
    
    
def test_promedio_clientes_cola():
    promedio_clientes_1 = turno1.promedio_clientes_cola()
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    promedio_clientes_2 = test_turno.promedio_clientes_cola()
    assert_that(promedio_clientes_2, less_than(promedio_clientes_1))
=======
    promedio_espera_cola_1 = turno1.tiempo_espera_cola()
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    promedio_espera_cola_2 = test_turno.tiempo_espera_cola()
    assert_that(promedio_espera_cola_2, less_than(promedio_espera_cola_1))
<<<<<<< HEAD
'''
Calculo de la probabilidad de que un cliente espere en la cola mas de 25 minutos.
'''
>>>>>>> a00fb7a (productividad y reformas #26 #27)


def test_tiempo_espera_cola():
    promedio_espera_cola_1 = turno1.tiempo_espera_cola()
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    promedio_espera_cola_2 = test_turno.tiempo_espera_cola()
    assert_that(promedio_espera_cola_2, less_than(promedio_espera_cola_1))
=======
>>>>>>> c1e480e (cambio comentarios)


def test_probabilidad_espera_cola():
    probabilidad_espera_cola_1 = turno1.probabilidad_espera_cola(30)
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    probabilidad_espera_cola_2 = test_turno.probabilidad_espera_cola(30)
    assert_that(probabilidad_espera_cola_2, less_than(probabilidad_espera_cola_1))
    

<<<<<<< HEAD



<<<<<<< HEAD
=======
def test_probabilidad_espera_cola():
<<<<<<< HEAD
    probabilidad_cola = turno1.probabilidad_espera_cola(25)
    assert_that(probabilidad_cola, close_to(0.23, 0.1))
>>>>>>> a042c13 (cambio planteamiento test #20)
=======
    probabilidad_espera_cola_1 = turno1.probabilidad_espera_cola(30)
    test_turno = Turno(horario1, servidores+1, datetime(2020, 12, 12, 00, 00))
    array_Tickets(test_turno,ticket)
    probabilidad_espera_cola_2 = test_turno.probabilidad_espera_cola(30)
    assert_that(probabilidad_espera_cola_2, less_than(probabilidad_espera_cola_1))
    

# print(turno1.saturacion())
# print(turno1.promedio_clientes_cola())
# print(turno1.tiempo_espera_cola())
# print(turno1.probabilidad_espera_cola(30))
>>>>>>> a00fb7a (productividad y reformas #26 #27)

=======
>>>>>>> c1e480e (cambio comentarios)





