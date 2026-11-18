from fastapi import FastAPI
from services import customer_service as service
from schema.customer_schema import studentupdate, studentresponse, studentcreate, studentbase
from config.database import SessionLocal, engine, Base

app =FastAPI(
    title="Successful",
    version="1.0.1"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def getall():
    return{
        "message" : "You are succesfully made api"
    }

@app.get("/search {studentid}", response_model=studentresponse)
def get_by_id(studentid:int):
    db=SessionLocal()
    return service.get_by_studentid(db, studentid)

@app.post("/add", response_model=studentresponse)
def adding(jh_student : studentcreate): #convert json to class then dict then class then sqlalchemy orm then database row
    db = SessionLocal()
    return service.add(db, jh_student)


