from fastapi import FastAPI
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

app = FastAPI(
    title ="Customer",
    version = "1.0.1"
)
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {
        "message":"my home"
    }

@app.get("/getallcustomer", responsemodel = CustomerResponse)
def getall(re)