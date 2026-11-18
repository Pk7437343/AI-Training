import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.engine import URL
from dotenv import load_dotenv

load_dotenv()

class Base(DeclarativeBase):
    pass

databaseurl = URL.create(
    drivername= "pymysql+mysql",
    username=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT", "3306"),
    password=os.getenv("DB_PASSWORD")
    database=os.getenv("DB_NAME", "PR_DB")
)

engine = create_engine.URL(
    databaseurl
)
SessionLocal = sessionmaker(
    bind = engine
)

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()