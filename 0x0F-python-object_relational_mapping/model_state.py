#!/usr/bin/python3
"""
a python file that contains the class definition of a State
"""
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import sessionmaker, declarative_base
from sys import argv

engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3])
        )

Base = declarative_base()


class State(Base):
    """class state"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
