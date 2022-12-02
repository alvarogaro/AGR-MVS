
from agr_mvs.Turno import *
from agr_mvs.tienda import *
from agr_mvs.empresa import *
from agr_mvs.Ticket import *
from datetime import datetime


empresa = Empresa("NRSUR")
tienda = Tienda(1, "KFC", empresa)
turno1 = Turno(1, TipoTurno.ALMUERZO, 3, datetime(2020, 12, 12, 00, 00))
turno2 = Turno(2, TipoTurno.CENA, 3, datetime(2020, 12, 12, 00, 00))
ticket1 = Ticket(1, datetime(2020, 12, 12, 13, 30))
ticket11 = Ticket(1, datetime(2020, 12, 12, 13, 40))
ticket12 = Ticket(1, datetime(2020, 12, 12, 13, 50))
ticket13 = Ticket(1, datetime(2020, 12, 12, 13, 55))
ticket2 = Ticket(2, datetime(2020, 12, 12, 14, 30))
ticket3 = Ticket(3, datetime(2020, 12, 12, 15, 30))
ticket4 = Ticket(4, datetime(2020, 12, 12, 16, 30))
ticket5 = Ticket(5, datetime(2020, 12, 12, 17, 30))
ticket6 = Ticket(6, datetime(2020, 12, 12, 18, 30))
ticket7 = Ticket(7, datetime(2020, 12, 12, 19, 30))
ticket8 = Ticket(8, datetime(2020, 12, 12, 20, 30))
ticket9 = Ticket(9, datetime(2020, 12, 12, 20, 40))
ticket10 = Ticket(10, datetime(2020, 12, 12, 22, 30))

turno1.addTicket(ticket1)
turno1.addTicket(ticket2)
turno1.addTicket(ticket3)
turno1.addTicket(ticket4)
turno1.addTicket(ticket5)
turno1.addTicket(ticket6)
turno1.addTicket(ticket7)
turno1.addTicket(ticket8)
turno1.addTicket(ticket9)
turno1.addTicket(ticket10)
turno1.addTicket(ticket11)
turno1.addTicket(ticket12)
turno1.addTicket(ticket13)


turno1.calculo_μ()
turno1.calculo_λ()
print(turno1)
print("El μ es: ", turno1.getμ())
print("El λ es: ", turno1.getλ())


# turno1.addTicket(ticket3)
