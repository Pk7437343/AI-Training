from fastapi import FastAPI
from config.database import Base, SessionLocal, engine
from schemas.trainer_schema import Trainer_Base, Trainer_create, Trainer_Response, Trainer_Update
from services import trainer_services as services

app = FastAPI(
    title = "Fast Api",
    version = "1:0:1"
)
Base.metadata.create_all(bind=engine)

#SQLAlchemy reads all the registered models and creates their tables in the engine's database if they don't already exist.

@app.post("/add", response_model=Trainer_Response)
def add_feedback(data: Trainer_Response):
    db = SessionLocal()
    return services.add_new_feedback(db,data)

@app.get("/get_all_feedback", response_model= list[Trainer_Response])
def get_feedback():
    db = SessionLocal()
    return services.get_all_feedback(db)

@app.get("/get_feedback_by_id{feedback_id}", response_model=Trainer_Response)
def get_feedback_by_id(feedback_id):
    db = SessionLocal()
    return services.get_by_id

@app.get("/update{feedback_id}", response_model=Trainer_Response)
def update(feedback_id:int, data:Trainer_Update):
    db = SessionLocal()
    return services.update(db, feedback_id, data)

@app.delete("/delete/{feedback_id}", response_model=Trainer_Response)
def delete(feedback_id:int):
    db = SessionLocal()
    deleted = services.delete(db, feedback_id)
    if deleted:
        return {"message": "feedback deleted successfully"}
    return {"message": "unable to find feedback"}
@app.get("/Search_by_trainer/{trainer_name}", response_model= list[Trainer_Response])
def Search_by_trainer(trainer_name:str):
    db = SessionLocal()
    return services.search_by_trainer(db, trainer_name)