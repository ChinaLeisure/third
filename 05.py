import requests
from bs4 import BeautifulSoup
#page_list > ul > li:nth-child(1) > div.result_btm_con.lodgeunitname > span.result_price > i
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
price = soup.select('#page_list > ul > li:nth-of-type(1) > div.result_btm_con.lodgeunitname > span.result_price > i')
print(price)