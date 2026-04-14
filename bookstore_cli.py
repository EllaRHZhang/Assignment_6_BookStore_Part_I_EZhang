import sqlite3

#connect to bookstore.db
DB_NAME = "bookstore.db"

def print_divider() -> None:
    print("\n" + "-" * 40)

def pause() -> None:
    input("\nPress Enter to continue...")

#display a menu
def print_menu() -> None:
    print_divider()
    print("Bookstore Menu")
    print("1. View all categories")
    print("2. View all books")
    print("3. View books in a category")
    print("4. Search books by title")
    print("5. Add a new book")
    print("6. Update a book price")
    print("7. Delete a book")
    print("8. View Read Now books")
    print("9. Quit")

def welcome_screen() -> None:
    print_divider()
    print("Welcome to the Bookstore CLI")
    print("Use the menu to browse and manage your books.")
    pause()

#1. View all categories
def view_categories(cursor: sqlite3.Cursor) -> None:
    #retrieve all categories from the category table
    cursor.execute(
        """
        SELECT categoryId, categoryName, categoryImage
        FROM category
        ORDER BY categoryId
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Categories")

    if rows:
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Image: {row[2]}")
    else:
        print("No categories found.")

#2. View all books
def view_books(cursor: sqlite3.Cursor) -> None:
    #retrieve all books and display key book information
    cursor.execute(
        """
        SELECT bookId, title, author, isbn, price, image, readNow
        FROM book
        ORDER BY title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books")

    if rows:
        for row in rows:
            read_now_text = "Yes" if row[6] == 1 else "No"
            print(
                f"ID: {row[0]} | Title: {row[1]} | Author: {row[2]} | "
                f"ISBN: {row[3]} | Price: ${row[4]:.2f} | "
                f"Image: {row[5]} | Read Now: {read_now_text}"
            )
    else:
        print("No books found.")

#3. View books in a category
def view_books_in_category(cursor: sqlite3.Cursor) -> None:
    category_id = input("Enter a category id: ").strip()

    cursor.execute(
        """
        SELECT book.bookId, book.title, book.author, category.categoryName, book.price
        FROM book
        JOIN category ON book.categoryId = category.categoryId
        WHERE category.categoryId = ?
        ORDER BY book.title
        """,
        (category_id,)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Books in Category")

    if rows:
        for row in rows:
            print(
                f"Book ID: {row[0]} | Title: {row[1]} | "
                f"Author: {row[2]} | Category: {row[3]} | Price: ${row[4]:.2f}"
            )
    else:
        print("No books found for that category.")

#4. Search books by title
def search_by_title(cursor: sqlite3.Cursor) -> None:
    keyword = input("Enter a title keyword: ").strip()

    cursor.execute(
        """
        SELECT bookId, title, author, price
        FROM book
        WHERE title LIKE ?
        ORDER BY title
        """, 
        (f"%{keyword}%",)
    )
    rows = cursor.fetchall()

    print_divider()
    print("Matching Books")

    if rows:
        for row in rows:
            print(
                f"Book ID: {row[0]} | Title: {row[1]} | "
                f"Author: {row[2]} | Price: ${row[3]:.2f}"
            )
    else:
        print("No matching books found.")

#5. Add a new book
def add_book(cursor: sqlite3.Cursor) -> None:
    try:
        print_divider()
        print("Add a New Book")

        category_id = int(input("Enter category id: ").strip())
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()
        price = float(input("Enter price: ").strip())
        image = input("Enter image filename: ").strip()
        read_now = int(input("Enter readNow (0 or 1): ").strip())

        if read_now not in (0, 1):
            print("readNow must be 0 or 1.")
            return

        #parameterized insert
        cursor.execute(
            """
            INSERT INTO book (categoryId, title, author, isbn, price, image, readNow)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (category_id, title, author, isbn, price, image, read_now)
        )

        print_divider()
        print("Book added.")

    except ValueError:
        print_divider()
        print("Invalid input.")
    except sqlite3.IntegrityError as error:
        print_divider()
        print("Database error:", error)

#6. Update a book price
def update_price(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id: ").strip())
        new_price = float(input("Enter the new price: ").strip())

        #update the price for a book using primary key
        cursor.execute(
            "UPDATE book SET price = ? WHERE bookId = ?",
            (new_price, book_id)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found with that id.")
        else:
            print("Price updated successfully.")

    except ValueError:
        print_divider()
        print("Invalid input. Please enter numeric values.")

#7. Delete a book
def delete_book(cursor: sqlite3.Cursor) -> None:
    try:
        book_id = int(input("Enter book id to delete: ").strip())

        cursor.execute(
            "DELETE FROM book WHERE bookId = ?",
            (book_id,)
        )

        print_divider()
        if cursor.rowcount == 0:
            print("No book found with that id.")
        else:
            print("Book deleted successfully.")

    except ValueError:
        print_divider()
        print("Invalid input. Please enter a numeric book id.")

#8. show only books with readNow = 1
def view_read_now_books(cursor: sqlite3.Cursor) -> None:
    cursor.execute(
        """
        SELECT bookId, title, author, price
        FROM book
        WHERE readNow = 1
        ORDER BY title
        """
    )
    rows = cursor.fetchall()

    print_divider()
    print("Read Now Books")

    if rows:
        for row in rows:
            print(
                f"Book ID: {row[0]} | Title: {row[1]} | "
                f"Author: {row[2]} | Price: ${row[3]:.2f}"
            )
    else:
        print("No Read Now books found.")

main() -> None:
    #open a connection to the SQLite database file
    with sqlite3.connect(DB_NAME) as connection:
        #cursor is the object used to execute SQL statements
        cursor = connection.cursor()

        welcome_screen()

        while True:
            print_menu()
            choice = input("\nChoose an option: ").strip()

            if choice == "1":
                view_categories(cursor)
                pause()
            elif choice == "2":
                view_books(cursor)
                pause()
            elif choice == "3":
                view_books_in_category(cursor)
                pause()
            elif choice == "4":
                search_by_title(cursor)
                pause()
            elif choice == "5":
                add_book(cursor)
                pause()
            elif choice == "6":
                update_price(cursor)
                pause()
            elif choice == "7":
                delete_book(cursor)
                pause()
            elif choice == "8":
                view_read_now_books(cursor)
                pause()
            elif choice == "9":
                print_divider()
                print("Goodbye!")
                break
            else:
                print_divider()
                print("Invalid option. Try again.")
                pause()


if __name__ == "__main__":
    main()
