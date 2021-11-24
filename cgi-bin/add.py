import cgi
import cgitb
import sys
import mysql.connector 
import base64
import io
import PIL.Image

form = cgi.FieldStorage()
event_id = form.getvalue('id')
name = form.getvalue('name')
email = form.getvalue('email')
phone = form.getvalue('phone')
print(name,email,phone,event_id)

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="evento" )
mycursor = mydb.cursor()
sql = """ INSERT INTO member (name,email,phone,event_id) VALUES (%s, %s, %s, %s) """
sql1 = f""" UPDATE events SET limits = limits - 1 WHERE id = {event_id}"""
val = (name,email,phone,event_id)
mycursor.execute(sql,val)
mycursor.execute(sql1)
mydb.commit()

mydb.close()