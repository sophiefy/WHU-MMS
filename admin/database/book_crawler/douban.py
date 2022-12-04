import time
from lxml import etree
import requests
import csv

def get_basic_info(page_num: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

    url = 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={}&type=T'.format(page_num)
    page_text = requests.get(url=url, headers=headers).text
    etree_html = etree.HTML(page_text)
    info_list = etree_html.xpath('//ul[@class="subject-list"]/li[@class="subject-item"]')

    basic_info = []

    for li in info_list:
        book_url = li.xpath('.//h2/a/@href')[0].strip()
        title = li.xpath('.//h2/a/@title')[0].strip()
        # [语言] 作者 译者 出版社 出版日期 定价
        info = li.xpath('.//div[@class="pub"]/text()')[0].strip()
        basic_info.append((title, info, book_url))

    return basic_info


def parse_basic_info(basic_info: list):
    parsed_basic_info = []
    for (title, info, book_url) in basic_info:
        info = info.replace(' ', '').split('/')
        if len(info) == 5:  # 外国作品
            author, press, release_date = info[0], info[2], info[3]
        elif len(info) == 4:  # 华语作品
            author, press, release_date = info[0], info[1], info[2]
        else:
            raise ValueError('Unknown type of info!')

        ISBN = get_ISBN(book_url)

        parsed_basic_info.append([title, author, press, release_date, ISBN])

    return parsed_basic_info


def get_ISBN(book_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

    page_text = requests.get(url=book_url, headers=headers).text
    etree_html = etree.HTML(page_text)
    info_list = etree_html.xpath('//div[@id="info"]/text()')
    ISBN = info_list[-2].replace(' ', '')

    return ISBN


if __name__ == '__main__':
    save_path = 'sample_data/douban.csv'

    total_page = 3
    with open(save_path, 'w', newline='') as fp:    # 如果是追加新的数据，将'w'改为'a'
        writer = csv.writer(fp)
        writer.writerow(['title', 'author', 'press', 'release_date', 'ISBN'])
        for page_num in range(1, (total_page+1)):
            basic_info = get_basic_info(page_num)
            parsed_basic_info = parse_basic_info(basic_info)
            writer.writerows(parsed_basic_info)
            print('Finished page {}'.format(page_num))
