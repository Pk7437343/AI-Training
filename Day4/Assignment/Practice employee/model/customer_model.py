from sqlalchemy import(Column,Integer,String,Numeric)
from config.database import Base

class Customer(Base):
    __tablename__ = "Practice"

    CustomerID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    CustomerName = Column(String(100), nullable=False)
    CustomerEmail = Column(String(100), nullable=False)
    CustomerAge = Column(Integer, nullable= False)
