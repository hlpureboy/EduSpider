# -*- coding: utf-8 -*-
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
def insert(Time,Title,level,Author):
    con=MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='edubug',charset='utf8')
    cursor=con.cursor()
    sql='insert into edubug(Time,Title,leve,Author) values (%s,%s,%s,%s)'
    parm=(Time,Title,level,Author)
    cursor.execute(sql,parm)
    con.commit()
    cursor.close()
    con.close()
