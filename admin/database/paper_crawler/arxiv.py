import time
import csv
import requests
from lxml import etree
from tqdm import tqdm

'''
url format:
https://arxiv.org/search/?query=Astrophysics&searchtype=all&source=header&start=50
'''


def get_basic_info(query, page_num):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }
    start = page_num * 50
    url = 'https://arxiv.org/search/?query={}&searchtype=all&source=header&start={}'.format(query, start)

    try:
        page_text = requests.get(url=url, headers=headers).text
    except:
        return None
    else:
        etree_html = etree.HTML(page_text)
        info_list = etree_html.xpath('//ol[@class="breathe-horizontal"]/li')
        basic_info = []

        for li in info_list:
            arxiv_url = li.xpath('.//p[@class="list-title is-inline-block"]/a/@href')[0]
            arxiv_num = arxiv_url.replace('https://arxiv.org/abs/', '').replace('.', '')
            title = li.xpath('.//p[@class="title is-5 mathjax"]/text()')[0]
            title = title.replace('\n', '').replace('  ', '')
            author = li.xpath('.//p[@class="authors"]/a/text()')
            author = ', '.join(author)
            release_date = li.xpath('./p[@class="is-size-7"]/text()')[0]
            release_date = release_date.replace('\n', '').replace('  ', '')
            release_date = release_date.replace(';', '').replace(',', '')
            release_date = release_date.strip(' ').replace(' ', '-')

            basic_info.append([title, author, release_date, arxiv_url, arxiv_num])
        return basic_info

if __name__ == '__main__':
    queries = ['Physics', 'Mathematics', 'Quantitative Biology', 'Quantitative Finance',
               'Statistics', 'Electrical Engineering and Systems Science', 'Economics']

    save_path = 'sample_data/arxiv.csv'
    total_page = 8000
    with open(save_path, 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['title', 'author', 'release_date', 'arxiv_url', 'arxiv_num'])
        for query in queries:
            print('Start collecting data from {}...\n'.format(query))
            time.sleep(1)
            for page_num in tqdm(range(total_page)):
                basic_info = get_basic_info(query, page_num)
                if basic_info:
                    writer.writerows(basic_info)