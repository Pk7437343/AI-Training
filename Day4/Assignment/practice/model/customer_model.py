from config.database import Base
from sqlalchemy import Column, String, Integer, Numeric

class Customer(Base):
    __tablename__ = "PR_DBT"

    CustomerId = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    CustomerName = Column(
        String(30),
        nullable=False
    )
    CustomerEmail = Column(
        String(30),
        nullable=False
    )
    CustomerAge = Column(
        Integer(30),
        nullable=False
    )