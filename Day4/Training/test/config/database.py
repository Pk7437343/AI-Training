import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

class Base(DeclarativeBase):
    pass

database_url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    host=os.getenv("DB_HOST"),
    password=os.getenv("DB_PASSWORD"),
    port=int(os.getenv("DB_PORT", 3306)),
    database=os.getenv("DB_NAME", "Practicedb")
)


engine = create_engine(
    database_url
)

SessionLocal = sessionmaker(
    bind=engine
)

def getdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()