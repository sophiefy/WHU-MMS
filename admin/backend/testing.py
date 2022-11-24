import sqlite3

conn = sqlite3.connect('../database/books.db')

cursor = conn.cursor()

try:
    cursor.execute('create table Books('
                   'name char(100) not null,'
                   'author char(20) not null,'
                   'press char(100) not null,'
                   'release_date date not null,'
                   'ISBN char(13) primary key not null);')

except:
    print('table already exists!')

cursor.execute('insert into Books (name, author, press, release_date, ISBN) '
               'values ("朝花夕拾", "鲁迅", "人民教育出版社", "2017-6", "9787107316616")')

cursor.close()
conn.commit()
conn.close()

print('success')

