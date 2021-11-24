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

mycursor = mydb.cursor()

mycursor.execute("SELECT ename,evdate,id,limits FROM events ")

myresult = mycursor.fetchall()


print('Content-type:text/html\r\n\r\n')

print('''

    <html>
  <had
    ><title>Evento</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <style>
      * {
        margin: 0;
        padding: 0;
      }
      .table-box {
        margin: 50px auto;
      }

      .table-row {
        display: table;
        width: 80%;
        margin: 10px auto;
        font-family: sans-serif;
        background: transparent;
        padding: 12px 0;
        color: #555;
        font-size: 13px;
        box-shadow: 0 1px 4px 0px rgba(0, 0, 50, 0.3);
      }
      .table-head {
        background: #8665f7;
        box-shadow: none;
        color: #fff;
        font-weight: 600;
      }
      .table-head .table-cell {
        border-right: none;
      }
      .table-cell {
        display: table-cell;
        width: 20%;
        text-align: center;
        padding: 4px 0;
        border-right: 1px solid #d6d4d4;
        vertical-align: middle;
      }
      .first-cell {
        text-align: left;
        padding-left: 10px;
      }
      .last-cell {
        border-right: none;
      }
      a {
        text-decoration: none;
        color: #555;
      }

      @media only screen and (max-width: 600px) {
        .table-row {
          font-size: 11px;
        }
      }
      .button {
        background-color: #ffa07a;
        color: white;
        padding: 10px 10px;
        margin: 3px 0;
        width: 60%;
      }
    </style>
  </had>
  <body>
    <div class="table-box">
      <div class="table-row table-head">
        <div class="table-cell first-cell">
          <p>Event Name</p>
        </div>
        <div class="table-cell">
          <p>Event Date</p>
        </div>
        <div class="table-cell last-cell">
          <p>Register</p>
        </div>
         <div class="table-cell last-cell">
          <p>Check</p>
        </div>
      </div>
      ''')
for x in myresult:
    
    print(f'''
           <div class="table-row">
        <div class="table-cell first-cell">
          <p>{x[0]}</p>
        </div>
        <div class="table-cell">
          <p>{x[1]}</p>
        </div>''')
    if(x[3] != 0):
          print(f'''
        <div class="table-cell last-cell">
          <a href="details.py?q={x[2]}">View</a>
        </div>''')
    print(f'''
        <div class="table-cell last-cell">
          <a href="participants.py?q={x[2]}">Participants</a>
        </div>
      </div>
    </div>''')
print('''
<center>
    <form action="new_event.py" method="GET">
      <input class="button" type="submit" value="Host Event" name="new"></button>
    </form>
    </center>
  </body>
</html>
''')

     

