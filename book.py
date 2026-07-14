# add a book
# update a book
# delete a book
# search books

class Book:

    def __init__(self, title, author, isbn, publication_year, total_copies, available_copies, category, ID):
        self.title = title
        self.author = author
        self.isbn = isbn  # international standard book number``
        self.publication_year = publication_year
        self.total_copies = total_copies
        self.available_copies = available_copies
        self.category = category
        self.ID = ID

    all_books = []
    # add a book

    def add_book(self):
        Book.all_books.append(self)
        print(f"Book '{self.title}' added successfully.")

    # update book information
    def update_book(self, title=None, author=None, isbn=None, publication_year=None, total_copies=None, available_copies=None, category=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        if publication_year:
            self.publication_year = publication_year
        if total_copies:
            self.total_copies = total_copies
        if available_copies:
            self.available_copies = available_copies
        if category:
            self.category = category
        print(f"Book '{self.title}' updated successfully.")
# delete a book

    def delete_book(self):
        Book.all_books.remove(self)
        print(f"Book '{self.title}' deleted successfully.")
    # search books, explaining the parameters and how they are used to filter the books first by title, then by author, then by isbn, then by publication year, and finally by category. If a parameter is not provided, it will not be used in the filtering process.
    # to be clear this code step by step filters the books based on the provided parameters, and returns a list of books that match all the specified criteria. If no parameters are provided, it will return all books in the collection.
    # =>let's see step by step how the search_books method works: first,
    # it initializes an empty list called searched_books to store the books that match the search criteria.
    # Then, it iterates through each book in the all_books list.
    # For each book, it checks if the title parameter is provided and if the book's title contains the specified title (case-insensitive).
    # If not, it continues to the next book. The same process is repeated for author, isbn, publication_year, and category.
    # If a book passes all the checks, it is added to the searched_books list. Finally,
    # the method prints the number of books found and returns the searched_books list.

    def search_books(self, title=None, author=None, isbn=None, publication_year=None, category=None):
        searched_books = []
        for book in Book.all_books:
            if title and title.lower() not in book.title.lower():
                continue
            if author and author.lower() not in book.author.lower():
                continue
            if isbn and isbn != book.isbn:
                continue
            if publication_year and publication_year != book.publication_year:
                continue
            if category and category.lower() not in book.category.lower():
                continue
            searched_books.append(book)
        print(f"Search results: {len(searched_books)} book(s) found.")
        return searched_books


b1 = Book("The Great Gatsby", "F. Scott Fitzgerald",
          "9780743273565", 1925, 5, 5, "Fiction", 10)
b2 = Book("To Kill a Mockingbird", "Harper Lee",
          "9780061120084", 1960, 3, 3, "Fiction", 2)
b3 = Book("1984", "George Orwell", "9780451524935", 1949, 4, 4, "Dystopian", 3)
b4 = Book("The Catcher in the Rye", "J.D. Salinger",
          "9780316769488", 1951, 2, 2, "Fiction", 4)
b5 = Book("Fiker eske mekaber", "Haddis Alemayehu",
          "9789994444444", 1965, 1, 1, "Fiction", 5)
b6 = Book("Pride and Prejudice", "Jane Austen",
          "9780141439518", 1813, 6, 6, "Romance", 6)
b3.add_book()
b1.add_book()
b2.add_book()
b6.add_book()
b4.add_book()
b5.add_book()
b6.update_book(title="haile",
               publication_year=1813, total_copies=7)
b3.delete_book()
b1.search_books(title="The Great Gatsby")
