# -*- coding: utf-8 -*-
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from scipy.misc import imread
import MySQLdb
def getinfo():
    sql='select Title from edubug'
    try:
        con=MySQLdb.connect(host='112.74.204.232',user='root',passwd='123pyj',db='edubug',charset='utf8')
        cursor=con.cursor()
        cursor.execute(sql)
        ls=cursor.fetchall()
        return ls
    except:
        print 'error'
def delword(ls):
    endls=''
    for i in ls:
        if u'漏洞' in i[0]:
            j=i[0].replace(u'漏洞','')
            #print j.encode('utf8')
            if u'存在' in j:
                q=j.replace(u'存在','')
                endls=endls+q
            else:
                endls=endls+j
    print endls.encode('utf8')
    return endls
def parseText(text):
    text=text.encode('utf8')
    tags=jieba.analyse.extract_tags(text,topK=40)
    print " ".join(tags)
    return " ".join(tags)
def drawPic(text,Pic):
    #img=imread(Pic,flatten=True)
    w=WordCloud(font_path="C:/Windows/Fonts/simhei.ttf",background_color='white').generate(text)
    plt.imshow(w)
    plt.axis("off")
    plt.savefig("F:/EduSpider/edubug.jpg",dpi=600)
if __name__ == '__main__':
    Pic='F:/EduSpider/edubug.jpg'
    ls=getinfo()
    text=delword(ls)
    t=parseText(text)
    drawPic(t,Pic)