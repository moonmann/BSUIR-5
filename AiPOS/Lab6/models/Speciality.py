from typing import List

from sqlalchemy import *
from sqlalchemy.orm import *

from . import Group
from . import Course
from .base import Base


class Speciality(Base):
    __tablename__ = "Speciality"
    id = mapped_column(Integer, primary_key=True)

    course_id = mapped_column(Integer, ForeignKey("Course.id"))
    course = relationship("Course", back_populates="speciality")

    name = Column(String)
    specialityNumber = Column(Integer, )

    groups = relationship("Group", back_populates="speciality")
