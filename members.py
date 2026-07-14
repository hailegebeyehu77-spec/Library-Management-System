import sqlite3
from database import connection, cursor
from datetime import date


def add_member():
    name = input("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")

        return

    email = input("Enter your email: ")
    phone = input("Ennter your phone number: ")
    try:
        cursor.execute(''' INSERT INTO members(
              name,
              email,
              phone
                   ) 
              VALUES (?,?,?)''',
                       (
                           name,
                           email,
                           phone
                       ))

        connection.commit()
        print("Member added succssefully!")
    except sqlite3.IntegrityError:
        print("this email is registerd")


def display_members(members):
    for member in members:
        member_id, name, email, phone = member
        print(f"member ID: {member_id}")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone number: {phone}")


def view_members():
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()

    display_members(members)


def search_members():
    search = input("Enter member name: ")
    search = "%" + search + "%"

    cursor.execute("""SELECT * 
                   FROM members
                   WHERE name LIKE ?
                   """, (search,))
    members = cursor.fetchall()
    if not members:
        print("No member found")
        return

    display_members(members)


def update_member():
    member_id = int(input("Enter your member ID: "))
    new_name = input("Enter the new name: ")

    cursor.execute("""UPDATE members
                      SET name=?
                      WHERE id=?""",
                   (new_name, member_id,))
    if cursor.rowcount == 0:  # this is used to
        print("member not found.")

    else:
        connection.commit()
        print("member updated successfully!")


def delete_member():
    # 1. Ask for the book ID
    member_id = int(input("Enter the book ID: "))
    # 2. Execute DELETE FROM books WHERE id = ?
    cursor.execute(
        '''DELETE FROM members
           WHERE id=?''',
        (member_id,)
    )
    # 3. Check cursor.rowcount

    if cursor.rowcount == 0:
        print("member not found.")
    else:
        connection.commit()
        print("member deleted successfully!")
