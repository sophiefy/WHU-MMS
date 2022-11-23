import sqlite3

# SECTION: books

class Database:
    def __init__(self, db_path):
        self.conn = None
        self.cursor = None
        self.db_path = db_path

    def create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)

    def add_book(self, name, author, press, release_date, ISBN):
        if self.conn:
            try:
                self.cursor.execute("insert into Books (name, author, press, release_date, ISBN) "
                                    "values ('{}', '{}', '{}', '{}', '{}')"
                                    .format(name, author, press, release_date, ISBN))
                self.conn.commit()
            except Exception as e:
                print(e)


    def delete_book(self, ISBN):
        if self.conn:
            try:
                self.cursor.execute("delete from Books where ISBN='{}'"
                                    .format(ISBN))
            except Exception as e:
                print(e)

    def read_book(self):
        if self.conn:
            try:
                self.cursor.execute("select * from Books")
            except Exception as e:
                print(e)
                return None
            else:
                book_table = self.cursor.fetchall()
                return book_table

    def update_book(self):
        pass


if __name__ == '__main__':
    database = Database('')
