import sqlite3


# connect to the database (library.db), if it doesn't create(exist)
connection = sqlite3.connect("test_library.db")
# create a cursor object to execute SQL commands, it helps us to interact with the database and perform operations like creating tables, inserting data, and querying data .
# it's a messanger between the database and the python code, it allows us to send SQL commands to the database and retrieve the results.
cursor = connection.cursor()

# SQL command to create the books table, it helps us to define the structure of the table and specify the data types and constraints for each column. The table will store information about books in the library, including their title, author, category, ISBN, published year, total copies, and available copies.
# it creates a table called "books" with the following columns:
# id: an integer that serves as the primary key and is automatically incremented for each new book added.
# title: a text field that stores the title of the book and cannot be null.
# author: a text field that stores the author's name and cannot be null.
# category: a text field that stores the category or genre of the book and cannot be null
# isbn: a text field that stores the International Standard Book Number (ISBN) of the book and must be unique.
# published_year: an integer field that stores the year the book was published.
# total_copies: an integer field that stores the total number of copies of the book available in the library and cannot be null.
# available_copies: an integer field that stores the number of copies of the book currently available for borrowing and cannot be null.
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cursor.fetchall())
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    isbn TEXT UNIQUE,
    published_year INTEGER,
    total_copies INTEGER NOT NULL, 
    available_copies INTEGER NOT NULL)'''
)
# Create the members table if it doesn't already exist.
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS members (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT 
    
        )'''
)
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS borrow_records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    member_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    borrow_date TEXT NOT NULL,
    return_date TEXT,

    FOREIGN KEY(member_id) REFERENCES members(id),
    FOREIGN KEY(book_id) REFERENCES books(id)
    )'''
)
# insert a sample book into the books table, it helps us to add an initial record to the table for testing purposes. The sample book has the following details:
# title: "ALEWELEDEM"
# author: "ABEBE"
# category: "Fictune"
# isbn: "86458483"
# published_year: 1973
# total_copies: 5
# available_copies: 5


# save the changes
connection.commit()

print("Book table created successfully")
