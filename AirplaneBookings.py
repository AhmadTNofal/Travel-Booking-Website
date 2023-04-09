#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

import cgi
import cgitb
import mysql.connector
cgitb.enable()

# Get form data
form = cgi.FieldStorage()
email = form.getvalue('email')

# Connect to the MySQL database
cnx = mysql.connector.connect(user='root', password='a1h2m3e4d5',
                              host='localhost', database='webprogramming')
cursor = cnx.cursor()

# Fetch Airplane bookings for the user
query = """SELECT t.AirplaneID, t.DayOfWeek, t.Price, t.JourneyTime, j.Departure, j.Destination
           FROM AirplaneBooking tb
           JOIN Account a ON tb.AccountID = a.AccountID
           JOIN Airplane t ON tb.AirplaneID = t.AirplaneID
           JOIN Journey j ON t.JourneyID = j.JourneyID
           WHERE a.Email = %s"""
cursor.execute(query, (email,))

# Print HTML headers
print("Content-Type: text/html")
print()

# Print fetched data in an HTML table
print("<html>")
print("<head><title>Airplane Bookings</title> <link href=\"CSS.css\" rel=\"stylesheet\" type=\"text/css\"></head>")
print("<body>")
print("<div class=\"card\">")
print("<div class=\"card2\">")
print("<h1 class=\"BookYourTrain\">Your Airplane Bookings:</h1>")
print("<table border='1'>")
print("<tr><th class=\"BookYourTrain\">Airplane ID</th><th class=\"BookYourTrain\">Day of Week</th><th class=\"BookYourTrain\">Price (£)</th><th class=\"BookYourTrain\">Journey Time (hrs)</th><th class=\"BookYourTrain\">Departure</th><th class=\"BookYourTrain\">Destination</th></tr>")
for row in cursor.fetchall():
    print("<tr>")
    for col in row:
        print("<td class=\"BookYourTrain\">{}</td>".format(col))
    print("</tr>")
print("</table>")
print("<table>")
print("<tr>")
print("<td>")
print("<a href=\"Search.html\">")
print("<button class=\"LoginButton\">New Booking</button>")
print("</a>")
print("</td>")
print("<td>")
print("<a href=\"booking_confirmation.html\">")
print("<button class=\"LoginButton\">View another booking</button>")
print("</a>")
print("</td>")
print("</tr>")
print("</table>")
print("</div>")
print("</div>")
print("</body>")
print("</html>")

cursor.close()
cnx.close()
