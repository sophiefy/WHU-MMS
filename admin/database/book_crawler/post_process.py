import os
import csv


def clean_author(csv_path, save_path=None):
    if save_path is None:
        save_path = csv_path + '.cleaned'

    cleaned_data = []
    with open(csv_path, 'r', encoding='utf-8') as fp:
        raw_data = list(csv.reader(fp))
        for line in raw_data:
            if len(line) > 25:  # 这是简介
                line = '暂缺作者'
            else:
                line = line.replace('（', '[').replace('）', ']')
                line = line.replace('(', '[').replace(')', ']')
                if (len(line) <=3 and '著' in line) or (line <=5 and '[' in line):
                    line = '暂缺作者'



if __name__ == '__main__':
    s = '他们沉默地吃饭，客气地应对，半抵触地亲密。爱情是未明朗半暧昧的情侣未满。…'
    print(len(s))
