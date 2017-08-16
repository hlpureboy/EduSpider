# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
url='https://src.edu-info.edu.cn/list/?page='
def getinfo(url):
    r = requests.get(url)
    html_soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf8')
    tr_soup = html_soup.find_all('tr', attrs={'class': 'row'})
    for r in tr_soup:
        r = str(r)
        r_soup = BeautifulSoup(r, 'html.parser')
        td = r_soup.find_all('td')
        print td[0].text.strip(), td[1].text.strip(), td[2].text.strip(), td[3].text.strip()
        f=open('D:/Buginfo.txt','a')
        f.write(td[0].text.strip()+'||'+td[1].text.strip()+'||'+td[2].text.strip()+'||'+td[3].text.strip())
        f.write('\n')
        f.close()
for i in range(1,582):
    Url=url+str(i)
    getinfo(Url)