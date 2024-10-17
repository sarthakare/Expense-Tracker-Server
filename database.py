from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base  # Import Base from models.py

# Database connection string
DATABASE_URL = "postgresql://postgres:root@localhost:5432/expense_tracker"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    # Create tables based on the Base class metadata (which should include User)
    Base.metadata.create_all(bind=engine)
