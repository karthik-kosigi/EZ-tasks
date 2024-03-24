import sqlite3

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_isbn(self):
        return self.isbn


class BookCollection:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                author TEXT,
                isbn TEXT
            )
        ''')
        self.conn.commit()

    def add_book(self, book):
        self.cur.execute('INSERT INTO books VALUES (?, ?, ?)', (book.title, book.author, book.isbn))
        self.conn.commit()

    def delete_book(self, title):
        self.cur.execute('DELETE FROM books WHERE title=?', (title,))
        self.conn.commit()

    def update_book(self, title, new_title, new_author, new_isbn):
        self.cur.execute('''
            UPDATE books
            SET title=?, author=?, isbn=?
            WHERE title=?
        ''', (new_title, new_author, new_isbn, title))
        self.conn.commit()

    def get_books(self):
        self.cur.execute('SELECT * FROM books')
        return self.cur.fetchall()


def print_menu():
    print("1. Add a book")
    print("2. Delete a book")
    print("3. Update a book")
    print("4. View all books")
    print("5. Exit")


def main():
    db_name = "book_collection.db"
    collection = BookCollection(db_name)

    while True:
        print("\n===== Book Collection Menu =====")
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            new_book = Book(title, author, isbn)
            collection.add_book(new_book)
            print("Book added successfully.")

        elif choice == '2':
            title = input("Enter title of the book to delete: ")
            collection.delete_book(title)
            print(f"Book '{title}' deleted.")

        elif choice == '3':
            title = input("Enter title of the book to update: ")
            new_title = input("Enter new title: ")
            new_author = input("Enter new author: ")
            new_isbn = input("Enter new ISBN: ")
            collection.update_book(title, new_title, new_author, new_isbn)
            print(f"Book '{title}' updated.")

        elif choice == '4':
            print("\n===== All Books =====")
            books = collection.get_books()
            if not books:
                print("No books in the collection.")
            else:
                for book in books:
                    print("Title:", book[0])
                    print("Author:", book[1])
                    print("ISBN:", book[2])
                    print("----------------------")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

    collection.conn.close()


if __name__ == "__main__":
    main()
