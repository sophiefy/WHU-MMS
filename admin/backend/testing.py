import CRUD

DB = CRUD.Database()

DB.create_connection()


DB.add_book("朝花夕拾", "鲁迅", "人民教育出版社", "文学", "2017-6", "9787107316616")


DB.cursor.close()
DB.conn.commit()
DB.conn.close()

print('success')

