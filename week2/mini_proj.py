"""
Mini Project (W2): Student Management System
- Store student data (name, marks, roll number) in a CSV file
- Add/Delete/Search functions
- Save changes permanently to file

Skill Gain: Data storage, file I/O, CRUD logic.
"""

import csv
import os

FILENAME = "students.csv"
FIELDNAMES = ["roll_number", "name", "marks"]


def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def load_students():
    with open(FILENAME, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_students(students):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    roll_number = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    students = load_students()
    students.append({"roll_number": roll_number, "name": name, "marks": marks})
    save_students(students)
    print(f"Student '{name}' added and saved.")


def delete_student():
    roll_number = input("Enter roll number to delete: ")
    students = load_students()
    filtered = [s for s in students if s["roll_number"] != roll_number]

    if len(filtered) == len(students):
        print("Student not found.")
    else:
        save_students(filtered)
        print(f"Student with roll number {roll_number} deleted.")


def search_student():
    roll_number = input("Enter roll number to search: ")
    students = load_students()

    for s in students:
        if s["roll_number"] == roll_number:
            print(f"Roll No: {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")
            return
    print("Student not found.")


def view_all():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    for s in students:
        print(f"Roll No: {s['roll_number']}, Name: {s['name']}, Marks: {s['marks']}")


def main():
    init_file()

    while True:
        print("\n----- Student Management System -----")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Search Student")
        print("4. View All Students")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_all()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()