import CRUD

DB = CRUD.Database()

DB.create_connection()


try:
    DB.add_book("朝花夕拾", "鲁迅", "人民教育出版社", "2017-06-13", "9787107316616",3)
except Exception as e:
    print(e)
    DB.conn.rollback()


DB.cursor.close()
DB.conn.commit()
DB.conn.close()

print('success')

