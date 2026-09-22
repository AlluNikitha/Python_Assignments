"""
Assignment 3: Even/Odd & Prime Number Checker
"""


def is_even(num):
    return num % 2 == 0


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    num = int(input("Enter a number: "))

    if is_even(num):
        print(f"{num} is Even")
    else:
        print(f"{num} is Odd")

    if is_prime(num):
        print(f"{num} is Prime")
    else:
        print(f"{num} is Not Prime")


if __name__ == "__main__":
    main()