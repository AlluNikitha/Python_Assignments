"""
Mini Project (W1): Simple ATM Simulator
- User login (PIN-based)
- Options: check balance, deposit, withdraw
- Uses functions for each operation

Skill Gain: Loops, conditionals, modular programming.
"""

CORRECT_PIN = "1234"   # demo PIN
balance = 5000.0       # starting balance


def login():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin == CORRECT_PIN:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
    print("Too many failed attempts. Card blocked.")
    return False


def check_balance(balance):
    print(f"Your current balance is: ₹{balance:.2f}")
    return balance


def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    if amount <= 0:
        print("Invalid amount.")
        return balance
    balance += amount
    print(f"₹{amount:.2f} deposited successfully.")
    return balance


def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Invalid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")
    return balance


def main():
    global balance

    if not login():
        return

    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            balance = check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()