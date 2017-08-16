# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import smtplib
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')
email_address=''
email_key=''
stmp_server="smtp.qq.com"
toaddr=[""]
url='https://src.edu-info.edu.cn/gift/4'
def getnumber():
    text=requests.get(url)
    soup=BeautifulSoup(text.content,'html.parser',from_encoding='utf8')
    number=soup.find_all('span',attrs={'class':'am-text-danger'})
    print number[0].text
    return number[0].text
def sendemail(number):
    number=str(number)
    content='教育行业src 京东卡剩余数量:'+number+'  <a href=\'https://src.edu-info.edu.cn/gift/4\'>点击兑换！</a>'
    msg=MIMEText(content,'html','utf-8')
    msg['From']='京东卡检测机器人<>'
    msg['subject']='教育行业src京东卡机器人报喜了！'
    server=smtplib.SMTP_SSL(stmp_server,465)
    server.login(email_address,email_key)
    server.set_debuglevel(1)
    server.sendmail(from_addr=email_address,to_addrs=toaddr,msg=msg.as_string())
    server.quit()
if __name__ == '__main__':
    while(True):
        number=getnumber()
        if(int(number)>0):
            sendemail(number)
        time.sleep(300)
