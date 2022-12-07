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
        sql = "INSERT INTO book (b_name, b_author, b_press, b_release_date, b_ISBN, b_num) VALUES (%s, %s, %s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql,(name, author, press, release_date, ISBN, num))
                self.conn.commit()
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
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_book(self,limit,offset=0):
        sql = "SELECT * FROM book LIMIT %d OFFSET %d" % (limit,offset)
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
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_book_num(self):
        sql = "SELECT COUNT(*) FROM book"
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

    # SECTION: documents
    def add_document(self, name, author, press, release_date, ISBN):
        sql = "INSERT INTO document (d_name, d_author, d_press, d_release_date, d_ISBN) VALUES (%s, %s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, author, press, release_date, ISBN))
                self.conn.commit()
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
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_document(self,limit,offset=0):
        sql = "SELECT * FROM document LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit,offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                document_table = self.cursor.fetchall()
                return document_table


    def update_document(self, d_id, d_name, d_author, d_press, d_release_date, d_platform, d_url):
        sql = "UPDATE document SET d_name = %s, d_author = %s, d_press = %s, d_release_date = %s, d_platform = %s, d_url = %s WHERE d_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (d_name, d_author, d_press, d_release_date, d_platform, d_url, d_id))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_document_num(self):
        sql = "SELECT COUNT(*) FROM document"
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

    # SECTION: users

    def add_user(self, name, password, age, dpt, grade, perm):
        sql = "INSERT INTO user (u_name, u_password, u_age, u_dpt, u_grade, u_perm) VALUES (%s, %s, %s, %s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, password, age, dpt, grade, perm))
                self.conn.commit()
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
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()


    def read_user(self,limit,offset=0):
        sql = "SELECT * FROM user LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit,offset))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                user_table = self.cursor.fetchall()
                return user_table

    def update_user(self,u_id, u_name, u_password, u_age, u_dpt, u_grade, u_perm):
        sql = "UPDATE user SET u_name = %s, u_password = %s, u_age = %s, u_dpt = %s, u_grade = %s, u_perm = %s WHERE u_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_name, u_password, u_age, u_dpt, u_grade, u_perm, u_id))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_user_num(self):
        sql = "SELECT COUNT(*) FROM user"
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

    # SECTION: buyer

    def add_buyer(self, u_id, b_id, buy_date):
        sql = "INSERT INTO buyer (u_id, b_id, buy_date) VALUES (%s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_id, b_id, buy_date))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)

    def delete_buyer(self, buy_id): # 需要删除购买记录吗？
        sql = "DELETE FROM buyer WHERE buy_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (buy_id,))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_buyer(self,limit,offset=0):
        sql = "SELECT * FROM buyer LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit,offset))
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


    # SECTION: upload

    def add_upload(self, u_id, d_id, upload_date):
        sql = "INSERT INTO upload (u_id, d_id, upload_date) VALUES (%s, %s, %s)"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_id, d_id, upload_date))
                self.conn.commit()
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
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def read_upload(self,limit,offset=0):
        sql = "SELECT * FROM upload LIMIT %s OFFSET %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (limit,offset))
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

if __name__ == '__main__':
    database = Database()
    database.create_connection()
