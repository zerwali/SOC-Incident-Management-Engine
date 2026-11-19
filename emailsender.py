import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

def send_email_notification(receiver_email, subject, body):
    load_dotenv()
    
    SENDER_EMAIL = os.getenv("SENDER_EMAIL")
    SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # Not your Gmail password

    # Build the email
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    # Connect to Gmail SMTP and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
    
