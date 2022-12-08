import pymysql
import numpy as np


class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.user_attr = ('u_id', 'u_name', 'u_password', 'u_age', 'u_dpt', 'u_grade', 'u_perm')
        self.book_attr = ('b_id', 'b_name', 'b_author', 'b_press', 'b_release_date', 'b_ISBN', 'b_num')
        self.document_attr = ('d_id', 'd_name', 'd_author', 'd_release_date', 'd_platform', 'd_url')
        self.buyer_attr = ('buy_id', 'b_id', 'u_id', 'buy_date')
        self.upload_attr = ('upload_id', 'u_id', 'd_id', 'upload_date')

    def create_connection(self):
        try:
            # 打开数据库连接
            self.conn = pymysql.connect(user="DB_USER08",
                                        password="DB_USER08@123",
                                        host="124.70.7.2",
                                        port=3306,
                                        database="user08db",
                                        charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e)
            return False
        self.check_table()
        return True

    def check_table(self):
        # 检测表是否存在
        sql = "SHOW TABLES"
        self.cursor.execute(sql)
        databases = self.cursor.fetchall()

        databases_arr = np.array(databases)

        databases_list = ('user', 'book', 'document', 'buyer', 'upload')

        function_mapping = {'user': self.create_user_table,
                            'book': self.create_book_table,
                            'document': self.create_document_table,
                            'buyer': self.create_buyer_table,
                            'upload': self.create_upload_table}

        for database in databases_list:
            if database in databases_arr:
                print("database {} exists".format(database))
            else:
                # 提示数据库不存在
                print("database {} not exists".format(database))
                # 创建数据库
                function_mapping[database]()

    def create_user_table(self):
        # 创建用户表
        sql = '''CREATE TABLE user (
                 u_id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 u_name  CHAR(20),
                 u_password CHAR(20),
                 u_age INT,  
                 u_dpt CHAR(20), 
                 u_grade CHAR(4),
                 u_perm INT DEFAULT 0
                  )'''
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def create_book_table(self):
        # 创建书籍表
        sql = '''CREATE TABLE book (
                 b_id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 b_name  CHAR(100),
                 b_author CHAR(20),
                 b_press CHAR(100),
                 b_release_date DATE,
                 b_ISBN CHAR(13),
                 b_num INT DEFAULT 0
                  )'''
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def create_document_table(self):
        # 创建文档表
        sql = '''CREATE TABLE document (
                 d_id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 d_name  CHAR(100),
                 d_author CHAR(20),
                 d_release_date DATE,
                 d_url CHAR(100)
                  )'''
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def create_buyer_table(self):
        # 创建购买表
        sql = '''CREATE TABLE buyer (
                 buy_id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 b_id  INT NOT NULL,
                 u_id  INT NOT NULL,
                 buy_date DATE,
                 CONSTRAINT FOREIGN KEY (b_id) REFERENCES book(b_id) ON DELETE NO ACTION ON UPDATE CASCADE,
                 CONSTRAINT FOREIGN KEY (u_id) REFERENCES user(u_id) ON DELETE NO ACTION ON UPDATE CASCADE
                  )'''
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

    def create_upload_table(self):
        # 创建上传表
        sql = '''CREATE TABLE upload (
                 upload_id  INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
                 u_id  INT NOT NULL,
                 d_id  INT NOT NULL,
                 upload_date DATE,
                 CONSTRAINT FOREIGN KEY (u_id) REFERENCES user(u_id) ON DELETE NO ACTION ON UPDATE CASCADE, 
                 CONSTRAINT FOREIGN KEY (d_id) REFERENCES document(d_id) ON DELETE NO ACTION ON UPDATE CASCADE
                  )'''
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print(e)
            self.conn.rollback()
        else:
            self.conn.commit()

    # SECTION: books

    def add_book(self, name, author, press, release_date, ISBN, num):
        sql = "INSERT INTO book (b_name, b_author, b_press, b_release_date, b_ISBN, b_num) VALUES (%s, %s, %s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, author, press, release_date, ISBN, num))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_book(self, b_id):
        sql = "DELETE FROM book WHERE b_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (b_id,))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_book(self, limit, offset=0):
        sql = "SELECT * FROM book LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                book_table = self.cursor.fetchall()
                return book_table

    def update_book(self, b_id, b_name, b_author, b_press, b_release_date, b_ISBN, b_num):
        sql = "UPDATE book SET b_name = %s, b_author = %s, b_press = %s, b_release_date = %s, b_ISBN = %s, b_num = %s WHERE b_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (b_name, b_author, b_press, b_release_date, b_ISBN, b_num, b_id))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_book_num(self, b_id=0, b_name='', b_author='', b_press='', b_release_date='', b_ISBN=''):
        if b_id == 0:
            sql = "SELECT COUNT(*) FROM book WHERE b_name LIKE %s AND b_author LIKE %s AND b_press LIKE %s AND b_release_date LIKE %s AND b_ISBN LIKE %s"
            sql = sql % (
                "'%" + b_name + "%'", "'%" + b_author + "%'", "'%" + b_press + "%'", "'%" + b_release_date + "%'",
                "'%" + b_ISBN + "%'")
        else:
            sql = "SELECT COUNT(*) FROM book WHERE b_id = %u"
            sql = sql % (b_id)

        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                num = self.cursor.fetchone()
                return num[0]

    def search_book(self, b_id=0, b_name='', b_author='', b_press='', b_release_date='', b_ISBN='', limit=10, offset=0):
        if b_id == 0:
            sql = "SELECT * FROM book WHERE b_name LIKE %s AND b_author LIKE %s AND b_press LIKE %s AND b_release_date LIKE %s AND b_ISBN LIKE %s"
            sql = sql % (
            "'%" + b_name + "%'", "'%" + b_author + "%'", "'%" + b_press + "%'", "'%" + b_release_date + "%'",
            "'%" + b_ISBN + "%'")
        else:
            sql = "SELECT * FROM book WHERE b_id = %u"
            sql = sql % (b_id)

        sql += " LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                book_table = self.cursor.fetchall()
                return book_table

    # SECTION: documents
    def add_document(self, name, author, release_date, url):
        sql = "INSERT INTO document (d_name, d_author, d_release_date, d_url) VALUES (%s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, author, release_date, url))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_document(self, d_id):
        sql = "DELETE FROM document WHERE d_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (d_id,))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_document(self, limit, offset=0):
        sql = "SELECT * FROM document LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit, offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                document_table = self.cursor.fetchall()
                return document_table

    def update_document(self, d_id, d_name, d_author, d_release_date, d_url):
        sql = "UPDATE document SET d_name = %s, d_author = %s, d_release_date = %s, d_url = %s WHERE d_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (d_name, d_author, d_release_date, d_url, d_id))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_document_num(self, d_id=0, d_name='', d_author='', d_release_date='', d_url=''):
        if d_id == 0:
            sql = "SELECT COUNT(*) FROM document WHERE d_name LIKE %s AND d_author LIKE %s AND d_release_date LIKE %s AND d_url LIKE %s"
            sql = sql % (
            "'%" + d_name + "%'", "'%" + d_author + "%'", "'%" + d_release_date + "%'", "'%" + d_url + "%'")
        else:
            sql = "SELECT COUNT(*) FROM document WHERE d_id = %u"
            sql = sql % (d_id)

        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                num = self.cursor.fetchone()
                return num[0]

    def search_document(self, d_id=0, d_name='', d_author='', d_release_date='', d_url='', limit=10, offset=0):
        if d_id == 0:
            sql = "SELECT * FROM document WHERE d_name LIKE %s AND d_author LIKE %s AND d_release_date LIKE %s AND d_url LIKE %s"
            sql = sql % ("'%" + d_name + "%'", "'%" + d_author + "%'", "'%" + d_release_date + "%'", "'%" + d_url + "%'")
        else:
            sql = "SELECT * FROM document WHERE d_id = %u"
            sql = sql % (d_id)

        sql += " LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                document_table = self.cursor.fetchall()
                return document_table

    # SECTION: users

    def add_user(self, name, password, age, dpt, grade, perm):
        sql = "INSERT INTO user (u_name, u_password, u_age, u_dpt, u_grade, u_perm) VALUES (%s, %s, %s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, password, age, dpt, grade, perm))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_user(self, u_id):
        sql = "DELETE FROM user WHERE u_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_id,))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_user(self, limit, offset=0):
        sql = "SELECT * FROM user LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit, offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                user_table = self.cursor.fetchall()
                return user_table

    def update_user(self, u_id, u_name, u_password, u_age, u_dpt, u_grade, u_perm):
        sql = "UPDATE user SET u_name = %s, u_password = %s, u_age = %s, u_dpt = %s, u_grade = %s, u_perm = %s WHERE u_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_name, u_password, u_age, u_dpt, u_grade, u_perm, u_id))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_user_num(self, u_id=0, u_name='', u_password='', u_age='', u_dpt='', u_grade='', u_perm=''):
        if u_id == 0:
            sql = "SELECT COUNT(*) FROM user WHERE u_name LIKE %s AND u_password LIKE %s AND u_age LIKE %s AND u_dpt LIKE %s AND u_grade LIKE %s AND u_perm LIKE %s"
            sql = sql % (
                "'%" + u_name + "%'", "'%" + u_password + "%'", "'%" + u_age + "%'", "'%" + u_dpt + "%'",
                "'%" + u_grade + "%'",
                "'%" + u_perm + "%'")
        else:
            sql = "SELECT COUNT(*) FROM user WHERE u_id = %u"
            sql = sql % (u_id)

        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                num = self.cursor.fetchone()
                return num[0]

    def search_user(self, u_id=0, u_name='', u_password='', u_age='', u_dpt='', u_grade='', u_perm='', limit=10, offset=0):
        if u_id == 0:
            sql = "SELECT * FROM user WHERE u_name LIKE %s AND u_password LIKE %s AND u_age LIKE %s AND u_dpt LIKE %s AND u_grade LIKE %s AND u_perm LIKE %s"
            sql = sql % (
            "'%" + u_name + "%'", "'%" + u_password + "%'", "'%" + u_age + "%'", "'%" + u_dpt + "%'", "'%" + u_grade + "%'",
            "'%" + u_perm + "%'")
        else:
            sql = "SELECT * FROM user WHERE u_id = %u"
            sql = sql % (u_id)

        sql += " LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                user_table = self.cursor.fetchall()
                return user_table

    # SECTION: buyer

    def add_buyer(self, u_id, b_id, buy_date):
        sql = "INSERT INTO buyer (u_id, b_id, buy_date) VALUES (%s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_id, b_id, buy_date))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_buyer(self, buy_id):  # 需要删除购买记录吗？
        sql = "DELETE FROM buyer WHERE buy_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (buy_id,))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_buyer(self, limit, offset=0):
        sql = "SELECT * FROM buyer LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit, offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                buyer_table = self.cursor.fetchall()
                return buyer_table

    def get_buyer_num(self):
        sql = "SELECT COUNT(*) FROM buyer"
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                num = self.cursor.fetchone()
                return num[0]

    def search_buyer(self, u_id=0, b_id=0, buy_date='',b_name='',u_name='', limit=10, offset=0):
        buyer_sql = "SELECT * FROM buyer WHERE"
        if u_id != 0:
            buyer_sql += " u_id = %d" % u_id
            user_sql = "SELECT u_id,u_name FROM user WHERE u_id = %d" % u_id

            buyer_sql += " AND"
        else:
            user_sql = "SELECT u_id,u_name FROM user WHERE u_name LIKE %s" % ("'%" + u_name + "%'")
        if b_id != 0:
            buyer_sql += " b_id = %d" % b_id
            book_sql = "SELECT b_id,b_name FROM book WHERE b_id = %d" % b_id
            buyer_sql += " AND"
        else:
            book_sql = "SELECT b_id,b_name FROM book WHERE b_name LIKE %s" % ("'%" + b_name + "%'")
        buyer_sql += " buy_date LIKE %s" % ("'%" + buy_date + "%'")

        sql = "SELECT * FROM buyer JOIN (%s) AS user ON buyer.u_id = user.u_id JOIN (%s) AS book ON buyer.b_id = book.b_id" % (user_sql, book_sql)
        sql += " LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                buyer_table = self.cursor.fetchall()
                return buyer_table

    # SECTION: upload

    def add_upload(self, u_id, d_id, upload_date):
        sql = "INSERT INTO upload (u_id, d_id, upload_date) VALUES (%s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_id, d_id, upload_date))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_upload(self, upload_id):  # 需要删除上传记录吗？
        sql = "DELETE FROM upload WHERE upload_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (upload_id,))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_upload(self, limit, offset=0):
        sql = "SELECT * FROM upload LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit, offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                upload_table = self.cursor.fetchall()
                return upload_table

    def get_upload_num(self):
        sql = "SELECT COUNT(*) FROM upload"
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                num = self.cursor.fetchone()
                return num[0]

    def search_upload(self, u_id=0, d_id=0, upload_date='',d_name='',u_name='', limit=10, offset=0):
        upload_sql = "SELECT * FROM upload WHERE"
        if u_id != 0:
            upload_sql += " u_id = %d" % u_id
            user_sql = "SELECT u_id,u_name FROM user WHERE u_id = %d" % u_id

            upload_sql += " AND"
        else:
            user_sql = "SELECT u_id,u_name FROM user WHERE u_name LIKE %s" % ("'%" + u_name + "%'")
        if d_id != 0:
            upload_sql += " d_id = %d" % d_id
            doc_sql = "SELECT d_id,d_name FROM document WHERE d_id = %d" % d_id
            upload_sql += " AND"
        else:
            doc_sql = "SELECT d_id,d_name FROM document WHERE d_name LIKE %s" % ("'%" + d_name + "%'")
        upload_sql += " upload_date LIKE %s" % ("'%" + upload_date + "%'")

        sql = "SELECT * FROM upload JOIN (%s) AS user ON upload.u_id = user.u_id JOIN (%s) AS doc ON upload.d_id = doc.d_id" % (user_sql, doc_sql)
        sql += " LIMIT %d OFFSET %d" % (limit, offset)
        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                upload_table = self.cursor.fetchall()
                return upload_table


if __name__ == '__main__':
    database = Database()
    database.create_connection()
