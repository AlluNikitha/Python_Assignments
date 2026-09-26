"""
Capstone Project (Week 4): Employee Data Analysis
Dataset: Employee Dataset (Kaggle) - employee_salary_dataset.csv

Tasks:
- Load CSV using Pandas
- Calculate average salary, department count
- Filter employees above a salary threshold
- Export results to a new CSV

Skill Gain: Pandas, CSV handling, filtering.

Setup:
    pip install pandas
"""

import pandas as pd

INPUT_FILE = "employee_salary_dataset.csv"
OUTPUT_FILE = "high_earners.csv"
SALARY_THRESHOLD = 80000


def load_data(filename):
    df = pd.read_csv(filename)
    print(f"Loaded {len(df)} employee records.\n")
    return df


def show_average_salary(df):
    avg_salary = df["Monthly_Salary"].mean()
    print(f"Average Monthly Salary (all employees): {avg_salary:.2f}")


def show_department_counts(df):
    counts = df["Department"].value_counts()
    print("\nEmployee count by department:")
    print(counts.to_string())


def filter_high_earners(df, threshold):
    filtered = df[df["Monthly_Salary"] > threshold]
    print(f"\nEmployees earning above {threshold}:")
    print(filtered.to_string(index=False))
    print(f"\n({len(filtered)} employees above the threshold)")
    return filtered


def export_results(df, filename):
    df.to_csv(filename, index=False)
    print(f"\nResults exported to '{filename}'.")


def main():
    df = load_data(INPUT_FILE)

    show_average_salary(df)
    show_department_counts(df)
    high_earners = filter_high_earners(df, SALARY_THRESHOLD)
    export_results(high_earners, OUTPUT_FILE)


if __name__ == "__main__":
    main()