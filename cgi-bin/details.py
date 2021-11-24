import cgi
import cgitb
import sys
import mysql.connector 
import base64
import io
import PIL.Image

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="evento"
)
q = cgi.FieldStorage().getvalue('q')

mycursor = mydb.cursor()

mycursor.execute(f"SELECT * FROM events WHERE id={q}")

myresult = mycursor.fetchall()[0]

print('Content-type:text/html\r\n\r\n')



print('''
<!DOCTYPE html>
<html>
  <head>
  
  <style>
    {css}
  </style>
   </head>
   <body>
   
   <div style="font-weight: bold; font-size: 17px; font-family: Daytona">
      {ename}<br /><br />
      Record<br /><br />{des}<br /><br />
      Mode:{mode} <br /><br />Event Date:{evdate}<br /><br />Registeration close Date:{edate}<br /><br />
      <br /><br />Link:<a href="member_reg.py?id={id}"
        >Register</a
      >
      </div>
      

   
  </body>
</html>

'''.format(ename = myresult[2],des = myresult[10], mode = myresult[4], evdate = myresult[7], edate= myresult[6], id = myresult[1], css = """
div{
      background-image: url("https://images.pexels.com/photos/7130469/pexels-photo-7130469.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500");
        background-repeat: no-repeat;
        background-size: cover;
        text-align: justify;
        width: 40%;
        border: 10px solid darkmagenta;
        padding: 50px;
        font-family: Lucida Calligraph;
        margin: 50px 0px 0px 315px;
    }"""))

    