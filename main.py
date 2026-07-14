import sqlite3
from database import connection, cursor
from datetime import date
from books import *
from members import *
from borrow import *
from reports import *
from books import add_book, view_books, search_book, update_book, delete_book
from members import add_member, view_members, search_members, update_member, delete_member
from borrow import borrow_book, return_book
from reports import (
    available_book,
    borrowed_books_report,
    library_statistics,
    member_borrow_history,
)

while True:
    print("\n===Library Management System===")
    print("1. Add a new book")
    print("2. View book information")
    print("3. Search book")
    print("4. Update book")
    print("5. Delete book")
    print("6. add members")
    print("7. view memebers")
    print("8. Borrow Book")
    print("9. Return book")
    print("10. view Borrowed books ")
    print("11. available_books")
    print("12. Borrowed books report")
    print("13. Librarystatistics")
    print("14. Search members")
    print("15 Member borrow history")
    print("16. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        update_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        add_member()
    elif choice == "7":
        view_members()
    elif choice == "8":
        borrow_book()
    elif choice == "9":
        return_book()
    elif choice == "10":
        view_borrowed_books()
    elif choice == "11":
        available_book()
    elif choice == "12":
        borrowed_books_report()
    elif choice == "13":
        library_statistics()
    elif choice == "14":
        search_members()
    elif choice == "15":
        member_borrow_history()
    elif choice == "16":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
connection.close()
