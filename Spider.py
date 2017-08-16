# -*- coding: utf-8 -*-
import requests
import SqlDB
from bs4 import BeautifulSoup
url='https://src.edu-info.edu.cn/list/?page='
def gogo(url):
    r = requests.get(url)
    html_soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf8')
    tr_soup = html_soup.find_all('tr', attrs={'class': 'row'})
    for r in tr_soup:
        r = str(r)
        r_soup = BeautifulSoup(r, 'html.parser')
        td = r_soup.find_all('td')
        print td[0].text.strip(),td[1].text.strip(),td[2].text.strip(),td[3].text.strip()
        #SqlDB.insert(td[0].text.strip(), td[1].text.strip(), td[2].text.strip(), td[3].text.strip())
if __name__ == '__main__':
    #queue=Queue()
    for i in range(1,582):
        Url=url+str(i)
        gogo(Url)