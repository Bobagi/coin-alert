import os
import smtplib
import time
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, to_email):
    from_email = os.getenv("EMAIL")
    password = os.getenv("PASSWORD")

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

def clear_alerts():
    url = "https://bobagi.net/api/cryptoAlert/clearAlerts"
    try:
        response = requests.post(url)
        response.raise_for_status()
        print("Alerts cleared successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error while clearing alerts: {e}")

while True:
    subject = "Test Email from coin-watcher"
    body = "This is a test email."
    to_email = os.getenv("DESTINY")
    send_email(subject, body, to_email)
    print("Email sent successfully!")

    clear_alerts()

    time.sleep(600)  # Sleep for 10 minutes
