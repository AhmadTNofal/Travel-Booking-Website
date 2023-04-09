#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

import cgi
import mysql.connector

def generate_booking_id(bus, Train, airplane, cursor):
    if bus:
        table = 'BusBooking'
    elif Train:
        table = 'TrainBooking'
    elif airplane:
        table = 'AirplaneBooking'
    else:
        return None

    cursor.execute(f"SELECT COUNT(*) FROM {table};")
    result = cursor.fetchone()
    return f"{table[0]}{result[0] + 1}"

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="a1h2m3e4d5",
  database="webprogramming"
)

form = cgi.FieldStorage()
email = form.getvalue("email")
departure = form.getvalue('departure')
destination = form.getvalue('destination')
weekday = form.getvalue('weekday')

sql_trip = "SELECT T.BusID, T.Price FROM journey J, Bus T WHERE J.Departure = %s AND J.Destination = %s AND T.DayOfWeek = %s AND J.JourneyID = T.JourneyID"
sql_get_account = "SELECT AccountID FROM account WHERE Email = %s"

try:
    cursor = mydb.cursor()
    cursor.execute(sql_trip, (departure, destination, weekday))
    trip_data = cursor.fetchone()

    if trip_data:
        Bus_id, price = trip_data
        cursor.execute(sql_get_account, (email,))
        account_id = cursor.fetchone()[0]

        booking_id = generate_booking_id(bus=True, Train=False, airplane=False, cursor=cursor)
        sql_insert_booking = "INSERT INTO BusBooking (BusBookingID, BusID, AccountID) VALUES (%s, %s, %s)"
        cursor.execute(sql_insert_booking, (booking_id, Bus_id, account_id))
        mydb.commit()

        print("Content-type:text/html\r\n\r\n")
        print(f'''
            <html>
<head>
<title>Account</title>
<link href="CSS.css" rel="stylesheet" type="text/css">
</head>

<body>
<div class="card">
<div class="card2">
    <h1 id="LoginTitle">Account details</h1>
    <p id="LoginTitle">The price is: {price}£</p>
<a href = \"Card.html\">
<button class="LoginButton">Pay Now</button>
</a>
</div>
</div>
</body>

</html>
        ''')

    else:
        print("Content-type:text/html\r\n\r\n")
        print("<html>")
        print("<head>")
        print("<title>Book your Bus</title>")
        print('<link href="CSS.css" rel="stylesheet" type="text/css">')
        print("</head>")
        print("<body>")
        print("<div class=\"card\">")
        print("<div class=\"card2\">")
        print("<p id=\"LoginTitle\">The trip is not available.</p>")
        print("<a href=\"Bus.html\">")
        print("<button class=\"LoginButton\"> Go Back</button>")
        print("</a>")
        print("</div>")
        print("</div>")
        print("</body>")
        print("</html>")
    mydb.close()

except mysql.connector.Error as error:
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<body>")
    print("<h1>Error connecting to database:</h1>")
    print("<p>{}</p>".format(error))
    print("</body>")
    print("</html>")

