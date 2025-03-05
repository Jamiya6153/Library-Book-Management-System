class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True  # book abailable?

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # list of patron's borrowed books

class Library:
    def __init__(self):
        self.books = []  # all books wowzers
        self.patrons = []  # all patrons wowzers

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print(f"Added '{title}' by {author}.")

    def register_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(f"Registered {name}.")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None  # returns none if book aint there

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        return None  # returns none if patron aint there

    def borrow_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        if patron is None:
            print("Error: Patron not found.")
            return  # so you dont have to enter book name before it realizes the patron doesnt exist

        book = self.find_book(book_title)
        if book is None:
            print("Error: Book not found.")
        elif not book.available:
            print("Error: This book is already borrowed.")
        else:
            book.available = False
            patron.borrowed_books.append(book)
            print(f"'{book_title}' borrowed by {patron_name}.")

    def return_book(self, patron_name, book_title):
        patron = self.find_patron(patron_name)
        if patron is None:
            print("Error: Patron not found.")
            return  # same as before, returns early

        book = self.find_book(book_title)
        if book is None:
            print("Error: Book not found.")
        elif book not in patron.borrowed_books:
            print("Error: This book was not borrowed by this patron.")
        else:
            book.available = True
            patron.borrowed_books.remove(book)
            print(f"'{book_title}' returned by {patron_name}.")

def main():
    library = Library()
    while True:
        print("\n1. Add Book")
        print("2. Register Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(title, author)

        elif choice == "2":
            name = input("Enter patron name: ")
            library.register_patron(name)

        elif choice == "3":
            patron_name = input("Enter patron name: ")
            # Check if the patron exists first
            if library.find_patron(patron_name) is None:
                print("Error: Patron not found.")
            else:
                book_title = input("Enter book title: ")
                library.borrow_book(patron_name, book_title)

        elif choice == "4":
            patron_name = input("Enter patron name: ")
            # Check if the patron exists first
            if library.find_patron(patron_name) is None:
                print("Error: Patron not found.")
            else:
                book_title = input("Enter book title: ")
                library.return_book(patron_name, book_title)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()