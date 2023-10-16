from sqlalchemy import *

from .base import Base


class Student(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    surName = Column(String)

