from fastapi import FastAPI, HTTPException
from service import customer_service
from schema.customer_schema import CustomerBase, CustomerCreate, CustomerResponse, CustomerUpdate
from config.database import Base, engine, create_engine, SessionLocal
from sqlalchemy import select, func
from service import customer_service as services
from sqlalchemy.exc import IntegrityError



app = FastAPI(
    title="My first api",
    version= "1.0.1"
)

Base.metadata.create_all(bind=engine)

# @app.get("/hommm")
# def home():
#     return {
#         "message" = "my homes"
#     }
@app.get("/")
def home():
    return{
        "message":"Welcome to Customer Management API"
    }
@app.get("/practice", response_model= list[CustomerResponse])
def getall():
    db = SessionLocal()
    customerdetails = services.get_all_customer(db)
    return customerdetails

@app.get("/practice/{CustomerID}", response_model=CustomerResponse)
def getCustomerBYID(CustomerId: int):
    db = SessionLocal()
    return services.get_all_customer_by_id(db, CustomerId)

@app.post("/add", response_model= CustomerResponse)
def add_employee(Customer:CustomerCreate): #for validation
    db= SessionLocal()

    try:
        new_customer = services.add_customer(db, Customer)
        return new_customer
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Customer already exists")
    finally:
        db.close()
