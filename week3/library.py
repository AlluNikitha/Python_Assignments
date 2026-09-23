"""
Assignment 2: Library Management System (OOP)
Add/remove books, issue/return books.
"""


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print("Book not found.")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_issued:
                    print(f"'{title}' is already issued.")
                else:
                    book.is_issued = True
                    print(f"You have issued '{title}'.")
                return
        print("Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_issued:
                    print(f"'{title}' was not issued.")
                else:
                    book.is_issued = False
                    print(f"You have returned '{title}'.")
                return
        print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)


def main():
    library = Library()

    while True:
        print("\n----- Library Management System -----")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Display All Books")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            title = input("Enter book title to issue: ")
            library.issue_book(title)
        elif choice == "4":
            title = input("Enter book title to return: ")
            library.return_book(title)
        elif choice == "5":
            library.display_books()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()