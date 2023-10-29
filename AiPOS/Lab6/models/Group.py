from sqlalchemy import *
from sqlalchemy.orm import *

from . import Speciality
from .base import Base


class Group(Base):
    __tablename__ = "Groups"
    id = mapped_column(Integer, primary_key=True)

    groupNumber = Column(Integer,)
    receipt_date = Column(Date)
    expiration_date = Column(Date)

    speciality_id = mapped_column(Integer, ForeignKey("Speciality.id"))
    speciality = relationship("Speciality", back_populates="groups")

    students = relationship("Student", back_populates="group")


