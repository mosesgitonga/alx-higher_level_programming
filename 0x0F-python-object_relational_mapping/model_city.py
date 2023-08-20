#!/usr/bin/python3
"""
city
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey

Base = declarative_base()


class City(Base):
    """
    cities table
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    state_id = Column(Integer, ForeignKey("state.id"), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True
                )
            )
    Base.metadata.create_all(engine)
