"""
3. Automate Email Sending with smtplib

SETUP REQUIRED before running:
1. You need a Gmail account (or any SMTP-supporting email provider).
2. Gmail blocks plain passwords for this — you must create an "App Password":
   - Go to https://myaccount.google.com/apppasswords
   - Enable 2-Step Verification if not already on
   - Generate an App Password for "Mail"
   - Use that 16-character password below (NOT your normal Gmail password)
3. Never upload your real password/app password to GitHub. Use the
   getpass() prompt below, or an environment variable, instead of
   hardcoding it in the file.
"""

import smtplib
from email.message import EmailMessage
from getpass import getpass


def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email/app password.")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    print("Email Sender (via Gmail SMTP)")
    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass("Enter your App Password (input hidden): ")
    receiver_email = input("Enter recipient's email: ")
    subject = input("Enter email subject: ")
    body = input("Enter email message: ")

    send_email(sender_email, sender_password, receiver_email, subject, body)


if __name__ == "__main__":
    main()