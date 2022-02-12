from distutils.command.config import config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings 

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip-address/hostname>/<databasename>"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:yankee005@localhost/fastapi2"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#connect to database using ORM making a session and close once its over
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()