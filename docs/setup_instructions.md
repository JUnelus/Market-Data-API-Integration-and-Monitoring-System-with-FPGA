# Market Data API Integration and Monitoring System Setup Instructions

This document provides step-by-step instructions to set up the **Market Data API Integration and Monitoring System**.

## Prerequisites

Before proceeding with the setup, ensure you have the following installed on your system:

1. **Python 3.11+**: [Download and install Python](https://www.python.org/downloads/)
2. **PostgreSQL**: [Download and install PostgreSQL](https://www.postgresql.org/download/)
3. **Virtual Environment**: (Optional but recommended)
4. **Alpha Vantage API Key**: Get a free API key from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
5. **Gmail App Password** (if using Gmail for alerts): [Generate an App Password](https://support.google.com/accounts/answer/185833?hl=en).

## 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/JUnelus/Market-Data-API-Integration-and-Monitoring-System-with-FPGA.git
```

## 2. Set Up a Virtual Environment (Optional but recommended)

Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## 3. Install Required Python Packages

Install the required dependencies listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, generate one from your installed packages:
```bash
pip freeze > requirements.txt
```

## 4. Set Up PostgreSQL Database

1. Install and configure PostgreSQL.
2. Create a database named `market_data`.

You can also use the provided `database_setup.py` script to create the database:

```bash
python database_setup.py
```

## 5. Create the `.env` File

In the root directory of the project, create a `.env` file to store your environment variables. Here’s an example of the required environment variables:

```bash
# PostgreSQL settings
POSTGRES_HOST=localhost
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

# Alpha Vantage API
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key

# Email settings for alert notifications
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
ALERT_EMAIL_TO=recipient_email@example.com
```

Make sure to replace the placeholders with your actual credentials.

## 6. Run the Initial Setup Scripts

1. **Verify Configuration**: Check that your `.env` file is properly configured by running:

   ```bash
   python config_verifier.py
   ```

2. **Create Database Table**: Ensure the `market_data` table is created by running:

   ```bash
   python main.py
   ```

## 7. Test the Email Alerts

Run the `alert.py` script to ensure that email alerts are working properly:

```bash
python monitoring/alert.py
```

If you receive the alert email, the setup is successful.

## 8. Schedule the Monitoring Script (Optional)

You can automate the execution of the monitoring script using a cron job (Linux/macOS) or Task Scheduler (Windows). For example, to schedule it every hour:

1. Open the crontab editor:
   ```bash
   crontab -e
   ```

2. Add the following line to run the monitoring script every hour:
   ```bash
   0 * * * * /bin/bash /path/to/your/project/cronjob.sh >> /path/to/your/project/cronjob.log 2>&1
   ```

