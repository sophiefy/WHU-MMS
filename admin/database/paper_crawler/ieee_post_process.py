import csv
import os
from tqdm import tqdm

'''
1. replace Year:
'''

ieee_files = os.listdir('./sample_data')

new_data = []

for ieee_file in tqdm(ieee_files):
    if ieee_file.startswith('IEEE'):
        csv_path = f'./sample_data/{ieee_file}'
        with open(csv_path, 'r', encoding='utf-8') as fp:
            data = list(csv.reader(fp))
            data = data[1:]
            for line in data:
                # article	author	url	DOI	year
                title = line[0].replace('\n', '')
                author = line[1].replace('\n', '').replace(';', ', ')
                release_date = line[4].replace('Year:', '').replace(' ', '')
                url = line[2]

                new_line = [title, author, release_date, url]
                new_data.append(new_line)

with open('./sample_data/ieee_clean.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['title', 'author', 'release_date', 'url'])
    for line in tqdm(new_data):
        writer.writerow(line)
