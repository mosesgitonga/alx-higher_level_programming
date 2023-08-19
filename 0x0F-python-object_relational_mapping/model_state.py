#!/usr/bin/python3
"""
this code connect to a database table and creates two columns
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
Base = declarative_base()


class State(Base):
    """this is the table name in which we will want to associate"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    """create engine to connect to mysql"""

    engine = create_engine(
            "mysql+pymysql://{}:{}@localhost:3306/{}.format(sys.argv[1],\
sys.argv[2], sys.argv[3], pool_pre_ping=True)")
    """create the table in the database"""
    Base.metadata.create_all(engine)
