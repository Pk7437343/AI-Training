from sqlalchemy import select, func, desc
from sqlalchemy.orm import session
from sqlalchemy.exc import IntegrityError
from models.trainer_models import Trainer

def add_new_feedback(db:session, data): #Session → type hint & db → actual(session) object
    feedback = Trainer(**data.model_dump())
    db.add(feedback)
    db.commit()
    db.referesh(feedback)
    return feedback

def get_all_feedback(db:session):
    query = select(Trainer).order_by(Trainer.feedback_id)
    result = db.scalars(query).all()
    return result

def get_by_id(db:session, feedback_id:int):
    result = db.get(Trainer, feedback_id)

def update(db:session, feedback_id:int, data):
    feedback = db.get(Trainer, feedback_id)
    if feedback is None:
        return False
    for key, value in data.model_dump(exclude_unset=True #not destroy old data
                                      ).items():
        setattr(feedback, key, value)
        try:
            db.commit()
        except IntegrityError:
            db.rollback()
            raise
def delete(db:session, feedback_id:int):
    feedback = db.get(Trainer, feedback_id)
    db.delete(feedback)
    db.commit()
    return True
def search_by_trainer(db:session, trainer_name:str):
    query = select(Trainer).where(Trainer.trainer_name==trainer_name)
    result = db.scalars(query).all()
    return result