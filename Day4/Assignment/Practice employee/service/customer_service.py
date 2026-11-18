from model.customer_model import Customer
from sqlalchemy.orm import Session
from sqlalchemy import select, func

def get_all_customer(db:Session):
    query = select(Customer).order_by(Customer.CustomerID)
    result=db.scalars(query)
    Customers=result.all()
    return Customers
def get_all_customer_by_id(db:Session, CustomerId):
    return db.get(Customer, CustomerId)

def add_customer(db:Session, data):
    customer_added = Customer(**data.model_dump())
    db.add(customer_added)
    db.commit()
    db.refresh(customer_added)
    return customer_added