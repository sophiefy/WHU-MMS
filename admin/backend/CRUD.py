import pymysql
import numpy as np

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

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
        self.check_table()

    def check_table(self):
        # 检测表是否存在
        sql = "SHOW TABLES"
        self.cursor.execute(sql)
        databases =self.cursor.fetchall()

        databases_arr = np.array(databases)


        databases_list = ('user','book','document','buyer','upload')

        function_mapping={'user':self.create_user_table,
                          'book':self.create_book_table,
                          'document':self.create_document_table,
                          'buyer':self.create_buyer_table,
                          'upload':self.create_upload_table}

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
                 u_grade CHAR(4)
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
                 d_url CHAR(100),
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

    def add_book(self, name, author, press, category, release_date, ISBN):
        if self.conn:
            try:
                self.cursor.execute("insert into Books (name, author, press, release_date, ISBN) "
                                    "values ('{}', '{}', '{}', '{}', '{}', '{}')"
                                    .format(name, author, press, category, release_date, ISBN))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)

    def delete_book(self, ISBN):
        if self.conn:
            try:
                self.cursor.execute("delete from Books where ISBN='{}'"
                                    .format(ISBN))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)

    def read_book(self):
        if self.conn:
            try:
                self.cursor.execute("select * from Books")
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                book_table = self.cursor.fetchall()
                return book_table

    def update_book(self, name, author, press, category, release_date, ISBN):
        # 认为ISBN是不可修改的

        if self.conn:
            try:
                self.cursor.execute("update Books set "
                                    "name='{}', author='{}', press='{}', category='{}', release_date='{}' "
                                    "where ISBN='{}'"
                                    .format(name, author, press, category,release_date, ISBN))
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
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
    database = Database()
    database.create_connection()
