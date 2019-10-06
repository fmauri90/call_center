import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *
from datetime import *
# from datetime import datetime

engine = create_engine('sqlite:///call_center.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

company = Company("Riam",  datetime.strptime('2019-10-03', '%Y-%m-%d'),  datetime.strptime('2019-10-03', '%Y-%m-%d'), None, {'company': 'Riam', 'City': 'Verona'})
session.add(company)

company = Company("Del Bo",  datetime.strptime('2019-10-03', '%Y-%m-%d'),  datetime.strptime('2019-10-03', '%Y-%m-%d'), None, {'company': 'Del Bo', 'City': 'Milano'})
session.add(company)

company = Company("Fusco",  date(2019, 10, 3),  date(2019, 10, 3), None, {'company': 'Fusco', 'City': 'Roma'})
session.add(company)

technician = Technician(1,  {'name': 'Matteo', 'Surname': 'Dal Molin', 'Phone': '3289769453'}, '', 1, '')
session.add(technician)

technician = Technician(2,  {'name': 'Giuseppe', 'Surname': 'Triolone', 'Phone': '3289768444'}, '', 1, '')
session.add(technician)

condominium = Condominium(1,  {'name': 'Condominio Rosa', 'Address': 'Via Trento,5', 'City': 'Verona'})
session.add(condominium)

condominium = Condominium(2,  {'name': 'Condominio Genova', 'Address': 'Via Bolzano,10', 'City': 'Milano'})
session.add(condominium)

call = Call(1, 1, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Maurizio', 'surname': 'Girardi', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Girardelli', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)


call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Giacomelli', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Randazzi', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Giggs', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Digianni', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

call = Call(2, 2, datetime.strptime('2019-09-30', '%Y-%m-%d'), {'name': 'Mauro', 'surname': 'Bellaria', 'Problem': 'Elevator is blocked'}, 1, '')
session.add(call)

# commit the record the database
session.commit()

session.commit()
