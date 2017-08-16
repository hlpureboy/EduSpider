# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import time
h={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36',
'Host':'weibo.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1'
}
coookie={
    'Cookie':'SINAGLOBAL=4316311496769.0317.1499490007129; UM_distinctid=15d30d11198391-0b1bb5c6866fcf-333f5902-100200-15d30d1119932f; UOR=news1.qau.edu.cn,widget.weibo.com,www.so.com; wvr=6; TC-Ugrow-G0=370f21725a3b0b57d0baaf8dd6f16a18; SSOLoginState=1502876140; SCF=Ang2QmzMBEksAcpGt1l8tGv9K0WuFuuu-x7Z5gzLhSJBl1g-NgvmWGD7cn8FjLCa5DO9cP-gey9PRviI4n_k2ck.; SUB=_2A250kGG9DeRhGeNJ7FAQ9yzNzTyIHXVX5NR1rDV8PUNbmtAKLRDZkW8gKn-jMMMy0MHIBGSgFjSi5Lsniw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhNZqG3_uQMESM5SILVoWeL5JpX5KzhUgL.Fo-NS0zpS0zpSo52dJLoI7LQdGWfMJHbdN.t; SUHB=0QS5pnBpf7Ww_T; ALF=1534412140; TC-V5-G0=784f6a787212ec9cddcc6f4608a78097; wb_cusLike_5772172160=N; _s_tentry=-; Apache=1649488883869.4744.1502876143180; ULV=1502876143205:12:12:4:1649488883869.4744.1502876143180:1502851888650; TC-Page-G0=9183dd4bc08eff0c7e422b0d2f4eeaec'
}
Url='http://weibo.com'
r=requests.get('http://weibo.com/p/1006051863847262/follow?relate=fans&page=1',headers=h,cookies=coookie)
#print r.content
soup=BeautifulSoup(r.content,'html.parser',from_encoding='utf8')
page_list=soup.find_all('script')[-1]
page_list=str(page_list)
page_soup=BeautifulSoup(page_list,'html.parser')
pagenumber=page_soup.find_all('script')
print pagenumber[0].text