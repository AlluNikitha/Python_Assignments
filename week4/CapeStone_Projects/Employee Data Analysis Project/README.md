# Week 4 – Capstone Project: Employee Data Analysis

## Dataset

`employee_salary_dataset.csv` (50 records)
Columns: EmployeeID, Name, Department, Experience_Years, Education_Level,
Age, Gender, City, Monthly_Salary

## Tasks

- Load CSV using Pandas
- Calculate average salary, department count
- Filter employees above a salary threshold (default: 80,000)
- Export results to a new CSV

**Skill Gain:** Pandas, CSV handling, filtering.

## Requirements

```
pip install pandas
```

## Run

```
python Employee_data_Analysis.py
```

Produces `high_earners.csv` containing employees earning above the
salary threshold. Adjust `SALARY_THRESHOLD` in the script to change it.
