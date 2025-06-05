'''
Lesson 24 - Environment variable
.env
dotenv
'''
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

def send_email(to_address, subject, body):
    msg = EmailMessage()
    msg['From'] = os.getenv('EMAIL_ADDRESS')
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.set_content(body)

    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as smtp:
        smtp.starttls()
        smtp.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
        smtp.send_message(msg)

def main():
    send_email(
        "redteainfusion@gmail.com",
        "Hello from Python!",
        "This is a test email with plain text."
    )

if __name__ == "__main__":
    main()