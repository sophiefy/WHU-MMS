from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
from tqdm import tqdm
import requests
from lxml import etree
'''
url format:
http://search.dangdang.com/?key=%C6%B7%B8%F1%D1%F8%B3%C9&act=input&sort_type=sort_score_desc&page_index='+str(page+1)+'#J_tab
'''

opt = webdriver.EdgeOptions()
opt.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Edge(options=opt)


def get_basic_info(query, page_num):


    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    # }
    url = 'http://search.dangdang.com/?key={}&act=input&sort_type=sort_score_desc&page_index={}'.format(query, page_num)
    # try:
    #     page_text = requests.get(url=url, headers=headers).text
    # except Exception as e:
    #     print(e)
    #     return None
    #
    # etree_html = etree.HTML(page_text)
    # elements = etree_html.xpath('//ul[@class="bigimg"]/li')
    driver.get(url)

    basic_info = []
    elements = driver.find_elements(By.XPATH, '//ul[@class="bigimg"]/li')
    for i, element in enumerate(elements):
        info = element.find_element(By.XPATH, './a')
        name = info.get_attribute('title')
        book_url = info.get_attribute('href')
        info_list = element.find_element(By.CLASS_NAME, 'search_book_author').find_elements(By.XPATH, './span')
        author = info_list[0].text
        release_date = info_list[1].text.replace('/', '')
        press = info_list[2].text.replace('/', '')
        ISBN = get_ISBN(book_url)
        basic_info.append([name, author, press, release_date, ISBN])
        driver.back()
    # for element in elements:
    #     name = element.xpath('./a/@title')[0]
    #     book_url = element.xpath('./a/@href')[0]
    #     book_url = 'http:' + book_url
    #     print(book_url)
    #     author = element.xpath('.//p[@class="search_book_author"]/span[1]/text()')[0]
    #     release_date = element.xpath('.//p[@class="search_book_author"]/span[2]/text()')[0]
    #     press = element.xpath('.//p[@class="search_book_author"]/span[3]/text()')[0]
    #     release_date = release_date.replace('/', '')
    #     press = press.replace('/', '')
    #     ISBN = get_ISBN(book_url)
    #     basic_info.append([name, author, press, release_date, ISBN])

    return basic_info


def get_ISBN(book_url, fisrt=False):
    driver.get(book_url)
    if fisrt:
        time.sleep(10)
    else:
        time.sleep(1)
    ISBN = driver.find_element(By.XPATH, '//ul[@class="key clearfix"]/li[contains(text(),"ISBN")]').text
    ISBN = ISBN.replace('国际标准书号ISBN：', '')

    return ISBN


if __name__ == '__main__':
    queries = ['国学', '美学', '哲学', '心理学', '法学', '政治', '军事', '经济', '教育', '社会', '中国', '外国', '语言',
               '建筑',
               '历史', '数学', '物理', '化学', '生物', '英语', '天文', '农业', '计算机', '小说', '医学', '环境', '美食',
               '电子',
               '信息', '文学', '科幻']

    save_path = f'sample_data/dangdang.csv'
    total_page = 100

    sample_ISBN = get_ISBN('http://product.dangdang.com/11307171768.html', True)
    print(sample_ISBN)

    with open(save_path, 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(['name', 'author', 'press', 'release_date', 'ISBN'])
        for query in queries:
            print('Start collecting data by searching {}...\n'.format(query))
            time.sleep(1)
            for page_num in tqdm(range(total_page)):
                basic_info = get_basic_info(query, page_num)
                if basic_info:
                    writer.writerows(basic_info)


    # get_ISBN('http://product.dangdang.com/23735016.html')
