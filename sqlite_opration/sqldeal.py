# -*- coding: utf-8 -*-
#this class is used to operate the sqlite database and do some text operation.
#article:zslove
import time
import csv
import os
import datetime
import sqlite3
conn = sqlite3.connect("test3.db")
conn.text_factory = str
c= conn.cursor()
class sqldeal():
    def __init__(self):
        pass
    def createtable(self,tablename):
        # create tables
        c.execute('''CREATE TABLE '''+tablename+'''
            (id int primary key, pname char(255),pid char(255),sex char(20),birthday char(40),address char(255),country char(20),mobile char(100),tel char(100),fax char(100),email char(100))''')
        # save the changes
        conn.commit()
        print "ok"
    def dirfile(self,filename):#being used to get the files name
        return os.listdir(filename)
    def insertdb(self,i, pname, pid, sex, birthday, address, country, mobile, tel, fax, email,tablename):
        v = (i, pname, pid, sex, birthday, address, country, mobile, tel, fax, email)
        c.execute("INSERT INTO "+tablename+" VALUES (?,?,?,?,?,?,?,?,?,?,?)", v)
        conn.commit()
    def checksql(self,sql):
        c.execute(sql)#'SELECT * FROM limit 200'
        result = c.fetchall()
        print result
    def delete(self,sql,i):
        c.execute(sql, i)#"delete from EmailInfo where id=?"
        conn.commit()
    def save(self,filename, contents): #being used to save the log info
        fh = open(filename, 'a+')
        fh.write(contents)
        fh.close()
    def main(self,i):
        array = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for j in array:
            try:
                filepath = []
                filename = dirfile("I:\\mimi\\xxx\\data\\" + j + "\\")
                for fn in filename:
                    filepath.append("I:\\mimi\\xxx\\data\\" + j + "\\" + fn)
                for f in filepath:
                    print "开始存储".decode("utf-8") + f + "中的用户名和密码...".decode("utf-8")
                    dmfile = open(f)
                    dm = dmfile.readlines()
                    for d in dm:
                        print d
                        try:
                            str2 = re.split(':|;', d)
                            insertdb(i, str2[0], str2[1])
                            if i % 5000 == 0:
                                conn.commit()
                        except:
                            continue
                        i = i + 1
                    save("log.txt", str(datetime.datetime.now()) + "log:" + "logpath：" + f + "rows：" + str(i) + "\r\n")
            except:
                continue




