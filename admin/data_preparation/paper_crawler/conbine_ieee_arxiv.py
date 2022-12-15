import csv

data = []

new_arxiv_data = []
with open('sample_data/arxiv_cleaned.csv', 'r', encoding='utf-8') as fp:
    arxiv_data = list(csv.reader(fp))
    arxiv_data = arxiv_data[1:]
    print(arxiv_data[0])
    for line in arxiv_data:
        title = line[0]
        author = line[1]
        release_date = line[2]
        url = line[4]
        new_line = [title, author, release_date, url]
        data.append(new_line)

with open('sample_data/ieee_clean.csv', 'r', encoding='utf-8') as fp:
    ieee_data = list(csv.reader(fp))
    ieee_data = ieee_data[1:]
    print(ieee_data[0])
    for line in ieee_data:
        data.append(line)

with open('sample_data/papers.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['title', 'author', 'release_date', 'URL'])
    for line in data:
        writer.writerow(line)