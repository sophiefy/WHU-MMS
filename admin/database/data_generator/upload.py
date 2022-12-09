import random
import csv

def date_generator():
    month = random.randint(1, 12)
    month = '%02d' % (month)
    day = random.randint(1, 30)
    day = '%02d' % (day)

    date = f'2022-{month}-{day}'

    return date

with open('sample_data/user.csv', 'r', encoding='utf-8') as fp:
    users = list(csv.reader(fp))
    users = users[1:]

with open('../paper_crawler/sample_data/papers.csv') as fp:
    papers = list(csv.reader(fp))
    papers = papers[1:]

length_users = len(users)
length_papers = len(papers)

upload = []

for i, paper in enumerate(papers):
    rand = random.randint(0, length_users-1)
    u_id = rand + 1
    d_id = i + 1
    date = date_generator()
    upload.append([u_id, d_id, date])

with open('sample_data/upload.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['u_id', 'd_id', 'upload_date'])
    for line in upload:
        writer.writerow(line)


