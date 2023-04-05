#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

import cgi
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="a1h2m3e4d5",
  database="webprogramming"
)

# Check if the form has been submitted
form = cgi.FieldStorage()

if form:
    # Get the form data
    departure = form.getvalue('departure')
    destination = form.getvalue('destination')
    weekday = form.getvalue('weekday')

    # Define the SQL query to check if the trip is available
    sql_trip = "SELECT COUNT(*) FROM journey J, airplane T WHERE J.Departure = %s AND J.Destination = %s AND T.DayOfWeek = %s"

    # Execute the SQL query
    cursor = mydb.cursor()
    cursor.execute(sql_trip, (departure, destination, weekday))
    result = cursor.fetchone()

    # Check if the trip is available
    if result[0] > 0:
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Book your airplane</title>")
        print('<link href="CSS.css" rel="stylesheet" type="text/css">')
        print("</head>")
        print("<body>")
        print("<div class=\"card\">")
        print("<div class=\"card2\">")
        print("<p id=\"LoginTitle\">The trip is available!</p>")
        print("<a href=\"Card.html\">")
        print("<button class=\"LoginButton\">Go To Payment</button>")
        print("</a>")
        print("</div>")
        print("</div>")
        print("</body>")
        print("</html>")
    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Book your airplane</title>")
        print('<link href="CSS.css" rel="stylesheet" type="text/css">')
        print("</head>")
        print("<body>")
        print("<div class=\"card\">")
        print("<div class=\"card2\">")
        print("<p id=\"LoginTitle\">The trip is not available.</p>")
        print("<a href=\"Train.html\">")
        print("<button class=\"LoginButton\"> Go Back</button>")
        print("</a>")
        print("</div>")
        print("</div>")
        print("</body>")
        print("</html>")
    mydb.close()
else:
    print("Content-type:text/html\r\n\r\n")
    print("<html>")
    print("<head>")
    print("<title>Book your airplane</title>")
    print('<link href="CSS.css" rel="stylesheet" type="text/css">')
    print("</head>")
    print("<body>")
    print("<div class=\"card\">")
    print("<div class=\"card2\">")
    print("<p id=\"LoginTitle\">No form data submitted</p>")
    print("<a href=\"Train.html\">")
    print("<button class=\"LoginButton\"> Go Back</button>")
    print("</a>")
    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")
