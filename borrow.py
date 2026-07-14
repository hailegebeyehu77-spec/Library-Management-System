import sqlite3
from database import connection, cursor
from datetime import date


def borrow_book():
    member_id = int(input("Enter your member ID: "))
    book_id = int(input("Enter the book ID: "))

    # check if member exists
    cursor.execute("SELECT*FROM members WHERE id =?",
                   (member_id,))
    member = cursor.fetchone()
    if member is None:
        print("Member not found.")
        return

    # check if book exists
    cursor.execute("SELECT * FROM books WHERE id =?",
                   (book_id,))
    book = cursor.fetchone()
    if book is None:
        print("Book is not found")
        return
    #
    available_copies = book[7]

    if available_copies == 0:
        print("Sorry, this book is not available")
        return  # "Stop executing this function immediately and go back to the main program."

    borrow_date = str(date.today().isoformat())

    cursor.execute(
        ''' INSERT INTO borrow_records(
            member_id,
            book_id,
            borrow_date
        )
        VALUES(?,?,?)
        ''',
        (member_id, book_id, borrow_date)
    )
    cursor.execute(
        """
           UPDATE books
           SET available_copies = available_copies - 1
           WHERE id = ?
    """,
        (book_id,)
    )

    connection.commit()
    print("Book borrowed successfully!")


def return_book():
    member_id = int(input("Enter your member ID: "))
    book_id = int(input("Enter your Book ID: "))
    cursor.execute(
        """SELECT * FROM borrow_records
         WHERE member_id=? 
         AND book_id=? 
         AND return_date IS NULL""",
        (member_id, book_id,))

    record = cursor.fetchone()

    if record is None:
        print("No active borrow record found.")
        return

    return_date = str(date.today().isoformat())
    cursor.execute("""UPDATE borrow_records 
                      SET return_date =? 
                      WHERE member_id =?
                      AND book_id=?
                      AND return_date IS NULL""",
                   (return_date, member_id, book_id,))
    cursor.execute("""
                   UPDATE books
                   SET available_copies=available_copies+1
                   WHERE id =? """,
                   (book_id,))

    connection.commit()
    print("Book returned successfully!")
