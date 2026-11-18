from models.customer_model import student
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def get_by_studentid(db: Session, data):
    query = select(student).order_by(student.studentid)
    result = db.scalars(query)
    return result

def add(db: Session, data):
    adding_customer = student(**data.model_dump())
    db.add(adding_customer)
    db.commit()
    db.refresh(adding_customer)
    return adding_customer