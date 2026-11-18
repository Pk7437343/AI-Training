from sqlalchemy import Column, Integer, String
from config.database import Base

class student(Base):
    __tablename__= "Practice"

    studentid = Column(
        Integer,
        primary_key=True,
        index= True,
        autoincrement=True
    )
    studentname = Column(
        String(30),
        nullable=False
    )
    studentemail = Column(
        String(100),
        nullable=False
    )
    studentage = Column(
        Integer, 
        nullable= False
    )