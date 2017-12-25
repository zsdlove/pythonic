**提高数据库存储速度**
-------------

最近在处理一个亿级的数据，这些数据被分散地存储在600多个文本文件中，需要通过编程将这些文件存储到数据库中。文本处理当然首选python啦，于是我便写了一个脚本，如下：
```
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
```
但是，运行后我就发现不对劲儿了。程序跑得好慢。跑了一个下午才存了一多百万条数据，这是无法接受的。那么，哪里出问题了呢？仔细分析了下程序，我发现每次读取一条数据便存储一条数据显然是非常愚蠢的，一亿条数据，那么你就要存储以一次亿次，这显然太耗时了。这里的解决方案是，分组存储。这里以5000条数据为一组，每凑齐5000条数据提交一次sql存储，这样就大大减少了存储次数。这里修改的方法也简单，只要添加如下代码就可以了：

```
if i%5000==0:
   conn.commit()
```
修改后的代码：

```
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
                        if i%5000==0:   #这里是我们修改的地方
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
```
顺便提一下，在需要重复处理一个操作的时候，使用try  ...except...语句包裹你的执行代码是很有必要的，这样做不至于当数据处理异常的时候导致程序退出。这里我们通过以：和；分割文本中的每一条字段，但是这么大数据中总有些畸形的数据，这样就导致我们获取的数据为空，导致数据处理异常，如果不做好异常处理机制，程序就会退出，所以这里要注意一下。