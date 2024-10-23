import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# PostgreSQL credentials
host = os.getenv('POSTGRES_HOST')
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PASSWORD')
database = "market_data"

# Connect to PostgreSQL server
def create_database():
    try:
        conn = psycopg2.connect(
            host=host,
            user=user,
            password=password
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Check if database exists
        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{database}';")
        exists = cur.fetchone()

        # Create the database if it doesn't exist
        if not exists:
            cur.execute(sql.SQL(f"CREATE DATABASE {database};"))
            print(f"Database '{database}' created successfully.")
        else:
            print(f"Database '{database}' already exists.")

        cur.close()
        conn.close()

    except Exception as error:
        print(f"Error creating database: {error}")

if __name__ == "__main__":
    create_database()
