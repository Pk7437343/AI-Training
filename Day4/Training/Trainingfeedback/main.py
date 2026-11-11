from fastapi import FastAPI
from config.database import Base, engine, SessionLocal
from schemas.employee_schema import EmployeeResponse, EmployeeUpdate, EmployeeCreate, EmployeeBase
from services import employee_service as service

app= FastAPI(
  title="my first api",
  version="1.0.1"
)
#Database engine 


@app.get("/")
def home():
    return{
        "message": "fff"
    }

Base.metadata.create_all(bind=engine)  
#Whatever tables are defined in the models, if they aren't in the database, create them.

@app.get("/employees", response_model=list[EmployeeResponse])
def getallemployee():
  db = SessionLocal()
  return service.get_all_employees(db)

@app.get("/employees/{employee_id}", response_model=EmployeeResponse)
def getEmployeesById(employee_id:int):
  db = SessionLocal()
  return service.get_employee_by_id(db, employee_id)