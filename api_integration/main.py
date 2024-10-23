import requests
import psycopg2
import time
from simulation.fpga_config import FPGAConfig  # Import FPGAConfig from fpga_config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Alpha Vantage API Key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'

# PostgreSQL database connection
conn = psycopg2.connect(
    host=os.getenv('POSTGRES_HOST'),
    database="market_data",
    user=os.getenv('POSTGRES_USER'),
    password=os.getenv('POSTGRES_PASSWORD')
)
cur = conn.cursor()

# Function to check if table exists and create if it doesn't
def create_table_if_not_exists():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS market_data (
        symbol VARCHAR(10),
        timestamp TIMESTAMP,
        open NUMERIC,
        high NUMERIC,
        low NUMERIC,
        close NUMERIC,
        volume NUMERIC
    );
    """
    cur.execute(create_table_query)
    conn.commit()

# Function to fetch market data
def fetch_market_data(symbol):
    url = f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to store data into PostgreSQL
def store_market_data(symbol, data):
    for timestamp, details in data['Time Series (1min)'].items():
        query = """
            INSERT INTO market_data (symbol, timestamp, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cur.execute(query, (
            symbol,
            timestamp,
            details['1. open'],
            details['2. high'],
            details['3. low'],
            details['4. close'],
            details['5. volume']
        ))
        conn.commit()

if __name__ == "__main__":
    # Ensure the table is created before storing data
    create_table_if_not_exists()

    # Initialize FPGAConfig and run the FPGA configuration and trading simulation
    fpga = FPGAConfig()
    fpga.configure_fpga()  # Configure the FPGA
    fpga.simulate_trading()  # Simulate low-latency trading

    # Track start time
    start_time = time.time()

    # Run the script for 5 minutes (300 seconds)
    while time.time() - start_time < 300:  # 300 seconds = 5 minutes
        # Fetch and store data for a stock (TSLA as an example)
        data = fetch_market_data('TSLA')
        store_market_data('TSLA', data)
        time.sleep(60)  # Fetch data every minute

    print("Script finished after running for 5 minutes.")
