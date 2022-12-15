import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67"
    }

url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&rowsPerPage=25&pageNumber=2'

try:
    page_text = requests.get(url=url, headers=headers).text
except Exception as e:
    print(e)