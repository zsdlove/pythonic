import sqldeal
#hwo to use this class ?
#here are some examples
s1=sqldeal.sqldeal()
s1.createtable("love")
print "get the files name:",s1.dirfile("C:\\Users\\zheng\\Desktop\\test\\")
s1.insertdb(2,'love','ds','ff','ffs','fdf','sss','ffff','eeee','eeee','wwww',"love")
s1.checksql("select*from love")
#...


