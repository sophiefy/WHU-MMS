import pandas as pd


def save_data(data: list):
    inf = pd.DataFrame(data, columns=['article', 'author',  'url','DOI','year'])
    outputpath = ('IEEE.csv')  #填写你要保存的路径
    inf.to_csv(outputpath, sep=',', index=False, header=True, encoding='UTF-8')