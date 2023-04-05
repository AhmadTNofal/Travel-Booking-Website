#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"
import cgi
import mysql.connector
print("Content-Type: text/html\n")

# establish database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="a1h2m3e4d5",
  database="webprogramming"
)
mycursor = mydb.cursor()

# get form data
form = cgi.FieldStorage()
email = form.getvalue('email')
password = form.getvalue('password')

# check if account details are valid
sql = "SELECT * FROM Account WHERE Email = %s AND Password = %s"
val = (email, password)
mycursor.execute(sql, val)
result = mycursor.fetchone()
if result:
    print("<meta http-equiv='refresh' content='0; url=Search.html'>")
else:
    print("<script>alert('Invalid email or password. Please try again.')</script>")
    print("<meta http-equiv='refresh' content='0; url=Login.html'>")
