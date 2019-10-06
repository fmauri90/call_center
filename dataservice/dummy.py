from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from datetime import *
from datetime import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

# from datetime import datetime

engine = create_engine('sqlite:///call_center.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

company = Company("Riam",  datetime.strptime('2019-10-03', '%Y-%m-%d'),  datetime.strptime('2019-10-03', '%Y-%m-%d'), None, {'company': 'Riam', 'city': 'Verona'})
session.add(company)

company = Company("Del Bo",  datetime.strptime('2019-10-03', '%Y-%m-%d'),  datetime.strptime('2019-10-03', '%Y-%m-%d'), None, {'company': 'Del Bo', 'city': 'Milano'})
session.add(company)

company = Company("Fusco",  date(2019, 10, 3),  date(2019, 10, 3), None, {'company': 'Fusco', 'city': 'Roma'})
session.add(company)

technician = Technician(1,  {'name': 'Matteo', 'surname': 'Dal Molin', 'phone': '3289769453'}, '', 1, '')
session.add(technician)

technician = Technician(2,  {'name': 'Giuseppe', 'surname': 'Triolone', 'phone': '3289768444'}, '', 1, '')
session.add(technician)

condominium = Condominium(1,  {'name': 'Condominio Rosa', 'address': 'Via Trento,5', 'city': 'Verona'})
session.add(condominium)

condominium = Condominium(2,  {'name': 'Condominio Genova', 'address': 'Via Bolzano,10', 'city': 'Milano'})
session.add(condominium)

call = Call(1, 1, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Maurizio', 'surname': 'Girardi', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Girardelli', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)


call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Giacomelli', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Randazzi', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Giggs', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Digianni', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Bellaria', 'problem': 'Elevator is blocked'}, 1, '')
session.add(call)

# commit the record the database
session.commit()

session.commit()
