import CRUD
import pandas as pd
import numpy as np
from tqdm import tqdm

# 模拟录入系统

path = u'../database/paper_crawler/sample_data/papers.csv'
# path = u'../database/book_crawler/sample_data/dushu_clean.csv'
# path = u'../database/data_generator/sample_data/buyer.csv'
data = pd.read_csv(path, encoding='utf-8')


DB = CRUD.Database()

DB.create_connection()

def write_data(data, table, stride=1000):
    try:
        for i in tqdm(range(0, data.shape[0], stride)):
            batch = data.iloc[i:min(i+stride, data.shape[0])].values.tolist()
            new_col = []
            for column in data.columns:
                new_col.append('d_'+column)
            sql = 'INSERT INTO %s (%s) VALUES (%s)' % (table, ','.join(new_col), ','.join(['%s'] * len(data.columns)))
            DB.cursor.executemany(sql, batch)
    except Exception as e:
        print(e)
        DB.conn.rollback()
    else:
        DB.conn.commit()


if __name__ == '__main__':
    write_data(data, 'document')
    DB.cursor.close()
    DB.conn.commit()
    DB.conn.close()


