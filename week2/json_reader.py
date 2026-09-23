"""
Assignment 3: JSON File Reader
Load JSON data & print formatted output.
"""

import json


def read_json(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


def print_formatted(data, indent=0):
    prefix = "  " * indent
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                print(f"{prefix}{key}:")
                print_formatted(value, indent + 1)
            else:
                print(f"{prefix}{key}: {value}")
    elif isinstance(data, list):
        for item in data:
            print_formatted(item, indent)
            print(f"{prefix}---")
    else:
        print(f"{prefix}{data}")


def main():
    filename = input("Enter the JSON filename (e.g. data.json): ")

    try:
        data = read_json(filename)
        print("\nFormatted Output:\n")
        print_formatted(data)
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
    except json.JSONDecodeError:
        print("Invalid JSON format in the file.")


if __name__ == "__main__":
    main()