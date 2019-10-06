from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from flask.json import JSONEncoder

engine = create_engine('sqlite:///call_center.db', echo=True)
Base = declarative_base()


############################################################


class Company(Base):
    """"""
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    name_company = Column(String)
    date_entered = Column(Date)
    date_change = Column(Date)
    date_cancel = Column(Date)
    data_company = Column(JSON)

    def __init__(self, name_company, date_entered, date_change, date_cancel, data_company):

        self.name_company = name_company
        self.date_entered = date_entered
        self.date_change = date_change
        self.date_cancel = date_cancel
        self.data_company = data_company

        # create table
        Base.metadata.create_all(engine)


class Technician(Base):
    """"""
    __tablename__ = "technicians"

    id_technician = Column(Integer, primary_key=True)
    id_company = Column(Integer)
    data_technician = Column(JSON)
    chat_id = Column(String)
    status = Column(Integer)

    def __init__(self, id_company, data_technician, chat_id, status):
        """"""
        self.id_company = id_company
        self.data_technician = data_technician
        self.chat_id = chat_id
        self.status = status

        # create table
        Base.metadata.create_all(engine)


class Condominium(Base):
    """"""
    __tablename__ = "condominiums"

    id_condominium = Column(Integer, primary_key=True)
    id_company = Column(Integer)
    data_condominium = Column(JSON)

    def __init__(self, id_company, data_condominium):
        """"""
        self.id_company = id_company
        self.data_condominium = data_condominium

        # create table
        Base.metadata.create_all(engine)


class Call(Base):
    """"""
    __tablename__ = "calls"

    id_call = Column(Integer, primary_key=True)
    id_company = Column(Integer)
    id_condominium = Column(Integer)
    date_call = Column(Date)
    data_call = Column(JSON)
    call_status = Column(Integer)

    def __init__(self, id_condominium, id_company, date_call,  data_call, call_status):
        """"""
        self.id_condominium = id_condominium
        self.id_company = id_company
        self.date_call = date_call
        self.data_call = data_call
        self.call_status = call_status

        # create table
        Base.metadata.create_all(engine)
