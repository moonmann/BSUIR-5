from typing import List
from sqlalchemy import *
from sqlalchemy.orm import *

from . import Speciality
from .base import Base


class Course(Base):
    __tablename__ = "Course"
    id = mapped_column(Integer, primary_key=True)

    title = Column(String)
    stage = Column(Integer)

    speciality = relationship("Speciality", back_populates="course")
