from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATA_URL = 'postgresql://db_user:db_password@localhost:5432/mydb'

engine = create_engine(DATA_URL)

SessionLocal=sessionmaker(autocommit = False, autoflush=False, bind=engine)

base = declarative_base()