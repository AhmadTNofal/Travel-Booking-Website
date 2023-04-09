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


import smtplib

sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@gmail.com'
password = 'your_password'

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    message = 'Hello, this is a test email!'
    server.sendmail(sender_email, receiver_email, message)
    print('Email sent successfully!')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ', e)
except socket.error as e:
    print('Socket error occurred: ', e)
except ssl.SSLError as e:
    print('SSL error occurred: ', e)
finally:
    server.quit()
