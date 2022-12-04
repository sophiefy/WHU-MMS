import csv
import os
from tqdm import tqdm

new_data = []
with open('sample_data/arxiv.csv', 'r', encoding='utf-8') as fp:
    raw_data = list(csv.reader(fp))
    for line in tqdm(raw_data):
        if line[0]:
            new_data.append(line)

with open('sample_data/arxiv_cleaned.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['title', 'author', 'release_date', 'arxiv_url', 'arxiv_num'])
    for line in tqdm(new_data):
        writer.writerow(line)