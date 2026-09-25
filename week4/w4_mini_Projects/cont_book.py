"""
1. Contact Book App using Dictionary
Add, view, search, and delete contacts stored in a dictionary.
"""

contacts = {}


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact '{name}' added.")


def view_contacts():
    if not contacts:
        print("No contacts saved.")
        return
    for name, info in contacts.items():
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")


def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"{name} -> Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def main():
    while True:
        print("\n----- Contact Book App -----")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()