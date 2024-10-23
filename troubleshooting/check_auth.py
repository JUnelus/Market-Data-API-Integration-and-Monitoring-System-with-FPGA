import requests
import os
from dotenv import load_dotenv
from monitoring.alert import send_alert  # Import the send_alert function for sending alerts

# Load environment variables from .env file
load_dotenv()

# Alpha Vantage API Key
API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
BASE_URL = 'https://www.alphavantage.co/query'


def check_authentication():
    """
    Function to check if the Alpha Vantage API key is valid.
    """
    url = f"{BASE_URL}?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=1min&apikey={API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        print("API Authentication Successful!")
    else:
        print(f"API Authentication Failed! Status Code: {response.status_code}")
        send_alert("API Authentication Alert", f"Failed API Authentication. Status Code: {response.status_code}")


if __name__ == "__main__":
    check_authentication()
