import time
import csv
import requests
from lxml import etree
from tqdm import tqdm


def get_basic_info(type_num: int, page_num: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

    url = 'https://www.dushu.com/book/{}_{}.html'.format(type_num, page_num)
    try:
        page_text = requests.get(url=url, headers=headers).text
    except:
        return None
    else:
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


def get_type_nums():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }
    url = 'https://www.dushu.com/'
    page_text = requests.get(url=url, headers=headers).text
    etree_html = etree.HTML(page_text)
    nav_list = etree_html.xpath('.//div[@class="class-nav"]')[0]
    nav_list = nav_list.xpath('./a')

    type_nums = []

    for nav in nav_list:
        type_num = nav.xpath('./@href')[0].split('/')
        if len(type_num) > 2:
            type_num = type_num[2].replace('.html', '')
            type_nums.append(type_num)

    return type_nums


if __name__ == '__main__':
    save_path = 'sample_data/dushu.csv'
    total_page = 100
    type_nums = get_type_nums()
    with open(save_path, 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['title', 'author', 'press', 'release_date', 'ISBN'])
        for type_num in type_nums:
            print('Start collecting data from type {}...'.format(type_num))
            for page_num in tqdm(range(1, (total_page + 1))):
                basic_info = get_basic_info(type_num, page_num)
                if basic_info:
                    writer.writerows(basic_info)
                time.sleep(1)

            time.sleep(3)
