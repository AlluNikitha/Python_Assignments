# Week 4 – Capstone Project (Automation / Data Handling)

**Focus:** Full working project combining file handling, OOP, and libraries.

This repository contains three capstone project options. Each is a
complete, independent, working project with its own folder, script(s),
sample dataset, and setup instructions.

```
capstone/
├── option1-employee-analysis/
│   ├── Employee_data_Analysis.py
│   ├── employee_salary_dataset.csv
│   └── README.md
├── option2-covid-tracker/
│   ├── covid_tracker.py
│   └── README.md
└── option3-email-automation/
    ├── email_automation_tool.py
    ├── students.csv
    └── README.md
```

---

## Option 1: Employee Data Analysis Project

**Dataset:** Employee Dataset (Kaggle) — `employee_salary_dataset.csv`

**Tasks:**
- Load CSV using Pandas
- Calculate average salary, department count
- Filter employees above a salary threshold
- Export results to a new CSV

**Skill Gain:** Pandas, CSV handling, filtering.

### Setup
```
pip install pandas
```

### Run
```
python Employee_data_Analysis.py
```

### Sample Output
```
Loaded 50 employee records.

Average Monthly Salary (all employees): 82288.80

Employee count by department:
Department
Marketing     13
Operations    10
IT            10
Finance       10
HR             7

Employees earning above 80000:
 EmployeeID        Name Department  ...  Monthly_Salary
          1  Employee_1  Marketing  ...          111416
          2  Employee_2 Operations  ...           95271
...
(23 employees above the threshold)

Results exported to 'high_earners.csv'.
```

---

## Option 2: COVID-19 Data Tracker

**Dataset:** [COVID-19 Dataset (Our World in Data)](https://ourworldindata.org/covid-deaths) —
downloaded automatically by the script on first run.

**Tasks:**
- Load data using Pandas
- Display top 5 countries by total cases
- Plot bar chart (Matplotlib)

**Skill Gain:** Data visualization + analysis.

### Setup
```
pip install pandas matplotlib requests
```

### Run
```
python covid_tracker.py
```

### Sample Output
```
Downloading COVID-19 dataset...
Download complete.
Loaded data for 247 locations.

Top 5 countries by total cases:
     location  total_cases
United States  103436829.0
        China   99373219.0
        India   45041748.0
       France   38997490.0
      Germany   38437756.0

Chart saved to 'top5_covid_cases.png'.
```

---

## Option 3: Email Automation Tool

**Dataset:** CSV of student names & emails — `students.csv`

**Tasks:**
- Read CSV
- Auto-send personalized emails (using `smtplib`)
- Add subject & message dynamically

**Skill Gain:** Python automation, real-world scripting.

### Setup
1. Create a Gmail **App Password**: https://myaccount.google.com/apppasswords
   (requires 2-Step Verification enabled first)
2. No extra installs needed — `smtplib`, `csv`, `email`, `getpass` are
   all built into Python.

### Run
```
python email_automation_tool.py
```

### Sample Output
```
Email Automation Tool (via Gmail SMTP)
Loaded 4 recipients from students.csv.

Enter your Gmail address: your.email@gmail.com
Enter your App Password (input hidden):

Use {name} anywhere you want the recipient's name inserted automatically.
Enter email subject (e.g. 'Hello {name}!'): Hi {name}, Assignment Reminder
Enter email message (e.g. 'Dear {name}, ...'): Dear {name}, please submit your assignment by Friday.

This will send 4 email(s). Continue? (y/n): y
Sent to Nikitha <nikitha@example.com>
Sent to Arjun <arjun@example.com>
Sent to Priya <priya@example.com>
Sent to Ravi <ravi@example.com>

Done. 4 email(s) sent successfully.
```

*(Note: real credentials are entered securely at runtime and never
hardcoded or committed to this repository.)*

---

## Notes

- Each option is self-contained — no need to run all three to
  demonstrate any one of them.
- Sample datasets are included for testing; real datasets (a full
  Kaggle CSV, a real class list) can be swapped in without changing
  the code, as long as column names match.
- No real credentials, API keys, or personal data are committed to
  this repository.
