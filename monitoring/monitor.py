import requests
import time
import os
from dotenv import load_dotenv
from alert import send_alert  # Import the send_alert function from alert.py

# Load environment variables from .env file
load_dotenv()

# Alpha Vantage API Key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'
SYMBOL = 'TSLA'

# Function to monitor API response
def check_api_status(symbol):
    url = f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={API_KEY}"
    try:
        start_time = time.time()
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        latency = time.time() - start_time
        return latency
    except requests.exceptions.RequestException as e:
        send_alert("API Monitoring Alert", f"API Error: {str(e)}")
        return None

if __name__ == "__main__":
    # Track start time
    start_time = time.time()

    # Run the script for 5 minutes (300 seconds)
    while time.time() - start_time < 300:  # 300 seconds = 5 minutes
        latency = check_api_status(SYMBOL)
        if latency:
            print(f"API response time: {latency} seconds")
        else:
            print("API check failed, alert sent.")
        time.sleep(60)  # Check every minute
    print("Script finished after running for 5 minutes.")
