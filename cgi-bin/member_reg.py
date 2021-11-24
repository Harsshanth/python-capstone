import cgi
import cgitb
import sys
import mysql.connector 
import base64
import io
import PIL.Image

form = cgi.FieldStorage()
ids = form.getvalue('id')
css = """
input[type=text],textarea ,select,input [type=file],input [type=checkbox],input[type=date],input [type=radio]{
width: 200%;
padding: 10px;
margin:15px 0px 15px 0px;
}
button{
background-color: 	#FFA07A;
color: white;
padding: 10px 10px;
margin: 3px 0;
width: 60%;
}"""

print('Content-type:text/html\r\n\r\n')

print(f'''
    <!DOCTYPE html>
<html>
<head>
<style>
{css}
</style>
</head>

<h3>REGISTRATION FORM </h3>


<form action="add.py"  method="get">

<input type="hidden" value="{ids}" name="id" />
<table>
<tr>
<td> <b>Name : </b> </td>
<td> <input type="text" name="name" size="15"> </td>
</tr>

<tr>
<td><b>Phone Number :</b> </td>
<td><input type="number" name="phone" size="10"> </td>
</tr>


<tr>
<td><b>Email :</b></td>
<td><input type="text" name="email"></td>
</tr>




</table>
<br><br>
<button type="submit" value="SUBMIT" name="submit" >Submit</button>
</form>

</div>
</body>
</html>

''')