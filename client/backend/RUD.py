import pymysql
import numpy as np
import traceback

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

        for database in databases_list:
            if database in databases_arr:
                print("database {} exists".format(database))
            else:
                # 提示数据库不存在
                print("database {} not exists".format(database))

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
                print(b_num)
                self.cursor.execute(sql, (b_name, b_author, b_press, b_release_date, b_ISBN, b_num, b_id))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def get_book_num(self, b_name='', b_author='', b_press='', b_release_date='', b_ISBN=''):
        sql = "SELECT COUNT(*) FROM book WHERE b_name LIKE %s AND b_author LIKE %s AND b_press LIKE %s AND b_release_date LIKE %s AND b_ISBN LIKE %s"
        sql = sql % (
            "'%" + b_name + "%'", "'%" + b_author + "%'", "'%" + b_press + "%'", "'%" + b_release_date + "%'",
            "'%" + b_ISBN + "%'")

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

    def search_book(self, b_name='', b_author='', b_press='', b_release_date='', b_ISBN='', limit=10, offset=0):
        sql = "SELECT * FROM book WHERE b_name LIKE %s AND b_author LIKE %s AND b_press LIKE %s AND b_release_date LIKE %s AND b_ISBN LIKE %s"
        sql = sql % (
        "'%" + b_name + "%'", "'%" + b_author + "%'", "'%" + b_press + "%'", "'%" + b_release_date + "%'",
        "'%" + b_ISBN + "%'")
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

    def get_document_num(self, d_name='', d_author='', d_release_date='', d_url=''):
        sql = "SELECT COUNT(*) FROM document WHERE d_name LIKE %s AND d_author LIKE %s AND d_release_date LIKE %s AND d_url LIKE %s"
        sql = sql % (
        "'%" + d_name + "%'", "'%" + d_author + "%'", "'%" + d_release_date + "%'", "'%" + d_url + "%'")

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

    def search_document(self, d_name='', d_author='', d_release_date='', d_url='', limit=10, offset=0):
        sql = "SELECT * FROM document WHERE d_name LIKE %s AND d_author LIKE %s AND d_release_date LIKE %s AND d_url LIKE %s"
        sql = sql % ("'%" + d_name + "%'", "'%" + d_author + "%'", "'%" + d_release_date + "%'", "'%" + d_url + "%'")
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

    def search_document_precise(self, d_name='', d_author='', d_release_date='', d_url=''):
        sql = "SELECT * FROM document WHERE d_name = %s AND d_author = %s AND d_release_date = %s AND d_url = %s"
        sql = sql % (d_name, d_author, d_release_date, d_url)

        if self.conn:
            try:
                self.cursor.execute(sql)
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                did = self.cursor.fetchone()
                return did[0]



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

            uid = self.search_user(name, password, age, dpt, grade)
            return uid

    def search_user(self, name, password, age, dpt, grade):
        sql = "SELECT u_id FROM user WHERE u_name = %s AND u_password = %s AND u_age = %s AND u_dpt = %s AND u_grade = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (name, password, age, dpt, grade))
            except Exception as e:
                print(e)
                return None
            else:
                uid = self.cursor.fetchone()
                if uid:
                    return uid[0]
                else:
                    return None


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

    def update_user(self, u_id, u_name, u_password, u_age, u_dpt, u_grade):
        sql = "UPDATE user SET u_name = %s, u_password = %s, u_age = %s, u_dpt = %s, u_grade = %s WHERE u_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (u_name, u_password, u_age, u_dpt, u_grade, u_id))
            except Exception as e:
                self.conn.rollback()
                print(e)
            else:
                self.conn.commit()

    def user_login(self, id, password):
        sql = "SELECT * FROM user WHERE u_id = %s AND u_password = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (id, password))
            except Exception as e:
                self.conn.rollback()
                print(e)
                return None
            else:
                user = self.cursor.fetchone()
                return user

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

    def delete_buyer(self, buy_id): # 需要删除购买记录吗？
        sql = "DELETE FROM buyer WHERE buy_id = %s"
        if self.conn:
            try:
                self.cursor.execute(sql, (buy_id,))
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
        print(u_id, d_id, upload_date)
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
