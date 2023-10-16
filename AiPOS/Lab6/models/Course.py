from sqlalchemy import *
from sqlalchemy.orm import *

from .base import Base


class Course(Base):
    __tablename__ = "Courses"
    id = Column(Integer, primary_key=True)
    title = Column(String)