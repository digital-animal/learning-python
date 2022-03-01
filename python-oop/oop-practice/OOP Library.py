import datetime
import random

class Library:
    current_books = {
        "War and Peace": 1,
        "Crime and Punishment": 2,
        "Pride and Prejudice": 2,
        "Anna Karenina" : 4,
        "Origin of Species": 1,
        "Theory of Everything": 2
    }

    issued_books = {}

    def __init__(self):
        pass
    def add_book(self, book_name):
        if book_name in Library.issued_books.keys():
            Library.issued_books[book_name] -= 1
            Library.current_books[book_name] += 1
        else:
            print("Invalid Book Name.")

    def issue_book(self, requested_book):
        if requested_book in Library.current_books.keys() and Library.current_books[requested_book] > 0:
            Library.current_books[requested_book] -= 1
            if requested_book not in Library.issued_books.keys():
                Library.issued_books[requested_book] = 1
            elif requested_book in Library.issued_books.keys():
                Library.issued_books[requested_book] += 1

            print("Book Issued Successfully for 14 Days")
            print(f"You must return the book within 4/9/2020")
            """
            implement datetime here
            """
        elif requested_book in Library.current_books.keys() and Library.current_books[requested_book] == 0:
            print("Sorry..this book is already issued to another user")
        elif requested_book not in Library.current_books.keys():
            print("Sorry..this book is not available in our library")

    def display_book_list(self):

        # print(Library.current_books.keys()) # debug print
        # print(Library.current_books.values()) # debug print

        print("## Currently Available Books: ")
        i = 1
        for book, quantity in Library.current_books.items():
            print(f"\t{str(i).zfill(3)} {book} : {quantity}")
            i += 1
        print()
        print("## Currently Issued Books: ")
        j = 1
        for book, quantity in Library.issued_books.items():
            print(f"\t{str(j).zfill(3)} {book} : {quantity}")
            j += 1


class UserRegistration(Library):
    user_data = {}

    def __init__(self):
        super().__init__()

    def register_user(self):
        pass


class User:
    def __init__(self):
        self.book_name = None
    # def __init__(self, name, id):
    #     self.name = name
    #     self.id = id
    def request_book(self):
        self.book_name = input("Enter Book Name> ")
        return self.book_name
    def return_book(self):
        self.book_name = input("Enter Book Name > ")
        return self.book_name


def main():
    # user = User("Zahid", id)
    user = User()
    library = Library()

    while True:
        print("\t======== Main Menu ========")
        print("\t1. Request A Book")
        print("\t2. Return A Book")
        print("\t3. Display Book List")
        print("\t4. Quit")
        choice = int(input(">> "))
        if choice == 1:
            requested_book = user.request_book()
            library.issue_book(requested_book)
        elif choice == 2:
            returned_book = user.return_book()
            library.add_book(returned_book)
        elif choice == 3:
            library.display_book_list()
        elif choice == 4:
            quit()

if __name__ == "__main__":
    main()

