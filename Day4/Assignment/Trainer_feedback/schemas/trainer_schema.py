from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional

class Trainer_Base(BaseModel):
    learner_name: str
    trainer_name: str
    course_name: str
    session_date: date

    content_rating: int = Field(...,ge=1, le=5)
    trainer_rating: int = Field(..., ge=1,le=5)
    hands_on_rating: int = Field(..., ge=1, le= 5)
    comments: Optional[str] = None
    would_recommend: bool
class Trainer_create(Trainer_Base):
    pass
class Trainer_Update(Trainer_Base):
    content_rating: Optional[int] = Field(None, ge=1, le=5)
    trainer_rating: Optional[int] = Field(None, ge=1, le=5)
    hands_on_rating: Optional[int] = Field(None, ge=1, le=5)
    comments: Optional[str] = None
    would_recommend: bool

class Trainer_Response(Trainer_Base):
    feedback_id: int
    model_config = ConfigDict(from_attributes=True)
    #fastAPI + SQLAlchemy me ORM object ko Pydantic response me convert karne ke liye use hoti hai.
    #from_attributes=True allows Pydantic to create response models directly from SQLAlchemy ORM objects by reading their attributes instead of expecting a dictionary.
