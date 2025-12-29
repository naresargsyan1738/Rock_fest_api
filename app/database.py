from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://rock_user:rock_pass@localhost/rock_fest_db"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
class Base(DeclarativeBase):
    pass
