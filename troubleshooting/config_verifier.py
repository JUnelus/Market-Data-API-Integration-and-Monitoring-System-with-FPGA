import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# List of required environment variables
required_vars = [
    'POSTGRES_HOST',
    'POSTGRES_USER',
    'POSTGRES_PASSWORD',
    'ALPHA_VANTAGE_API_KEY',
    'EMAIL_HOST',
    'EMAIL_PORT',
    'EMAIL_USER',
    'EMAIL_PASSWORD',
    'ALERT_EMAIL_TO'
]

def verify_configuration():
    """
    Function to verify that all required environment variables are set.
    """
    missing_vars = [var for var in required_vars if os.getenv(var) is None]

    if missing_vars:
        print(f"Missing environment variables: {', '.join(missing_vars)}")
    else:
        print("All required environment variables are properly set!")

if __name__ == "__main__":
    verify_configuration()
