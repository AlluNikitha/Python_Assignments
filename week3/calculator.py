"""
Assignment 3: Calculator Class with Exception Handling
"""


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None


def main():
    calc = Calculator()

    while True:
        print("\n----- Calculator -----")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid option. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numbers.")
            continue

        if choice == "1":
            print(f"Result: {calc.add(a, b)}")
        elif choice == "2":
            print(f"Result: {calc.subtract(a, b)}")
        elif choice == "3":
            print(f"Result: {calc.multiply(a, b)}")
        elif choice == "4":
            result = calc.divide(a, b)
            if result is not None:
                print(f"Result: {result}")


if __name__ == "__main__":
    main()