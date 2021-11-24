import cgi
import cgitb
import sys
import mysql.connector 
import base64
import io
import PIL.Image
import  os
import random
cgitb.enable()
form = cgi.FieldStorage()
ename = form.getvalue('ename')
oname = form.getvalue('oname')
mode = form.getvalue('mode')
sdate = form.getvalue('sdate')
edate = form.getvalue('edate')
evdate = form.getvalue('evdate')
phone = form.getvalue('phone')
des = form.getvalue('des')
email = form.getvalue('email')
limits = form.getvalue('limit')
photo = form.getvalue('photo')
submit = form.getvalue('submit')
id = random.randint(10000,100000)
print(id)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="evento"
)

mycursor = mydb.cursor()

sql = """ INSERT INTO events (id,ename,oname,mode,sdate,edate,evdate,phone,des,email,limits,photo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
val = (id,ename,oname,mode,sdate,edate,evdate,phone,des,email,limits,photo)
mycursor.execute(sql, val)

mydb.commit()

mydb.close()

print('''
<h1> Successfully Added </h1>
''')