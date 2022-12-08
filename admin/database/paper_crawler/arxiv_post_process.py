import csv
import os
from tqdm import tqdm

'''
1-December-2022 -> 2022-12-1
'''

month_map = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12'
}

def clean_month(month):
    try:
        month = month_map[month]
    except Exception as e:
        print(month)
        print(e)
        return None
    else:
        return month

new_data = []
with open('sample_data/arxiv.csv', 'r', encoding='utf-8') as fp:
    raw_data = list(csv.reader(fp))
    for line in tqdm(raw_data):
        new_data.append(line)

with open('sample_data/arxiv_cleaned.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['title', 'author', 'release_date', 'platform', 'url'])
    new_data = new_data[1:]
    for line in tqdm(new_data):
        old_date = line[2]
        day, month, year = old_date.split('-')
        month = clean_month(month)
        if month:
            date = f'{year}-{month}-{day}'
            print(date)
            line = [line[0], line[1], date, 'arxiv', line[3]]
            writer.writerow(line)