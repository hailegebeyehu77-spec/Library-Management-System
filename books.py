import sqlite3
from database import connection, cursor
from datetime import date


def add_book():
    # add a new book to the database
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    category = input("Enter the book category: ")
    isbn = input("Enter the book ISBN: ")
    published_year = int(input("Enter the book published year: "))
    total_copies = int(input("Enter the total number of copies: "))
    available_copies = int(input("Enter the number of available copies: "))

    cursor.execute("""
        INSERT INTO books(
         title,
         author,
         category,
         isbn,
         published_year,
         total_copies,
         available_copies
          )
         VALUES(?,?,?,?,?,?,?)
       """,    (
        title,
        author,
        category,
        isbn,
        published_year,
        total_copies,
        available_copies
    ))

    connection.commit()

    print("Book added successfully!")


def display_books(books):
    for book in books:
        book_id, title, author, category, isbn, published_year, total_copies, available_copies = book

        print(f"ID: {book_id}")
        print(f'Title: {title}')
        print(f'Author: {author}')
        print(f"Category: {category}")
        print(f'Isbn: {isbn}')
        print(f'Published_year: {published_year}')
        print(f'Total copies: {total_copies}')
        print(f'Available_copies: {available_copies}')
        print("-" * 40)


def view_books():
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()  # this is used to get result

    display_books(books)


def search_book():
    search = input("Enter book title: ")  # let's say we add Python
    search = "%" + search + "%"

    cursor.execute(
        # this means WHERE title LIKE '%Python%'
        "SELECT * FROM books WHERE title LIKE ?",
        (search,)
    )
    books = cursor.fetchall()  # to get results
    if not books:
        print("No books found")

        return

    display_books(books)


def update_book():
    new_title = input("Enter the new title: ")
    book_id = int(input("Enter the book id: "))
    cursor.execute(
        """UPDATE books
           SET title=? 
           WHERE id =?""",
        (new_title, book_id)
    )

    if cursor.rowcount == 0:  # this is used to
        print("Book not found.")

    else:
        connection.commit()
        print("Book updated successfully!")


def delete_book():
    # 1. Ask for the book ID
    book_ID = int(input("Enter the book ID: "))
    # 2. Execute DELETE FROM books WHERE id = ?
    cursor.execute(
        '''DELETE FROM books
           WHERE id=?''',
        (book_ID,)
    )
    # 3. Check cursor.rowcount

    if cursor.rowcount == 0:
        print("Book not found.")
    else:
        connection.commit()
        print("Book deleted successfully!")
