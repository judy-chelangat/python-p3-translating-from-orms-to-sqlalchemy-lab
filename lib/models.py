#!/usr/bin/env python3

from sqlalchemy import (Column, create_engine,String, Integer)
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())
    

    def __repr__(self):
        return f"student {self.id}"\
        + f"{self.name}, "\
        + f"grade {self.breed}"
   