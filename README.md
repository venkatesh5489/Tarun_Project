# Data-Driven Financial Analysis Platform

## Overview

This project is a data-driven financial analysis platform that provides historical stock price data analysis through RESTful APIs and interactive visualizations.

## Features

- Data ingestion from Yahoo Finance.
- Data cleaning and preprocessing using Pandas.
- Calculation of financial metrics (moving averages, volatility).
- FastAPI for API development.
- Interactive visualization using Plotly.
- Unit testing with pytest.

## Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

1. Clone the repository:

   
   git clone https://github.com/venkatesh5489/Tarun_Project.git
   cd Tarun_Project
   
2. Install dependencies:

   "pip install -r requirements.txt"

3. Set up PostgreSQL database:

   Create a database named financial_data.
   Import historical stock price data CSV into the database.

4. Run the FastAPI server:

   "uvicorn api.main:app --reload"

5. Access the FastAPI endpoints:

   Raw stock data: http://localhost:8000/raw_data/
   Financial metrics: http://localhost:8000/financial_metrics/


7. Contributing
   
   Contributions are welcome! Please fork the repository and create a pull request with your improvements. Follow 
   the Contributing Guidelines for more details.

8. License
    
   This project is licensed under the MIT License - see the LICENSE file for details.



