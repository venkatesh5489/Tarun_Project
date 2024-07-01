import pandas as pd
from sqlalchemy import create_engine

# Database credentials
DB_USER = 'one_user'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'financial_data'

# Create a connection to the database
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Load CSV data into a DataFrame
csv_file_path = 'NVDA (1).csv'  # Update with your actual CSV file path
df = pd.read_csv(csv_file_path)

# Rename columns to match PostgreSQL conventions
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Write DataFrame to PostgreSQL
df.to_sql('nvda_stock_data', engine, if_exists='replace', index=False)

print("Data ingestion completed.")
