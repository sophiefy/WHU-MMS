import time
import csv
import requests
from lxml import etree


def get_basic_info(type_num: int, page_num: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

    url = 'https://www.dushu.com/book/{}_{}.html'.format(type_num, page_num)
    page_text = requests.get(url=url, headers=headers).text
    etree_html = etree.HTML(page_text)
    info_list = etree_html.xpath('//div[@class="bookslist"]/ul/li')

    basic_info = []

    for li in info_list:
        book_url = li.xpath('./div/h3/a/@href')[0].strip()
        book_url = f'https://www.dushu.com{book_url}'
        title = li.xpath('./div/h3/a/@title')[0].strip()
        author = li.xpath('./div/p/text()')[0].strip()
        press, release_date, ISBN = get_detailed_info(book_url)

        basic_info.append([title, author, press, release_date, ISBN])

    return basic_info


def get_detailed_info(book_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

    page_text = requests.get(url=book_url, headers=headers).text
    etree_html = etree.HTML(page_text)

    press = etree_html.xpath('.//div[@class="book-details-left"]//table[1]/tbody/tr[2]/td[2]/text()')[0]
    info = etree_html.xpath('.//div[@class="book-details"]//td[@class="rt"]/text()')

    ISBN, release_date = info[0], info[1]

    return press, release_date, ISBN


if __name__ == '__main__':
    save_path = 'sample_data/dushu.csv'
    total_page = 3
    type_num = 1617 # 国学
    with open(save_path, 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['title', 'author', 'press', 'release_date', 'ISBN'])
        for page_num in range(1, (total_page+1)):
            basic_info = get_basic_info(type_num, page_num)
            writer.writerows(basic_info)
            print('Finished page {}'.format(page_num))

