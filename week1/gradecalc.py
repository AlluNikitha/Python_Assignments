"""
Assignment 2: Student Grade Calculator
Take marks as input, calculate average & assign grades.
"""


def calculate_average(marks):
    return sum(marks) / len(marks)


def assign_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    n = int(input("Enter number of subjects: "))
    marks = []

    for i in range(n):
        m = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(m)

    average = calculate_average(marks)
    grade = assign_grade(average)

    print(f"\nAverage marks: {average:.2f}")
    print(f"Grade: {grade}")


if __name__ == "__main__":
    main()