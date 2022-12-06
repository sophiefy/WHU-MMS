import CRUD

DB = CRUD.Database()

DB.create_connection()


try:
    DB.update_book(b_id=1,b_num=1)
except Exception as e:
    print(e)
    DB.conn.rollback()


DB.cursor.close()
DB.conn.commit()
DB.conn.close()

print('success')

