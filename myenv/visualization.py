import pandas as pd
import plotly.graph_objs as go
from sqlalchemy import create_engine

# Database credentials
DB_USER = 'one_user'
DB_PASSWORD = '123456'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'financial_data'

# Create a connection to the database
engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Query data from PostgreSQL
query = """SELECT date, close, "50_day_ma", "200_day_ma" FROM nvda_stock_data_processed"""
df = pd.read_sql(query, engine, parse_dates=['date'])

# Create traces for the plot
trace1 = go.Scatter(x=df['date'], y=df['close'], mode='lines', name='NVDA Close Price')
trace2 = go.Scatter(x=df['date'], y=df['50_day_ma'], mode='lines', name='50-Day Moving Average')
trace3 = go.Scatter(x=df['date'], y=df['200_day_ma'], mode='lines', name='200-Day Moving Average')

# Create layout for the plot
layout = go.Layout(title='NVDA Stock Price with Moving Averages',
                   xaxis=dict(title='Date'),
                   yaxis=dict(title='Price'))

# Create figure object
fig = go.Figure(data=[trace1, trace2, trace3], layout=layout)

# Save the plot as an HTML file
fig.write_html('stock_visualization.html', auto_open=True)
