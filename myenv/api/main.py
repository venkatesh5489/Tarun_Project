from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List
import pandas as pd

# Database credentials
DB_USER = 'one_user'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'financial_data'

# Create a connection to the database
SQLALCHEMY_DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Initialize FastAPI app
app = FastAPI()


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/raw_data/", response_model=List[dict])
def get_raw_stock_data(db: Session = Depends(get_db)):
    """Endpoint to fetch raw stock data"""
    query = "SELECT * FROM nvda_stock_data"
    df = pd.read_sql(query, db.bind)
    return df.to_dict(orient='records')


@app.get("/financial_metrics/", response_model=List[dict])
def get_financial_metrics(db: Session = Depends(get_db)):
    """Endpoint to fetch calculated financial metrics"""
    query = """
    SELECT date, close, "50_day_ma", "200_day_ma", volatility FROM nvda_stock_data_processed
    """
    df = pd.read_sql(query, db.bind)
    return df.to_dict(orient='records')
