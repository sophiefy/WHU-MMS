import csv
import random

max_uid = 1000000
max_bid = 100000


def uid_generator():
    uid = random.randint(1, max_uid)

    return uid

def bid_generator():
    bid = random.randint(1, max_bid)

    return bid

def date_generator():
    month = random.randint(1, 12)
    month = '%02d' % (month)
    day = random.randint(1, 30)
    day = '%02d' % (day)

    date = f'2022-{month}-{day}'

    return date

with open('sample_data/buyer.csv', 'w', encoding='utf-8', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(['bid', 'uid', 'buy_date'])
    for i in range(100000):
        bid = bid_generator()
        uid = uid_generator()
        date = date_generator()

        writer.writerow([bid, uid, date])