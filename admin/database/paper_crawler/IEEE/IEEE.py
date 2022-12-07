from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_paperinfo(topic):
    opt = webdriver.EdgeOptions()
    opt.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Edge(options=opt)
    url='https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(%22Full%20Text%20.AND.%20Metadata%22:{})'.format(topic)
    driver.get(url)
    # 等待3秒，让页面加载，防止爬不到
    time.sleep(3)
    df=[]
    print(url + '&pageNumber=1')
    for i in range(1, 3):
        elements=driver.find_elements(By.XPATH,'//div[@class=\'List-results-items\']')
        print(len(elements))
        for j in range(0,len(elements)):
            element=elements[j]
            papername=element.find_element(By.CLASS_NAME,'text-md-md-lh')
            # 子查询中用XPath默认为上次查询结果，查询子元素不用加/，若使用//则从全局中查找而不是继续上次查找
            paper_url=papername.find_element(By.XPATH,'a').get_attribute('href')
            papername=papername.text
            authors=element.find_element(By.CLASS_NAME,'text-base-md-lh').text
            year=element.find_element(By.CLASS_NAME,'publisher-info-container').find_element(By.XPATH,'span').text
            print(papername)
            print(year)
            # print(paper_url)
            # print(authors)
            driver.get(paper_url)
            try:
                DOI=driver.find_element(By.XPATH,'//strong[text()=\'DOI: \']/following::*').text
            except:
                DOI=None
            df.append([papername,authors,paper_url,DOI,year])
            print(DOI)
            driver.back()
        driver.get(url+'&pageNumber={}'.format(i+1))
        # print(url+'&pageNumber={}'.format(i+1))
        time.sleep(3)
    return df


# save_data(get_paperinfo())

if __name__ == '__main__':
    pass