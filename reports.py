import sqlite3
from database import connection, cursor
from datetime import date
from books import *
from members import *
from borrow import *
# list borrowed books
# list available books
# show overdue books
# most borrowed books


def view_borrowed_books():
    cursor.execute("""
        SELECT
              members.name,
              books.title,
              borrow_records.borrow_date,
              borrow_records.return_date
              FROM borrow_records
              JOIN members
              ON borrow_records.member_id=members.id
              JOIN books
              ON borrow_records.book_id =books.id
    """)
    records = cursor.fetchall()

    if not records:
        print("No borrow records found.")
        return

    for record in records:
        member_name, book_title, borrow_date, return_date = record

        if return_date is None:
            return_date = "Not Returned"

        print(f"Member: {member_name}")
        print(f"Book: {book_title}")
        print(f"Borrowed: {borrow_date}")
        print(f"Returned: {return_date}")
        print("-" * 40)


"""output become:- 
Member: Haile
Book: Python
Borrowed: 2026-07-13
Returned: None
----------------------------------------

Member: John
Book: SQL
Borrowed: 2026-07-12
Returned: 2026-07-13
----------------------------------------"""


def available_book():

    cursor.execute("""
        SELECT * FROM books
        WHERE available_copies > 0
        ORDER BY title
    """)

    books = cursor.fetchall()
    if not books:
        print("No available books.")
        return
    display_books(books)


def borrowed_books_report():
    cursor.execute(""" SELECT * 
                        FROM books
                        WHERE available_copies < total_copies
                        ORDER BY title
                    """)
    books = cursor.fetchall()
    if not books:
        print("No books are currently borrowed. ")
        return
    display_books(books)


def library_statistics():
    cursor.execute(""" SELECT
                       COUNT(*) FROM books
                   
                   """)
    result = cursor.fetchone()
    total_books = result[0]  # to get the actual number
    print(f"Total Books: {total_books}")

    cursor.execute("""SELECT COUNT(*)
                     FROM members
                   """)
    result = cursor.fetchone()
    total_members = result[0]
    print(f"Total members: {total_members}")

    cursor.execute(""" SELECT COUNT(*)
                      FROM books
                      WHERE available_copies<total_copies""")

    result = cursor.fetchone()
    total_available_copies = result[0]
    print(f"Total available copies: {total_available_copies}")
    cursor.execute(""" SELECT SUM(available_copies)
                     FROM books
            
                    """)
    result = cursor.fetchone()
    available_copies = result[0]
    print(f"Sum of available copies: {available_copies}")


def member_borrow_history():
    try:
        member_id = int(input("Enter member ID: "))
    except ValueError:
        print("Please enter a value number")
        return
    cursor.execute('''SELECT
                   members.name,
                   borrow_records.borrow_date,
                   borrow_records.return_date,
                   books.title
                   FROM borrow_records
                   JOIN members
                   ON borrow_records.member_id=members.id
                   JOIN books
                   ON borrow_records.book_id = books.id  
                   WHERE borrow_records.member_id =?
                      ''',
                   (member_id,))
    result = cursor.fetchall()
    if not result:
        print("No history found")
        return
    for record in result:
        name, borrow_date, return_date, title = record
        print(f"Name: {name}")
        print(f"Borrow date: {borrow_date}")
        print(f"Return date: {return_date}")
        print(f"Book title: {title}")
    if return_date is None:
        return_date = "Not Returned"
