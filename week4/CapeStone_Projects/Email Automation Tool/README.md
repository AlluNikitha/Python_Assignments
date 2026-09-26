# Week 4 – Option 3: Email Automation Tool (Large Dataset)

## Dataset

`students_large.csv` — 200 sample students with realistic Indian
names and unique emails (Name, Email columns). Replace with a real
class list any time; just keep the same column headers.

## Tasks

- Read CSV
- Auto-send personalized emails (using `smtplib`)
- Add subject & message dynamically

**Skill Gain:** Python automation, real-world scripting.

## Setup

1. Create a Gmail **App Password**: https://myaccount.google.com/apppasswords
   (requires 2-Step Verification turned on first)
2. `pip install` nothing extra needed — `smtplib`, `csv`, `email`,
   `getpass` are all built into Python.

## Run

```
python email_automation_tool.py
```

- Enter your Gmail address and App Password when prompted
- Enter subject/message using `{name}` for automatic personalization
- Confirm before sending — the tool loops through all 200 rows and
  sends a personalized email to each recipient

## Note

**Sending 200 real emails at once can trigger Gmail's daily sending
limit** (500/day on free Gmail accounts, lower for brand-new
accounts) or get flagged as spam-like activity if sent too fast. For
testing, either:
- Use a small subset of `students_large.csv` first (e.g. copy the
  first 5 rows into a separate test file), or
- Point the script at your own email address repeated a few times

Only send to the full 200-row list once you've verified the tool
works correctly on a small batch.
