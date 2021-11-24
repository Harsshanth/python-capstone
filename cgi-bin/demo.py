import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="evento"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM events")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)