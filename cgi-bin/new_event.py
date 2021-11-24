import cgi
import cgitb
import sys
import mysql.connector 
import base64
import io
import PIL.Image

print('Content-type:text/html\r\n\r\n')

print('''
    <!DOCTYPE html>
<html>
<head>
<style>
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
}
</style>
</head>

<h3>REGISTRATION FORM </h3>

<form  action="registration.py" method="post">
<table>
<tr>
<td> <b>Event Name : </b> </td>
<td> <input type="text" name="ename" size="15"> </td>
</tr>
<tr>
    <td> <b>Organizer Name : </b> </td>
    <td> <input type="text" name="oname" size="15"> </td>
</tr>
<tr>
<td><b>Mode : </b</td>
<td><input type="radio" value="online" name="mode" checked>Online
<input type="radio" value="offline" name="mode"> Offline </td>
</tr>
<tr>
<td><b>Registration Start Date :</b></td>
<td><input type="date" name="sdate"></td>
</tr>
<tr>
<td><b>Registration End Date :</b></td>
<td><input type="date" name="edate"></td>
</tr>
<tr>
<td><b>Event Date :</b></td>
 <td><input type="date" name="evdate"></td>
</tr>
<tr>
<td><b>Phone Number :</b> </td>
<td><input type="number" name="phone" size="10"> </td>
</tr>
<tr>
<td><b>Description : </b></td>
<td><textarea name="des">
</textarea> </td>
</tr>

<tr>
<td><b>Email :</b></td>
<td><input type="text" name="email"></td>
</tr>

<tr>
    <td><b>Number of Participant allowed :</b></td>
    <td><input type="number" name="limit"></td>
    </tr>

<tr>
<td><b> Poster :  </b></td>
<td><input type="file" name="photo" accept="image/*"></td>
</tr>

</table>
<br><br>
<button type="submit" value="SUBMIT" name="submit">Submit</button>
</form>

</div>
</body>
</html>

''')