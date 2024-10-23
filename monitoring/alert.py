import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email settings from .env
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
ALERT_EMAIL_TO = os.getenv('ALERT_EMAIL_TO')

# Function to send email alerts
def send_alert(subject, message):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USER
    msg['To'] = ALERT_EMAIL_TO

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USER, ALERT_EMAIL_TO, msg.as_string())
        print(f"Alert sent to {ALERT_EMAIL_TO}")
    except Exception as e:
        print(f"Failed to send alert: {str(e)}")

if __name__ == "__main__":
    # Example usage
    subject = "API Monitoring Alert"
    message = "There is an issue with the API. Please check the logs for more details."
    send_alert(subject, message)
