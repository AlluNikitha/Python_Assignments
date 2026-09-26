"""
Option 3: Email Automation Tool
Dataset: CSV of student names & emails (students_large.csv)

Tasks:
- Read CSV
- Auto-send personalized emails (using smtplib)
- Add subject & message dynamically

Skill Gain: Python automation, real-world scripting.

SETUP REQUIRED before running:
1. You need a Gmail account (or any SMTP-supporting email provider).
2. Gmail requires an "App Password" instead of your normal password:
   - Go to https://myaccount.google.com/apppasswords
   - Enable 2-Step Verification if not already on
   - Generate an App Password for "Mail"
   - Use that 16-character password when prompted below
3. Never hardcode your real password in this file. It is entered
   securely at runtime (hidden input) and never saved anywhere.
4. students_large.csv must be in the same folder as this script, with
   columns: Name, Email
"""

import csv
import os
import smtplib
from email.message import EmailMessage
from getpass import getpass

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(SCRIPT_DIR, "students_large.csv")


def read_students(filename):
    with open(filename, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def build_message(sender_email, receiver_email, receiver_name, subject_template, body_template):
    # Dynamically insert the student's name into the subject and body
    subject = subject_template.format(name=receiver_name)
    body = body_template.format(name=receiver_name)

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(body)
    return msg


def send_emails(students, sender_email, sender_password, subject_template, body_template):
    sent_count = 0
    failed = []

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)

            for student in students:
                name = student["Name"]
                email = student["Email"]
                try:
                    msg = build_message(sender_email, email, name, subject_template, body_template)
                    server.send_message(msg)
                    print(f"Sent to {name} <{email}>")
                    sent_count += 1
                except Exception as e:
                    print(f"Failed to send to {name} <{email}>: {e}")
                    failed.append(name)

    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email/app password.")
        return
    except Exception as e:
        print(f"Could not connect to email server: {e}")
        return

    print(f"\nDone. {sent_count} email(s) sent successfully.")
    if failed:
        print(f"Failed for: {', '.join(failed)}")


def main():
    print("Email Automation Tool (via Gmail SMTP)")

    students = read_students(CSV_FILE)
    print(f"Loaded {len(students)} recipients from students_large.csv.\n")

    sender_email = input("Enter your Gmail address: ")
    sender_password = getpass("Enter your App Password (input hidden): ")

    print("\nUse {name} anywhere you want the recipient's name inserted automatically.")
    subject_template = input("Enter email subject (e.g. 'Hello {name}!'): ")
    body_template = input("Enter email message (e.g. 'Dear {name}, ...'): ")

    confirm = input(f"\nThis will send {len(students)} email(s). Continue? (y/n): ")
    if confirm.strip().lower() != "y":
        print("Cancelled.")
        return

    send_emails(students, sender_email, sender_password, subject_template, body_template)


if __name__ == "__main__":
    main()