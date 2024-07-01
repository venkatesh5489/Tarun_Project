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

# Load data from PostgreSQL into a DataFrame
df = pd.read_sql('SELECT * FROM nvda_stock_data', engine)

# Data cleaning and preprocessing
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)
df.sort_index(inplace=True)
df.dropna(inplace=True)

# Calculate moving averages
df['50_day_ma'] = df['close'].rolling(window=50).mean()
df['200_day_ma'] = df['close'].rolling(window=200).mean()

# Calculate volatility (standard deviation of closing prices over 30 days)
df['volatility'] = df['close'].rolling(window=30).std()

# Save the processed data back to the database
df.to_sql('nvda_stock_data_processed', engine, if_exists='replace', index=True)

print("Financial metrics calculated and data saved to database.")
print(df.head())