import sqlite3

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

    # SECTION: books

    def add_book(self, name, author, press, category, release_date, ISBN):
        if self.conn:
            try:
                self.cursor.execute("insert into Books (name, author, press, release_date, ISBN) "
                                    "values ('{}', '{}', '{}', '{}', '{}', '{}')"
                                    .format(name, author, press, category, release_date, ISBN))
                self.conn.commit()
            except Exception as e:
                print(e)

    def delete_book(self, ISBN):
        if self.conn:
            try:
                self.cursor.execute("delete from Books where ISBN='{}'"
                                    .format(ISBN))
                self.conn.commit()
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

    def update_book(self, name, author, press, category, release_date, ISBN):
        # 认为ISBN是不可修改的
        print('date: ', release_date)
        if self.conn:
            try:
                self.cursor.execute("update Books set "
                                    "name='{}', author='{}', press='{}', category='{}', release_date='{}' "
                                    "where ISBN='{}'"
                                    .format(name, author, press, category,release_date, ISBN))
                self.conn.commit()
            except Exception as e:
                print(e)

    # SECTION: papers
    def add_paper(self, name, author, press, release_date, ISBN):
        pass

    def delete_paper(self, ISBN):
        pass

    def read_paper(self):
        pass

    def update_paper(self, name, author, press, release_date, ISBN):
        pass

    # SECTION: users

    def add_user(self):
        pass

    def delete_user(self):
        pass

    def read_user(self):
        pass

    def update_user(self):
        pass



if __name__ == '__main__':
    database = Database('')
