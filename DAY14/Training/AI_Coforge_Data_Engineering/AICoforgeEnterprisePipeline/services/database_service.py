from sqlalchemy import create_engine
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from config.settings import(
    MYSQL_DATABASE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_USER
)

database_url= URL.create(
    drivername="mysql+pymysql",
    username=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host= MYSQL_HOST,
    database=MYSQL_DATABASE
)
    # port=3306,


engine = create_engine(
    database_url
)


def get_database_engine():
    return engine