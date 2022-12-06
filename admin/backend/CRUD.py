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
                 u_perm CHAR(20)
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
                 d_platform CHAR(20),
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

    def add_book(self, name, author, press,  release_date, ISBN, num):
        sql = "INSERT INTO book (b_name, b_author, b_press, b_category, b_release_date, b_ISBN, b_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', {})".format(
            name, author, press, release_date, ISBN, num)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_book(self, b_id):
        sql = "DELETE FROM book WHERE b_id = {}".format(b_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_book(self):
        sql = "SELECT * FROM book"
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

    def update_book(self, b_id, **kwargs):
        sql = "UPDATE book SET "
        for key, value in kwargs.items():
            if key in self.book_attr:
                sql += "{} = '{}', ".format(key, value)
        sql = sql[:-2] + " WHERE b_id = {}".format(b_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    # SECTION: documents
    def add_document(self, name, author, press, release_date, ISBN):
        sql = "INSERT INTO document (d_name, d_author, d_press, d_release_date, d_ISBN) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}')".format(name, author, press, release_date, ISBN)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_document(self, d_id):
        sql = "DELETE FROM document WHERE d_id = {}".format(d_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_document(self):
        sql = "SELECT * FROM document"
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


    def update_document(self, d_id, **kwargs):
        sql = "UPDATE document SET "
        for key, value in kwargs.items():
            if key in self.document_attr:
                sql += "{} = '{}', ".format(key, value)
        sql = sql[:-2] + " WHERE d_id = {}".format(d_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    # SECTION: users

    def add_user(self, name, password, age, dpt, grade, perm):
        sql = "INSERT INTO user (u_name, u_password, u_age, u_dpt, u_grade, u_perm) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(name, password, age, dpt, grade, perm)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()


    def delete_user(self, u_id):
        sql = "DELETE FROM user WHERE u_id = {}".format(u_id)

        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()


    def read_user(self):
        sql = "SELECT * FROM user"
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

    def update_user(self,u_id, **kwargs):
        sql = "UPDATE user SET "
        for key, value in kwargs.items():
            if key in self.user_attr:
                sql += "{} = '{}', ".format(key, value)
        sql = sql[:-2] + " WHERE u_id = {}".format(u_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    # SECTION: buyer

    def add_buyer(self, u_id, b_id, buy_date):
        sql = "INSERT INTO buyer (u_id, b_id, buy_date) " \
                "VALUES ('{}', '{}', '{}')".format(u_id, b_id, buy_date)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)

    def delete_buyer(self, buy_id): # 需要删除购买记录吗？
        sql = "DELETE FROM buyer WHERE buy_id = {}".format(buy_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_buyer(self):
        sql = "SELECT * FROM buyer"
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
        sql = "INSERT INTO upload (u_id, d_id, upload_date) " \
                "VALUES ('{}', '{}', '{}')".format(u_id, d_id, upload_date)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def delete_upload(self, upload_id):  # 需要删除上传记录吗？
        sql = "DELETE FROM upload WHERE upload_id = {}".format(upload_id)
        if self.conn:
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_upload(self):
        sql = "SELECT * FROM upload"
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
