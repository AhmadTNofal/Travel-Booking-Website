#!"C:\Users\Ahmad Taher\AppData\Local\Programs\Python\Python311\python.exe"

import mysql.connector
import cgi
import random

def generate_wallet_id():
    """Generates a unique 8-digit wallet ID."""
    # Keep generating random wallet IDs until a unique one is found
    while True:
        # Generate a random 8-digit number
        wallet_id = random.randint(10000000, 99999999)
        
        # Check if the wallet ID already exists in the database
        cursor.execute("SELECT COUNT(*) FROM wallet WHERE WalletID = %s", (wallet_id,))
        result = cursor.fetchone()
        if result[0] == 0:
            # Unique wallet ID found, return it
            return wallet_id

try:
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Get values from form fields
    first_name = form['first_name'].value
    last_name = form['last_name'].value
    telephone_number = form['telephone_number'].value
    email = form['email'].value
    password = form['password'].value
    confirm_password = form['confirm_password'].value

    # Connect to database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="a1h2m3e4d5",
        database="webprogramming"
    )

    # Create cursor
    cursor = db.cursor()

    # Insert account data into account table
    insert_query = "INSERT INTO account (ForeName, SurName, TelNo, Email, Password, WalletID) VALUES (%s, %s, %s, %s, %s, %s)"
    wallet_id = generate_wallet_id()
    values = (first_name, last_name, telephone_number, email, password, wallet_id)
    cursor.execute(insert_query, values)

    # Get ID of new account
    account_id = cursor.lastrowid

    # Insert wallet data into wallet table
    insert_query = "INSERT INTO wallet (WalletID, CardID, Balance) VALUES (%s, %s, %s)"
    values = (wallet_id, '', 0)
    cursor.execute(insert_query, values)

    # Commit changes to database
    db.commit()

    # Print message confirming account creation
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<head>")
    print("<link href=\"CSS.css\" rel=\"stylesheet\" type=\"text/css\">")
    print("</head>")
    print("<body>")
    print("<div class=\"card\">")
    print("<div class=\"card2\">")
    print("<h1 id=\"LoginTitle\">Your account has been created!</h1>")
    print("<p id=\"LoginTitle\">Account ID: {}</p>".format(account_id))
    print("<p id=\"LoginTitle\">Wallet ID: {}</p>".format(wallet_id))
    print("<div class=\"registerbutton\">")
    print("<a href=\"Login.html\">")
    print("<button class=\"LoginButton\"> Back To Login </button>")
    print("</a>")
    print("</div>")
    print("</div>")
    print("</div>")
    print("</body>")
    print("</html>")

    # Close database connection
    db.close()

except mysql.connector.Error as error:
    # Handle database connection errors
    print("Content-Type: text/html")
    print()
    print("<html>")
    print("<body>")
    print("<h1>Error connecting to database:</h1>")
    print("<p>{}</p>".format(error))
    print("</body>")
    print("</html>")
