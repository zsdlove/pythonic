# -*- coding: utf-8 -*-
import sqlite3
import re
import os
import datetime
import time
conn = sqlite3.connect("test.db")
conn.text_factory = str
c= conn.cursor()
def save(filename, contents):
  fh = open(filename, 'a+')
  fh.write(contents)
  fh.close()
def dirfile(filename):
    return os.listdir(filename)
def insertdb(i,emailname,psw):
    v=(i,emailname,psw)
    c.execute("INSERT INTO EmailInfo VALUES (?,?,?)",v)
   # conn.commit()
# execute "INSERT"
def delete(i):
    c.execute("delete from EmailInfo where id=?",i)
    conn.commit()
def checksql():
    c.execute('SELECT * FROM EmailInfo')
    result=c.fetchall()
    print(result)
    conn.commit()
def main(i):
    array=['0','1','2','3','4','5','6','7','8','9','10','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for j in array:
        try:
            filepath = []
            filename = dirfile("I:\\mimi\\xxx\\data\\"+j+"\\")
            for fn in filename:
                filepath.append("I:\\mimi\\xxx\\data\\"+j+"\\" + fn)
            for f in filepath:
                print "开始存储".decode("utf-8")+f+"中的用户名和密码...".decode("utf-8")
                dmfile = open(f)
                dm=dmfile.readlines()
                for d in dm:
                    print d
                    try:
                        str2 = re.split(':|;',d)
                        insertdb(i,str2[0],str2[1])
                        if i%5000==0:
                            conn.commit()
                    except:
                        continue
                    i=i+1
                save("log.txt", str(datetime.datetime.now())+"log:"+"logpath："+f+"rows："+str(i)+"\r\n")
        except:
            continue
#starttime1=datetime.datetime.now()
timestart=time.time()
main(1)
timedf=time.time()-timestart
#endtime1=datetime.datetime.now()
print  "完成本文件夹下的所有存储工作".decode("utf-8")
print "一共花费时间为：".decode("utf-8"),timedf,"秒".decode("utf-8")