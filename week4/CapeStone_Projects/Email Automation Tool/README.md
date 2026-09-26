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

## How to Run

1. Install requirements (none extra needed — `smtplib`, `csv`, `email`,
   `getpass` all come built into Python)
2. Make sure `students_large.csv` is in the same folder as
   `email_automation_tool.py`
3. Open a terminal in that folder and run:
   ```
   python email_automation_tool.py
   ```
4. Follow the prompts:
   - Gmail address
   - App Password (hidden input, see Setup above)
   - Subject line (use `{name}` for personalization)
   - Message body (use `{name}` for personalization)
   - Confirm with `y` to send

## Sample Output

```
Email Automation Tool (via Gmail SMTP)
Loaded 200 recipients from students_large.csv.

Enter your Gmail address: your.email@gmail.com
Enter your App Password (input hidden):

Use {name} anywhere you want the recipient's name inserted automatically.
Enter email subject (e.g. 'Hello {name}!'): Hi {name}, Assignment Reminder
Enter email message (e.g. 'Dear {name}, ...'): Dear {name}, please submit your assignment by Friday.

This will send 200 email(s). Continue? (y/n): y
Sent to Ayaan Sharma <ayaan.sharma@example.com>
Sent to Riya Rao <riya.rao@example.com>
Sent to Kiara Iyer <kiara.iyer@example.com>
...

Done. 200 email(s) sent successfully.
```

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
