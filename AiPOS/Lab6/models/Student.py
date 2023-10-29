from sqlalchemy import *
from sqlalchemy.orm import relationship

from .base import Base


class Student(Base):
    __tablename__ = "Students"
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)

    dateOfBirth = Column(Date)
    studentNumber = Column(Integer,)
    gpa = Column(Float)

    group_id = Column(Integer, ForeignKey("Groups.id"))
    group = relationship("Group", back_populates="students")
