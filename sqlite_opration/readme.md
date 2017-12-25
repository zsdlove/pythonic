**

Sqlite Operations
-----------------------------
**
by zsdlove
this is a a class for sqlite operations。you can use this class to operate the
sqlite database。 

method list：

```
def createtable(self,tablename) #create a table 
def dirfile(self,filename)  #get the files name frome files
def insertdb(self,i, pname, pid, sex, birthday, address, country, mobile, tel, fax, email,tablename)   #add one record
def checksql(self,sql) #check the record
def delete(self,sql,i)#delete the record
def save(self,filename, contents)#save the log 
def main(self,i) #a text operation example
```

how to use this class？
here are some examples：
```
import sqldeal
#hwo to use this class ?
#here are some examples
s1=sqldeal.sqldeal()
s1.createtable("love")
print "get the files name:",s1.dirfile("C:\\Users\\zheng\\Desktop\\test\\")
s1.insertdb(2,'love','ds','ff','ffs','fdf','sss','ffff','eeee','eeee','wwww',"love")
s1.checksql("select*from love")
#...
```