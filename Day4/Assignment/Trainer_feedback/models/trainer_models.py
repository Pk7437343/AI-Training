from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date

class Trainer(Base):
    __tablename__ = "Trainerfeedback"

    feedback_id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True
    )

    learner_name = Column(
        String(50),
        nullable=False
    )

    trainer_name = Column(
        String(50),
        nullable=False
    )

    course_name = Column(
        String(40),
        nullable=False
    )

    session_date = Column(
        Date,
        nullable=False
    )

    content_rating = Column(
        Integer,
        nullable=False
    )

    trainer_rating = Column(
        Integer,
        nullable=False
    )

    hands_on_rating = Column(
        Integer,
        nullable=False
    )

    comments = Column(
        String(200),
        nullable=True
    )

    would_recommend = Column(
        Boolean,
        nullable=False
    )
